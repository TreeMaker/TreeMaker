import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-1.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-10.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-2.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-3.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-4.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-5.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-6.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-7.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-8.root',
'root://hepxrd01.colorado.edu:1094///store/user/aperloff/ExoEMJAnalysis2020/Signal/2018/step4_MINIAOD_mMed-1000_mDark-10_ctau-0p1_unflavored-down_n-500_part-9.root',
] )