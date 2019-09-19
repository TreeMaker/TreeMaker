import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/1CF62A29-392F-E911-A46E-842B2B42C162.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/241AB667-2F2F-E911-9ADB-001E67792488.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/245C1558-2F2F-E911-9C4E-0025904C66A6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/2AAEA91B-2F2F-E911-909C-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/40E118FF-332F-E911-B600-00269E95B014.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/486BC966-2F2F-E911-AFFF-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/5EDD112D-2F2F-E911-B4F8-002590D9D8AC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/602DA620-A02F-E911-A390-0026B94DBE31.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/6AAAE601-432F-E911-95E3-0CC47AD9901C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/78AEE658-2F2F-E911-BA37-AC1F6B1AF03C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/80DE7875-2F2F-E911-81B2-44A84225C7BB.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/82B94C13-3B2F-E911-B9BF-002590E7DE26.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/8A4F4CBD-2F2F-E911-9FA0-405CFDFF480E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/8A977A4C-2F2F-E911-BE9D-D067E5F9156C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/9617656C-392F-E911-A71C-0CC47A7FC72C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/A4235BEA-6033-E911-89FF-AC1F6B0F7196.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/B411735F-2F2F-E911-B445-B02628343630.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/C43C6807-2F2F-E911-ACED-FA163EABB05B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/D28C4323-392F-E911-8772-24BE05CEEDB1.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/E2E1B870-392F-E911-A2F4-44A842CF0627.root',
       '/store/mc/RunIISummer16MiniAODv3/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/90000/E6AA1DC6-2F2F-E911-84F6-008CFA0A5914.root',
] )
