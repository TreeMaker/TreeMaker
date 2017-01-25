import sys,os,subprocess,glob,shutil,json
from optparse import OptionParser
import htcondor,classad

class CondorJob:
    def __init__(self, result, schedd):
        self.stdout = result["Out"].replace(".stdout","")
        self.name = "_".join(self.stdout.split('_')[:-1])
        self.num = str(result["ClusterId"])+"."+str(result["ProcId"])
        self.schedd = schedd
        self.why = result["HoldReason"] if "HoldReason" in result.keys() else ""
        self.args = result["Args"]
        self.status = result["JobStatus"] # 2 is running, 5 is held

def getJobs(options, scheddurl=""):
    constraint = ""
    if len(options.user)>0: constraint += 'Owner=="'+options.user+'"'
    if options.held: constraint += ' && JobStatus==5'
    elif options.running: constraint += ' && JobStatus==2'

    if len(scheddurl)>0:
        if len(options.coll)>0: coll = htcondor.Collector(options.coll)
        else: coll = htcondor.Collector() # defaults to local
        scheddAd = coll.locate(htcondor.DaemonTypes.Schedd, scheddurl)
        schedd = htcondor.Schedd(scheddAd)
    else:
        schedd = htcondor.Schedd() # defaults to local

    # get info for selected jobs
    jobs = []
    for result in schedd.xquery(constraint,["ClusterId","ProcId","HoldReason","Out","Args","JobStatus"]):
        # check greps
        if len(options.grep)>0 and not options.grep in result["Out"]: continue
        if len(options.vgrep)>0 and options.vgrep in result["Out"]: continue
        jobs.append(CondorJob(result,scheddurl))

    return jobs

def printJobs(jobs, stdout=False, why=False):
    if len(jobs)==0: return
    
    if stdout:
        print "\n".join([j.stdout+(" : "+j.why if why and len(j.why)>0 else "") for j in jobs])
    else:
        print "\n".join([j.name+(" : "+j.why if why and len(j.why)>0 else "") for j in jobs])

parser = OptionParser(add_help_option=False)
parser.add_option("-c", "--coll", dest="coll", default="", help="view jobs from this collector (default = %default)")
parser.add_option("-u", "--user", dest="user", default="pedrok", help="view jobs from this user (submitter) (default = %default)")
parser.add_option("-a", "--all", dest="all", default=False, action="store_true", help="view jobs from all schedulers (default = %default)")
parser.add_option("-h", "--held", dest="held", default=False, action="store_true", help="view only held jobs (default = %default)")
parser.add_option("-r", "--running", dest="running", default=False, action="store_true", help="view only running jobs (default = %default)")
parser.add_option("-g", "--grep", dest="grep", default="", help="view jobs with [string] in the job name (default = %default)")
parser.add_option("-v", "--vgrep", dest="vgrep", default="", help="view jobs without [string] in the job name (default = %default)")
parser.add_option("-o", "--stdout", dest="stdout", default=False, action="store_true", help="print stdout filenames instead of job names (default = %default)")
parser.add_option("-x", "--xrootd", dest="xrootd", default="", help="edit the xrootd redirector of the job (default = %default)")
parser.add_option("-e", "--edit", dest="edit", default="", help="edit the ClassAds of the job (JSON dict format) (default = %default)")
parser.add_option("-s", "--resubmit", dest="resubmit", default=False, action="store_true", help="resubmit the selected jobs (default = %default)")
parser.add_option("-k", "--kill", dest="kill", default=False, action="store_true", help="remove the selected jobs (default = %default)")
parser.add_option("-d", "--dir", dest="dir", default="", help="directory for stdout files (used for backup when resubmitting) (default = %default)")
parser.add_option("-w", "--why", dest="why", default=False, action="store_true", help="show why a job was held (default = %default)")
parser.add_option("--help", dest="help", action="store_true", default=False, help='show this help message')
(options, args) = parser.parse_args()

if options.help:
   parser.print_help()
   sys.exit()

# check for exclusive options
if options.held and options.running:
    parser.error("Can't use -h and -r together, pick one!")
if options.resubmit and options.kill:
    parser.error("Can't use -s and -k together, pick one!")
if options.all and (options.kill or options.resubmit):
    parser.error("Can't use job modification options (-s, -k) with -a.")
if len(options.xrootd)>0 and options.xrootd[0:7] != "root://":
    parser.error("Improper xrootd address: "+options.xrootd)
if len(options.xrootd)>0 and options.xrootd[-1]!='/':
    options.xrootd += '/'
    
jobs = []
if options.all:
    # loop over schedulers
    all_nodes = list(xrange(23,39))
    all_nodes.append(41)
    for sch in ["cmslpc"+str(schnum)+".fnal.gov" for schnum in all_nodes]:
        jobs_tmp = getJobs(options,sch)
        if len(jobs_tmp)>0: print sch
        printJobs(jobs_tmp,options.stdout,options.why)
        jobs.extend(jobs_tmp)
else:
    jobs = getJobs(options)
    printJobs(jobs,options.stdout,options.why)

# resubmit jobs
if options.resubmit:
    # get scheduler
    schedd = htcondor.Schedd() # defaults to local
    # process edits from JSON into dict
    edits = {}
    if len(options.edit)>0:
        try:
            edits = json.loads(options.edit)
        except:
            print "edit not specified in JSON format! Exiting."
            sys.exit(1)
    # create backup dir if desired
    backup_dir = ""
    tmp_dir = ""
    if len(options.dir)>0:
        backup_dir = options.dir+"/backup"
        if not os.path.isdir(backup_dir):
            os.mkdir(backup_dir)
        tmp_dir = options.dir+"/tmp"
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
    for j in jobs:
        logfile = options.dir+"/"+j.stdout+".stdout"
        # hold running jobs first (in case hung)
        if j.status==2:
            if len(options.dir)>0:
                logfile = tmp_dir+"/"+j.stdout+".stdout"
                # generate a backup log from condor_tail
                cmdt = "condor_tail -maxbytes 10000000 "+j.num
                with open(logfile,'w') as logf:
                    subprocess.Popen(cmdt, shell=True, stdout=logf, stderr=subprocess.PIPE).communicate()
            schedd.act(htcondor.JobAction.Hold,[j.num])
        # backup log
        if len(options.dir)>0:
            prev_logs = glob.glob(backup_dir+"/"+j.stdout+"_*")
            num_logs = 0
            # increment log number if job has been resubmitted before
            if len(prev_logs)>0:
                num_logs = max([int(log.split("_")[-1].replace(".stdout","")) for log in prev_logs])+1
            # copy logfile
            if os.path.isfile(logfile):
                shutil.copy2(logfile,backup_dir+"/"+j.stdout+"_"+str(num_logs)+".stdout")
        # reset counts to avoid removal
        schedd.edit([j.num],"JobRunCount","0")
        schedd.edit([j.num],"NumJobStarts","0")
        schedd.edit([j.num],"NumShadowStarts","0")
        # any other classad edits
        for editname,editval in edits.iteritems():
            schedd.edit([j.num],str(editname),'"'+str(editval)+'"')
        # edit redirector
        if len(options.xrootd)>0:
            args = j.args.split(' ')[2:]
            args = [a.replace("\"","").rstrip() for a in args]
            if "root:" not in args[-1]: args.append(options.xrootd)
            else: args[-1] = options.xrootd
            schedd.edit([j.num],"Args",'"'+" ".join(args[:])+'"')
        # release job
        schedd.act(htcondor.JobAction.Release,[j.num])
# or remove jobs
elif options.kill:
    # get scheduler
    schedd = htcondor.Schedd() # defaults to local
    for j in jobs:
        schedd.act(htcondor.JobAction.Remove,[j.num])
