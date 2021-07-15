import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/0E69D734-1E09-ED41-93B9-EEFEA0F14281.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1B5D2777-2B11-4740-9671-EC561E18BB41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1F1FD02D-C1C6-3F4D-814B-899B3BBED026.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/2CDC0B04-140A-5246-8196-9FB8FFC1619E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/4038DD1B-FA0C-F74F-B617-F2B73E50D29D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/440CA798-10E9-B34A-8FEA-384AE3C6C7AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/4B0CE91A-B5FF-0545-AAD9-B6AF220A1174.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/820A90D1-5503-CA42-97E1-EC46CDB5AD5A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/9E0E970A-CEC4-3C49-ACEA-D911C4D990CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/A4A81C82-2F99-9D49-9D1C-EDA065CF1DF7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/B70578E8-985E-0B48-BB46-521F28751641.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/C58F0834-D87F-1A44-B4A3-0C2C08EBC820.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/C7618206-60BD-AF41-8D83-CF8863C4AA8B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D9768E41-B165-E641-94BB-EDA9E7B0F5ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/DA7D68AE-2B61-8B40-BE05-056174BC6191.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/E8FC17FA-A8B6-A140-9938-F85B7593C768.root',
] )
