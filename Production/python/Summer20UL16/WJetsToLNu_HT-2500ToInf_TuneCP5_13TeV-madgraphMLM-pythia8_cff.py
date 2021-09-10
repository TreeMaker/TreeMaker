import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/120000/198DB35C-A78C-0C40-B51D-04A4AC38C54A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/120000/79797602-9555-0F44-BD7D-8BD21DD23DAB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/130000/BD13D659-D81F-204D-BA1A-6D51ECD560EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/230000/226E5600-52C4-3F49-B5C0-EF28C78992CB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/387BF11E-726F-AD40-85AC-6BC4FDF327D4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/625BED18-7EC9-DC4A-BD67-D53AD210DC62.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/FE984B6D-6CA0-BC4D-8E62-2DA599CEDD57.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/0FFD1109-3432-AC4D-8D21-F419604551F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D080FFA7-B0DA-7B40-BFD0-A5AE21D4ED19.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0572040E-4BE8-2545-8E42-66CD28416EAC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0EF31419-2262-7D46-8801-F9FCFAA9C566.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/42A6E84E-2C7D-FE45-9694-E1ACD4505E78.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/54A58275-18C6-8248-BBF7-1A2F66F3BA2D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/5676243E-B78C-8F4E-AFEB-56E49118D47B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/61E83D0D-A8BE-3149-B49D-A0A06F92703A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/96D4D5F2-35CB-1D41-AAB5-8C6B83383EBE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/98BC4B17-B815-594E-850E-50E6F490CFFF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9D420444-1EDE-D34A-A5AB-51EAD1809240.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/BEBF9739-180D-3F4A-9F96-B38E3015684C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/1B3C192B-468B-9849-9D56-CEEE36EAEE10.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/1DF0C592-293A-8B49-84E3-401DD560EA31.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/5888C38F-331D-0947-9C55-63F4936B7F82.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/58FA5918-5191-3841-8149-10BC88605EE5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/5AE06FC9-8747-3B4D-BCBB-1565AE7EECAC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/76E8BDA2-863D-854D-81A2-67B6B37F06DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/83A1829F-08DD-214A-8F95-2C5836843235.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/D3A277B4-F561-9044-BF5B-8ED1B63561CE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/D565EF39-510F-2B49-8AE0-498A9A724F25.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/280000/EF63FF1E-1B0B-1748-B6BF-3DAB2449E7C9.root',
] )
