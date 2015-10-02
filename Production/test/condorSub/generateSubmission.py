import os, bisect
from optparse import OptionParser
from FWCore.PythonUtilities.LumiList import LumiList

# define options
parser = OptionParser()
parser.add_option("-n", "--nFiles", dest="nFiles", default=1,
                                    help="number of files to process per job")

parser.add_option("-f","--filesConfig",dest="filesConfig", default="Spring15.SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
                                       help="which config file to retrieve the full file list from (leave off _cff.py)")

parser.add_option("-o","--outputDir",dest="outputDir", default="",
                                       help="path to ouput directory that root files will be stored in")

parser.add_option("-s","--submit",dest="submit", default=False,action="store_true",
                                       help="submit jobs to condor once they are configured")

parser.add_option("-c","--scenario",dest="scenario", default="Spring15",
                                       help="scenario: Phys14, Spring15, 2015B, re2015B, 2015C")
                                       
parser.add_option("-j","--firstJob",dest="firstJob", default=0,
                                       help="first job to submit")
                                       
parser.add_option("-d","--data",dest="data", default=False,action="store_true",
                                       help="if jobs are data (check runs in json)")

parser.add_option("--json",dest="json", default="",
                                       help="manually specified json file to check data")

(options, args) = parser.parse_args()

jsonfile = options.json
if options.data and jsonfile=="":
    # get from scenario
    from TreeMaker.Production.scenarios import Scenario
    scenario = Scenario(options.scenario)
    # data directory is next to condor directory
    jsonfile = "../"+scenario.jsonfile

if options.outputDir=="":
    raise Exception, 'No ouput directory (-o) specified'
    
if options.data and jsonfile=="":
    raise Exception, 'data was specified, but no json file was found'

# verify specified options
print "nFiles: ",options.nFiles
print "filesConfig: ",options.filesConfig
print "scenario: ",options.scenario
print "submit: ",options.submit
print "firstJob: ",options.firstJob
if options.data: print "json: ",jsonfile

# for data, get the (sorted) list of good runs from the json
runlist = []
if options.data:
    runlist = LumiList(jsonfile).getRuns()

# grab full file list from config files
readFiles = getattr(__import__("TreeMaker.Production."+options.filesConfig+"_cff",fromlist=["readFiles"]),"readFiles")

# to keep track of how many data files have been divied up
fileListLen = len(readFiles)

print "There are "+str(fileListLen)+" files in your sample"

# calculate the number of jobs necessary
if options.nFiles==-1:
    nJobs = 1
else:
    nJobs = fileListLen / int( options.nFiles )
    if ( fileListLen % int( options.nFiles ) != 0 ) :
        nJobs += 1

netJobs = nJobs - int(options.firstJob)
print "I will create "+str(netJobs)+" jobs for you!"
if options.firstJob>0: print "(starting from job "+str(options.firstJob)+")"

# start loop over N jobs
nActualJobs = 0
for iJob in range( int(options.firstJob), nJobs ) :
    # get starting file number
    nstart = iJob*int(options.nFiles)

    # skipping data files with bad runs only works with nFiles==1 right now
    if options.data and int(options.nFiles)==1:
        # check if this file's run is in the list of good runs
        readFileSplit = readFiles[iJob].split('/')
        # some filenames don't have the run in them
        if len(readFileSplit)==12:
            readFileRun = readFileSplit[8]+readFileSplit[9]
            i = bisect.bisect_left(runlist,readFileRun)
            # skip this file if the run was not found
            if i==len(runlist) or runlist[i]!=readFileRun:
                print "skipping run "+readFileRun
                continue
    
    # replace placeholders in template files
    jobname = options.filesConfig
    if nJobs>1: jobname = jobname+"_"+str(iJob)
    os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "\
                 +"-e 's~OUTDIR~"+options.outputDir+"~g' "\
                 +"-e 's|JOBNAME|"+jobname+"|g' "\
                 +"-e 's|SAMPLE|"+options.filesConfig+"|g' "\
                 +"-e 's|NPART|"+str(iJob)+"|g' "\
                 +"-e 's|NSTART|"+str(nstart)+"|g' "\
                 +"-e 's|NFILES|"+str(options.nFiles)+"|g' "\
                 +"-e 's|SCENARIO|"+options.scenario+"|g' "\
                 +"< jobExecCondor.jdl > jobExecCondor_"+jobname+".jdl")

    # submit jobs to condor, if -s was specified
    if ( options.submit ) :
        os.system("condor_submit jobExecCondor_"+jobname+".jdl")
        
    nActualJobs += 1
if options.data: print "("+str(nActualJobs)+" actual jobs)"
