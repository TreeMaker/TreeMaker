import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/209E6B38-ECE4-E811-91B3-00259074AE3A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3CD820E3-17E5-E811-B3A6-20CF3027A702.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/40142754-FCE4-E811-BF88-00259073E50C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B034246C-0BE5-E811-B5F6-20CF305B05AE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BE6F12B3-23E5-E811-AFD8-0CC47A1DF80A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CADB8FA4-ECE4-E811-9070-0CC47A1E0DCE.root',
] )
