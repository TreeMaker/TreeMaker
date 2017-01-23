import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00BA2518-0BCE-E611-B6A8-6CC2173BBEE0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/18A9055C-04D2-E611-AC79-90B11C2AA430.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/20735960-22C6-E611-BD0E-001E67FA394D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/20C07C04-22C6-E611-8598-001E67E6F8CD.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22D8A807-EDC5-E611-A6C0-0CC47AA99436.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4A67E67F-DAC5-E611-BA91-000101000026.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4ED820FC-3BCF-E611-81D0-00266CFFC80C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/569CC0DC-6BD0-E611-9E51-00010100008A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5828C2BB-03CA-E611-AB64-F04DA275C2CE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/646DE31F-FFC5-E611-B33F-02163E014E88.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7CBF49DE-9FCD-E611-AF33-002590494DA4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/806753FB-04D2-E611-8F34-002590A36F46.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CCCBDE17-FEC6-E611-BD5C-001E67F8FA15.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EEA2572D-CACD-E611-BBCB-0CC47AD98BC2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FE6C70C0-FCC9-E611-A9F3-00259048B920.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEAB3042-DAC5-E611-97D8-02163E01763E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7479959B-98D3-E611-B2D5-0CC47A6C138A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AA2B5DC8-98D3-E611-BA77-001E67396D56.root',
] )
