import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/24A15483-1785-7A47-BCE5-F140CA1F824B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/3216ABB0-3D2F-AD48-8FE9-66BA009578AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/36EBA390-944B-B744-B775-8F24F2D65F18.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/421FE39F-97C2-3C46-9A36-42BBB5770F47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/94A45150-4EF5-A74C-B460-9A216B5C6F60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/BEED9BB9-65AF-0240-B854-AF495D25A62D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/F17A20AC-9F92-574D-A1EC-B7B9BA8DF346.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/F2224C34-1175-F943-809F-EB42F2246530.root',
] )
