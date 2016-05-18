import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/12A02AF7-7505-E611-A6F5-001E6739801B.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/1680C9CC-B404-E611-9F84-0025905C4264.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/1C12CB79-F103-E611-B5CE-B083FED024B2.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/2A69C471-B304-E611-9708-D4AE526A0922.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/2A9E50E3-550C-E611-8570-001F29089F2A.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/388F880D-6B04-E611-88D3-00266CFAE764.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/403DF3BA-E803-E611-BC94-90B11C08AD1E.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/6888AE12-7005-E611-8724-0CC47A13CEF4.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/80A5FB55-BF04-E611-A5B1-1CB72C1B63C2.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/8A8F12DD-6904-E611-90B6-0017A4771038.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/92803B35-B304-E611-8124-008CFA197B80.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/9C60CE04-CB04-E611-8B89-90B11C0506C6.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/A0366FF4-4E0C-E611-B448-0025905B858C.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/A4700CCF-4005-E611-ADE1-549F3525BF58.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/A486A58B-7005-E611-8A84-003048CB8610.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/B0510C8E-4A04-E611-947C-B083FED42A6E.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/B204F820-B204-E611-94BD-B083FED76D99.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/B41542C5-E803-E611-85DB-001E67DDC88A.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/EEACAB98-9304-E611-9CE1-0090FAA572C0.root',
       '/store/mc/RunIISpring16MiniAODv1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FC1AF137-E803-E611-AEFB-008CFAF06084.root',
] )
