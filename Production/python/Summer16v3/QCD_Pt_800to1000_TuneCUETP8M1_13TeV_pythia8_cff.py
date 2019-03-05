import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0A25E81C-76E3-E811-AB2F-E0071B73C640.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0A54BB15-85E3-E811-BD68-24BE05C63651.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0A69759E-5FE3-E811-9B54-506B4BB134E6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0EC7EC7A-63E3-E811-89EC-EC0D9A809802.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1C08B6F6-6FE3-E811-BBB1-EC0D9A82261E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1C2FDA65-6FE3-E811-85AB-506B4BB16ADE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1EF66A0B-70E3-E811-B483-EC0D9A82261E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/24CC0ABF-63E3-E811-98F8-EC0D9A8222F6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2677AA32-71E3-E811-9E71-EC0D9A8221DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C3D87AA-78E3-E811-9250-EC0D9A82220E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3676E521-6FE3-E811-8FC2-506B4BB16AE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/42E8DD34-6DE3-E811-B4D1-E0071B7A68D0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/505A461B-71E3-E811-B968-EC0D9A89AA0A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/54AC511E-71E3-E811-AA98-EC0D9A89AA0A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/56ED5E99-73E3-E811-8AA5-EC0D9A8222E6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6E79D47E-6FE3-E811-8997-506B4BB16ADE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/728C4EA3-78E3-E811-8F88-EC0D9A82220E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/761D2D7C-63E3-E811-AF13-EC0D9A809802.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7862CB21-6FE3-E811-91B9-506B4BB16AE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/78EE1B7E-63E3-E811-A9A9-EC0D9A809802.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7CEDC681-70E3-E811-97F3-506B4BB16AEE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/82B33207-63E3-E811-90EB-EC0D9A822616.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/96ABE020-71E3-E811-9AB1-EC0D9A8221DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/983CE595-5FE3-E811-827F-506B4BB134E6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A49EDB21-6FE3-E811-93DA-506B4BB16AE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A82C0AED-19E4-E811-8F93-24BE05CE0E41.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A850E820-71E3-E811-8EAE-EC0D9A8221DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B086D565-6FE3-E811-ADD5-506B4BB16ADE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BC1AE8B1-75E3-E811-BDB2-EC0D9A822626.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C895921B-71E3-E811-93A4-EC0D9A89AA0A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D4037FBD-63E3-E811-A9C1-EC0D9A8222F6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D83245DD-6DE3-E811-A530-24BE05C6C7F1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/DCA9FEB6-78E3-E811-861F-24BE05C3FBB1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E2C47EAD-63E3-E811-AB39-EC0D9A8222F6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EEE854A9-75E3-E811-822F-EC0D9A822626.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F46840FC-6FE3-E811-8AB4-EC0D9A82261E.root',
] )
