# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dataset = parameters.value("dataset","/store/data/Run2015C/HTMHT/MINIAOD/PromptReco-v1/000/254/096/00000/66E02E54-9145-E511-8BB1-02163E01476F.root")
#dataset = parameters.value("dataset","/store/mc/RunIISpring15DR74/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/145F5185-1019-E511-9ACA-0025901ABD1A.root")
#Phys14 MC: use CMSSW_7_2_3_patch1
#dataset = parameters.value("dataset","/store/mc/Phys14DR/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04860BAA-B673-E411-8B20-002481E0D50C.root")
outfile=parameters.value("outfile","test_run")
globaltag = parameters.value("globaltag","74X_dataRun2_Prompt_v1")
lostlepton= parameters.value("lostlepton", False)
tagandprobe= parameters.value("tagandprobe", False)
hadtau= parameters.value("hadtau", False)
applybaseline= parameters.value("applybaseline", False)
doZinv=parameters.value("doZinv", False)
gridcontrol=parameters.value("gridcontrol", False)
numevents=parameters.value("numevents",-1)
geninfo=parameters.value("geninfo",False)
tagname=parameters.value("tagname","RECO")
jsonfile=parameters.value("jsonfile","")
jecfile=parameters.value("jecfile","")
residual=parameters.value("residual",False)
era=parameters.value("era","Run2_25ns")
QCD=parameters.value("QCD", False)

print "***** SETUP ************************************"
print " outfile : "+outfile
print " dataset : "+dataset
print " global tag : "+globaltag
print " storing lostlepton variables: "+str(lostlepton)
print " storing hadtau variables: "+str(hadtau)
print " storing tag and probe variables: "+str(tagandprobe)
print " storing Zinv variables: "+str(doZinv)
print " Applying baseline selection filter: "+str(applybaseline)
print " Including gen-level information: "+str(geninfo)
print " Instance name of tag information: "+tagname
if len(jsonfile)>0: print " JSON file applied: "+jsonfile
if len(jecfile)>0: print " JECs applied: "+jecfile+(" (residuals)" if residual else "")
print " era of this dataset: "+era
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("RA2EventSelection")
if era=="Run2_25ns":
    process = cms.Process("RA2EventSelection",eras.Run2_25ns)
elif era=="Run2_50ns":
    process = cms.Process("RA2EventSelection",eras.Run2_50ns)

## configure geometry & conditions
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
process = makeTreeFromMiniAOD(process,
  outfile=outfile,
  reportfreq=1000,
  dataset=dataset,
  globaltag=globaltag,
  numevents=numevents,
  hadtau=hadtau,
  lostlepton=lostlepton,
  tagandprobe=tagandprobe,
  applybaseline=applybaseline,
  doZinv=doZinv,
  geninfo=geninfo,
  tagname=tagname,
  jsonfile=jsonfile,
  jecfile=jecfile,
  residual=residual,
  QCD=QCD
)

