import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/4E725089-4B24-E511-92A7-0025904B26B4.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/62600390-6C24-E511-92D2-02163E0136C4.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/6AAC588A-4B24-E511-90EC-02163E00F510.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/80BB416E-6324-E511-A683-003048F5B6A9.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/821246CD-8E23-E511-9348-002590E39F36.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/8A79097E-4B24-E511-BADD-02163E00B82F.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/92EEBD4E-0923-E511-A387-842B2B7680DF.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/A2E8AFAA-3C24-E511-92EB-008CFA197998.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/D43DD67D-4D24-E511-BF26-02163E0133B0.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/D69F8C60-1E24-E511-B6F2-782BCB161F1B.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/DE0ADE51-F523-E511-A265-009C02AAB484.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/F2F2673C-FD23-E511-A0CF-0025905C42A6.root',
       '/store/mc/RunIISpring15DR74/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/F2D3D725-9722-E511-9F6C-0025901D0C4E.root' ] );


secFiles.extend( [
               ] )

