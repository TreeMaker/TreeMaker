import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/306372CE-3E74-E511-9F2B-008CFA0A5684.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/54B28AB6-3E74-E511-8EF6-549F35AF44C9.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6291D191-3E74-E511-B96E-008CFA14F814.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A663B2B3-3E74-E511-B357-008CFA580920.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AA62736D-3E74-E511-B9B0-549F35AD8BA2.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C4BD6CE0-3E74-E511-8866-008CFA0A59E0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FAB9C3E3-3E74-E511-ADF0-008CFA1CB55C.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FC77A0DD-3E74-E511-A5C2-549F35AC7E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/0833AD46-B174-E511-89E6-549F35AD8B95.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/0A27C6F2-A574-E511-981F-549F35AD8BF0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/0CDEEBB3-AB74-E511-B795-008CFA1983E0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/180486FC-AA74-E511-9EEF-549F358EB7E4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/1C3704FC-AA74-E511-99E6-549F35AD8BBC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/1ED209F5-AF74-E511-80E5-549F35AD8B95.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/2657A7CA-A574-E511-B922-549F358EB7B0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/26E5F2AF-A574-E511-B1C9-549F35AF44F0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/407C13B5-AB74-E511-B8DC-008CFA1980B8.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/4E9AE9B2-AB74-E511-B307-549F35AE500A.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/662FB0EF-A574-E511-9E1D-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/68C5AEB2-AB74-E511-B559-549F358EB73B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/68DDC7FA-AA74-E511-8D31-A0369F739F08.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/6AA8A6B2-AB74-E511-A34A-008CFA1C64B0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/6CA83EFB-AA74-E511-B19F-549F35AD8B7B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/7A46D8F6-AF74-E511-923A-549F35AD8BBC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/7E2C53F6-AF74-E511-9777-549F35AD8B88.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/962943FB-AA74-E511-A2C6-549F35AD8B7B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/9E7E83DC-BD74-E511-9ECC-008CFA582D78.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/A2B412EF-A574-E511-A0D8-549F35AD8B88.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/A6896DF7-AF74-E511-AC1D-549F358EB7D7.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/B0E971F7-AF74-E511-A171-549F35AD8B7B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/B6FC2AC6-A574-E511-8094-008CFA1CB740.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/BAA511F6-AF74-E511-B59B-549F35AE4FFD.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/C60D96F8-AF74-E511-B5D5-008CFA111200.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/CA1EDBFD-AF74-E511-866C-549F35AD8B7B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/CCF23DB0-AB74-E511-BB9A-549F35AD8B95.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D6369EB1-AB74-E511-9CC1-549F358EB7A3.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D6795B56-B174-E511-A269-549F358EB73B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D6C375F8-AF74-E511-AAE1-008CFA111200.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/DA3DAEFB-AA74-E511-AB2E-549F35AD8B88.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/F2A1FFF6-AF74-E511-AD8B-549F35AD8B88.root' ] );


secFiles.extend( [
               ] )

