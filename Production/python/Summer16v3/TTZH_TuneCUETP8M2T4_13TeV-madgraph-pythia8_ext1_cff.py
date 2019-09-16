import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0C71120A-8E33-E911-8011-28924A33B9AA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2481DC76-8E33-E911-89A3-EC0D9A0B30A0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/24A6DB0C-8E33-E911-B80A-20CF3027A6DB.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C1BC5F6-8D33-E911-82F1-0CC47AFF02F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2CD3332A-8E33-E911-9607-B02628346770.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3489777D-8E33-E911-B67B-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/348C15E2-8D33-E911-885A-002481DE4BF0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3C36423A-8E33-E911-B7A7-FA163ECF2A31.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/525BA131-8E33-E911-8DEB-A0369FE2C1A8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/54D7370E-8E33-E911-97CB-68CC6EA5BE0A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5C152C0B-8E33-E911-8EA2-1866DA87B0FE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7CBDDD81-8E33-E911-AE67-0CC47AA989BA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/984583A1-8E33-E911-A6C9-AC1F6BB17808.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9E3B1938-8E33-E911-B084-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A460730D-8E33-E911-B671-B083FED13C9E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/AAAEA7FC-8E33-E911-91D6-0CC47A4C8EB6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B0D689D4-8D33-E911-8F76-F04DA274BBF6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C4D98D4F-8E33-E911-AC4B-008CFAEEAD4C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CE829D2D-8E33-E911-B01D-A4BF011596BC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/DA9CBCA1-8E33-E911-B42B-14187741212B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/E04F000F-8E33-E911-BB90-509A4C748064.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/E25E7EDF-8D33-E911-8123-24BE05C46B11.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EA9BC610-8E33-E911-ACB9-B499BAAC0270.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EC404405-8E33-E911-97CD-549F35AF4495.root',
       '/store/mc/RunIISummer16MiniAODv3/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EEB3D07B-8E33-E911-8177-14187727F981.root',
] )
