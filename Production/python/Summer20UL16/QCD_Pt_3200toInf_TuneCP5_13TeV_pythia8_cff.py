import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/06952735-4580-8042-A4D0-32AEF82560B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/9212ABB1-7D8C-D644-829E-6BD2981F4B1B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/F2B609CF-3453-DF4B-B483-8CC5A7872D9F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/621F4CEB-0C16-C740-976F-E7C23AF7930B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A2C54981-32A8-8142-8D80-DB142BBEDD1D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/004C258A-3D9C-2B4A-A9F2-458D221F0952.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0E3B718F-5504-E143-9F65-FE2FDDE39EF0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/18059C51-3D3E-7C4B-AAA4-9B568BC708F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4F811C67-8B70-8F40-B3CD-80DFB5BB73CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8488026B-9442-0041-9498-3F1E4D0A95F9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8929EF63-0F73-B643-AF6D-2B3D667E28D4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C28A84D2-96F5-A147-8581-AD803E5441CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/CD3E95C7-678E-3D4F-B6AE-AD3E8FE527FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/062A4C80-6C20-724A-95B8-0AE1D2A1E354.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/09877EFC-A0ED-9C4B-A5BC-C3E1AE040487.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2EEA39E4-232C-A640-AE91-4DE449F77AED.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/30AD803A-570C-3945-BF31-66AD8DCDD149.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4C34C6FA-6122-6C40-B2B9-002EBCB29959.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4CF742D6-601F-1543-9E5B-EABF1E9920E9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5D3ED1A3-FE35-0E45-A985-D67289009168.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5F9D49E9-FA57-3342-9EA7-294C2D15A05A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/678542BE-0E9B-3648-AECB-2DB9422A09F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/91E98205-9C73-5C42-B1F6-8D6A61DF8E87.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9D673CF1-1F69-1E43-8DA9-5849AB4F2349.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/CB049A8E-2E91-E141-B619-1D15A90FD24B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D0B4A934-314B-6146-83B0-B151D9495934.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F82EA0B9-E6AF-2B4F-9BC3-13C15C32BF99.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FAD805B0-D882-6146-87D1-B774DDCB00BD.root',
] )
