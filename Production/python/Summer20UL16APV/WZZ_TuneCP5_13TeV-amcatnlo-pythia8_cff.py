import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/179FFCF9-0FC5-6D44-B2BA-078D3DAB0C4A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/228E51D9-0D58-FF41-A561-078EDC5053D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/27508F48-709B-E841-B533-8D975D2D3036.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/33C73CB8-3D65-C142-8C1D-100B1FEAF507.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/3A47437F-5C75-EB49-89B5-EF088FA450DB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/43106697-44BF-274E-913B-C7126BA5059F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/5FB7E826-378C-E446-86F9-F54041BBABDA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/63E51344-9AD2-1241-9DB1-D0A0244B12E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/899F605C-18E9-8342-B41F-4C4B4951D478.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/8A8C65AA-9D9C-4D44-9374-91B7BE5B2944.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/943D1973-6F83-3042-8C19-F4790CDAB472.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/98EDC21D-2C2E-634A-9ED9-3DAD1590209C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/A44197DA-940E-7348-87FA-A23921523A11.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/A5089133-A68B-BC48-94E9-02B6AD8F6195.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/BDD58488-1672-5D44-A1C8-83E2530B9756.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/C55A9D56-4A81-3A48-B0C2-743743DDEA63.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/E8335B20-B3A8-F54A-854B-82F057E136A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/F382FAEA-2DDA-7F48-9BDE-AFE38F242026.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/FD1EDFEB-AB37-8C42-9E55-F8EA325E474C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/FE29E28D-3AFE-D840-8327-CE9016842856.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/120000/FE9E31E7-EBFF-6449-92CD-9C65E7526508.root',
] )
