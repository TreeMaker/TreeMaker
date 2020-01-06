import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/3E9CCA72-F10F-EA11-A60B-98039B3B01CA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/48D6A505-EA0F-EA11-9520-AC1F6B1E2F64.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/0E798AF2-440C-EA11-B630-AC1F6B0DE4A2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/1071BBC6-130C-EA11-BA5C-0025905A607E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/2432B1E9-9609-EA11-9568-0CC47AFF249E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/52BC141C-6C09-EA11-9E10-FA163E69C31B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/7C21352F-290C-EA11-A4C1-28924A35056E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/7E7FB36A-6C09-EA11-B171-40F2E9C6AC5E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/94B9467A-EC0E-EA11-9C60-001E67792702.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/A6672D45-6C09-EA11-B4B7-34E6D7E3879B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/D8C037AA-6C09-EA11-A619-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/EE8BC6EA-6B09-EA11-9699-20040FE8E914.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/F6408607-A80B-EA11-892F-0017A477107C.root',
] )
