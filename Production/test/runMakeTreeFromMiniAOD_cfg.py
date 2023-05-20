import sys

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()

from TreeMaker.TreeMaker.maker import maker
theMaker = maker(parameters)

# run-only parameters
reportfreq=parameters.value("reportfreq",1000)
dump=parameters.value("dump",False)
mp=parameters.value("mp",False)
threads=parameters.value("threads",1)
streams=parameters.value("streams",0)
tmi=parameters.value("tmi",False)
trace=parameters.value("trace",False)
debugjets=parameters.value("debugjets",False)
debugweights=parameters.value("debugweights",False)

# print out settings
print "***** SETUP ************************************"
theMaker.printSetup()
if mp: print " running memory profile"
if threads>1:
    print " threads: "+str(threads)
    if streams>0: print " streams: "+str(streams)
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
from TreeMaker.TreeMaker.TMEras import TMeras
eralist = []
if len(theMaker.era)>0:
	eralist.append(getattr(eras,theMaker.era))
if len(theMaker.localera)>0:
	eralist.append(getattr(TMeras,theMaker.localera))
process = cms.Process("RA2EventSelection",*eralist)

# configure geometry & conditions
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = theMaker.globaltag

# log output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = reportfreq
if theMaker.verbose:
    process.MessageLogger.categories.append('TreeMaker')
    process.MessageLogger.cerr.TreeMaker = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        limit = cms.untracked.int32(10000000),
    )
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
)

# memory profiling
if mp:
    process.IgProfService = cms.Service("IgProfService",
        reportEventInterval = cms.untracked.int32(1),
        reportFirstEvent = cms.untracked.int32(1),
        reportToFileAtPostEndJob = cms.untracked.string('| gzip -c > '+outfile+'___memory___%I_EndOfJob.gz'),
        reportToFileAtPostEvent = cms.untracked.string('| gzip -c > '+outfile+'___memory___%I.gz')
    )

# multithreading options
if threads>1:
    process.options.numberOfThreads = cms.untracked.uint32(threads)
    process.options.numberOfStreams = cms.untracked.uint32(streams if streams>0 else 0)

# simpler profiling
if tmi:
    from Validation.Performance.TimeMemoryInfo import customise
    process = customise(process)

if trace:
    process.add_(cms.Service("Tracer", dumpPathsAndConsumes = cms.untracked.bool(True)))

# setup makeTree modules
process = theMaker.makeTreeFromMiniAOD(process)

producer_types_to_debug = []
# to check user floats and discriminators
if debugjets:
    producer_types_to_debug.extend(["JetProperties"])
# to check theory weights
if debugweights:
    producer_types_to_debug.extend(["LHEWeightProductProducer","GenWeightProductProducer"])
if len(producer_types_to_debug)>0:
    from HLTrigger.Configuration.common import producers_by_type
    for prod in producers_by_type(process,*producer_types_to_debug):
        prod.debug = True

# if requested, dump and exit
if dump:
    print process.dumpPython()
    sys.exit(0)
