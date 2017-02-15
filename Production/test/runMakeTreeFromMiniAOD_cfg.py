import sys

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
scenarioName=parameters.value("scenario","")
inputFilesConfig=parameters.value("inputFilesConfig","")
dataset=parameters.value("dataset",[])
nstart = parameters.value("nstart",0)
nfiles = parameters.value("nfiles",-1)
numevents=parameters.value("numevents",-1)
reportfreq=parameters.value("reportfreq",1000)
outfile=parameters.value("outfile","test_run")
dump=parameters.value("dump",False)

# background estimations on by default
lostlepton=parameters.value("lostlepton", True)
hadtau=parameters.value("hadtau", True)
hadtaurecluster=parameters.value("hadtaurecluster", 1)
doZinv=parameters.value("doZinv", True)

# compute the PDF weights
doPDFs=parameters.value("doPDFs", True);

# other options off by default
debugtracks=parameters.value("debugtracks", False)
applybaseline=parameters.value("applybaseline", False)
gridcontrol=parameters.value("gridcontrol", False)

# auto configuration for different scenarios
from TreeMaker.Production.scenarios import Scenario
scenario = Scenario(scenarioName)

# take command line input (w/ defaults from scenario if specified)
globaltag=parameters.value("globaltag",scenario.globaltag)
tagname=parameters.value("tagname",scenario.tagname)
geninfo=parameters.value("geninfo",scenario.geninfo)
pmssm=parameters.value("pmssm",scenario.pmssm)
fastsim=parameters.value("fastsim",scenario.fastsim)
signal=parameters.value("signal",scenario.signal)
jsonfile=parameters.value("jsonfile",scenario.jsonfile)
jecfile=parameters.value("jecfile",scenario.jecfile)
residual=parameters.value("residual",scenario.residual)
jerfile=parameters.value("jerfile",scenario.jerfile)
pufile=parameters.value("pufile",scenario.pufile)
era=parameters.value("era",scenario.era)

#temporary redirector fix
#fastsim signal is phedexed to LPC Tier3
redir=parameters.value("redir", "root://cmseos.fnal.gov/" if fastsim and signal else "root://cmsxrootd.fnal.gov/")

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("RA2EventSelection")
if len(era)>0:
    process = cms.Process("RA2EventSelection",getattr(eras,era))

# configure geometry & conditions
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

# Load input files
readFiles = cms.untracked.vstring()

if inputFilesConfig!="" :
    if nfiles==-1:
        process.load("TreeMaker.Production."+inputFilesConfig+"_cff")
        readFiles.extend( process.source.fileNames )
    else:
        readFilesImport = getattr(__import__("TreeMaker.Production."+inputFilesConfig+"_cff",fromlist=["readFiles"]),"readFiles")
        readFiles.extend( readFilesImport[nstart:(nstart+nfiles)] )

if dataset!=[] :    
    readFiles.extend( [dataset] )

for f,val in enumerate(readFiles):
    if readFiles[f][0:6]=="/store":
        readFiles[f] = redir+readFiles[f]
    
# print out settings
print "***** SETUP ************************************"
print " dataset: "+str(readFiles)
print " outfile: "+outfile+"_RA2AnalysisTree"
print " "
print " storing lostlepton variables: "+str(lostlepton)
print " storing hadtau variables: "+str(hadtau)+" w/ reclustering "+str(hadtaurecluster)
print " storing Zinv variables: "+str(doZinv)
print " "
print " storing PDF weights: "+str(doPDFs)
print " "
print " storing track debugging variables: "+str(debugtracks)
print " Applying baseline selection filter: "+str(applybaseline)
print " "
print " scenario: "+scenarioName
print " global tag: "+globaltag
print " Instance name of tag information: "+tagname
print " Including gen-level information: "+str(geninfo)
print " Including pMSSM-related information: "+str(pmssm)
print " Using fastsim settings: "+str(fastsim)
print " Running signal uncertainties: "+str(signal)
if len(jsonfile)>0: print " JSON file applied: "+jsonfile
if len(jecfile)>0: print " JECs applied: "+jecfile+(" (residuals)" if residual else "")
if len(jerfile)>0: print " JERs applied: "+jerfile
if len(pufile)>0: print " PU weights stored: "+pufile
print " era of this dataset: "+era
print "************************************************"

from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
process = makeTreeFromMiniAOD(process,
    outfile=outfile+"_RA2AnalysisTree",
    reportfreq=reportfreq,
    dataset=readFiles,
    globaltag=globaltag,
    numevents=numevents,
    hadtau=hadtau,
    hadtaurecluster=hadtaurecluster,
    lostlepton=lostlepton,
    applybaseline=applybaseline,
    doZinv=doZinv,
    debugtracks=debugtracks,
    geninfo=geninfo,
    pmssm=pmssm,
    tagname=tagname,
    jsonfile=jsonfile,
    jecfile=jecfile,
    residual=residual,
    jerfile=jerfile,
    pufile=pufile,
    doPDFs=doPDFs,
    fastsim=fastsim,
    signal=signal,
    scenario=scenarioName
)

# final tweaks to process
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.TFileService.closeFileFast = cms.untracked.bool(True)

# if requested, dump and exit
if dump:
    print process.dumpPython()
    sys.exit(0)
