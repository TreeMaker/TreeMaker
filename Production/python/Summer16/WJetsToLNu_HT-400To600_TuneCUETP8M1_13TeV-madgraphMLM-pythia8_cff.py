import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0488B5D9-C3B5-E611-B98A-008CFA197C34.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/12488152-CAB5-E611-A773-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/329D7E4D-BCB5-E611-887E-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/44FD51C4-C3B5-E611-A0D9-0CC47AA99070.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4AB25425-B9B5-E611-9CA2-24BE05C46B11.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4CCCA7D1-C0B5-E611-996A-24BE05C63721.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/50AAF825-BCB5-E611-ADEA-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56A8A282-C0B5-E611-993D-24BE05C6C7F1.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/760F7AE1-C1B5-E611-B475-0025901D08EA.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E706ED0-CAB5-E611-AB82-0026181D28D0.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E8DF2FA-BDB5-E611-B320-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/807B723D-CAB5-E611-A1DA-02163E01312F.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/868A42F1-BDB5-E611-ADB1-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C4893E4-BFB5-E611-B10D-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/940FE02C-C0B5-E611-9A3B-24BE05CE2E81.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/98EDFE7D-BEB5-E611-B4E7-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A67E526-C7B5-E611-A553-0CC47AA99070.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9AA9C654-BCB5-E611-B48A-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A44AEF72-CAB5-E611-A9AB-0CC47AD98BCC.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A60EBC25-BCB5-E611-9B8F-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BA917653-C4B5-E611-9827-0CC47AD98D12.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE407BA5-BEB5-E611-BD01-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D6BA3F43-C1B5-E611-A4A7-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EC58BD4E-CAB5-E611-95EA-002590551F7E.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F0246F1E-BAB5-E611-9B3F-24BE05CE4D91.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F086651A-BBB5-E611-BE80-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F8CAB93D-CAB5-E611-802E-02163E013C71.root',
       '/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FC30D1F0-BDB5-E611-84E5-A0000420FE80.root',
] )
