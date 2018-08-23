import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/149C88E3-56A2-E811-88D5-0242AC130002.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/160AA26D-2A9D-E811-B985-0CC47A57CD56.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/2253A52C-4A9D-E811-8C43-E0071B7AC760.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/22AC08AD-DB9C-E811-A33E-E0071B74AC10.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/24A6169A-DE9D-E811-BA85-0026B927865E.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/3A2CD623-FF9C-E811-BEEC-00266CFEFE70.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/3A55E42C-419D-E811-81A0-0CC47A5FC2A5.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/3CF5EF52-FF9C-E811-80D3-44A84225CFF0.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/4427F806-FF9C-E811-B0AE-801844E55F38.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/446621AF-E39D-E811-8569-842B2B71EDBE.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/4661DF8F-E89D-E811-ADED-008CFA197E58.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/4A078338-DE9D-E811-8D8C-782BCB4FBF56.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/52CBA9DE-FF9C-E811-974F-7CD30AD08EAE.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/56AC46C1-FF9C-E811-BEFB-A4BF0115A298.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/5C499321-009D-E811-B967-44A842CFCA34.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/62D64B11-F19D-E811-BAF8-B4969109FE2C.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/744CD876-FF9C-E811-86DE-7CD30AC03016.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/8A861C5B-FF9C-E811-A0A4-003048F5B6A9.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/9848FA10-009D-E811-A993-008CFAF7363A.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/A631A063-009E-E811-8ABD-001EC9ADD6D2.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/A649649A-E39D-E811-86B0-0CC47A4DEE0C.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/AA41917E-FF9C-E811-937E-0025905C43EC.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/B014FD34-FF9C-E811-8774-0CC47A745284.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/B0AB60A2-419D-E811-9032-002590E7E00A.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/BE622285-009D-E811-AE50-0CC47A706D70.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/C6851063-FF9C-E811-8078-A0369F5BE308.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10_ext1-v3/20000/F2A94118-009D-E811-9C4C-AC1F6B8DD1F8.root',
] )
