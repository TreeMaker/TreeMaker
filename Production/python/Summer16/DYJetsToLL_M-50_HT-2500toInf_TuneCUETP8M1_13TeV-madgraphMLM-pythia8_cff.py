import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/064884B1-9AC1-E611-B6D0-02163E013D77.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C99DA93-79C1-E611-8D0B-FA163EEA85D4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2ACBB09B-7DC1-E611-84C0-02163E0165C2.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/308C289B-B8C0-E611-A7C6-0025905A606A.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/52E65577-96C1-E611-8600-24BE05C488E1.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C8C9696-AFC0-E611-BF54-0025905AA9CC.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6694BD4E-9AC1-E611-8C51-003048F5B2B4.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A45D33F-7FC1-E611-BAA5-0025905B85D2.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/72F8D219-9AC1-E611-A48F-842B2B42B536.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/844FF1A4-B5C0-E611-90C3-0CC47A4D7630.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/947C3809-B4C0-E611-8344-0025905A609E.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/94C4848A-84C1-E611-9A92-0025905A6092.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AA6E5A5C-9AC1-E611-AB17-001E674FCA99.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BE1438F4-B1C0-E611-A7B5-FA163E6EC48D.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C07C7369-9BC1-E611-A79A-002590494C38.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CAD47782-AEC0-E611-A8D3-02163E00B829.root',
       '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F2CBBFBF-AAC0-E611-8F2A-FA163E4BD49B.root',
] )
