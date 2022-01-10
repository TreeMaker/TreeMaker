import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/20DEEAA0-62E9-D44B-BC0B-F6D06FDDAB4B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/349CDDC4-792D-A04B-8A1C-688ABF4E8A25.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/45DD0B6E-2E62-8F46-B7CB-E295B44A9092.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/4E914E2A-774E-4849-898B-398FB3CE5553.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/5DD6BB37-4C20-E940-8E51-666C56F47CEB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/6386CEF4-5973-D245-9154-4B6E494BFC7E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/6F113CDF-6AD3-C542-879B-E93D758C7AFA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/9C2FA230-C7F1-AA49-B03A-19C3E58110D3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/AB4F30FF-A403-D940-BA1B-AD4375D4B9DC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/ABBE0136-D9D1-694E-A059-60D1ADBC9225.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/B8AAD063-E113-9F4D-89B9-C4A8A8EE8B18.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/CCF3C016-8C49-8F4C-A832-E41DBFEA060A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/ECC30C7A-0D89-DD43-B079-F3E992985722.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/06730323-0F84-314D-A53B-51AB86A618FD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/1688C6FF-1296-8C4A-8669-574BADE1CBBA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/858A81EA-DFBE-1B45-9694-339ECB3F2A02.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/CB052EA8-7F88-E44B-9C0C-F76F511CA9AA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/F9D24952-C2E3-6E43-8F6E-6516CDB9DC3B.root',
] )
