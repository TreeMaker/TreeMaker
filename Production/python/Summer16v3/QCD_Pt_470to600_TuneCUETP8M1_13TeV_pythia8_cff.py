import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/00E2EBE0-8CE3-E811-AC35-7CD30ACDD44E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/18021145-7BE3-E811-B69A-008CFAF73232.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/18E76306-82E3-E811-8241-3417EBE64C7B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1E5098B3-6DE3-E811-B071-7CD30AD0973C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/243BA45A-97E3-E811-ACEE-7CD30ACE1DB6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/26440450-91E3-E811-B67B-509A4C781389.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/30C1B1C3-8EE3-E811-A78F-7CD30AD09B08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3CACC09C-8CE3-E811-BC3F-7CD30AD0A690.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/429A1314-6FE3-E811-B8FC-509A4C838C7C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/4AFD78EC-89E3-E811-99BB-848F69FEFFC5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/54C62312-8CE3-E811-ACEA-008CFAF72476.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/58924DCF-8EE3-E811-A947-008CFAFC5BB2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5A95124E-7DE3-E811-A594-3417EBE34D1A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6CCA1E1C-70E3-E811-869F-7CD30AB15C58.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/703958BF-7AE3-E811-B173-3417EBE645A9.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/76FE2535-7BE3-E811-9797-7CD30AB04FE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7E65DF09-8DE3-E811-8209-3417EBE2EC98.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7E9FFB76-92E3-E811-9DC6-509A4C74801C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/80E3A0AE-88E3-E811-9E06-008CFAF5223A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/88411B30-63E3-E811-9D8F-7CD30ACDD44E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8CFB9DA0-98E3-E811-9E10-008CFAFBE880.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/98077C06-ADE1-E811-9BA5-509A4C749125.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/AA07A8B2-8EE3-E811-BFB8-7CD30ACDCBA8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C093FE42-97E3-E811-B72A-509A4C7489DC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C6150895-95E3-E811-8E2A-509A4C74D08F.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C61C00A5-7CE3-E811-A3FD-7CD30AD08CFE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CABE8345-85E3-E811-96FC-509A4C74806E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CE981423-70E3-E811-B9D6-3417EBE64CB1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E6B8C690-95E3-E811-9466-008CFAF73232.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F087E00C-7CE3-E811-86F6-509A4C78134B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F264DB90-6EE3-E811-8792-7CD30ACE10DE.root',
] )
