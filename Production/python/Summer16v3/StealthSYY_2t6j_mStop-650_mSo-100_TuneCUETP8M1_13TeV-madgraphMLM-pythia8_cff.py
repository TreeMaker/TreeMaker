import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/2EB884F3-5005-EA11-9B16-008CFA197C70.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/324E7348-5005-EA11-BCE8-0025905C3D3E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/5A9D6F01-5105-EA11-B4D9-F01FAFD68FB4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/883891E9-5005-EA11-8717-EC0D9A8221D6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9A95AADE-5005-EA11-8CD4-44A842CFCA27.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9E36BDD6-5005-EA11-B86D-00259090821E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9ECE80EE-5005-EA11-AFFF-1418774124DE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/A66EBD5F-5005-EA11-9375-A0369FE2C204.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/B81A48DF-5005-EA11-BFD6-0CC47A5FA211.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/C8D21B31-B805-EA11-97FA-0025902D14EA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/D01F9ED0-5005-EA11-B042-509A4C9EF924.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/EE97756C-C905-EA11-BD95-008CFAFBE046.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/FA0A603A-5105-EA11-A0F9-0242AC1C0501.root',
] )
