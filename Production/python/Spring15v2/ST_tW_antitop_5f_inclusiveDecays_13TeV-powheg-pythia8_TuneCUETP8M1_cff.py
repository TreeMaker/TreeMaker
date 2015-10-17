import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/044B267A-7D6F-E511-B43A-00221981B438.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/1C9DEB79-766F-E511-8157-0024E85A4066.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/1CB7FAF9-776F-E511-9472-00221981B434.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/1E1211EB-776F-E511-8856-0024E85A4066.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/2C898979-7D6F-E511-B1F7-68B599B95960.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/36510969-7D6F-E511-B045-0024E85A5153.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/3AC28E91-7D6F-E511-887B-00221981B43C.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/528895F3-776F-E511-B0E7-00221981BAA3.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/547B2389-7D6F-E511-9094-0024E85A4FD7.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/6AA9B067-7D6F-E511-91A4-6CC2173DC2E0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/74E2AC82-7D6F-E511-B2FA-0024E85A3F69.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/7A10626C-7D6F-E511-B49F-0024E85A4FB7.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/7A30006D-7D6F-E511-B954-6CC2173DC240.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/86CFAC74-7D6F-E511-B7C8-0022198273C0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9412E284-7D6F-E511-9BD8-00221981BA9F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/A62996F3-776F-E511-8F79-00221981BAA3.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/BA3724E9-776F-E511-B1A8-00221981B410.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/D291AABF-766F-E511-A820-0024E85A4FDF.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/DED61976-7D6F-E511-B0E4-68B599B95740.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/E66F99D8-776F-E511-887D-0024E85A4066.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/E8B99B66-7D6F-E511-AD98-68B599B9B998.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F0D96574-7D6F-E511-8372-00221981866E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/FC30537E-7D6F-E511-835C-0024E85A3F0C.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/200726C6-C46D-E511-BAAF-0024E85A4066.root' ] );


secFiles.extend( [
               ] )

