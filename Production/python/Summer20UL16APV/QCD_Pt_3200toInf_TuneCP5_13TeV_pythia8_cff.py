import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/078C5862-FCBD-754B-974F-465C2D961A88.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/09335583-61D9-764E-9013-E05BC9C3AC22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/2371E114-2ECC-FF45-B843-A907FD3DB689.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/4167FF10-1A1D-6747-BC35-7F8E784AD67B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/440DD4E3-5F88-7747-85AA-16F31A518692.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/5059EBDF-78DB-2148-BEBB-D3CFB98F56F0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/51F1791A-D1A6-4341-A770-D2D065068B92.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/54CA60F9-8BC2-984D-B40B-B4A886E837F0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/76B3B6D3-B4A6-8A47-9EC8-9A97934628EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/97FBFE34-2722-9846-90EA-15CCADB16D5C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/A6268548-9CF6-C24A-A517-690C46E6F651.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/AC9AC158-B497-0D45-94CE-6CCF3886ED92.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/B9644680-9309-3842-976D-363A24ADB95D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/BAB875AD-5CA9-C04A-8E37-4F15AB726520.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/ECB2A737-6204-E049-87E2-4C4702FDFCFA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/ECDF4923-E34E-E24E-9B51-ADD1869B565A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F2AAFE51-E4E8-E044-B9FD-1118E48D84BC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/08DB2D5C-72AA-ED42-8434-F3A666612104.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/10E3ACE5-1BB0-1E4F-8912-3F834EA530CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2AAC2029-252F-464A-8ABC-13D5B16788D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/44D0A0AC-4F6E-DF48-B167-F083DF998385.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/493AF989-A8D7-5440-992F-5556BA015AB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6C0E9835-3554-5545-811A-74323450A447.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/702035C1-3C57-2542-A3D5-5BDB3DCA0D66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8F58DEF9-93F8-F54D-8207-1ADB8A123294.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C037062D-9F5B-624D-8B44-07EB706CF647.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D4F2A11B-1ADC-0F4B-B2DF-D060BA759BCF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E3511CE8-A301-F14B-B1BB-060747E5F5D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E8224502-52FC-B348-BA32-428781473757.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/FA25DA26-E85D-2C41-8AA0-87BA70F93042.root',
] )
