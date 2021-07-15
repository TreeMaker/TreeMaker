import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/026A0C87-1B59-0C45-AB31-631C00D19CC4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/03ACE3F2-B39B-7542-8E37-DA50B7B9CE01.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/136AF90A-1F69-0C4C-88FE-A889A7583420.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/16995EA3-5009-1041-B765-C0E01CC76F8B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/1CDFFB0D-1384-8C48-832A-C3DE620E20AD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/2E608CF3-5CE2-6241-86E9-4F25B1B737C9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/324F8299-9C7A-9C4A-A457-573C638513AF.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/42CBE6EE-BEEA-8C40-8F90-E0D871F24731.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/4D805C94-5B7F-5843-8990-5116C0BAD4A1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/5037384B-56DE-B34D-ACCD-DEA312BDACFA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/512BE4B9-B358-D043-AF6F-F9E08BCED920.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/5188E567-3724-9746-B1A3-34B6C7F4CC51.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/54369A6A-A13D-1947-89B6-DA92DABF648F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/56C66612-76BC-6844-AE77-D20BD62DB2B2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/57D0BC4C-42E1-854E-ABEC-BE1DE4B585F3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/58547144-BA46-3C43-A70D-1275C317413F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/6870F963-8094-0B41-99A7-67C24C6648B4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/740B2E12-1D67-9245-9353-381A1F188C56.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/7E264CFE-8360-E447-8627-428AB169EDF5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/82A13875-6A50-094E-87F5-2C8D65DA44D0.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/838FF5AF-BA80-994B-B785-8B8D5CAC3C2D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/8952D558-8C50-724B-881B-3439DB58852E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/8AB5AF47-FD14-B542-B79A-0892C2BB8B4E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/91DABA9B-B47F-B944-9CFE-8A2E51AF2DF4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/96296CA1-828C-FF44-AD48-FC26C8F20593.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/A306D3D2-B5C0-E04C-8DDE-696539C74A2A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/A7FE9E4E-A748-D041-B3DE-2021C7570CB6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/AD54B436-5076-B042-9CBB-0F24FEAD4869.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/B4BF16A5-13C7-964B-8848-D392611672E3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/B953EBEF-886B-864F-A99E-3ACF666C650D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/D0C7E420-5FF9-8D40-A7C7-C3D17D1E70F2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/D5294920-B66E-644F-A2F4-4FD59CC2AA7D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/E54C67E5-C8F5-1B4E-BCE7-DDCDA59AB77A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/F4203F24-CBFC-4549-B624-5CC0E70A0E67.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/280000/F501C0BE-211E-C04E-90A4-4D7C5D39B260.root',
] )
