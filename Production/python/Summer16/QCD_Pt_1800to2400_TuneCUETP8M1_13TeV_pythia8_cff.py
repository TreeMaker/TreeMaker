import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/544D528B-03B3-E611-B70A-B083FED4263D.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5EFDBA29-01B3-E611-8B99-0CC47AD98B98.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6AA7601B-FFB2-E611-8EA5-0CC47AD9908C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/88789C1E-FEB2-E611-91F6-0CC47AA99070.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/98137CA8-02B3-E611-B8A1-002590E39D90.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A05C6679-FBB2-E611-9DA7-001C23C0F1F4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E608AA31-F9B2-E611-812A-0CC47AD98F72.root',
] )
