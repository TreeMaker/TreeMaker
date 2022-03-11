import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-1.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-10.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-2.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-3.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-4.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-5.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-6.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-7.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-8.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-10_ctau-0p1_unflavored-down_n-500_part-9.root',
] )
