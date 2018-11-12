import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/181A15BF-2B4E-E711-815B-A0369F836430.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/2EBE8201-0D4E-E711-8157-001E673972E7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/2EE8D9FF-194E-E711-86DE-1CC1DE782F02.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/30DF411A-124E-E711-9AA6-0017A4770478.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/4A5A2B99-374E-E711-ACE0-0025905A4964.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/4C7219F0-2D4E-E711-9560-0026B9278678.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/5262561E-6E4D-E711-92F9-0025905B8580.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/68247EF8-384E-E711-A91E-002590FD5A48.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/6E19D6F7-314E-E711-9AFB-0090FAA58974.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/7C06D0B8-354E-E711-971B-0242AC110004.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/AA732980-154E-E711-9ACE-0025904CDDF8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/ACFE1458-154E-E711-918C-001E6750489D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/B2555655-6F4E-E711-B672-3417EBE64AFE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/C21971D9-1A4E-E711-B70E-008CFA152104.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/C2E18BBD-2B4E-E711-B4DD-0023AEFF2CD0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/DC5C08C7-104E-E711-99DE-FA163E91615A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/E017C1D8-694D-E711-BCEA-0025905B857C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/F454F204-384E-E711-AB9E-002590E7D7D0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/F67F31FA-1C4E-E711-8569-B499BAAC039C.root',
] )
