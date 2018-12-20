import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0202D63D-27EA-E811-9BF9-A4BF01026229.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/06AC8AFF-2FEA-E811-9368-001E67A3EB1A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2649C61A-30EA-E811-9DCB-90B11C070100.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2A624B05-30EA-E811-85D4-001E67A3EC2D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2C18CC08-30EA-E811-95AD-001E67A3E8CC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/4C4DE0C3-3DEA-E811-A3E9-0026181D28BB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5A393E37-27EA-E811-A146-001E67A3EF48.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5EFC68FF-26EA-E811-B852-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/60CA603C-27EA-E811-973B-90B11C12D371.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/6AFDDACE-28EA-E811-BC4D-A4BF01025C07.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/72783599-3AEA-E811-B293-001517FAB928.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/7CD1193E-30EA-E811-89E1-001517F7F6A0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/84AAE7D5-2FEA-E811-B340-EC0D9A0B3070.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/869CE52D-27EA-E811-BAA6-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/8CC41CE1-45EA-E811-8493-001517FA7A98.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9E679CFA-97EA-E811-AD0E-001E67A3FDF8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/A2220E4F-27EA-E811-BEF3-90B11C08AD1E.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/A8B23A83-26EA-E811-A66C-A4BF0101F533.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/AE8E8028-27EA-E811-9593-001E67A3AEB8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C20054D6-0FEB-E811-A33C-A4BF01025630.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C45487BC-28EA-E811-832B-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/CCBA95F9-28EA-E811-9584-001517F807D4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D63FB5C1-2FEA-E811-9673-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/EAD3BB66-27EA-E811-8D8E-001E675A6A63.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/F87E823D-44EA-E811-9EB1-0026181D2917.root',
] )
