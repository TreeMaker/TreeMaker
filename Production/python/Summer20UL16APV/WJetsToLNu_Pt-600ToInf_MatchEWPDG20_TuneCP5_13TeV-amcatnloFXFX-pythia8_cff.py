import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/0446DF0B-2A5E-894F-94A1-3778160D4F75.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/0F3142CE-C537-D244-97E6-7F0C1FE9343A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/139EA782-493D-3B49-8E01-1A730E9CAAEB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1782D249-EB3A-E646-B0F3-ABD82136A322.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1AAC44FA-AE22-C04B-9C64-3B130F81A462.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/296D28AD-E711-A94F-B51E-C817DEDE13E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/2BCA076F-72AC-F84B-A681-D190D0662134.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/2BD5B7A6-4294-2745-94B2-73D6FDCCEF56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/2D119495-B010-9347-89F9-339059E0EC7A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/2E9473C0-484C-894D-9E85-05B703F719B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/39EDADD1-F0F9-974F-9EF5-1374E330E6CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/39FBE9CC-BB51-D74E-BC1C-B6E4DFA6FACB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/449E7582-8C9E-7F42-A8C7-DB433D708C2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/505954CD-56CB-4946-8832-28F58D55FA2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/52123FA9-0C0E-8D49-AD5F-20FF51082EC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/5988B3A0-733E-5541-A2E9-3EDC65AC1236.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/5F4EFCC1-B877-AD4B-BC52-A43F8905B1D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/637D3D46-036A-7644-A899-F0A0FE876299.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/696743BF-CCBE-3B42-A795-E9E84B8A9890.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/69A14EC4-18F7-C747-B2D4-1C35DA93AC27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/6D3BE925-4CA4-D54F-B25D-7AD015209860.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/6DF2F33A-3A4D-9442-97B9-B8D686599470.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/7D6EAFF9-75F2-A64A-8ED2-37E0B293532C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/7F01FFA3-1E84-EC4B-8E62-88F19F10BF49.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/8F5CCDCC-183C-9A43-9C54-4E8DD476FC0B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/941F1FC0-EEE6-BB49-814A-22051FB79FE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/9EF74296-A2ED-C34C-9BF3-1B61AD53C947.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/A2679C27-33C8-494E-A8C2-CD8585AD077E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/C9942494-F0A3-E14C-9D5C-46C00089BFE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D35F0A62-A86F-7840-96BB-93ACB8B50E93.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/DAEF6044-9FDF-E14D-8995-B3E1A04B0ACC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/E0328879-E440-404F-8C37-0F557BDDEED3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/E67564F5-664E-2F48-BD3B-21E594C2E840.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/F6FBC671-E697-CC4A-8F03-97F209D66CDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WJetsToLNu_Pt-600ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/F71CC03D-A7A1-374C-AB87-F24610D4560E.root',
] )
