import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0C7DDAEC-D831-E911-962A-0CC47AFB7D48.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/0E45E2F3-D731-E911-9A03-003048F5ADEE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/147E4509-DA31-E911-8DC5-AC1F6B0DE294.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2C3E7E5D-D931-E911-92B0-008CFAF558E0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3CEDFA9B-D731-E911-BFDD-FA163E212AD3.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/50328E6C-D931-E911-A1C3-44A842B451FE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5C1AA369-D831-E911-9384-509A4C748AB3.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/66504CF9-D731-E911-B6B1-00266CFFBC38.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/68BE8D5A-D931-E911-8D17-6CC2173CAAE0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/807D2D6C-D831-E911-95B0-3417EBE7047A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/82A9EF71-D831-E911-8A5F-0CC47A1DF7EE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/86C7360D-D931-E911-8762-484D7E8DF06B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/86CAC4D2-D731-E911-8AB0-001E677926E6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8AE71970-D831-E911-AB32-1866DA87931C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8E90DE94-D831-E911-8B7C-509A4C7812EC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9018FD6E-D831-E911-A2A1-D8D385AE8848.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/92151C6A-D831-E911-834D-509A4C9EF929.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B676A258-D931-E911-ACF5-14187741120B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C6D8ED5A-D831-E911-8491-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CABBD12F-D931-E911-B6D2-D48564593F96.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EC496AD4-D731-E911-897B-D4AE528FF122.root',
       '/store/mc/RunIISummer16MiniAODv3/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/281FD158-7A33-E911-A11A-40F2E9C6ADD2.root',
] )
