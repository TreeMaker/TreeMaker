import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0E3EAEF1-72E3-E811-B7B9-001E677923E2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0EC8E3BC-6AE3-E811-9504-A4BF01158DE0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/16AD7942-5DE3-E811-8568-001E677928AE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1CA943A5-6AE3-E811-8B81-A4BF0107E164.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/20D42B6F-6BE3-E811-9781-A4BF01125D86.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/2820D429-69E3-E811-826F-A4BF01125E47.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/28CF309E-6BE3-E811-BF7B-A4BF010F0F2A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/2EE02868-65E3-E811-B08A-A4BF011253A8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/42E950CF-72E3-E811-A6AD-001E67E6F49F.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/4428CD0D-77E3-E811-A259-A4BF0112BDF2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/44F8C03D-65E3-E811-9979-A4BF01159634.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/52AAC414-66E3-E811-A9B1-001E6779254C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5C3F3BAC-B3E3-E811-A4DE-A4BF0112BDFE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/687EEC0A-68E3-E811-A65F-A4BF0112F6B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/6A628EBA-E4E3-E811-BA40-A4BF01125E47.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/74C4E0BB-70E3-E811-A028-A4BF0112E0F0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/86D60902-74E3-E811-B790-A4BF0112E330.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/8AE16C65-71E3-E811-B577-001E67E6F8AA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/8C72D404-6EE3-E811-8AD3-A4BF0112BD8C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/902E5333-B0E3-E811-8282-A4BF0112BC82.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/90AA4CE7-72E3-E811-BFBD-001E677925A2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9281D888-71E3-E811-AF7E-A4BF01125C68.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B2EAFEC6-A6E3-E811-89D3-A4BF0112DFA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B86367C8-72E3-E811-9E9E-002590A4FFE8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/C22BB178-65E3-E811-80FE-A4BF0112BDF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CA6637A0-6FE3-E811-9A49-001E67E71412.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D0DCD256-ABE3-E811-B13B-001E6779238C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D2D48AAF-73E3-E811-8399-A4BF0112E310.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D4658E95-65E3-E811-802C-A4BF01159474.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/DE767D8F-66E3-E811-A411-A4BF0112BC58.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E0687EE9-67E3-E811-B0B0-002590A37118.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/ECA76809-72E3-E811-8395-001E67E6F8EB.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F4DCA359-6DE3-E811-A551-A4BF0115A070.root',
] )
