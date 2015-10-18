import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/10B3B366-4C71-E511-8364-00259074AE3C.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/16A783C4-3371-E511-8FCD-0025904C66F0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/18E11AFF-4871-E511-A1DC-0025905C2D98.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/1AE37EF6-3471-E511-81C9-0025905C3DF6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/1AEBE837-4A71-E511-B16E-0CC47A4128F8.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/1AF09B1F-3C71-E511-BD09-0025905C42B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/1E1E8EDF-3471-E511-A891-0025905C3E66.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/24C6BAEE-4A71-E511-9826-0025905C3DCE.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/26E3F8DF-3371-E511-BCC7-0025905C3DF6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/28894F8D-4171-E511-89B5-0025904C4F50.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/2AD9898D-4171-E511-A541-0025905C2CD2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/30CC881D-3C71-E511-BA63-0025905C3E66.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/347D2D0A-5071-E511-8F64-005056020789.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/38BF8917-4171-E511-A9EC-00259073E340.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/3A86F4DB-3471-E511-AA09-0025904C66F0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/427F712D-4271-E511-B3D8-0CC47A4129F4.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/46450A68-5471-E511-964E-0CC47A4DEDF2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/4AAE4CEF-3171-E511-99F9-0025905C96A6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/4CA114C7-3371-E511-8D19-0025905C3E66.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/528D1FA1-5271-E511-8DF4-3417EBE64519.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/54779932-3D71-E511-A7D6-0025905C94D0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/587B8793-C771-E511-BC4A-002590747DE2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/5A1F62A2-3371-E511-A8E9-0025905C2D98.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/5A489B9A-4271-E511-8A1B-002590574604.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/5EA4915D-4C71-E511-BF66-00259073E4B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/62627CC6-3171-E511-9BDF-0025905C9726.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/6691E847-3471-E511-B479-0025905C3D3E.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/7019EFF2-4A71-E511-A85A-0025905C2CBA.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/721844A0-3371-E511-B87F-0025905C42B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/76475342-4571-E511-92D9-0025904C66A6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/7A40E935-4171-E511-84F7-0025905C2CD0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/7E4F85A2-7571-E511-85DF-00259073E412.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/7E51FCC7-4A71-E511-A6BD-00259073E4B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/84B67B82-3271-E511-A1DE-0025905C42B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/A4E0BB7D-3E71-E511-A36B-0025905C94D0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/A82C76DF-4071-E511-882A-0CC47A4129F4.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/ACA126FF-4C71-E511-AA78-0CC47A4DEDA2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/AE69EC85-4071-E511-905D-0025904C66E6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/B2052594-3171-E511-993F-0025905C2CD2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/B4292343-4571-E511-8EF1-0025904C67B8.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/BC281F83-4371-E511-B852-0025904C66A4.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/BC72AEB4-5171-E511-9D26-00266CFAE304.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/C256AAAB-5171-E511-AB57-00266CFAE844.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/CA7EC456-4D71-E511-B675-002590747D90.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/CC19A13F-3671-E511-8C62-0025905C95F8.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/CE56C142-6571-E511-92E6-00259073E3CA.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/D0CA455C-4C71-E511-B637-0CC47A4DEDA2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/DE1A1F1B-3D71-E511-BF21-0025905C42B6.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/DEC97183-3271-E511-9D7B-0025904C66F0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/EE2C8E72-5471-E511-8426-00259073E374.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/EE5DE4BC-3C71-E511-B7CB-0CC47A4DEDF2.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/EEA2E6DC-3471-E511-B3B1-0025905C94D0.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/F036AC3E-3671-E511-83A4-0025905C3D3E.root',
       '/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/F22ABDE8-4871-E511-B3AC-0025904C6214.root' ] );


secFiles.extend( [
               ] )

