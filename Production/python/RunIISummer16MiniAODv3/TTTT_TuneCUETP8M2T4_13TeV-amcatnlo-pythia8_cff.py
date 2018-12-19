import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/0411821D-BBC3-E811-98BA-0CC47A57CBBC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/04F58752-31C5-E811-94E4-00259075D706.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/188992D4-DAC3-E811-97DE-0CC47A57CBBC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/22E45026-ACC3-E811-9ECC-002590D9D956.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/2C9A77F0-B4C3-E811-9E96-0025901AEDA4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/5C14A925-D6C3-E811-89F3-0CC47A57D13E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/706F0B69-85C3-E811-8457-0CC47AA53D6A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/8A27FE9F-A0C5-E811-AA66-0CC47AA53D6E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/92E447D4-F6C2-E811-B8DD-0CC47A57D13E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/B66C5EBB-A4C5-E811-9F9B-0CC47A0AD780.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/B83BD09B-EDC2-E811-B2BF-0CC47A57CEB4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/C40D43C0-2CC3-E811-BD6F-0CC47A0AD456.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/C45BBAAC-BBC3-E811-8738-0CC47AA53D5A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/D828D6BA-F2C2-E811-BA51-002590AB3A88.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/E24257DC-D5C3-E811-9FF8-0CC47AA53D60.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/FAF8E0E9-1BC3-E811-8BC4-002590FD5A78.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/FCA73641-D6C3-E811-9098-0CC47AD24CD8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/FEDC235C-F2C2-E811-BA36-0025907859B8.root',
] )
