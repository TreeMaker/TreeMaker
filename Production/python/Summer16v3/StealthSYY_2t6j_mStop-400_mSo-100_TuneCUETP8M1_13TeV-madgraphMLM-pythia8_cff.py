import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/08862866-AB00-EA11-BE05-00266CFFBCFC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/1880E574-3A00-EA11-9D7D-40F2E9C6AC5E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/1883A2BD-58F2-E911-AC1C-FA163E41767C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/1EDED99D-5900-EA11-A75B-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/2A029A48-5A00-EA11-BF17-AC1F6B792C68.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/2CB7C4D6-5800-EA11-8B72-24BE05BD72E2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/32E1D9F4-1C01-EA11-A88C-0242AC1C0505.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/4641D540-9400-EA11-A7EF-00259090845A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/56268178-7A00-EA11-9538-CCC5E5EF4F61.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/5C48DAC2-4000-EA11-B78F-1866DA7F90B8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/6422A399-7D00-EA11-97F8-AC1F6B0DE294.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/7EC19283-34F3-E911-814C-FA163EFA93A6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/9CAD4798-5800-EA11-ACC2-008CFAC93BC8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/B4672BA9-88FF-E911-9CCC-FA163EAEE440.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/B6F4B4C2-5000-EA11-82AE-90E2BACBAA90.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/B8CA39D4-5000-EA11-8A62-A0369FC5B7B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/CC5D02D3-5000-EA11-88A3-008CFAF0842A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/CCFB8A17-B4FF-E911-8057-B083FED1321B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/DAB4EDD2-5000-EA11-BF70-0CC47AFCC372.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/FEA4636B-6A00-EA11-B0E2-7CD30AB15AD8.root',
] )
