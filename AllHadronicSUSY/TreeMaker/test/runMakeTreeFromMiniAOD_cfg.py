# Read parameters
from AllHadronicSUSY.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
#dataSetName = parameters.value("dataset","file:/pnfs/desy.de/cms/tier2/store/mc/Phys14DR/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F452BBD7-BE76-E411-B1D7-002590DB928E.root")
dataSetName = parameters.value("dataset","/store/mc/Phys14DR/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04860BAA-B673-E411-8B20-002481E0D50C.root")
global_tag = parameters.value("global_tag","")
lostlepton= parameters.value("lostlepton", False)
gammajets= parameters.value("gammajets", False)
tagandprobe= parameters.value("tagandprobe", False)
applybaseline= parameters.value("applybaseline", False)
print "***** SETUP ************************************"
print " dataSetName : "+dataSetName
print " global_tag : "+global_tag
print " storing lostlepton variables: "+str(lostlepton)
print " storing gammajets variables: "+str(gammajets)
print " storing tag and probe variables: "+str(tagandprobe)
print " Applying baseline selection filter: "+str(applybaseline)
print "************************************************"

# The process needs to be defined AFTER reading sys.argv,
# otherwise edmConfigHash fails
import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2EventSelection")

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
  outFileName="ReducedSelection",
  reportEveryEvt=5000,
  testFileName=dataSetName,
  Global_Tag=global_tag,
  numProcessedEvt=1000,
  lostlepton=lostlepton,
  gammajets=gammajets,
  tagandprobe=tagandprobe,
  applybaseline=applybaseline
  )
