import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/0EEB957A-6ACE-E811-AC41-F02FA768CFD4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/104C0D9F-6BCE-E811-92DC-A0369FD0B20C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/182AD148-63CE-E811-8C60-48FD8EE73AC5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/26A7C475-6CCE-E811-8DF6-48FD8E282495.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/2ED7BB52-65CE-E811-94CA-A0369FD0B144.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/3257AEDE-6CCE-E811-B95C-A0369FD0B306.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/3404324B-64CE-E811-97D8-48D539F38674.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/38EC61D7-6BCE-E811-B021-48FD8E2824B3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/4888F697-65CE-E811-AFC9-0090FAA57C74.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/522B9814-63CE-E811-954A-F02FA768CFD8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/5EA43139-61CE-E811-AD58-346AC29019DC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/88ED4BE3-6ACE-E811-87A9-AC1F6B0F7196.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A0AC35C9-69CE-E811-95BF-AC1F6B0DE45C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A28558FC-60CE-E811-A5DD-AC1F6B0DE338.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A44D6665-89CE-E811-9192-A0369FD0B33E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/B418BD76-55CE-E811-B174-48FD8E282493.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C0F460FA-5ECE-E811-BBC5-48FD8EE739EB.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C21B25DB-6DCE-E811-8B0A-AC1F6B0F7B16.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C2AD150C-65CE-E811-98E2-F02FA768CFFE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/C663C358-65CE-E811-8E71-AC1F6B0DE49C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/D8584A96-6CCE-E811-964F-F02FA768CB4A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/E439CEE8-62CE-E811-823E-48FD8EE73A85.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/F2BCC7D0-EACE-E811-ABE6-A0369FE2C22E.root',
] )
