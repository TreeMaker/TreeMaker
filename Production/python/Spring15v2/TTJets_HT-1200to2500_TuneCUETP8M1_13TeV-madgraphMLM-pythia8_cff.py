import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/021A6D02-CA6D-E511-835B-002590188680.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/18424046-D96D-E511-A0F9-0025902D14EC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1A37D663-C06D-E511-85B8-0025904CFB8A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3865F739-C86D-E511-A097-0025902D144C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/40707F64-BC6D-E511-B2C7-0025902CF9E2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/40B16990-BF6D-E511-A26A-0025902CFC3E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/44C50448-C86D-E511-92BB-003048C7BA46.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/46C45EAB-BE6D-E511-A017-003048C56E54.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4C725E39-C86D-E511-B19B-0025904B8ABA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6293CBD0-C86D-E511-B9D1-0025904CEBE2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6ABD6413-CF6D-E511-8003-00259018959C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7E14B328-C46D-E511-A824-0025902D10E4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9204E01C-CC6D-E511-B62D-003048CD72CE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9435C5F1-C06D-E511-B798-0025904CEC28.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/94639A96-C36D-E511-847D-003048C6B4EA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9C0C4621-BE6D-E511-A69D-0025901895D8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B4F8DE3E-C26D-E511-AFC4-0025904CFB8A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B8B4924B-BA6D-E511-AE68-0025902D10E2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C2532297-BD6D-E511-BF57-0025904CEC20.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9EEF1C5E-C56D-E511-98C5-002590188680.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/BC4FAB13-C26D-E511-925A-0025902D11AC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/62D54EC2-C16D-E511-A820-0025902D10E6.root',
       '/store/mc/RunIISpring15MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8AF49143-CA6D-E511-92D9-0025904CF052.root' ] );


secFiles.extend( [
               ] )

