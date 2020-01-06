import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/06C0C7E5-B404-EA11-A80A-B49691408E94.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/08D668F5-B404-EA11-89B6-B496910A868C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0AEEF4DB-B404-EA11-96CA-CCC5E5EF4F61.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0E3DE138-B404-EA11-9A34-90B11C27F8B2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1401DA20-B404-EA11-BD12-A0369FE2C170.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/1CBE662E-B404-EA11-8E18-EC0D9A0B33A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/600DFF25-B404-EA11-9058-B02628346260.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/60CF83DE-B404-EA11-8FA8-44A84225C851.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/648EB1E3-B404-EA11-90AC-C45444922D6C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9C222932-B404-EA11-8367-E0071B7A08F0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9CC67D2A-B404-EA11-9E83-1CC1DE1CF69A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B4855418-B404-EA11-BEC3-FA163ED2F081.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B8037CE1-B404-EA11-8FE4-AC1F6B0DE0A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CE7354E3-B304-EA11-90D0-0025905C54C4.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1050_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D4148C8D-B704-EA11-B25A-0CC47AA47824.root',
] )
