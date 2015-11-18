import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/04DA3CC8-1F7F-E511-B898-C81F66B782DD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/066D1D2A-207F-E511-9356-D4AE527EEA1F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0867C180-1F7F-E511-964F-02163E01617F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0AB8CBAA-1F7F-E511-B6A9-0026B9457805.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0EBF1C35-207F-E511-95E9-001D091C6771.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/10EB30A3-1F7F-E511-A13E-B083FED046D9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/12E4982B-207F-E511-A941-D4AE527EEA1F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1CC8672D-207F-E511-9222-782BCB67A0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E19A2AA-1F7F-E511-8278-842B2B1807B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/22B2612A-207F-E511-92A3-842B2B1814F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/323A7EA3-1F7F-E511-AA7C-D4AE526567E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3A76F0A1-1F7F-E511-B64C-B083FECF83AB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3CFE83A2-1F7F-E511-9E81-B083FED42488.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/404F70A2-1F7F-E511-BAF7-D4AE526DF80A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4AA73228-207F-E511-93FE-00259074AE52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/50F542A6-1F7F-E511-9352-02163E00EA4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/546CF6A4-1F7F-E511-96C1-D4AE526DF090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/56039B2A-207F-E511-A778-782BCB678096.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/66821F2B-207F-E511-9D3D-D4AE526DF090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6A1770A1-1F7F-E511-8EC5-3417EBE645D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7AD7A4A1-1F7F-E511-9CA6-B083FED04CAB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C9472BA-1F7F-E511-BAE7-C81F66B78DC1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7E4E20A1-1F7F-E511-84D0-B083FED429D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8C51302A-207F-E511-8613-D4AE527EE0FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/92A1A2A3-1F7F-E511-86E6-782BCB20E307.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A08050C7-1F7F-E511-807A-C81F66B79075.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A40B0FA2-1F7F-E511-8E8E-782BCB678096.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A82A4F2A-207F-E511-850E-782BCB678096.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AC23389F-1F7F-E511-88DE-00259073E520.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B05D662D-207F-E511-98AF-782BCB67A0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B6550126-207F-E511-AB90-782BCB67826E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C88AA8A1-1F7F-E511-8705-B083FED426E5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CCD7BD2B-207F-E511-968A-B083FED42FC4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CE5C292A-207F-E511-AAD4-D4AE526DF5D7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D2324BA2-1F7F-E511-A705-B083FED177B1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D24422A5-1F7F-E511-8174-D4AE527EDE00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D6F525A1-1F7F-E511-A04E-D48564593FAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8971EA5-1F7F-E511-9550-D4AE526DF090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DC99E3A7-1F7F-E511-8EAC-842B2B180882.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DCF6A9CA-1F7F-E511-AB82-C81F66B73F37.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E0E7F8A9-1F7F-E511-BAF5-842B2B18118F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E0EDF2A4-1F7F-E511-B3C1-0026B93785F5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F223AEDA-F07E-E511-899B-02163E013D21.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FCFE55A1-1F7F-E511-B99B-B083FED42FB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FE98E1A1-1F7F-E511-8095-B083FED00118.root' ] );


secFiles.extend( [
               ] )

