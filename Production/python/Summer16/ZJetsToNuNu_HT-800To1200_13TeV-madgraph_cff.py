import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0EE78F3F-DEBA-E611-8E40-0CC47A4C8E86.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/12450BCB-4CBB-E611-808C-00266CFCCD00.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1E768FDE-E1BA-E611-9C94-0CC47A7452D8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1EEB0528-EEBA-E611-9DEE-0CC47A7C3472.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/247ABCE6-4CBB-E611-9F86-001E67CBE45A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2A5216AA-E3BA-E611-9809-0025905B85B8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2CDD338B-DABA-E611-9003-0CC47A78A478.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/36F74F85-FABA-E611-ABE5-0CC47A7C3472.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/380180EF-12BB-E611-9B5A-0025905B85BC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A777C8E-E6BA-E611-AB9E-0025905A6076.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/40F08699-4CBB-E611-B01D-24BE05CEEDB1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/40F63331-FDBA-E611-AE3F-0025905A608E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/48F2838A-DCBA-E611-9869-0CC47A4D7654.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4C297CEE-D6BA-E611-A4DE-0CC47A4D76D2.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/50762A77-F4BA-E611-A3A7-0025905B857C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/52991218-ECBA-E611-AAD4-0CC47A4D76D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E236726-FDBA-E611-B408-0CC47A4C8E8A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/74134AAC-4CBB-E611-AC57-00304833557A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/74DAE9D8-E1BA-E611-973D-0025905A612A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/782A90D7-4CBB-E611-B687-001EC94BF09D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C66E17C-E4BA-E611-B27C-0025905B85AE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E7937E0-E8BA-E611-99F7-0CC47A4D76D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/88993FB5-D7BA-E611-8747-0CC47A4D764A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8AB305C7-4CBB-E611-B636-FA163E0D417B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8AF177FD-4CBB-E611-8ABB-001CC4A68B9C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/927903FD-FFBA-E611-9DD2-0CC47A74524E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/92B34F4A-E6BA-E611-82A6-0CC47A4C8E14.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9AFB92EA-DFBA-E611-9C47-0CC47A4D7698.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C126B2B-E5BA-E611-976B-0CC47A4D7678.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6B5699F-4CBB-E611-BF31-001E67DDC0FB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AAF7899D-4CBB-E611-A4EF-001E674FB063.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AEE14A87-E6BA-E611-B071-0CC47A7C361E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B29CEC51-F7BA-E611-9222-0CC47A4C8E2A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B6865AF0-4CBB-E611-B4B5-0025905A60F8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B8FF7D86-E6BA-E611-B0C3-0CC47A7C3422.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BC1C5760-DBBA-E611-ACDC-0CC47A7C3612.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C087C49E-4CBB-E611-8733-0CC47AA989C0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C22060F4-4CBB-E611-B18C-0025905A497A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA35615A-F6BA-E611-A68A-0CC47A4C8E3C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D250E3E9-DFBA-E611-A8E7-0025905A60A6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D6BCDEAB-0CBB-E611-B8C8-0025905B8564.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E06ADC17-13BB-E611-B84D-0025905AA9CC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E0BE99A7-0DBB-E611-9C5A-0025905B85BC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E28F52AB-E7BA-E611-A4EF-0025905A48F0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E4A32FA3-E3BA-E611-9D88-0CC47A78A360.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6485E8A-E9BA-E611-988B-0025905B85BA.root',
] )
