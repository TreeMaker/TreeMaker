import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/0645E48E-8471-E511-B93F-001F29087EFC.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/08BA9786-D26F-E511-85CC-44A842CFC998.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1C7ED7CB-D46F-E511-A0A6-6C3BE5B56498.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1E7CC5E2-D46F-E511-BEC3-001F2908CFBC.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/269D24BA-E36F-E511-BE89-001E0BEC51FE.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/56A161AB-DB6F-E511-BD12-6C3BE5B5C0C0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/62A63EBA-C56F-E511-B758-6C3BE5B54138.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/661CA49C-8471-E511-B909-B499BAAC055E.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8A176097-D36F-E511-B796-001E0B486068.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8CC00F1A-0070-E511-B3E2-6C3BE5B51238.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/922FD2D3-F06F-E511-A42E-009C02AB98A6.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A6715A8C-D26F-E511-8BD2-6C3BE5B51238.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B0F52183-8471-E511-B1F4-44A842CF061A.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C2F943CB-6772-E511-8D28-001CC4A63C8E.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C62C09EE-D26F-E511-B570-6C3BE5B5F228.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CCD77DB2-C56F-E511-8AA8-44A842CFD60C.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DA0753E3-DB6F-E511-9A63-44A842CFD60C.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DED10185-2170-E511-8CCD-001CC47DEC24.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E0A3588B-D26F-E511-BE52-6C3BE5B51168.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E2CC9D4B-D46F-E511-A1CE-6C3BE5B564A8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E4086F4C-7672-E511-B93B-44A842CFD5E5.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F0292C50-7472-E511-B417-001F2908BE52.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/20A9A976-D56D-E511-944A-D4AE526A0A39.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/92F3F1B2-D56D-E511-B85C-00259021A4BE.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/CCC0C7BC-D56D-E511-91E7-6C3BE5B581A8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/DAE2F978-D56D-E511-B3BA-B499BAAC04AA.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/681CB312-CF6D-E511-8109-BC305B390A32.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/76947C0E-CF6D-E511-99C5-6C3BE5B56490.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D84D5A06-CF6D-E511-98A0-6C3BE5B55390.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/000DECB6-A86F-E511-AD25-6C3BE5B541F8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/10F2516F-AE6F-E511-AA85-44A842CFCA1A.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/12C8C79E-8471-E511-9526-44A842CFD5F2.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2808EBEE-A86F-E511-8C9A-44A842CFD619.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2AEF81F5-AE6F-E511-BB40-44A842CF05A5.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/308E5DF3-A86F-E511-9904-B499BAAC09C8.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/38D03576-AE6F-E511-A428-001CC47D3F94.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3A43196E-AE6F-E511-A43A-44A842CF0571.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/546F0258-AE6F-E511-8A67-6C3BE5B5F228.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/688F1EF4-A86F-E511-BB1C-B499BAAC0A22.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7A62FB72-AE6F-E511-862C-001F290980AE.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/84D99AEE-A86F-E511-826C-44A842CF0598.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/967644E0-D570-E511-84F6-6C3BE5B58000.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A2D56DF2-A86F-E511-B1BF-6C3BE5B5E4C0.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B0C4F6B6-D471-E511-8FA3-D8D385B0EE2E.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B8A5524F-AE6F-E511-83A3-44A842CF05E6.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DC7635CC-696E-E511-B8B6-02163E0148F2.root',
       '/store/mc/RunIISpring15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F81A04FD-A86F-E511-A617-001CC4A62CEE.root' ] );


secFiles.extend( [
               ] )

