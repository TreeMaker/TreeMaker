import os
from optparse import OptionParser

# define options
parser = OptionParser()
parser.add_option("-n", "--nFiles", dest="nFiles", default=-1,
                                    help="number of files to process per job")

parser.add_option("-f","--filesConfig",dest="filesConfig", default="Spring15.SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
                                       help="which config file to retrieve the full file list from (leave off _cff.py)")

parser.add_option("-s","--submit",dest="submit", default=False,action="store_true",
                                       help="submit jobs to condor once they are configured")

(options, args) = parser.parse_args()

# verify specified options
print "nFiles: ",options.nFiles
print "filesConfig: ",options.filesConfig
print "submit: ",options.submit

# grab full file list from config files
import FWCore.ParameterSet.Config as cms
process = cms.Process("demo")
process.load("TreeMaker.Production."+options.filesConfig+"_cff")

# to keep track of how many data files have been divied up
fileListLen = len(process.source.fileNames)

print "There are "+str(fileListLen)+" files in your sample"

# calculate the number of jobs necessary
if options.nFiles==-1:
    nJobs = 1
else:
    nJobs = fileListLen / int( options.nFiles )
    if ( fileListLen % int( options.nFiles ) != 0 ) :
        nJobs += 1

print "I will create "+str(nJobs)+" jobs for you!"

# start loop over N jobs
for iJob in range( nJobs ) :
    # get starting file number
    nstart = iJob*int(options.nFiles)

    # replace placeholders in template files
    jobname = options.filesConfig
    if nJobs>1: jobname = jobname+"_"+str(iJob)
    os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "\
                 +"-e 's|JOBNAME|"+jobname+"|g' "\
                 +"-e 's|SAMPLE|"+options.filesConfig+"|g' "\
                 +"-e 's|NSTART|"+str(nstart)+"|g' "\
                 +"-e 's|NFILES|"+str(options.nFiles)+"|g' "\
                 +"< jobExecCondorNeff.jdl > jobExecCondorNeff_"+jobname+".jdl")

    # submit jobs to condor, if -s was specified
    if ( options.submit ) :
        os.system("condor_submit jobExecCondorNeff_"+jobname+".jdl")
    

