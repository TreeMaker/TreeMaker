import os
from optparse import OptionParser

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

(options, args) = parser.parse_args()

if options.outputDir=="":
    raise Exception, 'No ouput directory (-o) specified'

# verify specified options
print "nFiles: ",options.nFiles
print "filesConfig: ",options.filesConfig
print "scenario: ",options.scenario
print "submit: ",options.submit
print "firstJob: ",options.firstJob

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

netJobs = nJobs - int(options.firstJob)
print "I will create "+str(netJobs)+" jobs for you!"
if options.firstJob>0: print "(starting from job "+str(options.firstJob)+")"

# start loop over N jobs
for iJob in range( int(options.firstJob), nJobs ) :
    # get starting file number
    nstart = iJob*int(options.nFiles)

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
