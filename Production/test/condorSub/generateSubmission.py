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

(options, args) = parser.parse_args()

if options.outputDir=="":
    raise Exception, 'No ouput directory (-o) specified'

# varify specified options
print "nFiles: ",options.nFiles
print "filesConfig: ",options.filesConfig
print "scenario: ",options.scenario
print "submit: ",options.submit

# grab full file list from config files
import FWCore.ParameterSet.Config as cms
process = cms.Process("demo")
process.load("TreeMaker.Production."+options.filesConfig+"_cff")

# index is to count jobs for labeling input and output files
index=0
# to keep track of how many data files have been divied up
fileListLen = len(process.source.fileNames)

print "There are "+str(fileListLen)+" files in your sample"

# calculate the number of jobs necessary
nJobs = fileListLen / int( options.nFiles )
if ( fileListLen % int( options.nFiles ) != 0 ) :
    nJobs += 1

print "I will create "+str(nJobs)+" jobs for you!"

# start loop over N jobs
for iJob in range( nJobs ) :

    # initialize list string
    list = ""

    # build string which is a list of files
    # loop over options.nFiles
    for iFile in range( int(options.nFiles) ) :

        # protection against index going out of range of
        # process.source.fileNames
        if ( iFile+iJob*int( options.nFiles ) >= fileListLen ) :
            break

        if ( iFile == 0 ) :
            list += process.source.fileNames[iFile+iJob*int( options.nFiles )]
        else :
            list += ','+process.source.fileNames[iFile+iJob*int( options.nFiles )]

    # replace placeholders in template files
    jobname = "jobExecCondor_"+options.filesConfig+"_"+str(iJob)+".jdl"
    os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "\
                 +"-e 's~OUTDIR~"+options.outputDir+"~g' "\
                 +"-e 's|SAMPLE|"+options.filesConfig+"_"+str(iJob)+"|g' "\
                 +"-e 's|FILELIST|"+list+"|g' "\
                 +"-e 's|SCENARIO|"+options.scenario+"|g' "\
                 +"< jobExecCondor.jdl > "+jobname)

    # submit jobs to condor, if -s was specified
    if ( options.submit ) :
        os.system("condor_submit "+jobname)
    

