import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/0B7A5B4E-7FB2-1046-804E-4AF02FDAFC42.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/589B2178-A7A7-4F4E-A57A-9848A7C5683B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/7A58D81C-DFF0-D347-ABFF-5D72E6DAE5E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/D5F029AA-0ED8-0845-8E5B-C6A964387AD8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/E7455295-7AF6-E046-B1A5-4390067ADD55.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F1ACCD00-B8FB-CF4F-9A35-17AFE3670B27.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/92054F49-64C1-7D49-9DD4-699D71663BFC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/F2B8C24B-633D-9147-8B11-37ABC2EC2525.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/18F5EC58-B7E2-3040-91D2-56537883C4CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/9F73942D-0412-0744-A53D-72EC77A7E7D7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/EC2BB207-FB47-C940-A5F8-48E31DC79E47.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3D6C7163-2FA4-1F41-BBC9-1650A3E93874.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/50EB97CF-5E91-9A41-9C56-DF56CF87E480.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/56CF5AD9-1275-7042-8C6D-A51BEA3AE2DA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9E7D4E0B-6BCE-2C4B-A43C-94B56D5E5146.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D7BABA1E-8C4C-BA49-816A-F0B8C0E17DDB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/332E0840-8C80-A248-BB0F-C2F02AE89357.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5F391DE7-6EC1-574F-A20B-B7867CCC922A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZLLGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/995E25EB-7BDD-8840-AB1D-C693EBE3EDF4.root',
] )
