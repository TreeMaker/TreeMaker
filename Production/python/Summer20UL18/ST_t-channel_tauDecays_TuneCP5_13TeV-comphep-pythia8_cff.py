import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/10D9DC93-F8BC-624C-A212-15CBDDE2C23D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/111242A7-3270-1E4B-9600-E5CA1235CA07.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/136CA2D8-B3E6-8B42-BDD2-0B89623A0AB6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/1EA0C7C5-CE11-8140-87D6-82D1873E76FB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/2207122B-0045-F54E-A8EC-35E341E1D3E4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/2C8A34BC-BEC6-7B4C-A04E-1DC7DBAA567C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/37E4FCD9-64D8-D544-9C9A-044CD43AD202.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/3F756123-06D4-F443-ACE6-753FFF6E501F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/405B38C1-5CD4-4847-8ED0-6488C9ACBDB5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/4172F4E4-A45C-704F-AB0A-348455B0CF15.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/4878C678-2444-914B-BCEA-6A011AEA346B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/527ABD13-AA1D-EB45-9364-798A71E17EA9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/53643D51-96AE-F148-8379-4789DF3583B6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/565BC45A-2AD0-7247-A513-B8CDC7FFE2B5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/5B336795-296F-BC43-BAC0-B1EF72AE24A2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/5BFA8D1A-892A-9D4F-988F-9F4BF2E102EE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/72ADDC5F-A066-F848-AF33-3C88FCCDC1A7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/7F2FC749-CDF5-3F44-8D8B-CD68572AE563.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/85E815D8-F4AB-6947-AA54-0BC08A68F5B4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/8BCF5137-C4A0-554D-AD56-9A2279C78647.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/AB83F343-D98F-FA4C-80B0-6DD7980AA9B2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/B8656345-B033-5D47-9580-777D6E6D185A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/C0B62134-DFEB-7F42-A8AA-27631A6F6D8E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/C5E3A342-867D-974C-9910-81CC1016A6EA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/C9472AD7-5EF9-9041-839B-EC5F07F0BC7E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/CACF8226-F4DE-FE4B-ACB4-BCF086A240E7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/D05C2064-512C-4B43-BDF4-29699802A27E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/DF59E583-C980-8C48-9C5D-A3021E979D1E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/E257B9D9-5B8C-FA4F-918F-E0BB3F58DEDA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/E31939EE-66DE-194A-A18F-059317888EB5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/F50D83B7-7AB5-4641-9F3D-D2BD2B874078.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/F772003A-055A-F74D-A8E2-7DAD7AAC13D2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/240000/FF73D214-C9E9-704D-8CA3-D5F172CF234F.root',
] )
