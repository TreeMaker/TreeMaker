import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/04AC2C2D-C46D-E511-AEB8-003048FFD7BE.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/12B9DE92-C36D-E511-BA27-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/16FBDA59-C46D-E511-AA43-0025905B861C.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/1CC9912E-C46D-E511-8642-002590596468.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/220B892B-C46D-E511-91F6-0025905B85D6.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2219A98A-C36D-E511-B28E-0026189438D8.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/22EC7229-C46D-E511-BD2D-0026189438E6.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/24C11A23-C46D-E511-A127-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3890FE8E-C36D-E511-AC83-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3CAE702C-C46D-E511-9B4D-003048FFD728.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3CF29A27-C46D-E511-B80F-0026189438C9.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3E049CB7-C46D-E511-8EB6-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4016BCED-C36D-E511-B9E4-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/44938331-C46D-E511-A178-003048FFD7A2.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4C2CBB8B-C36D-E511-B4D2-0025905A60A6.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4EA27D92-C36D-E511-9704-0025905A60E0.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4EA73292-C36D-E511-B0D1-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/56C4542C-C46D-E511-AC94-003048FFCB9E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/602E7D5D-C46D-E511-B4EC-0025905A611C.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/66EBCF2E-C46D-E511-BCFD-003048FFD770.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6AF73EB4-C46D-E511-8872-0025905A60B0.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/707C912C-C46D-E511-80A7-0025905A497A.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/70B5792E-C46D-E511-8B11-003048FFD732.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/721CE88E-C36D-E511-80E4-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/745F1E77-C46D-E511-A6E2-0025905B8576.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8C9B252B-C46D-E511-B418-003048FFD796.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8CE4F292-C36D-E511-AABF-0025905938A4.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9271F08E-C36D-E511-B893-0025905A6136.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A022492B-C46D-E511-BD18-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A23FC72E-C46D-E511-AE9C-003048FFCBA8.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/AA5CE28F-C36D-E511-AFD9-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B448B331-C46D-E511-AF75-003048FFCBA4.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BA24252E-C46D-E511-9E98-003048FFCB74.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C0C4662D-C46D-E511-AD3D-0025905A60DE.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/CCDE99B5-C46D-E511-B67E-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D0102E92-C36D-E511-97BC-0025905A606A.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D04BD5FA-C36D-E511-B819-0025905A60DE.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/DA6D2A29-C46D-E511-9F34-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/DE20AC2C-C46D-E511-BD54-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E0B22AB0-C46D-E511-A719-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E27F4B2F-C46D-E511-8DC9-0025905B85D0.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E4226A25-C46D-E511-A4A4-002618943967.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E6F2BF8A-C36D-E511-9D83-0026189438D8.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/EA68200A-C46D-E511-AFCE-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/EEE98EC0-C46D-E511-845C-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/FED2A32B-C46D-E511-B3EE-003048FFCB6A.root' ] );


secFiles.extend( [
               ] )

