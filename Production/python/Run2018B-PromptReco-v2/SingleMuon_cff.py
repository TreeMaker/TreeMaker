import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/070/00000/FC42DE19-0476-E811-B579-FA163E78589E.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/563/00000/DACE08EA-EB79-E811-B7AE-FA163E8BC7EE.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/651/00000/046EEF42-A17A-E811-82F1-FA163E048F61.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/733/00000/BEAE5A42-D17B-E811-A212-02163E017F53.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/0206915B-1D7C-E811-8696-FA163E2E52D5.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/204FCC42-207C-E811-BBD5-FA163E65E6CA.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/2A492229-177C-E811-96EF-FA163E64E527.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/646A5687-247C-E811-984A-FA163E802403.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/7C297997-3D7C-E811-AA84-FA163E09F2C4.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/7CC0BFB7-127C-E811-B312-FA163ED2A73C.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/88DD0A35-267C-E811-95FF-FA163E89BD5B.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/AED30E2C-2D7C-E811-A355-02163E019EEA.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/B894FCC7-787C-E811-B6FC-FA163ED06402.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/816/00000/FE9ED76E-297C-E811-8003-FA163E002EF6.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/819/00000/A4D8C5A3-627C-E811-BAE5-FA163E687EE7.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/819/00000/A6994F71-3E7C-E811-AAE1-FA163EF2167E.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/820/00000/02354F28-3B7C-E811-A664-FA163EA10FDF.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/820/00000/08E583F5-377C-E811-BF9C-FA163EA2324A.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/820/00000/0E071947-6A7C-E811-80C3-FA163EDCAD2D.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/820/00000/2E87F16F-417C-E811-B256-FA163EB83F5F.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/827/00000/BE1F88D2-2E7C-E811-B76F-02163E019ECE.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/828/00000/045B9EBB-717C-E811-826D-FA163EF673CF.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/828/00000/40354768-6A7C-E811-AA93-02163E019F14.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/828/00000/52C4B046-597C-E811-A486-FA163E1588A7.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/828/00000/D29A4639-577C-E811-B0ED-FA163E8F57B5.root',
       '/store/data/Run2018B/SingleMuon/MINIAOD/PromptReco-v2/000/318/828/00000/DCB2F6CE-537C-E811-A8DB-FA163E7A3564.root',
] )
