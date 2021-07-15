import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/005BD159-5C34-CC42-89EF-54E9A5D73668.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/01980885-B2A8-4849-92F7-815BDCBF0F7D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/0601D1C5-8FCF-5C44-B888-01D28A117693.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/0B53E9E3-1297-A74D-AEC5-CEED905DFCE1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/16D3E807-94D9-BB4F-A919-F4E8C87F9FB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/1F9A995C-F7DE-2A4D-B63D-6AE49890787F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/311594AB-853F-094E-83B7-0F184569C4C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/48AACBC6-3AAB-C540-90BA-27627B672F2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/523A3B85-925D-E844-9662-3C9FC30C169E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/53C10091-FE32-3B4C-932C-42F7606C91F2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/53E645A9-5FE7-3040-B6F5-0C42FBE216CB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/56E09787-6ACB-7B4F-B859-4CC794195A7F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/5739E046-F85D-5C40-B875-7F8DE5E04A5A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/60708E17-499E-CF49-A1EE-4269D6D7340F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/61AE48E8-5147-2044-BCBC-282C7C8C3659.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/64293B41-4502-1846-BCB1-19E1F303C4D2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/6779DEE2-8246-854D-ADE6-853673714767.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/698F1184-FD7B-6C4D-9202-527D7293200F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/703FA0EC-0FBC-6343-9144-A6A9CF42E52B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/786F7EAD-B576-764F-B323-969BFEAAB4AF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/7FF71C52-E30F-DD46-9000-ECAB08853A50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/804BB038-4D0B-AA48-BC29-DDE1614E355B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/81E2E5FC-161A-E247-AAF6-AFBE0A3B087C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/872ED98A-C3BB-134F-82D9-F28B7EB6F6AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/957CB792-E9B2-874D-9EF6-36A4D9092078.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/9F8EB479-CA91-8642-B272-21A962058BA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/A2951666-642A-EB48-9593-BB177B55480B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/B9345638-B27B-C449-A5FB-4C5DE059C31A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/BFCE7255-B669-CC42-B9F6-EBE5F0DD269C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C22D58A2-6EC6-F246-8CD8-3522CEA6CCDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C267FA44-5399-554B-9989-9CCDB32B9620.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C61D1127-89EC-844F-9465-B24B0FE3CFA0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/C9B672ED-76C6-2446-A411-057FE60AA828.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/tZq_ll_4f_ckm_NLO_TuneCP5CR2_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/280000/D7E5938B-7E8A-2F4B-B671-49C0EAE284CE.root',
] )
