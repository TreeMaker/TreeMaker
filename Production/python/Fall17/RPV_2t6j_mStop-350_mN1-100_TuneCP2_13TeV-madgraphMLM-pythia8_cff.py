import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/009229AA-05C3-E811-A6BC-7CD30AD096BE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/0EBA875B-6BD1-E811-BD29-90E2BACBAE58.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/12547737-6BD1-E811-8887-008CFAFBFEBE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/127579CE-6AD1-E811-882F-008CFA197CA0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/1AE1618E-1FC4-E811-B472-7CD30ACDDFBE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/1ED3974F-6BD1-E811-BFCB-0CC47AD98BEA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2C5BE55C-6BD1-E811-B447-10983627C3DB.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/2E0EA89A-E7C2-E811-955E-008CFAFBEBF2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/3255203B-6BD1-E811-BD7A-0CC47AFB7DDC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/68B42537-6BD1-E811-846B-0CC47A745294.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/6CA872D0-01C1-E811-B758-003048F29C9C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/70FA6E65-C5C0-E811-9C63-0CC47AA98A3A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/742DDFC2-4FC3-E811-9178-509A4C781310.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/82BA7CA7-42D1-E811-9BA3-008CFA1111A0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/907C181A-40C8-E811-BA9D-001E675A68BF.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/944F284A-6BD1-E811-83D1-008CFA111290.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B4A59E07-F4D0-E811-8C71-008CFA1113D8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C0E79E98-4CC1-E811-9A61-E0071B7B2350.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/CAF57B16-72C9-E811-B6BD-001E67DDC2CC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/E4FCB1BF-F8BF-E811-89AD-3417EBE2F4B1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/ECF70548-C8C0-E811-AD95-EC0D9A0B32F0.root',
] )
