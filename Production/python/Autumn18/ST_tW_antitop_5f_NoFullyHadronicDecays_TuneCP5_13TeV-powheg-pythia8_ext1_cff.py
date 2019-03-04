import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/066DF377-779B-044E-9F92-5AABAB71D027.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/138B1308-D71D-6944-A538-0C7D0613701E.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/1F769EE8-3430-4048-AF2E-0057625B3E6B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/2CABD638-2E1A-6640-BF43-28DA13FE5E36.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/2F801710-29E2-1947-B1C1-D8E06D90FF99.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/30256243-050C-884F-9359-B67801B23E31.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/3A75837A-098B-4D4D-AC98-E8DDE7900E99.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/4A5A4AB1-B346-724C-9549-0124124CBB1F.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/4B4DA63A-C933-C14A-AAF7-AB6D1DB624B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/5EDD10EF-4C24-5340-8F3F-BAD1FB0153A1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/63EC4FB2-A34F-AB4A-9A59-8573EB38D356.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/6668E3CA-4950-0546-A5B5-338E3C5B5526.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/679C06E7-88B3-F542-9A3B-A9B072565C61.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/6B0B2AB6-4118-1847-9BEC-4E7DC7BD23CB.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/6B8E5143-8AE7-3C46-816E-AECBC08CC591.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7904B03F-4431-EA49-85D8-48A9D68C1C69.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7E3BB30F-EEBE-C04B-854A-56C3DD33E2A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/8BDB51D0-A8F5-924B-AFD2-CED3C23DA3BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/A382DE4F-E760-D54F-B42E-FDA5EBEDAE3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/A64375BB-47D9-BA40-86B3-160CE72C8979.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/AB3E85BA-93E8-0B49-BA02-78420505B39E.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/AC3D4815-66BE-7441-BD7B-293918BB54C6.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/D407135A-B2F4-4F4C-954B-7C2143E383E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/DD87B386-FC8A-CD45-9834-1C386E2B77C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/E1D9CC64-CD9E-E440-B195-58D53E0F9ADE.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/F1A07110-AD04-8B48-8F12-5F1E1982D3B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/F294102B-F538-6541-9715-45926EF0818C.root',
] )
