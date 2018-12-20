import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/068EA087-42DF-E811-991D-AC1F6B23C82E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/16F6F4E3-55DF-E811-8465-0CC47A545062.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2842828A-32DF-E811-9673-0CC47A5451E4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/4A2B8F08-F2DE-E811-AC65-0CC47A544F5A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/583F831E-39DF-E811-8E1F-B4E10FD218CF.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6640FDD7-3CDF-E811-B967-0CC47AB6503C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/78855FA8-44DF-E811-B5EE-AC1F6B23C848.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/7AC6AFFA-45DF-E811-A940-0CC47AB64EF4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8031A519-43DF-E811-94C2-AC1F6B23C77A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8AF1AB08-15DF-E811-B4D4-AC1F6B23C7E0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/940C6424-03DF-E811-A847-AC1F6B23C93A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/9466A862-3FDF-E811-AB3A-AC1F6B23C86A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/98A03FC9-44DF-E811-820E-AC1F6B23C830.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A025ECC9-41DF-E811-B032-AC1F6B23C812.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A261DEC1-41DF-E811-BAAE-0CC47AB65044.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B6262828-27DF-E811-BC54-0025904CEC28.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BA0B7ABB-3FDF-E811-9559-AC1F6B23C736.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/BE392199-42DF-E811-B15D-0CC47AB65046.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C60E6E4A-3FDF-E811-B3B2-0CC47AB64EF6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/C8AEF672-46DF-E811-B49D-AC1F6B23C94C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DA65924F-41DF-E811-98D4-0CC47AB58BE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/DC8F585C-42DF-E811-8CCD-AC1F6B23C80C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FEB6B05D-1CE0-E811-A081-0025904B307E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4EE4CACE-96DF-E811-86A7-AC1F6B23C96A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7EDDAFD6-C7DE-E811-8E1A-AC1F6B23C832.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BC9395E4-D0DE-E811-B45B-AC1F6B23C812.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D6C65356-CCDE-E811-93ED-0CC47AB58BE4.root',
] )
