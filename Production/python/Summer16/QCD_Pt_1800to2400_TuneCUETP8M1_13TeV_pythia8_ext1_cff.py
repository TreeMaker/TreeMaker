import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/02C95882-00BC-E611-BFD8-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/0424171C-FBBB-E611-B1F7-0CC47A745282.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/0A78B16D-23BC-E611-BA18-B499BAAC0414.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/180B84C2-FBBB-E611-AE9E-0CC47A4C8E0E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/20047D80-FDBB-E611-8CD7-0025905A60B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/24F4E10B-FBBB-E611-94CF-0025905A60B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/260B9B74-01BC-E611-89CE-0025905B8562.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/30CED158-00BC-E611-B63E-0CC47A74524E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/30EF774C-FFBB-E611-BD8B-0CC47A4D75F4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/340E8BFE-02BC-E611-B0E9-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/3AD684B9-FDBB-E611-9E0D-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/42F6EF31-FCBB-E611-B134-0025905A608C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/54303921-FFBB-E611-9DF5-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/626CCFF2-ABBC-E611-B9E7-0CC47A4C8E1C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/64D7585A-FEBB-E611-9D72-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/6686D120-FFBB-E611-9AB8-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/9C026202-F9BB-E611-A6DB-0025905A48F2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/AA699C65-FABB-E611-B427-0025905A48B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/AE65E900-21BC-E611-AB45-001E674FCAE9.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/B6569C5A-FDBB-E611-9906-0CC47A4D7618.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/D4AFDF14-FCBB-E611-BC74-0CC47A78A3E8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DAF42654-20BC-E611-AAF4-001E67E6F404.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DC3C9715-53BD-E611-BF1E-0025905B855C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/E240C704-21BC-E611-BBC0-008CFA1C907C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/EAC064B7-2ABC-E611-AD47-0CC47A4D7678.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/EE7F21B5-FDBB-E611-913D-0CC47A4C8ECA.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/EEFAF434-F8BB-E611-9078-0CC47A74524E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/F0851BB2-F9BB-E611-A8AA-0CC47A4D76B6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/F2BE3C09-FBBB-E611-A777-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/F44BC11C-01BC-E611-A6E6-0CC47A4D7618.root',
] )
