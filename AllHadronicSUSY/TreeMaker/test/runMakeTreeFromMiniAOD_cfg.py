# Read parameters
from AllHadronicSUSY.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dataSetName = parameters.value("dataset","/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/12284DB9-4227-E511-A438-02163E013674.root")
#dataSetName = parameters.value("dataset","/store/mc/RunIISpring15DR74/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/145F5185-1019-E511-9ACA-0025901ABD1A.root")
#Phys14 MC: use CMSSW_7_2_3_patch1
#dataSetName = parameters.value("dataset","/store/mc/Phys14DR/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04860BAA-B673-E411-8B20-002481E0D50C.root")
outFileName=parameters.value("outfile","ReducedSelection")
global_tag = parameters.value("global_tag","GR_P_V56::All")
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

print "***** SETUP ************************************"
print " outfile : "+outFileName
print " dataset : "+dataSetName
print " global_tag : "+global_tag
print " storing lostlepton variables: "+str(lostlepton)
print " storing tag and probe variables: "+str(tagandprobe)
print " storing Zinv variables: "+str(doZinv)
print " Applying baseline selection filter: "+str(applybaseline)
print " Including gen-level information: "+str(geninfo)
print " Instance name of tag information: "+tagname
if len(jsonfile)>0: print " JSON file applied: "+jsonfile
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2EventSelection")

## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
  outFileName=outFileName,
  reportEveryEvt=1000,
  testFileName=dataSetName,
  Global_Tag=global_tag,
  numProcessedEvt=numevents,
  hadtau=hadtau,
  lostlepton=lostlepton,
  tagandprobe=tagandprobe,
  applybaseline=applybaseline,
  doZinv=doZinv,
  geninfo=geninfo,
  tagname=tagname,
  jsonfile=jsonfile
)

