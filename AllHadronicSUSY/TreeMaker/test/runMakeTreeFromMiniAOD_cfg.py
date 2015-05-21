# Read parameters
from AllHadronicSUSY.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
#dataSetName = parameters.value("dataset","file:/data3/store/user/borzou/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU20bx25_POSTLS170_V5AN1-miniAOD706p1/141014_155652/0000/miniAOD-prod_PAT_9.root")
#dataSetName = parameters.value("dataset","/store/mc/Phys14DR/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/00C90EFC-3074-E411-A845-002590DB9262.root")


#dataSetName = parameters.value("dataset","/store/mc/Phys14DR/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/4836AA58-5A6B-E411-8865-20CF305B053E.root")
dataSetName = parameters.value("dataset","/store/mc/Phys14DR/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/829D372D-7F6B-E411-81B1-0025907B5048.root")
#dataSetName = parameters.value("dataset","/store/mc/Phys14DR/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/C43D68C5-8D6B-E411-B030-0025907750A0.root")



#global_tag = parameters.value("global_tag","")
global_tag = parameters.value("global_tag","PHYS14_25_V1::All") # Ahmad 
lostlepton= parameters.value("lostlepton", True)
gammajets= parameters.value("gammajets", True)
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

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeTreeFromMiniADO
makeTreeTreeFromMiniADO(process,
  outFileName="ReducedSelection",
  reportEveryEvt=5000,
  testFileName=dataSetName,
  Global_Tag=global_tag,
  numProcessedEvt=-1,
  lostlepton=lostlepton,
  gammajets=gammajets,
  tagandprobe=tagandprobe,
  applybaseline=applybaseline,
  LowPtJets=True
  )
