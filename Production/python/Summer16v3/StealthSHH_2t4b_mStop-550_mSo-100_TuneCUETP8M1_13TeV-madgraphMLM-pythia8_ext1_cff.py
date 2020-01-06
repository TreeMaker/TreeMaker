import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/108F950B-2405-EA11-8FB9-B02628341EF0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/2CB94E8E-E804-EA11-A72D-48FD8EE73ABD.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/34E48D19-2C05-EA11-AB56-002590908F8E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/3600D86C-A705-EA11-8098-00E081B705D6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/48670616-6105-EA11-A4B3-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/52FECA2F-4605-EA11-936C-0025905C54DA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/64897774-EF04-EA11-91E3-C4346BC7AAE0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/6C449490-0205-EA11-9126-00215A45F882.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/828B93D6-2305-EA11-98B9-FA163E1C8935.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/8CA0F797-3E05-EA11-A3AE-246E96D149C4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/8E0D4B1E-3C0A-EA11-AD59-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/92EA270F-E804-EA11-BDFE-0CC47AA989C6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/94E54C4E-EB04-EA11-B7CB-24BE05C3CBE1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/989B2279-1C05-EA11-B0BC-CCC5E5F2B53B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/A05CB5D6-2B05-EA11-B75A-F0D4E2E523B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/A2AD348C-6705-EA11-8E95-AC1F6BAC7D1A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/DA90AB07-EC04-EA11-B1DB-0CC47A57CD88.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/20000/F2693C99-2805-EA11-A373-A0369F7FE970.root',
] )
