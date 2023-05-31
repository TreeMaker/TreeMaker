import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/B97ECF18-883B-4647-BEED-C5108EED3E4C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/29FB4979-BE7A-8B43-83DA-01B955BD2757.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/53C69304-133B-174E-9204-24D7ADD9F359.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/1EFF53DD-1A89-4B46-9587-2ABB105E8D14.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/B44B3BC1-1C10-EE4D-B693-6E4D3DD1DFE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/EC5A8650-83DA-6345-A5F9-6D45490D0FCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/EF0B9A2A-998D-B042-B50A-989D017E67B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/017D4C3A-C9EF-2A45-981C-11642D7F77C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/02DEDF04-E757-E146-8A6C-A8E59C9186A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/143E8F80-F30D-9A42-BD98-DCD0F9C6917C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/1F79899F-ECEC-D647-A2E9-34AD2C87B565.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/4C601CC8-629F-954B-8C58-9B6E3D2CBFAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/6E9D5340-08EF-3B4B-B57A-FB2CD56E6D87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/7E8F0281-1378-484A-B0F2-51AF3D722B21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/94A758AC-192D-EF44-8147-1D699C5A6BE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/94D44A7F-F062-494E-8134-D53429119C56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/95309C62-3ED0-EB4A-95B7-0FDC54714B8C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/9A0F604D-B36E-7F4D-9C37-9CE8CB38D898.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/9A73DF16-1200-6948-B70E-DB6B6CB9E6BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/9FCD3F55-C199-F74F-8722-BD3B99E440BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/A4503B4F-5C08-C64B-917A-FA34A8AE9C02.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/AF3B2672-6E0E-5344-BC98-D4FEB8001DFB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B0397395-F645-9C4F-9597-EF6656E4ED07.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/BA09A88E-E2A1-1E40-AE41-C39B45A30254.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/C1F8359F-9A95-2443-91D4-CB6651439CBD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/D612D2E7-DAC1-E74E-A15E-C5B248A0CCF2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DAF017A6-68E4-074F-8412-455E6FE8618C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/EB55473E-A38B-1346-A280-13FB1FD2EAAC.root',
] )
