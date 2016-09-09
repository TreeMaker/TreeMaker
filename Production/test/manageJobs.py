import sys,os,subprocess,glob,shutil
from optparse import OptionParser

class CondorJob:
    def __init__(self, stdout, schedd):
        self.stdout = stdout
        self.name = "_".join(stdout.split('_')[:-1])
        self.num = stdout.split('_')[-1]+".0"
        self.schedd = schedd

def makeJobQuery(options, prop, schedd=""):
    #make query
    cmd = "condor_q "
    if len(schedd)>0: cmd += "-name "+schedd+" "
    cmd += options.user+" "
    if options.held: cmd += "-hold "
    if options.running: cmd += "-run "
    cmd += "-long "
    cmd += "| grep \""+prop+"\" "
    if len(options.grep)>0: cmd += "| grep \""+options.grep+"\" "
    if len(options.vgrep)>0: cmd += "| grep -v \""+options.vgrep+"\" "
    cmd += "| sort"
    return cmd
        
def getJobs(options, schedd=""):
    cmd = makeJobQuery(options,"stdout",schedd)

    #get info for selected jobs
    joblist = filter(None,subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split('\n'))
    joblist = [j.split(' ')[2].replace("\"","").replace(".stdout","") for j in joblist]
    jobs = []
    if len(schedd)>0 and len(joblist)>0: print schedd
    for j in joblist:
        jobs.append(CondorJob(j,schedd))
    return jobs
        
def printJobs(jobs, stdout=False):
    if len(jobs)==0: return
    
    if stdout:
        print "\n".join([j.stdout for j in jobs])
    else:
        print "\n".join([j.name for j in jobs])

parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="user", default="pedrok", help="view jobs from this user (submitter) (default = %default)")
parser.add_option("-a", "--all", dest="all", default=False, action="store_true", help="view jobs from all schedulers (default = %default)")
parser.add_option("-h", "--held", dest="held", default=False, action="store_true", help="view only held jobs (default = %default)")
parser.add_option("-r", "--running", dest="running", default=False, action="store_true", help="view only running jobs (default = %default)")
parser.add_option("-g", "--grep", dest="grep", default="", help="view jobs with [string] in the job name (default = %default)")
parser.add_option("-v", "--vgrep", dest="vgrep", default="", help="view jobs without [string] in the job name (default = %default)")
parser.add_option("-o", "--stdout", dest="stdout", default=False, action="store_true", help="print stdout filenames instead of job names (default = %default)")
parser.add_option("-e", "--edit", dest="edit", default="", help="edit the redirector of the job (default = %default)")
parser.add_option("-s", "--resubmit", dest="resubmit", default=False, action="store_true", help="resubmit the selected jobs (default = %default)")
parser.add_option("-k", "--kill", dest="kill", default=False, action="store_true", help="remove the selected jobs (default = %default)")
parser.add_option("-d", "--dir", dest="dir", default="", help="directory for stdout files (used for backup when resubmitting) (default = %default)")
parser.add_option("--help", dest="help", action="store_true", default=False, help='show this help message')
(options, args) = parser.parse_args()

if options.help:
   parser.print_help()
   sys.exit()

#check for exclusive options
if options.held and options.running:
    parser.error("Can't use -h and -r together, pick one!")
if options.resubmit and options.kill:
    parser.error("Can't use -s and -k together, pick one!")
if options.running and options.resubmit:
    parser.error("Can't use -r and -s together, pick one!")
if options.all and (options.kill or options.resubmit):
    parser.error("Can't use -s or -k with -a.")

#can only resubmit held jobs (via release)
if options.resubmit: options.held = True

jobs = []
if options.all:
    #loop over schedulers    
    for sch in ["cmslpc"+str(schnum)+".fnal.gov" for schnum in xrange(23,43)]:
        jobs_tmp = getJobs(options,sch)
        printJobs(jobs_tmp,options.stdout)
        jobs.extend(jobs_tmp)
else:
    jobs = getJobs(options)
    printJobs(jobs,options.stdout)

#resubmit jobs
if options.resubmit:
    #create backup dir if desired
    backup_dir = ""
    if len(options.dir)>0:
        backup_dir = options.dir+"/backup"
        if not os.path.isdir(backup_dir):
            os.mkdir(backup_dir)

    for j in jobs:
        #backup log
        if len(options.dir)>0:
            prev_logs = glob.glob(backup_dir+"/"+j.stdout+"_*")
            num_logs = 0
            #increment log number if job has been resubmitted before
            print prev_logs
            if len(prev_logs)>0:
                num_logs = max([int(log.split("_")[-1].replace(".stdout","")) for log in prev_logs])+1
            #copy logfile
            print num_logs
            shutil.copy2(options.dir+"/"+j.stdout+".stdout",backup_dir+"/"+j.stdout+"_"+str(num_logs)+".stdout")
        #edit redirector
        if len(options.edit)>0:
            cmd1 = "condor_q -long "+j.num+" | grep \"Args\""
            args = filter(None,subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split('\n'))
            args = args[0].split(' ')[2:]
            args = [a.replace("\"","").rstrip() for a in args]
            if "root:" not in args[-1]: args.append(options.edit)
            else: args[-1] = options.edit
            cmd2 = "condor_qedit "+j.num+" Args '\""+" ".join(args[:])+"\"'"
            subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()        subprocess.Popen(["condor_release",j.num], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#or remove jobs
elif options.kill:
    for j in jobs:
        subprocess.Popen(["condor_rm",j.num], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
