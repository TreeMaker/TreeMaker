import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/00B1ED9A-D57E-7E41-90F6-CC26F068C9AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/03CF7A37-ED14-8A40-9BC9-CFDB05A677E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/0478A002-EA5D-2048-A9EB-1B9EBE256F93.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/05D49E35-18A0-1C45-847C-FBF870A347CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/12827339-D451-7147-8C2D-6C93D278F7E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/17146099-30EF-DA4D-990D-87B0F42E4AEC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/235D61E4-1113-3648-9A72-E5A087FA0FC9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2A269698-9304-8048-AEFF-2DFE9F464DD0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/2AD72DA1-E917-0841-9B42-B249BEB80E94.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/32E84334-73FF-FE45-990F-4EABFB438B90.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/4F869BCC-B755-984F-A633-11A2785B9BC7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/59BC3257-42A0-4948-B081-EB9B001C6A8E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/6AC3C67D-4B55-0C43-92EB-4F5EF5EE0D2C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/7E086CF3-4468-A54C-8B44-E2F1B13F5C6B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/81774F59-78FC-A94E-A7E9-C3F34245CB9F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/825595AE-C9E4-344A-BEA0-0EFEC9C537D0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/88F729EF-1DFA-E54E-A5C9-D072BA563682.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/8950FA4D-C184-A740-933C-313E451E7521.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/9F12D874-E3DB-834A-842A-5E18159CFD68.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/ACB95BE9-94D6-7E45-B35F-262205BA1146.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/C08DB33E-D38C-844D-BC34-EC581D1BECDE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CA557157-FED4-0B4A-9B94-505FC885F151.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CDF7CFF7-B7D2-E240-87DA-9BBE58AA6FCE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CF14B6EE-FB73-434A-8828-4F491AFE32F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/CF3C6B48-D09B-984E-B1BA-0E62F2014380.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/D3598D9D-E60F-3547-8E43-076F3C5CA057.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/E011389D-D7A9-774B-997A-BF758D7BA776.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/EA5B5780-1380-BA41-86A8-C2166E556A83.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/F802245A-AD56-6144-B011-1256690E3BAB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/FBAB3A97-6E7D-AE47-B966-06C301E6C64C.root',
] )
