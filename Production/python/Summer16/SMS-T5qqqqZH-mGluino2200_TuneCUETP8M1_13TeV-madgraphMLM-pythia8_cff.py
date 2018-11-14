import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/043CDA7F-4B5E-E711-8CEC-001E67792592.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/126BECF8-735E-E711-B3B4-14187763B811.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/169F6A88-6F5E-E711-B205-141877343E6D.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/18CD2A50-0D5E-E711-AD86-047D7B2E8578.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1AF67B68-CE5D-E711-8586-FA163EB9735B.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/24457F6C-1D5E-E711-AEDC-A0369F8363EE.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/28D164CA-585E-E711-B037-0242AC110008.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/30BB2CF6-365E-E711-A2AD-0CC47A4C8EC8.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3406B7C0-335E-E711-9479-002590E7DFFE.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C2909EC-0C5E-E711-ABEE-001517F80574.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50EE02CC-375E-E711-8A86-02163E013029.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/52642D31-535E-E711-82E2-002590FD5E70.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5CA1D8D7-B95E-E711-81C7-008CFAF554CE.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60E05728-115E-E711-B1A3-001EC9ADC8BB.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6CA25FBE-185E-E711-824B-02163E00B6B5.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88123FEB-075E-E711-BBE4-008CFAFBF576.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8ED483C1-475E-E711-85E9-0025905A6092.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9233A76B-9F5D-E711-BAE7-002590D5FFF2.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A211751A-7F5E-E711-8905-008CFA197D14.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2241DA5-2E5E-E711-9796-0CC47AC08C1A.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B4AD9EDF-B95E-E711-8888-FA163EEE60C7.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE981177-7E5E-E711-BF41-00259074AE8A.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C05CD193-185E-E711-9186-A0369F7F9350.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CEBD6095-185E-E711-B4E3-BC305B390A32.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DAFCA762-FF5D-E711-9897-24BE05C63791.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0322705-655E-E711-806F-0025907859B8.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EC90A7AC-0F5E-E711-9AA8-00266CFE7C08.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE1C4D91-155E-E711-858E-00266CF32A34.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F2DBD582-505E-E711-84D0-0025905C3E36.root',
'/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F80E0565-655E-E711-99BB-D067E5F91482.root' ] );


secFiles.extend( [
               ] )