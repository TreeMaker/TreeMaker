import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/563/00000/608C4E1E-ED79-E811-AC9C-FA163EB4EA3A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/651/00000/3E10E4EF-A07A-E811-8FA1-FA163E7FF480.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/712/00000/886DEC61-157B-E811-93F3-FA163E396B84.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/733/00000/0EFFD694-A37B-E811-8241-FA163EDDAF1A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/733/00000/64D7FEFB-A47B-E811-92D1-FA163EFD4E69.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/300744CB-5C7C-E811-85CA-FA163E72781F.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/423388F1-457C-E811-AAC1-FA163E35DF95.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/44132C30-4A7C-E811-989B-FA163E0BA969.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/4ED73F80-4F7C-E811-BC23-FA163E188988.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/68E0A413-757C-E811-B1FE-FA163ED06402.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/6C8932A8-697C-E811-AE20-FA163E04D7E4.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/72C0A2FE-387C-E811-B232-02163E00BE39.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/74133402-547C-E811-9D7D-FA163E80686C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/82BD703A-407C-E811-8557-FA163E791A6F.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/C02FD7DA-607C-E811-9D4F-FA163E4844DA.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/816/00000/DC1D0948-587C-E811-B98D-FA163E60AAEB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/819/00000/746DEE01-547C-E811-8540-FA163EF2167E.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/819/00000/D69C7B7D-967C-E811-A51E-FA163E9F7389.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/820/00000/7ABFC497-587C-E811-A2DD-FA163E96155D.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/820/00000/9CBC639F-517C-E811-B7C3-FA163EC93A6F.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/820/00000/B670706E-897C-E811-9D36-02163E00B416.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/820/00000/CA9FF2C6-4D7C-E811-9260-FA163E80686C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/827/00000/52EE2171-2F7C-E811-B41D-FA163E46A172.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/18ED1D3E-6F7C-E811-AEAC-02163E019FEA.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/28860ABE-687C-E811-AD17-FA163E5214A2.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/3434EDAA-5C7C-E811-B087-FA163EDB1403.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/58BB0AD1-867C-E811-9D67-02163E00AF4E.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/5E0B6690-667C-E811-B703-FA163E3CC492.root',
       '/store/data/Run2018B/EGamma/MINIAOD/PromptReco-v2/000/318/828/00000/64ECB4B9-6B7C-E811-9DDA-FA163E2D1094.root',
] )
