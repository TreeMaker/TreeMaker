import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00D97021-CFBE-E611-AD3F-0025901D08B8.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/061DAB15-66BE-E611-B8D6-0CC47AA99438.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/06425366-CFBE-E611-9B7F-FA163E4ACE9B.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0A7BA7B6-48BE-E611-834D-3417EBE6446E.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/143D8567-CFBE-E611-82DE-0025905A48C0.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1CE9292C-7CBD-E611-AE79-1866DAEA79A4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/248B8E65-7FBD-E611-926B-00266CF9BDFC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2AE9984E-D2BD-E611-8213-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4428DF1F-CFBE-E611-A1FC-002590AC4CCC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58A4DC19-CFBE-E611-B851-B8CA3A70BAC8.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6054B80B-B8BE-E611-B02E-FA163ED5C256.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/60DB5426-CFBE-E611-B5F2-0CC47A0AD456.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/72066A7C-C8BD-E611-A1B9-0025905A612C.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7E08BD8B-93BE-E611-890D-0CC47A7C34E6.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8250F7A9-44BE-E611-8F8F-00266CFFC7E4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8E3E0DF0-94BD-E611-B665-001EC94BA119.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A08CFC64-CFBE-E611-BE5B-00259073E4E4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA3B1D84-CFBE-E611-BAF4-002590A887AC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CC1302B2-75BD-E611-9365-782BCB537E8B.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CEB21306-B4BE-E611-BB9C-FA163ED46F52.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E2A0DD9A-77BD-E611-92B4-7845C4F92E7F.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E6F44563-CFBE-E611-853F-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EAA7B2BB-95BD-E611-AAFA-0CC47AD98D08.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F80713D4-3FBE-E611-AB6B-24BE05C626C1.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F877A452-5BBE-E611-B76D-B083FED42488.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FAF03F4F-CFBE-E611-A89F-0CC47A1E0DA6.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/06CC68D5-EEBD-E611-AD82-001E67A40442.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/12FF21E2-EEBD-E611-9311-0019B9CABE16.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3ADC4A69-8FBD-E611-8739-B083FED42FC4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5031C6D7-EEBD-E611-BA79-0025907D2000.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6C3D3BFE-EEBD-E611-BAED-0CC47A7C35A4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8AA311D6-EEBD-E611-8455-0CC47AD98F70.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D47ADF17-31BE-E611-9048-001E674FB24D.root',
] )
