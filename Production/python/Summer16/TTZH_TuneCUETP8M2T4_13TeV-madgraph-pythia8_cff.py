import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/0CB08F74-6550-E711-AC08-A0369F739F08.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/126CCEB6-604E-E711-99D8-C4346BBC1498.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/12AA4BEA-444E-E711-B2AD-E0071B7A8590.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/1A14F365-644E-E711-B0B8-20CF3027A582.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/20FFE4CC-4C4E-E711-A2C0-000D3AB057BF.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/44562577-5A4E-E711-A2FC-0242AC110003.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/56E50FDE-584E-E711-A70F-0025905C53F2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/5890051B-BB4D-E711-9577-0CC47A4C8EBA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/784282FA-8B4E-E711-9CEB-B499BAAC014E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/8886D9B1-334E-E711-BE1B-001E67792598.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/9035F654-5D4E-E711-A81D-3417EBE6459A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/905A7240-494E-E711-A221-90B11CBCFF4E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/ACB8BDD4-3A4E-E711-AD29-3417EBE51BD1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/C4081A19-8C4E-E711-A307-0242AC130003.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/C6C38C0E-854E-E711-A88C-0025905A609A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/CA516615-4F4E-E711-B0A1-002590207984.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/CCB60099-4F50-E711-AC55-008CFAFBFB7C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/DCD270B5-CF4E-E711-A746-00304867FEBB.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/E487D7C0-3C4E-E711-83E1-0026B9278678.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/E6E9543A-BE4E-E711-83A7-FA163EEFD873.root',
] )
