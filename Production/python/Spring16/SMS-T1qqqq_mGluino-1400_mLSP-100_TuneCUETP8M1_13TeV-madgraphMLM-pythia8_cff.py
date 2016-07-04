import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/40000/F029E56B-3E37-E611-A129-6C3BE5B533A8.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/20494B05-A239-E611-AA03-0025905C43EA.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/28F3AE18-DE38-E611-83CE-002590550538.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/2A9A698C-493C-E611-A4A0-44A842CF05E6.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/487F18AE-4D3C-E611-9713-6C3BE5B52368.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/64C10841-463A-E611-8623-44A84225D0B7.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/689AA8F3-3039-E611-8071-02163E01795C.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/729FFF34-F338-E611-8269-0025905A613C.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/BADC91FD-C03A-E611-B096-0CC47A78A3EE.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/D43742CA-723C-E611-B697-6C3BE5B51168.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/D640AFE4-B43A-E611-9AA0-0242AC130005.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/FA599738-3839-E611-9BFE-02163E0139EC.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/90000/42244B93-C436-E611-9FFB-002590FD0F20.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/90000/8CF1BD0A-8236-E611-AA94-6CC2173CAAE0.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/90000/D0F0214F-8C36-E611-9870-00259090841E.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/90000/D4A4F2EF-5C37-E611-83BF-001F29082E68.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/90000/D8EAE12B-6037-E611-98C2-24BE05BD4F81.root',
] )
