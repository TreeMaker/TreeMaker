import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

readFiles.extend( [
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch1_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch2_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch3_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch5_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch6_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch7_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch8_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch9_MiniAODv2.root',
'/store/user/lpcsusyhad/SusyRA2Analysis2015/T1ttbb/T1ttbb_1300_5_batch10_MiniAODv2.root',
] )

secFiles.extend( [
               ] )