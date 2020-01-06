import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1230A77C-4C07-EA11-98A8-00269E95B014.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1C431B9B-4C07-EA11-B83D-0CC47A706FFE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/26FFBC79-4C07-EA11-9505-28924A33B9AA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3CFE287B-4C07-EA11-91A7-48FD8EE73AE5.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/42F1BA6D-4C07-EA11-AAA4-0CC47A6C1864.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4889B3EF-4C07-EA11-B378-34800D4F9410.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/62D5EB74-4C07-EA11-93CC-F4E9D4AF0AF0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/760107A1-4C07-EA11-9DF5-6CC2173D5F20.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/7607FA7F-4C07-EA11-A53C-0CC47AFF02FC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A8C84A9B-4C07-EA11-B08B-D4856459AE7C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AA24F420-4C07-EA11-AD06-001E67792742.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AE6E8F64-4C07-EA11-B859-24BE05C6C7F1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B459157A-4C07-EA11-9C18-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/CE457E29-4C07-EA11-BF1B-AC1F6B8DBEC2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/DA0B1F7F-4C07-EA11-9596-782BCB78621B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/ECB1727D-4C07-EA11-BD82-00259090763A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/FC5F9F7E-4C07-EA11-9C16-0CC47A7C3572.root',
] )
