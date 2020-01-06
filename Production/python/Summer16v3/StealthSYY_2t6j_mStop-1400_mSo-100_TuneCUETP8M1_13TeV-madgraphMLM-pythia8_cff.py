import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/00A4CB3B-B805-EA11-9AB9-BC305B390A66.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/0AD31818-8D05-EA11-81F8-24BE05CE1E01.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/2EFC8CA5-3D06-EA11-B4AB-C45444922B77.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/4C216D30-B805-EA11-80A3-44A842CF05F3.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/526A3367-8A05-EA11-9136-003048F5ADEC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/5808D5C0-B805-EA11-B67C-0CC47A4DED8E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/62D0B01A-8E05-EA11-BF2B-0CC47AF973C2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/72B2D137-B805-EA11-B9B3-0CC47A1E0466.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9457FD59-8A05-EA11-AFB6-0025909081F2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/C224DA46-F705-EA11-8BF0-001E6758651B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/D4DCA531-B805-EA11-B1DB-405CFDE5759B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/D4ED8A99-9006-EA11-A9BC-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/F03020E2-B805-EA11-98E2-0025905A60B8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/F4F361ED-D006-EA11-B3E0-6CC2173D44D0.root',
] )
