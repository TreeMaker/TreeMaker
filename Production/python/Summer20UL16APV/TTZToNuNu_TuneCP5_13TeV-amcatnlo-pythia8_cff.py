import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/041C32F2-AEFE-8248-8D1F-FA61E22ADCA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/329A320D-2E49-E24E-A1BF-EEE69E59814D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3E23B61E-832B-A04F-96ED-DEBF0DA3F2CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/487626B8-3F7D-D247-8D5E-DD287C24A555.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/509E6B47-0038-C341-856D-B6B5CB85BE87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/56600739-B60B-1940-9CD4-57DD5E2B0D28.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/6FD95C61-AA01-754A-8075-1698C5719AC8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CD31F565-8385-E345-811B-57244BF9C34C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/24CBA2CE-6C7F-744D-85C4-0F7D676238ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2947F669-DA35-5C4D-8992-D932EBE964A1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5695F7A1-DF11-4D40-8258-5C2BC3A2CC58.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/74676C54-B334-8F46-A3DD-7F9AF3396353.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8236FEBA-06C8-014E-BA64-76E98BD7895E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8570437B-05C2-D44E-A6DF-F03A59532308.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8945D522-6D25-6B47-AA1F-D96CFD85859D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/952FF624-7E06-1D46-A1BD-DF7C774D6855.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9A8C5184-DE59-2C48-8C1B-9AA07DCED11F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9EBB53F3-F56A-E94E-BB29-86B3B6FD8D1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A0338D19-D83D-3C4C-8E5D-2B4A98CBDFE1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D3135D21-DB2D-814C-A655-68D7058E17F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D4EE13CF-AD11-9B46-B348-65251B2F060E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DAEFC1AB-EA12-3C4C-8F6D-DE22D6C01137.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E3B1E3A4-30E7-9F4F-930B-65309AD7E793.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F44BA90E-D8A2-8848-BEBA-51F36E274CC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/FBD3BB89-F2AF-7C4C-B4C5-0AFF5D3DAD44.root',
] )
