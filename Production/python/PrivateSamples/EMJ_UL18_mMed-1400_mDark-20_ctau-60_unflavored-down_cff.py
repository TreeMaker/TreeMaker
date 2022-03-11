import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-11.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-12.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-14.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-15.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-16.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-17.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-18.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-19.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-20.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL18/step4_MINIAODv2_mMed-1400_mDark-20_ctau-60_unflavored-down_n-500_part-21.root',
] )
