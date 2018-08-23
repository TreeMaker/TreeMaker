import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/02091571-8D9C-E811-BF6A-3417EBE64BB5.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/0222148B-8D9C-E811-9C3E-0242AC1C0500.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/0AAEBFF5-8D9C-E811-AF6F-0019B9CB02FE.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/0AB23458-6C97-E811-9BD6-0CC47A6C1864.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/1A93E1A6-309B-E811-B441-10983627C3DB.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/2413BA4E-D99C-E811-89D0-801844DEF4C0.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/288CAE12-4A97-E811-BCC1-0CC47A4C8E5E.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/2E4E2615-319B-E811-A468-002590DE6E92.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/30005FD5-1A9B-E811-A5E4-008CFAC91CD0.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/3247A65D-0296-E811-AB2B-0CC47A4C8EC6.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/364CD1FB-2F9B-E811-8373-0CC47A4C8ECA.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/38BBEBC9-309B-E811-A922-0CC47AFB80D8.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/400C4B6B-319B-E811-902C-008CFA56D58C.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/56165405-9B96-E811-9966-A0369FE2C210.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/6CE17841-319B-E811-94D8-0CC47A57CBCC.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/6E8056E0-B297-E811-B92B-A4BF01159190.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/6ED018D2-6E9B-E811-84F2-20474791DE54.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/72245C85-8D9C-E811-A7BF-F01FAFD69094.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/7846F701-CC9B-E811-802F-EC0D9A0B3260.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/8CF6E8A6-309B-E811-8D31-001E67504445.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/8EB8BC7B-249F-E811-97C9-0242AC130002.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/92024F6A-319B-E811-B85B-0025901D094A.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/96D8B8C1-229B-E811-A2E0-008CFAC93C88.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/988E2270-8D9C-E811-AF13-44A842CFD5E5.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/9E0E449F-309B-E811-B2EE-0017A477044C.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/A4893E55-5D97-E811-9090-0025905B857C.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/A66F0B48-8D9C-E811-AFC9-5065F37D7172.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/B0ED65FE-559A-E811-8D0D-549F3525A184.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/B2A39E19-9496-E811-80EE-A0369FE2C206.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/B82ACE71-8D9C-E811-9B76-002590DE6E8A.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/BE0A5293-309B-E811-BF1C-246E96D10C28.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/D6D49D92-A39B-E811-93A4-0CC47A4D9A72.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/DA76F268-329B-E811-92D2-00266CFFBF50.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/ECB815C7-2F9B-E811-82A7-FA163EE353A4.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/EE7FD302-319B-E811-AFED-AC1F6B0DE140.root',
       '/store/mc/RunIISpring18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v1/20000/FE369B14-319B-E811-9281-001E67792488.root',
] )
