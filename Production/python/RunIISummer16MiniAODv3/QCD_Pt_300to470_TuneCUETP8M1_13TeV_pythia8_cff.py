import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/08E20FFD-B2E3-E811-84F7-90E2BACBB038.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/12EFB401-29E4-E811-A75A-D8D385AE8BAE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1C4F5AE6-8AE3-E811-A43C-002590FD030A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C055648-16E4-E811-820E-90E2BACBAA90.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C0B2D7B-93E3-E811-855A-0425C5DE7BEE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/30F1BF83-90E3-E811-BE44-002590FD5E88.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/340227BB-B4E3-E811-A7C1-90E2BAD1BDF0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/4619787C-19E4-E811-8E67-D8D385AF889C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/4A76E51D-8CE3-E811-90FE-002590FD5E3E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/4EA2535F-A7E3-E811-AEA1-D8D385AE888A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/50284303-22E4-E811-A8CA-90E2BAD4912C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/56301E8C-88E3-E811-B1E9-90E2BACBAD58.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/642790B0-28E4-E811-B16A-90E2BACBAE58.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/64578398-18E4-E811-9C67-14DDA924324B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6AC8417E-A8E3-E811-92E6-1CB72C0A3DC1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8275B75E-28E4-E811-95E7-002590FD5E88.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/86F375DC-28E4-E811-9EAA-90E2BACBB038.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8E525A1F-18E4-E811-BDAF-90E2BAD492E8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9A27A17C-F7E3-E811-B0CB-AC1F6B8DD212.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9A3F7DA1-A7E3-E811-BE42-C0BFC0E56866.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A2619553-26E4-E811-90FD-D8D385AF8994.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/AE1B8C5F-81E3-E811-A3F8-34E6D7E3878E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B06C87CE-87E3-E811-A83E-1CB72C0A3DC5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B42B2921-99E3-E811-B8D6-441EA173397A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BA09DFE4-30E4-E811-8E01-90E2BAD1BDF0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C0D4D845-19E4-E811-ABE0-C0BFC0E5682E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C4BEAE03-29E4-E811-8C41-C0BFC0E56846.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CA9C8B59-B3E3-E811-8434-90E2BACC5EEC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E88B5CDA-26E4-E811-A231-441EA17344AC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EC6D8796-18E4-E811-849E-0425C590303A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F0F9B645-18E4-E811-B70C-D8D385AF8AE4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F4EE8B15-2AE4-E811-A74A-68CC6EA5BE7A.root',
] )
