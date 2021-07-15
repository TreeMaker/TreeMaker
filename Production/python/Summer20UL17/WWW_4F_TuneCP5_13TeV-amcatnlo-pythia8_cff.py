import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/05D384DF-CA07-CB4D-825A-264AE7FA09B3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/177272B2-61F1-E24E-9B0B-16CEDF5213DE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/1C5752A8-AF07-5E42-A84C-9B1E86440834.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/27512322-CC96-564D-9641-5E4A7A4471C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/289A3CAF-D3EC-6C4F-B609-506FFA0A9357.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/3AB0080E-C00E-A541-AE7E-F451F31E1191.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/5346A457-CBA8-0742-8074-A40A646CB7DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/5FACAA9B-4F75-714B-8B28-3CFBD14354DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/618B13DE-1330-7A4B-B2EA-EE0103472C8F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/63954389-4615-4247-A155-9889DC442166.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/6814599E-FBFC-AD48-8ADC-3D26B2193020.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/71F571A5-2215-864E-B710-51ABE990144B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/74C0AEDD-7F4A-6948-8CC9-DFA799224841.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/7AEFEEF4-E09C-C647-A1C1-03C74F0E323D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/ADBF3CAD-F4E7-0747-8541-C5A8B285D7C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/B6CB7236-0E3F-334B-A446-D4DF63C2D112.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/BDADC96D-852A-074E-BF4D-70A6384EBC8E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/C4BC4E60-1DE7-4644-BDB8-E656DC3DA765.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/D66D7680-1FCE-634D-8DF0-2537AA9800B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/DA1A2EFF-89A9-BF4F-BE7A-EE6F731C1A0E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/E23B23AE-3808-504D-9222-2E566578A4D9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/ED356278-BB0D-6548-9843-D27EE45D091C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/EF63B607-1074-C848-8418-69A633A3E0E5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/EFEC3B86-A497-5949-9799-2EBAC3CBF85F.root',
] )
