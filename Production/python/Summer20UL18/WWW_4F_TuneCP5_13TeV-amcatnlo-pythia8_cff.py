import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/17C0547F-4A3F-5041-9D7D-45E77418694E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/23D018C9-769D-FF4A-9ECE-CB398A6496C8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/254D99BA-5983-7342-BEEF-592C243FFC6B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/288775DE-E3F6-534B-875A-4C423A4720F9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/2DF257FB-354D-2246-96C1-2B45D338A497.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/308DFE10-8F3B-1446-997A-C12FD5CF12FA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3096BF35-0E59-5043-9396-D6CA8AECA293.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3A6F13DA-EC07-594C-8953-2E97D07212E1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3BCFC597-94A1-9A42-8116-4A458970D0D1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3E0D101D-9617-3448-AEAA-56961C14759B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/415FB515-4B7B-3B49-84FE-5C576E18D0EC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/45D3A746-FA04-5A48-A9AF-F3BC08477A94.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/4F0E134D-488E-1043-BF32-3E2F8BEE7DFD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5479F75B-A7E1-F541-AE20-0AB3DBC3FCEF.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5A5E6CB6-BF52-E74F-A299-1EBA1A29E254.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5E331C65-5901-8543-8A00-6E535C1FC67C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7DCF3D6E-E8D2-EC4C-AA70-25729462E384.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7E32A60B-6A97-FF45-9EE9-9E21014D6D09.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8C0D2474-0121-384E-8D75-52323B3BCEEA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/9050AC6A-7850-674A-8E81-3DBAE51B4C98.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/9984D07E-AA09-104C-B3B6-82B7BC31B454.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A6394B94-EEED-7B47-ADCF-4146C2B019DE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/AB7FB9F4-1E34-A14C-A047-67C15D908920.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/AC2B3390-D02D-2348-B531-DC9BE48B4649.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/AD29D9B6-0BA3-4D41-A786-459A4C4961B0.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/B89556B7-0561-0544-832B-8A1E1478AE5D.root',
] )
