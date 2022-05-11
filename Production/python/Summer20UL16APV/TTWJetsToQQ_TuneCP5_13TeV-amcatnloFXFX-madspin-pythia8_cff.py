import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/C75BC7D3-B019-8C4A-B695-42EDBCE79990.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/EAB4922D-81FE-1244-B7BB-50E916DA0FC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2540000/11361C1F-00ED-1D41-8A48-88052EEC90BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/52EFB65C-C3AB-D145-B6C4-016FB8851DAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/9C03EBDE-390C-DD49-84AB-E109DDAFCB56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C50FC0A6-2EC4-CF49-8B88-29281016B57C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/38988CBE-E730-F347-9A92-ABC3FF47B8F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/5402D515-353D-5B45-B0F3-0E5539871208.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/549895CA-82C2-3F41-B5DD-6DD04CD5502B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/59DDCC6E-2596-A54C-B4F2-E452A277B77B.root',
] )
