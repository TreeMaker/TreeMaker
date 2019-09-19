import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0C26BD86-93E3-E811-B6B3-246E96D14C70.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0E718D8C-9DE3-E811-9CFD-246E96D14E34.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2C890FEE-92E3-E811-A6EB-246E96D14AB0.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/3CF4B343-A0E3-E811-98AA-44A84225C827.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4A9B426C-8EE3-E811-B221-1418776375C9.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4C3D3585-93E3-E811-928F-44A842240F8D.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/503D0EDC-A0E3-E811-8976-0025907276DA.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/56F96C0B-97E3-E811-BD24-00259073E51E.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/70B36BFF-75E3-E811-859D-246E96D10C28.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/74058010-87E3-E811-9357-44A84224053C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/786C370C-87E3-E811-8612-00259073E522.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/92C4BDB0-99E3-E811-9D1B-B083FED16468.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9E85F6AE-9AE3-E811-8D60-44A842240F8D.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A0B23AF2-B1E3-E811-BF6E-002590D5FFF2.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A68B9C45-A0E3-E811-AA25-B083FED13C9E.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A84A770C-89E3-E811-8286-14187763B811.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/AA71E882-AFE3-E811-892F-246E96D149A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/AA7EE03E-99E3-E811-B1DE-002590D8C724.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/B0F29710-96E3-E811-844D-246E96D10C28.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/B2F4A783-0BE2-E811-8BE8-D48564599CAA.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/C01F9D8A-BBE3-E811-A4D2-B083FED138B3.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D2AA8CC0-ADE3-E811-AD82-B083FED13803.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/DEEC7B5C-ACE3-E811-A5E1-246E96D14B5C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F052648E-8DE3-E811-A30E-B083FED138B3.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F46BAEDA-98E3-E811-B76D-246E96D14C78.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F62645EF-94E3-E811-858A-246E96D14D9C.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F64B55FF-86E3-E811-A436-246E96D14B94.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FE5922A5-99E3-E811-9222-44A84225C4EB.root',
       '/store/mc/RunIISummer16MiniAODv3/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D4CF5AB4-0DE1-E811-91DD-20CF3027A561.root',
] )
