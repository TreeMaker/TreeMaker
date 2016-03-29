import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/0A69ADC9-CA6D-E511-9A59-34E6D7E05F28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/0AD1C1D9-CA6D-E511-8E18-68B59972C578.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/0E648ACA-CA6D-E511-A274-D8D385AE8A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1A1975C9-CA6D-E511-9324-34E6D7E387A8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1C1D72CB-CA6D-E511-9FC1-441EA171A0FC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/20003EE1-CA6D-E511-A353-D8D385AF8ACC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/20A19295-CB6D-E511-879D-D8D385AF8B40.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/28C0051E-CC6D-E511-A764-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/30283ACB-CA6D-E511-A668-D8D385AE8C68.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3A50EA83-CB6D-E511-A97D-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3E20DCCD-CA6D-E511-A2D2-B499BAABCF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/40E92784-CB6D-E511-B71A-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/440C6B8D-CB6D-E511-BE2E-D8D385AF8ADC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4619A585-CB6D-E511-ACA9-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4E1649C9-CA6D-E511-A4B8-D8D385AF8AE2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4E6C98A5-CB6D-E511-85E6-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/549ED689-CB6D-E511-AD28-D8D385AF8ADC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6058DD02-CC6D-E511-957D-34E6D7BDDEDB.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6088A6A5-CB6D-E511-9F23-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/66688987-CB6D-E511-876A-34E6D7BDDEE8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/725105C7-CA6D-E511-9872-34E6D7E05F1B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/765CCC86-CB6D-E511-A52C-D8D385AE8C68.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/80A0555F-CB6D-E511-8E89-68B59972C37C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/82CE9085-CB6D-E511-8A6F-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/88A4FBC6-CA6D-E511-98B3-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8C1DC787-CB6D-E511-980B-34E6D7E387A8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8C284620-CC6D-E511-9C88-441EA17344AC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8CFC1FC9-CA6D-E511-95CB-B499BAABD280.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9240ECCB-CA6D-E511-B777-D8D385FF1954.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/965A8CD6-CA6D-E511-A3A1-34E6D7E38781.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/98A8F395-CC6D-E511-82FD-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A06A89A5-CB6D-E511-92DF-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A2AD1ED1-CA6D-E511-96FC-D8D385AE85A6.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AA5F75C5-CA6D-E511-8315-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B0FE8C85-CB6D-E511-900C-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B4AADF7C-CC6D-E511-A1B0-68B59972C578.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B4C8E789-CB6D-E511-BA34-D8D385FF1A02.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B8181C84-CB6D-E511-B5DB-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BC845A85-CB6D-E511-A295-34E6D7E38781.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C27D7CC9-CA6D-E511-B48D-D8D385AF8AB2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C4497321-CC6D-E511-BF25-D8D385AF8AB2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C4BC4ECA-CA6D-E511-958E-D8D385FF1946.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C4D8F11D-CC6D-E511-8C72-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C6C280C7-CA6D-E511-AE63-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D297E79C-CB6D-E511-BC46-B499BAABD280.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D49D13C9-CA6D-E511-B816-D8D385AF8ACC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DC4A2584-CB6D-E511-9760-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DEEB0BC9-CA6D-E511-B95D-D8D385AF8AE2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E09ED2CF-CA6D-E511-9ED6-441EA1733A7A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F2409F85-CB6D-E511-AE42-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F2EDE8C6-CA6D-E511-854D-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F84776C5-CA6D-E511-8579-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FA08349E-CB6D-E511-9907-B499BAABD280.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FC156ADC-CA6D-E511-BC16-0022640691CC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FC1F2B84-CB6D-E511-959A-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FC7E08CB-CA6D-E511-968A-441EA1733CCC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FCB30F84-CB6D-E511-A2A0-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/04624909-CA6D-E511-A8D6-D8D385AF8A12.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/58B2814A-CA6D-E511-A659-D8D385FF1946.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/8A4D360A-CA6D-E511-9D15-441EA1733CDE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/9229551B-CA6D-E511-9531-D8D385AF889C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/9CF6A629-CA6D-E511-B952-B499BAABCF1A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/BE070809-CA6D-E511-82C5-34E6D7BDDEE8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/E402B30A-CA6D-E511-832B-D8D385FF1940.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/E627CB0C-CA6D-E511-B305-D8D385FF1A02.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/F688FC0A-CA6D-E511-B95C-D8D385AE8862.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/009CC28F-CB6D-E511-B380-B499BAABCF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/021F22E8-CA6D-E511-94AF-34E6D7BDDEDB.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0234EAE7-CA6D-E511-9FDD-D8D385AF8AE4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/02D50EE6-CA6D-E511-9021-68B59972C37C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/06AD7F8E-CB6D-E511-B725-00226406719E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/0A3EDC92-CB6D-E511-8113-D8D385AE8B08.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/14632CCE-CA6D-E511-A191-D8D385AF8994.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/1480B8E3-CA6D-E511-8828-441EA173385A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/165C408C-CB6D-E511-B2FB-34E6D7BEAF28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/168958D4-CA6D-E511-B0A2-D8D385FF1A02.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/18DE1499-CA6D-E511-9DFA-441EA1733CDA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/1AF3B545-CA6D-E511-8FA9-B499BAABCF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2A922BE9-CA6D-E511-AE97-441EA1733A74.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2C60ABE9-CA6D-E511-966B-441EA1733A7A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/36CBD08F-CB6D-E511-8E11-441EA173385A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3E7B53E7-CA6D-E511-8CA1-D8D385AF8AE4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/409D42A6-CB6D-E511-B99D-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/42A5C9E8-CA6D-E511-BE10-34E6D7BDDECE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/4A30B38E-CB6D-E511-9706-441EA1733A8E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/50F2ABE7-CA6D-E511-A705-D8D385AF8B7A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/5879E190-CB6D-E511-994C-34E6D7BDDEE8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6801F792-CB6D-E511-95D1-D8D385AF8B64.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6A94AD92-CB6D-E511-AA41-441EA17344AC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/74C8CA91-CB6D-E511-B2A5-34E6D7E38781.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/805442E7-CA6D-E511-9296-441EA1733A7A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/906732ED-CA6D-E511-B5BE-B499BAABD482.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/90CC26E9-CA6D-E511-8576-34E6D7BEAF28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/92642992-CB6D-E511-B770-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/92E20278-CA6D-E511-9442-D8D385AF8902.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/946F12A6-CB6D-E511-90B5-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9C8E1C01-CC6D-E511-B634-D8D385AF8A12.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A0A58BE1-CA6D-E511-80C3-441EA173397A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/ACB6CB8E-CA6D-E511-9FC4-D8D385AF8A12.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B461B88E-CB6D-E511-8166-441EA1733A8E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B62C5698-CA6D-E511-AA42-D8D385AF8AB2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B6720BA6-CB6D-E511-A285-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B8E9A1AB-CA6D-E511-8BAB-34E6D7BEAF01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BC423F92-CB6D-E511-8BCE-34E6D7E38781.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BEDC6BA6-CB6D-E511-8C17-34E6D7E3878E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C0524498-CA6D-E511-84EB-D8D385AF8AB2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C05B3DE1-CA6D-E511-BB65-441EA173397A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C06E058D-CB6D-E511-A5B0-34E6D7BEAF1B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C6580A8E-CB6D-E511-A71C-34E6D7BEAF1B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D292998B-CB6D-E511-8599-34E6D7BDDEE8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D600118E-CB6D-E511-9CF8-D8D385AE8A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E28ECA94-CB6D-E511-8EB0-D8D385AF8B64.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/E6D23EE8-CA6D-E511-8E33-D8D385AF8AE4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/EADC2ED1-CA6D-E511-916B-D8D385AF8AEE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/EAFD0386-CA6D-E511-84C2-D8D385AF8A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/ECDD9E99-CB6D-E511-A5CA-D8D385AE8B24.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/F4BAB6F2-CA6D-E511-8F3F-34E6D7BDDEE8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/F82A5CE3-CA6D-E511-822D-34E6D7BEAF1B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/16947502-CA6D-E511-87DB-34E6D7E05F28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/188AB366-CB6D-E511-A4CB-34E6D7E05F28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/2C5C29E3-CA6D-E511-A023-34E6D7E05F01.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/2C9B90E7-CA6D-E511-92D9-441EA1733A8E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/30A5EC00-CA6D-E511-BF6E-00226406A18A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/4E51C1DE-CA6D-E511-A7B7-B499BAABCF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/589016DC-CA6D-E511-B914-D8D385FF1A02.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5E279330-CB6D-E511-ABFA-D8D385AE8ACA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/72EC96E5-CA6D-E511-A698-441EA1733A9E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/7640CEDD-CA6D-E511-9FE4-B499BAABCF1A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9281E9EC-CA6D-E511-815C-D8D385AE8466.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/AA000EDC-CA6D-E511-8127-34E6D7E05F0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/B2DFEFDB-CA6D-E511-B217-34E6D7BEAF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/BE7363DC-CA6D-E511-B937-34E6D7BDDECE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/E2A3F0DC-CA6D-E511-B05A-68B59972C37C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/E8B95D09-CA6D-E511-B1F0-D8D385AF891A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/EAC566F7-C96D-E511-B612-34E6D7E3879B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F2A71CDE-CA6D-E511-87AD-441EA1733FD6.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F2C299DC-CA6D-E511-96EF-34E6D7BDDECE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6A6B7437-CA6D-E511-956C-441EA17344AC.root' ] );


secFiles.extend( [
               ] )

