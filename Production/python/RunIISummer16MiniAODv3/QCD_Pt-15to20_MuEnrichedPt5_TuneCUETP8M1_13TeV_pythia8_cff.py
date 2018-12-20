import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/00BC2F40-FCE2-E811-9028-AC1F6B0F676A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0219064F-41E1-E811-ABED-AC1F6B0DE45C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0407A1FE-47E1-E811-BCB0-AC1F6B0F7B08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/0ADBAC25-54E1-E811-9420-AC1F6B0DE3E8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/182AFE46-57E1-E811-A3D8-AC1F6B0DE456.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2452960E-55E1-E811-8CB6-48FD8EE739FF.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/2A16CA51-55E1-E811-82A3-AC1F6B0F6758.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/30CA4890-56E1-E811-A64F-AC1F6B0DE4A2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/34C6868E-56E1-E811-8E4D-48FD8E282499.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/3ABB731B-50E1-E811-8DBA-AC1F6B0DE22A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/468BAF53-50E1-E811-9B06-AC1F6B0F7B08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/48C560AC-49E3-E811-8404-AC1F6B0DE3FA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/6EE989B9-79E2-E811-9F39-48FD8E28249D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/92671DF0-54E1-E811-9E90-48FD8E069BA7.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9493B4DF-54E1-E811-99C8-48FD8EE739FF.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9AF90FAF-4AE1-E811-89EB-AC1F6B0DE45A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9CCA9929-46E1-E811-A254-48FD8EE73AC5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/9ED3B5B0-51E1-E811-9963-48FD8EE739AB.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A0133C95-30E2-E811-B074-AC1F6B0DE2F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/A47653B9-79E2-E811-808E-AC1F6B0DE3F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/ACF7CC8A-47E1-E811-83BF-AC1F6B0DE22A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/B611A23B-57E1-E811-BF16-346AC29F11B8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CA78649C-54E1-E811-947A-AC1F6B0DE340.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/CAD80000-54E1-E811-9DD4-48FD8E2824B3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/D8642CE7-56E1-E811-9D38-48FD8EE739CB.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DA088BBB-50E1-E811-9168-48FD8EE73A85.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/DA9E5E40-58E1-E811-8794-48FD8EE73AD7.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/E2061A96-54E1-E811-BA22-48FD8E2824D5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F68EF782-52E1-E811-A524-48FD8E2824C3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/F8555838-4BE1-E811-A534-48FD8EE739D1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/100000/FA3EACDA-49E3-E811-9C04-AC1F6B0DE348.root',
] )
