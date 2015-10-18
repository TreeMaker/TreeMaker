import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3ABB7937-EB6D-E511-8A51-44A842CF057E.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/521010DC-ED6D-E511-AB5E-44A842CFC9BF.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/5415A069-EC6D-E511-9A1C-44A842CF05B2.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/546955FF-ED6D-E511-A7A5-44A842CFC9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/5C5ACA4B-ED6D-E511-B285-44A842CF05BF.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/789DA363-ED6D-E511-9DB3-6C3BE5B50180.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7ABCCE68-EC6D-E511-8048-44A842CF0634.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/98BB8A4A-EB6D-E511-ABE2-6C3BE5B50180.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9C1D997D-EE6D-E511-9FFF-6C3BE5B5F0A0.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A661B9DF-EB6D-E511-958E-6C3BE5B5F0A0.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AA21C16C-ED6D-E511-BDCB-44A842CF05F3.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AEC4363C-ED6D-E511-BC4D-44A842CFC9F3.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B6348C55-ED6D-E511-A611-6C3BE5B5C0B0.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B813F755-EC6D-E511-8548-44A842CFC9BF.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B85B3EAE-EB6D-E511-AE90-009C029C178C.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BE1763B2-EC6D-E511-B5D7-6C3BE5B59050.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BE56460C-EE6D-E511-850A-44A842CFC9E6.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CA78484B-ED6D-E511-A05F-44A842CF061A.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CEFC4F22-EB6D-E511-AF90-44A842CFC9BF.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DC79D599-EA6D-E511-BF88-6C3BE5B564A8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E03361B7-EC6D-E511-9E0A-6C3BE5B50178.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E0676537-EE6D-E511-B343-44A842CF05B2.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E4109AC5-EC6D-E511-BA58-6C3BE5B564A8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E8DBDFD2-ED6D-E511-A780-6C3BE5B594A8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F442936C-EC6D-E511-B863-44A842CFC9E6.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F636F146-EB6D-E511-BCB6-6C3BE5B594A8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FC41368A-ED6D-E511-BCEB-44A842CF0634.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FE9903E5-ED6D-E511-9100-009C029C178C.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/08B7F443-026F-E511-A80A-6C3BE5B58058.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/0C810E2A-026F-E511-9308-6C3BE5B58058.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/129CE667-026F-E511-BA9B-6C3BE5B593F8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/2C5EF17A-036F-E511-8F99-6C3BE5B593F8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/4A38D260-036F-E511-A60C-44A842CFCA27.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/6465B9C3-BB70-E511-8682-44A842CF05D9.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/6652F256-026F-E511-AFB1-6C3BE5B56498.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/6AA78E8A-016F-E511-994A-44A842CF05CC.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/7A05E14A-086F-E511-8987-B499BAAC09C8.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/8224E754-036F-E511-95E3-A0B3CCE45C2A.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/9C118B32-026F-E511-B3AA-6C3BE5B50210.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/A0FDD5C3-036F-E511-9974-6C3BE5B51238.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/A4CFDD4B-026F-E511-B0A4-44A842CFD5F2.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/B4433029-036F-E511-B628-44A842CFD619.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/B4FBCC2F-026F-E511-B33F-44A842CFC9D9.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/C6C5686C-026F-E511-9103-44A842CFD640.root',
       '/store/mc/RunIISpring15MiniAODv2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/F86D47FD-036F-E511-9424-6C3BE5B58198.root' ] );


secFiles.extend( [
               ] )

