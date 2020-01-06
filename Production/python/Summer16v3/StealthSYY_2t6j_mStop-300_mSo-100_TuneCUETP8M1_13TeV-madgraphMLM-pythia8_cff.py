import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/00A91809-4900-EA11-8624-002590DD7E50.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/0409FCBA-1C01-EA11-BEFA-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/06B1A113-7A00-EA11-AB57-0CC47A78A440.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/1E8398BA-EBF2-E911-BC65-FA163ECFA5FE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/261F6CCC-9A00-EA11-8BD4-001F2908CFBC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/3485B85F-5100-EA11-B3BA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/48F280C0-1EF2-E911-AAC6-FA163E723F18.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/4EADDE99-5900-EA11-98F1-0CC47AD9901E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/52F34099-72FF-E911-8303-FA163E76CDC2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/56266F25-3A00-EA11-9EBE-549F35AF4495.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/5ECFAE40-6A00-EA11-B967-509A4C84EADC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/7E537D7C-4300-EA11-989A-0025905C2D9A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/88D0A1E8-6200-EA11-B243-A4BADB22A4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/924B8EE2-6BFF-E911-8BEF-E0071B73C630.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/9E714E2E-3200-EA11-BE95-A4BF010114DB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/AE6E066D-D300-EA11-A3EB-001E67E71BF5.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/B2BB043B-9300-EA11-B87C-00259090833A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/C4965A2B-5B00-EA11-9609-AC1F6BB17570.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/D0FCC599-7D00-EA11-8B9F-AC1F6B0DE294.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E0213876-5900-EA11-84B4-509A4C845414.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E0C82A90-AA00-EA11-8C87-0CC47A5FC67D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E83B3C6C-6A00-EA11-B55E-008CFAE45300.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F848DAF4-4900-EA11-8AFD-68CC6EA5BE7A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F8F1342A-7A00-EA11-BDEC-B083FED03632.root',
] )
