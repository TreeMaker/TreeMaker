import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C3B472C-467C-E511-A043-001E67A401B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0E95E725-467C-E511-B30A-001E675A5262.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/10956690-467C-E511-9145-001E67A404B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/22E4A0BD-467C-E511-91A4-001E67A3FDF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/40614EAD-457C-E511-BD4C-001E67A42A71.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48A7F3C7-467C-E511-A662-001E67586629.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58962529-467C-E511-B11D-001E67A3EC2D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68FC3444-467C-E511-BE4C-001E67A3F70E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A6063BE-467C-E511-8613-001E67A40451.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A024822-467C-E511-9D92-001E67A40604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/909D467E-457C-E511-A954-001E67A402C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9253CC53-467C-E511-B060-001E67A3AEB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/984FB90A-467C-E511-979E-001E67A4069F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A8CE330B-467C-E511-BDDB-001E67A3F8A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE876E57-467C-E511-8822-001E67A401B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B05F40C4-467C-E511-B216-001E67A3FB9B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B619A5A5-457C-E511-BE21-001E67A40604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC2C5351-467C-E511-9D16-001E67A41EA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE3BB070-457C-E511-839A-001E67A404B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C03ECBA5-457C-E511-89D0-001E67A40451.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE4EE445-467C-E511-92B8-001E67A402C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D01EDB82-457C-E511-BEF9-001E675A681F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE050F8C-457C-E511-9700-001E675A6AB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E88D09C2-467C-E511-A556-001E67A40604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA74B965-467C-E511-A790-001E67A3EA7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F26C08C7-457C-E511-8663-001517F7F6A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F402D5A2-467C-E511-B4B4-001E67A402C1.root' ] );


secFiles.extend( [
               ] )

