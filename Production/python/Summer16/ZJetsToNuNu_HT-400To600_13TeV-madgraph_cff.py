import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/685AFEA8-BDD6-E611-8CE5-02163E01441E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8278A6A0-BDD6-E611-BB37-02163E019B4A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/86157995-BED6-E611-B83F-02163E0144D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/925F1A8E-BFD6-E611-9D1C-02163E01192C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D2DC1B32-BCD6-E611-8925-02163E013496.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EA97BA73-BDD6-E611-8C7B-02163E01381F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/FEB6B8A6-BDD6-E611-81FF-02163E014339.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/7490E970-78D6-E611-8B1A-02163E019C23.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/1010000/E0393970-78D6-E611-BC5E-02163E0145B6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3CF62AF0-B7D5-E611-9FCF-02163E0138C0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4AC04D78-D0D5-E611-951B-02163E01275B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/827061E5-BCD5-E611-8D52-02163E014448.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A86B16B8-AAD5-E611-B507-02163E019BB6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A8943F58-B3D5-E611-8602-02163E019B9F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/06BDBDDD-A1D5-E611-915A-02163E011FEC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1EE6F9CD-93D5-E611-8B84-02163E0140DC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/24B0F100-8FD5-E611-97BE-02163E0143AB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2887AD24-89D5-E611-973B-02163E01411B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4494413A-89D5-E611-A9F9-02163E01470D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50B83F62-83D5-E611-95BB-02163E011F99.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/940F8B27-A0D5-E611-9E99-02163E019DBD.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E22BC335-90D5-E611-A0AA-02163E019D1F.root',
] )
