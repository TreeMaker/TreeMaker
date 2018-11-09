import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/04F61006-C4B5-E611-94E8-D8D385AE8C68.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/3E8A9586-BEB5-E611-85E5-441EA1733FD6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/589E93B2-D3B6-E611-9218-0025905A60BE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/5CAF99E6-CBB5-E611-9C51-008CFA5D2758.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/64C47F11-D9B6-E611-AB78-0025905A60E4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/6CD5BCA6-C6B5-E611-99D4-90E2BAC9B7A8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/8C92D308-D9B6-E611-8242-0025905A60A0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/8E365CAD-C5B5-E611-AF0E-008CFA111234.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/CCA65E95-90B6-E611-AC39-90E2BACBAD58.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/DC0CC3E8-C2B5-E611-AFA3-002590551F7E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E8B58C93-C1B5-E611-B058-002590FD583A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/EA64EA90-D7B6-E611-91F8-0CC47A4D7606.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/EE84A535-C3B5-E611-8D6F-D8D385AF8ADC.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F4E8EC6A-9FB6-E611-88B8-008CFA197BD4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F6E636F7-C4B5-E611-98ED-90E2BAC9B7A8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9AD8E8F5-C8B6-E611-A2EB-0CC47A4C8EB6.root',
] )
