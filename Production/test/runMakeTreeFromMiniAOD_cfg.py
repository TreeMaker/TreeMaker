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

# background estimations on by default
lostlepton=parameters.value("lostlepton", True)
hadtau=parameters.value("hadtau", True)
doZinv=parameters.value("doZinv", True)
QCD=parameters.value("QCD", True)

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
fastsim=parameters.value("fastsim",scenario.fastsim)
signal=parameters.value("signal",scenario.signal)
jsonfile=parameters.value("jsonfile",scenario.jsonfile)
jecfile=parameters.value("jecfile",scenario.jecfile)
residual=parameters.value("residual",scenario.residual)
era=parameters.value("era",scenario.era)

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("RA2EventSelection")
if era=="Run2_25ns":
    process = cms.Process("RA2EventSelection",eras.Run2_25ns)
elif era=="Run2_50ns":
    process = cms.Process("RA2EventSelection",eras.Run2_50ns)

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

#temporary redirector fix
redir="root://cmsxrootd.fnal.gov/"
#fastsim signal is phedexed to LPC Tier3
if fastsim and signal: redir="root://cmseos.fnal.gov/"
for f,val in enumerate(readFiles):
    if readFiles[f][0:6]=="/store":
        readFiles[f] = redir+readFiles[f]
    
# print out settings
print "***** SETUP ************************************"
print " dataset: "+str(readFiles)
print " outfile: "+outfile+"_RA2AnalysisTree"
print " "
print " storing lostlepton variables: "+str(lostlepton)
print " storing hadtau variables: "+str(hadtau)
print " storing Zinv variables: "+str(doZinv)
print " storing QCD variables: "+str(QCD)
print " "
print " storing PDF weights: "+str(doPDFs)
print " "
print " storing track debugging variables: "+str(debugtracks)
print " Applying baseline selection filter: "+str(applybaseline)
print " "
if scenario.known: print " scenario: "+scenarioName
print " global tag: "+globaltag
print " Instance name of tag information: "+tagname
print " Including gen-level information: "+str(geninfo)
print " Using fastsim settings: "+str(fastsim)
print " Running signal uncertainties: "+str(signal)
if len(jsonfile)>0: print " JSON file applied: "+jsonfile
if len(jecfile)>0: print " JECs applied: "+jecfile+(" (residuals)" if residual else "")
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
    lostlepton=lostlepton,
    QCD=QCD,
    applybaseline=applybaseline,
    doZinv=doZinv,
    debugtracks=debugtracks,
    geninfo=geninfo,
    tagname=tagname,
    jsonfile=jsonfile,
    jecfile=jecfile,
    residual=residual,
    doPDFs=doPDFs,
    fastsim=fastsim,
    signal=signal
)

# final tweaks to process
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.TFileService.closeFileFast = cms.untracked.bool(True)
