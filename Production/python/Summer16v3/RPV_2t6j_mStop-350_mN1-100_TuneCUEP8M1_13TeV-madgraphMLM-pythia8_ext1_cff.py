import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/08D581BA-10FE-E911-885F-AC1F6BB17570.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/0AAE17D3-40FE-E911-92F8-008CFA197964.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/0E7030B5-D5FD-E911-ACD9-A4BF01283A8B.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/10D4A852-22FE-E911-A7E2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/2ADB362C-21FE-E911-A627-FA163E0435A2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/2C54930B-34FD-E911-98BC-0CC47A4DEDD6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/30C1EAE1-0CFE-E911-83D1-B499BAAB427C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/3C6C45A4-2AFD-E911-83AB-0025905C53F2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4600FA18-1CFE-E911-A58A-B026283461F0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/48AC08E6-C4FD-E911-BE97-002590907802.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/4AC038BE-C4FD-E911-B839-6CC2173D46A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/5C492441-56FE-E911-AE6A-0CC47A7C347E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/62331737-87FE-E911-99D4-509A4C9EF8EC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/68DDDE09-3DFE-E911-A508-0CC47A13CCEE.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/74ED9967-53FE-E911-8813-B49691386CFC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/7800A688-05FE-E911-A7A2-001E67E71C95.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/7A94D64D-29FE-E911-AC9F-001517F7F6A0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/8008843B-05FE-E911-BF18-506B4BB16AB6.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/86AE3CDC-09FE-E911-8BED-AC1F6B1B2358.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/86BFFBD8-C4FD-E911-A9B6-34800D4F9410.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/88CC66E5-BBFD-E911-BF06-002590DE6E72.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/9E5A9BF9-D8FD-E911-815B-002590FD5E80.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/ACD322DA-11FE-E911-861E-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B46C6995-05FE-E911-9016-0CC47A1E0466.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/BC409E85-CDFD-E911-BD64-7CD30ACE1660.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/CA9B4BDC-81FF-E911-971B-A0369FF88396.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/D26A8E7B-10FE-E911-A0C8-002590207C28.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/D2BBBBCD-17FE-E911-8D16-20040FE9AD78.root',
] )
