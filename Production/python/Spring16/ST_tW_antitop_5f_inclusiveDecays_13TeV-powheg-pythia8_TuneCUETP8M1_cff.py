import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/10B2302E-DA08-E611-884E-001E67DDD348.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/16D82C80-6607-E611-A9A4-0002C94CD0BC.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/1CB53CA5-6B08-E611-9683-00259075D72E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/1E556A19-9B08-E611-847A-0090FAA57F14.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/2A72AFEE-6B08-E611-942B-002590D9D8C4.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/2C50190A-BC07-E611-860B-0CC47A6C1054.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/3A00C199-C508-E611-8C97-90B11C08AD1E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/42E67F66-6607-E611-AC04-24BE05CECB71.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/4C3D1DCB-7508-E611-9B8A-002590791D36.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5032141D-BC07-E611-9192-00259075D72C.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/566A7173-6607-E611-9B1E-0002C94CDAF6.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5CC1A0B5-8807-E611-B19C-001E67A3EC2D.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/620956AB-6B08-E611-86A9-002590D9D9F6.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/68371CB1-6B08-E611-8E7C-002590FD5694.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/6EFB94B9-6B08-E611-A959-0CC47A57CC42.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/765F04BE-C307-E611-9685-00259048AC9A.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/76E190A2-6B08-E611-88F0-0CC47A0AD3BC.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/80C3F760-8807-E611-A3E0-002590E3A0EE.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/848D8273-9E08-E611-896E-002590D9D8C0.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/94746AF0-BB07-E611-BE2C-008CFA111294.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/9EC9240F-7507-E611-A1D2-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/AE74D6E7-5F09-E611-8903-14187741120B.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/B652CFF4-BB07-E611-8564-0002C94D54EC.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/BC824CA5-6B08-E611-9AAF-00259075D72E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/BE185C63-6607-E611-B4FD-0002C94CD2A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/C41B08A8-6B08-E611-A11D-00259048AC9A.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/D2A51794-8807-E611-AEAB-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/D8CF610E-BC07-E611-822B-0002C94CDA12.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/DC028DE7-7508-E611-9F47-0025907D244A.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/E8F33C65-8807-E611-BD75-0002C94CD11E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F037B427-BC07-E611-9CF4-001E67DFF6E0.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FE5CD6FF-BB07-E611-A35A-A4BADB0F5175.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/008F30FA-5C06-E611-982D-00259073E3E4.root',
] )
