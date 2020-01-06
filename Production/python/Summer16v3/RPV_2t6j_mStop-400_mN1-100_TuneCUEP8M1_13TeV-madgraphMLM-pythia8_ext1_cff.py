import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/00B04800-E1FD-E911-8854-B8CA3A709648.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/0658ECD8-BBFD-E911-84D8-7CD30ACE23EC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/0C0BC5CF-83FD-E911-A4F4-C45444922BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/14CEF3B1-F3FC-E911-A1BC-98039B3B01BE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1A1DF6B4-89FD-E911-9138-00E081B18DBE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/1A857D5C-01FE-E911-A999-B499BAAC0612.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/26EB1141-E9FD-E911-BEC2-0CC47AFCC69E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/38D82417-B2FC-E911-9A9D-002590747D9C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4807C7BE-AAFD-E911-846A-008CFAC8DB40.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4A20B67E-86FD-E911-AA3E-001E67E6F42C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4CEE1CE7-40FE-E911-8224-0026B94DBDBC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/588344B4-05FE-E911-9E96-801844E560A4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/66CEDC5D-29FE-E911-8DF9-0025904A8EC8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/86E0A449-99FD-E911-A5CF-00259029E71C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8CDBDED0-B3FD-E911-82B1-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8E16C96B-D3FD-E911-91A5-1CB72C0A3A61.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9859D6DB-B3FD-E911-BEBE-0017A4770474.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/98DF842C-56FE-E911-B71B-0CC47A7452DA.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9ED6455F-89FD-E911-BD23-509A4C84EA0C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/A6E6AA9C-D6FF-E911-8886-008CFA197C38.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AA3F23EB-F0FD-E911-B68C-FA163E0F4AE9.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/AEC00B4B-FBFD-E911-8C3F-001E675A58D9.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/BEA5595C-89FD-E911-90C9-6CC2173D5F20.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/D6E0243A-87FE-E911-A6D1-509A4C9EF923.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/DE2807DD-E5FC-E911-8CA6-0090FAA57E54.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/EEFC8567-89FD-E911-A43A-B496912ED4D0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/F0E83A38-11FD-E911-B862-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/3C61A160-620D-EA11-ACCC-FA163EFA1E5D.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/6A342086-D90E-EA11-8F04-0CC47A1E0DCC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/280000/96BD168A-440D-EA11-921A-5065F381E1B2.root',
] )
