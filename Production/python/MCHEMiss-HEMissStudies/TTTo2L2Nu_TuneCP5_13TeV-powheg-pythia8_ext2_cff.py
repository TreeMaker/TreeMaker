import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/0023F0DC-D79D-E811-AB4C-0CC47A7FC696.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/0EEE7386-D79C-E811-B6EF-0CC47A0AD6C4.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/18F5CE06-D79C-E811-B73E-0CC47AFB80DC.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/1E1D2974-D79C-E811-9A4F-1CB72C1B6CC6.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/20526CC6-D79D-E811-A8FF-0017A4770458.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/209005FC-6B9D-E811-A6A8-0242AC130002.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/445164D0-D69C-E811-960E-0CC47A4C8E7E.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/4887695E-D79C-E811-B050-008CFA111174.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/68F255B0-D69C-E811-9AEA-5065F381D2C1.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/8652F1BE-D69C-E811-AED9-901B0E5427BA.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/90080719-D89D-E811-B3D3-44A842BECCB1.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/98B269D2-D79D-E811-B626-6C3BE5B51238.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/9CD73FE9-D69C-E811-820E-AC1F6B1E3070.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/A86019C6-D69C-E811-AA47-002590E7E010.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/AE1D1D1D-279D-E811-B276-A4BF01158888.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/B6E06EF5-459D-E811-A233-002590DE6E74.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/B811E5ED-D69C-E811-9A5E-A4BF0101F533.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/BA627394-309D-E811-BCB9-D4AE5269DC07.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/BC9656B0-D79D-E811-A46D-90E2BACBAA90.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/C43F0CAB-D69C-E811-BDA3-B4969109FDFC.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/CEFD2077-F69C-E811-8880-0CC47A13CD9C.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/DA8D4DC7-D79D-E811-97DE-002590766A2A.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/EA2DB6E2-6B9E-E811-B9BD-A0369FD0B2EA.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/ECAF50B8-D79D-E811-90D2-FA163E21FCC0.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/ECB414C2-D79D-E811-AEED-3CFDFE636600.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/F23DA2BB-D69C-E811-9E58-509A4C730E2E.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/FE385804-179D-E811-808B-1866DAEA8220.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/20000/FEF9330C-D79C-E811-B92A-F04DA275BFEC.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/40000/10036583-5CA4-E811-B172-EC0D9A0B30A0.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/40000/2EAF14F7-9FA5-E811-977D-0CC47AB0B826.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/40000/6E3BCA0B-A0A5-E811-BD4F-0026182FD776.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/40000/A84479AD-35A4-E811-90CD-B4969109F230.root',
       '/store/mc/RunIISpring18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1/40000/CED0F5A9-86A5-E811-988F-AC1F6B1AF140.root',
] )
