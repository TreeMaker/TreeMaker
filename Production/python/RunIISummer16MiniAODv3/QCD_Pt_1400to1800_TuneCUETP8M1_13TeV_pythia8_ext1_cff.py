import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0CD32078-FDE5-E811-B601-0025905A6092.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/16922B65-FBE5-E811-9901-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/16B1EE1B-FEE5-E811-9F97-0025905A6084.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1E452C1D-FBE5-E811-B93A-0CC47A78A4B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/326BAD37-48E6-E811-A92F-0CC47A4C8EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/38F05569-FCE5-E811-901E-0025905A6122.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/525D5C02-FEE5-E811-AA68-0025905A6134.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/66679C11-3BE6-E811-8D2A-0CC47A4C8F12.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/848975D1-89E6-E811-8200-0CC47A4D76A2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/98EF0947-FCE5-E811-9A51-0CC47A4C8E3C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9AAA9DBB-FAE5-E811-8FEA-0CC47A4D7638.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9E254903-42E6-E811-AEF2-0CC47A78A440.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/A0E393DA-FBE5-E811-BB7B-0025905A6122.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D4783CD3-CCE6-E811-B447-0CC47A7C34C4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D6BA9271-FEE5-E811-A6B3-0025905B85C6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/DA5C2857-FBE5-E811-A673-0CC47A4C8E64.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F0759596-FCE5-E811-8772-0CC47A7C347A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F2A5232B-D9E6-E811-B883-0CC47A745284.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F4FB5561-FBE5-E811-847F-0CC47A4D769E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/FEA39EB5-FCE5-E811-A2FE-0025905A60DE.root',
] )
