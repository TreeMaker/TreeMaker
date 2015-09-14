import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/604/00000/1606A3BF-972A-E511-86A7-02163E013515.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/612/00000/7A0CE8FF-A72A-E511-B7DC-02163E011D1C.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/638/00000/10C07DF0-FA2A-E511-846A-02163E01474A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/642/00000/D20F8A8A-DE2A-E511-9D16-02163E0133FF.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/1E72D617-BE2C-E511-96A0-02163E0139A2.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/3C563818-BE2C-E511-993B-02163E0144D6.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/C061E81E-BE2C-E511-AA5F-02163E01208E.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/C6F9761A-BE2C-E511-932C-02163E011D30.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/CC199B16-BE2C-E511-B1A5-02163E012B30.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/D4FE721A-BE2C-E511-856B-02163E01250C.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/30BD3F39-542C-E511-A5DA-02163E011DA4.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/329A9A3B-542C-E511-B6B8-02163E01360E.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/781/00000/CE3105FD-A82C-E511-B330-02163E011955.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/089D049E-262D-E511-85A7-02163E0146EB.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/62919ECB-1F2D-E511-B387-02163E013796.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/E2546D9E-492D-E511-9977-02163E011D46.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/E49261AB-492D-E511-9FCA-02163E011E24.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/116/00000/7E03BD9B-7730-E511-BA13-02163E011976.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/201D1572-EB31-E511-852A-02163E01340A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/2471A7F2-6C31-E511-A71B-02163E0133F0.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/58D01EE9-6B31-E511-852A-02163E0139B0.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/647C27E8-E231-E511-A3D9-02163E012704.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/9E0526D6-F131-E511-94B7-02163E01428F.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/A0BF6FF9-8231-E511-AD78-02163E0133AD.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/BA9B25ED-E231-E511-976A-02163E01340A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/BE4EB725-7131-E511-84DD-02163E0139B0.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/DAF3D992-ED31-E511-812B-02163E014181.root' ] );


secFiles.extend( [
               ] )

