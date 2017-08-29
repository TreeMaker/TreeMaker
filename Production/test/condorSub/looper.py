import os, bisect, stat, subprocess, sys
from optparse import OptionParser
from collections import defaultdict
import htcondor,classad
from FWCore.PythonUtilities.LumiList import LumiList
from TreeMaker.Production.scenarios import Scenario
from parseConfig import list_callback, parser_dict

def generateSubmission(options,verbose,filesConfig,scenario,firstJob,filesSet,runSet):
    # fix malformed options
    if filesConfig[-7:]=="_cff.py":
        filesConfig = filesConfig[:-7]
    elif filesConfig[-4:]=="_cff":
        filesConfig = filesConfig[:-4]

    thescenario = Scenario(scenario)
    data = not thescenario.geninfo
    
    jsonfile = options.json
    if data and jsonfile=="":
        # get from scenario
        # data directory is next to condor directory
        jsonfile = "../"+thescenario.jsonfile
        
    if data and jsonfile=="":
        raise Exception, "data was specified, but no json file was found"

    # verify specified options
    if verbose:
        print "nFiles: ",options.nFiles
        print "filesConfig: ",filesConfig
        print "scenario: ",scenario
        print "submit: ",options.submit
        print "firstJob: ",firstJob
        if data: print "json: ",jsonfile

    # for data, get the (sorted) list of good runs from the json
    runlist = []
    if data:
        runlist = LumiList(jsonfile).getRuns()

    # grab full file list from config files
    readFiles = getattr(__import__("TreeMaker.Production."+filesConfig+"_cff",fromlist=["readFiles"]),"readFiles")

    # to keep track of how many data files have been divied up
    fileListLen = len(readFiles)

    if verbose: print "There are "+str(fileListLen)+" files in your sample"

    # calculate the number of jobs necessary
    if options.nFiles==-1:
        nJobs = 1
    else:
        nJobs = fileListLen / int( options.nFiles )
        if ( fileListLen % int( options.nFiles ) != 0 ) :
            nJobs += 1

    netJobs = nJobs - int(firstJob)
    if verbose:
        print "I will create "+str(netJobs)+" jobs for you!"
        if firstJob>0: print "(starting from job "+str(firstJob)+")"

    # start loop over N jobs
    nActualJobs = 0
    jobSet = set()
    jobNums = []
    discontinuousJobs = (firstJob>0)
    for iJob in range( int(firstJob), nJobs ) :
        # get starting file number
        nstart = iJob*int(options.nFiles)

        # skipping data files with bad runs only works with nFiles==1 right now
        if data and int(options.nFiles)==1:
            # check if this file's run is in the list of good runs
            readFileSplit = readFiles[iJob].split('/')
            # some filenames don't have the run in them
            if len(readFileSplit)==12:
                discontinuousJobs = True
                readFileRun = readFileSplit[8]+readFileSplit[9]
                i = bisect.bisect_left(runlist,readFileRun)
                # skip this file if the run was not found
                if i==len(runlist) or runlist[i]!=readFileRun:
                    if verbose: print "skipping run "+readFileRun
                    continue
        
        jobname = filesConfig+"_"+str(iJob)
        jobNums.append(str(iJob))
        
        # keep list of jobs
        if options.missing:
            jobSet.add(jobname)
            continue

        nActualJobs += 1
        if options.count:
            continue
            
        # write job options to file - will be transferred with job
        with open("input/args_"+jobname+".txt",'w') as argfile:
            args = (options.args+" " if len(options.args)>0 else "")+"outfile="+jobname+" inputFilesConfig="+filesConfig+" nstart="+str(nstart)+" nfiles="+str(options.nFiles)+" scenario="+scenario
            argfile.write(args)

    if not options.count and not options.missing:
        if os.uname()[1]=="login.uscms.org":
            extras = ("+DESIRED_Sites = \""+options.sites+"\"") if len(options.sites)>0 else ""
        else:
            extras = (
                r'ONE_DAY = 864000\n'
                r'periodic_hold = (\\\n'
                r'    ( JobUniverse == 5 \&\& JobStatus == 2 \&\& CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 1.75 ) || \\\n'
                r'    ( JobRunCount > 8 ) || \\\n'
                r'    ( JobStatus == 5 \&\& CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 6 ) || \\\n'
                r'    ( DiskUsage > 38000000 ) || \\\n'
                r'    ( ResidentSetSize > RequestMemory * 950 ) )\n'
                r'periodic_hold_reason = strcat("Job held by PERIODIC_HOLD due to ", \\\n'
                r'    ifThenElse(( JobUniverse == 5 \&\& JobStatus == 2 \&\& CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 1.75 ), "runtime longer than 1.75 days", \\\n'
                r'    ifThenElse(( JobRunCount > 8 ), "JobRunCount greater than 8", \\\n'
                r'    ifThenElse(( JobStatus == 5 \&\& CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 6 ), "hold time longer than 6 days", \\\n'
                r'    ifThenElse(( DiskUsage > 38000000 ), "disk usage greater than 38GB", \\\n'
                r'                strcat("memory usage ",ResidentSetSize," greater than requested ",RequestMemory*1000))))), ".")'
            )

        # replace placeholders in template files
        os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "
                     +"-e 's~OUTDIR~"+options.outputDir+"~g' "
                     +"-e 's|SAMPLE|"+filesConfig+"|g' "
                     +"-e 's|THREADS|"+options.threads+"|g' "
                     +"-e 's~EXTRASTUFF~"+extras+"~g' "
                     +"< jobExecCondor.jdl > jobExecCondor_"+filesConfig+".jdl")
                     
        # append queue comment
        queuecmd = "-queue "+str(nActualJobs)
        if discontinuousJobs: queuecmd = "-queue Process in "+','.join(jobNums)
        with open("jobExecCondor_"+filesConfig+".jdl",'a') as jdlfile:
            jdlfile.write("# "+queuecmd.replace("-queue","Queue")+"\n")
        
        # submit jobs to condor, if -s was specified
        if options.submit:
            submitcmd = "condor_submit jobExecCondor_"+filesConfig+".jdl "+queuecmd
            if verbose: print submitcmd
            os.system(submitcmd)

    if verbose and data: print "("+str(nActualJobs)+" actual jobs)"

    # check for missing jobs
    diffList = []
    if options.missing:        
        # find difference, also checking for still running jobs
        diffSet = jobSet - filesSet
        diffList = list(sorted(diffSet))
        diffSet = diffSet - runSet
        diffList = list(diffSet)

    return (nActualJobs,diffList)

# define options (get some defaults from config file)
parser = OptionParser()
parser.add_option("-k", "--keep", dest="keep", default=False, action="store_true", help="keep existing tarball for job submission (default = %default)")
parser.add_option("-n", "--nFiles", dest="nFiles", default=1, help="number of files to process per job (default = %default)")
parser.add_option("-i", "--input", dest="input", type="string", action="callback", callback=list_callback, default=parser_dict["looper"]["input"],
    help="comma-separated list of input dicts; each prefixed by dict_ and contains scenario + list of samples (default = %default)")
parser.add_option("-o", "--outputDir", dest="outputDir", default="", help="path to ouput directory in which root files will be stored (required)")
parser.add_option("-s", "--submit", dest="submit", default=False, action="store_true", help="submit jobs to condor once they are configured (default = %default)")
parser.add_option("-c", "--count", dest="count", default=False, action="store_true", help="count the expected number of jobs (default = %default)")
parser.add_option("-m", "--missing", dest="missing", default=False, action="store_true", help="check for missing jobs (default = %default)")
parser.add_option("-r", "--resub", dest="resub", default="", help="make a resub script with specified name (default = %default)")
parser.add_option("-j", "--json", dest="json", default="", help="manually specified json file to check data (override scenario) (default = %default)")
parser.add_option("-u", "--user", dest="user", default=parser_dict["common"]["user"], help="view jobs from this user (submitter) (default = %default)")
parser.add_option("-t", "--threads", dest="threads", default=1, help="specify number of CPU threads per job (default = %default)")
parser.add_option("-a", "--args", dest="args", default="", help="additional common args to use for all jobs (default = %default)")
parser.add_option("--sites", dest="sites", default="", help="comma-separated list of sites for global pool running (default = %default)")
(options, args) = parser.parse_args()

# check for option errors
if options.submit and (options.count or options.missing) or (options.count and options.missing):
    parser.error("Options -s, -c, -m are exclusive, pick one!")
if options.input is None or len(options.input)==0:
    parser.error("Required option: -i [dict]")
if len(options.outputDir)==0:
    parser.error("Required option: -o [directory]")
if options.threads<1:
	options.threads = 1

# special settings
verbose = True
if options.missing or options.count:
    verbose = False
    options.submit = False # exclusive
if not options.submit:
    options.keep = True # no need to retar if not submitting

cmd = "./FScheck.sh"
if options.keep: cmd += " -k"
sp = subprocess.Popen(cmd, shell=True, stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr)
sp.wait()
    
# check finished jobs
filesSet = set()
if options.missing:
    outDir = options.outputDir.replace("root://cmseos.fnal.gov/","")
    files = filter(None,os.popen("xrdfs root://cmseos.fnal.gov/ ls "+outDir).read().split('\n'))
    # basename
    filesSet = set([ f.split("/")[-1].replace("_RA2AnalysisTree.root","") for f in files])
    
# check running jobs
runSet = set()
if options.missing:
    from collectors import collectors
    constraint = ""
    if len(options.user)>0: constraint += 'Owner=="'+options.user+'"'
    for collector in collectors:
        coll = htcondor.Collector(collector[0])
        for sch in collector[1]:
            scheddAd = coll.locate(htcondor.DaemonTypes.Schedd, sch)
            schedd = htcondor.Schedd(scheddAd)
            for result in schedd.xquery(constraint,["Out"]):
                runSet.add("_".join(result["Out"].replace(".stdout","").split('_')[:-1]))

# loop over dicts
njobs = 0
diffList = []
for input in options.input:
    # loop over dict entries
    process = input.replace(".py","")
    flist = __import__("dict_"+process).flist
    scenario = flist["scenario"]
    tot = 0
    for file in flist["samples"]:
        fname = file[0]
        firstJob = 0
        # extra optional field for updating data
        if len(file)>1: firstJob = file[1]
        ntmp, dtmp = generateSubmission(options,verbose,fname,scenario,firstJob,filesSet,runSet)
        tot += ntmp
        diffList.extend(dtmp)
    njobs += tot
    if options.count:
        print process+": "+str(tot)
if options.count:
    print str(njobs)+" jobs"
if options.missing:
    if len(diffList)>0:
        if len(options.resub)>0:
            with open(options.resub,'w') as rfile:
                rfile.write("#!/bin/bash\n\n")
                diffDict = defaultdict(list)
                for dtmp in sorted(diffList):
                    stmp = '_'.join(dtmp.split('_')[:-1])
                    ntmp = dtmp.split('_')[-1]
                    diffDict[stmp].append(ntmp)
                for stmp in sorted(diffDict):
                    rfile.write('condor_submit jobExecCondor_'+stmp+'.jdl -queue Process in '+','.join(diffDict[stmp])+'\n')
                # make executable
                st = os.stat(rfile.name)
                os.chmod(rfile.name, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        else: print '\n'.join(sorted(diffList))
    else: print "No missing jobs!"
