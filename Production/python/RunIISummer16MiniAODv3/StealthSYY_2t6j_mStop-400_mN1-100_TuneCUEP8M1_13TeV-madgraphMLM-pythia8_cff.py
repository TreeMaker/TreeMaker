import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2ABD3630-3BF0-E811-B5A4-0CC47A4D76C6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/4A9BB0CE-89EF-E811-80C9-0CC47A7C357A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5C851538-8DEF-E811-B889-0025905A60B2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8A7D43D4-83EF-E811-8F5B-0025905AA9CC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AC3F8080-6BEF-E811-8D1A-0CC47A7C35A4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B05017BC-83EF-E811-BD46-0CC47A78A458.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C46EC3F6-6AEF-E811-8BFA-0CC47A4C8F2C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E82B9840-66EF-E811-BE18-0025905A612E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/FC012AD3-66EF-E811-A07D-003048FF9ABC.root',
] )
