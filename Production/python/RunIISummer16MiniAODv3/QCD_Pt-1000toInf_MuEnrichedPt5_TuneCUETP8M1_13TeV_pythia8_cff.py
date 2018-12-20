import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0ECB363C-F7E5-E811-8B0A-0025905C3D96.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1A06BEC5-F9E5-E811-A838-0CC47AFB81B4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1A95E28D-F6E5-E811-8BAE-0CC47AFCC6A6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/24149B32-3DE6-E811-96DD-0025905C3D40.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/261D5EBF-FBE5-E811-9CDD-0025904C5DE2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2EC565C5-3DE6-E811-B2FA-0CC47AF9B302.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/34660ECC-F6E5-E811-87E8-0025905C3E38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/38AD8D84-FBE5-E811-99AA-0CC47AFB80F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/38BD0A7F-FBE5-E811-8F55-0025905D1D60.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/44945106-F5E5-E811-BB70-0CC47AFB7D48.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/485DB1E3-F9E5-E811-B392-0025904C669E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/564E66BF-F6E5-E811-94B1-0025905C54F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/66B43617-3FE6-E811-8566-0CC47AFB7DCC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/80C8E05A-FBE5-E811-B8E5-0025904C516E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8E92BF2A-42E6-E811-B3ED-0025905C9740.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/90A98C9E-42E6-E811-A707-0025905D1D7A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/92DEC622-A2E6-E811-9DE8-0025904CDDF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/96401F34-FBE5-E811-AEC4-0CC47AF9B2E2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A249F82C-05E6-E811-AFCA-0025905C5476.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B07A9290-F5E5-E811-9E09-0CC47AF9B2BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B6697DEF-F7E5-E811-8A59-0025904C67B6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B87EF6EE-3FE6-E811-B5E1-0CC47AFB7D08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BC8D359B-FBE5-E811-AA49-0025904C678A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C8A92140-3DE6-E811-820D-0025905D1D52.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D02C9492-42E6-E811-A859-0CC47AFCC6BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/DC836BEE-F7E5-E811-9CA4-003048947BB9.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E21AB516-F8E5-E811-8B80-0CC47AF9B2BA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E49496F8-3FE6-E811-B3B9-0025905C54F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E8A2B423-3FE6-E811-BFDD-0CC47AF9B1B2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EC935955-FBE5-E811-A6CE-0025905C3E68.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F4FAD09B-3CE6-E811-AED1-0CC47AF9B1D6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FADA24EC-E8E6-E811-95B0-0025905C543A.root',
] )
