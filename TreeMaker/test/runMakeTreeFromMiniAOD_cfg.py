# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dataset = parameters.value("dataset","/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/12284DB9-4227-E511-A438-02163E013674.root")
#dataset = parameters.value("dataset","/store/mc/RunIISpring15DR74/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/145F5185-1019-E511-9ACA-0025901ABD1A.root")
#Phys14 MC: use CMSSW_7_2_3_patch1
#dataset = parameters.value("dataset","/store/mc/Phys14DR/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04860BAA-B673-E411-8B20-002481E0D50C.root")
outfile=parameters.value("outfile","test_run")
globaltag = parameters.value("globaltag","GR_P_V56::All")
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
applyjec=parameters.value("applyjec",False)

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
print " Applying new JECs: "+str(applyjec)
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2EventSelection")

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
  applyjec=applyjec
)

