import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/007292AF-5500-EA11-A4C7-3CFDFE733430.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/0AD2E8E3-5EFD-E911-BC30-001E675A5262.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/268277D9-5EFD-E911-BF0D-20040FF469BC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/2A52C92E-61FD-E911-85F8-0CC47A6C1034.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/2A74F4D6-BBFD-E911-98AA-509A4C748146.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/42D17741-5EFD-E911-85EC-00259090840A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/6045C55C-5EFD-E911-B719-24BE05CEADA1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/64BF5C51-5EFD-E911-AF6F-AC1F6B0DE456.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/7EFA322D-56FE-E911-96DC-0CC47A4D763C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/B248EB44-6EFD-E911-B878-001E67DBE3EF.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/BA9CD44B-5EFD-E911-BD2E-0025905504C8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/BE79C805-7AFD-E911-BEBE-AC1F6BABF8E3.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/CACDD69A-67FD-E911-938D-0CC47AFF2A6E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/230000/F881A354-5EFD-E911-9539-002590A83190.root',
] )
