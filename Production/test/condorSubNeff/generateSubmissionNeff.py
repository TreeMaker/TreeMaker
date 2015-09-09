import os
from optparse import OptionParser

# define options
parser = OptionParser()

parser.add_option("-f","--filesConfig",dest="filesConfig", default="Spring15.SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
                                       help="which config file to retrieve the full file list from (leave off _cff.py)")

parser.add_option("-s","--submit",dest="submit", default=False,action="store_true",
                                       help="submit jobs to condor once they are configured")

(options, args) = parser.parse_args()

# verify specified options
print "filesConfig: ",options.filesConfig
print "submit: ",options.submit

# replace placeholders in template file
jobname = "jobExecCondorNeff_"+options.filesConfig+".jdl"
os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "\
             +"-e 's|SAMPLE|"+options.filesConfig+"|g' "\
             +"< jobExecCondorNeff.jdl > "+jobname)

# submit job to condor, if -s was specified
if ( options.submit ) :
    os.system("condor_submit "+jobname)
    

