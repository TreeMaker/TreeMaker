import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/604/00000/92E20DD1-902A-E511-8B3A-02163E012A2C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/612/00000/E48F3C2B-A42A-E511-A2FB-02163E011C0F.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/638/00000/327469FD-0D2B-E511-96BD-02163E012B30.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/642/00000/684E983C-D12A-E511-B288-02163E0134A9.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/1A95440B-CF2C-E511-A850-02163E0138F6.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/4C593916-CF2C-E511-9FED-02163E014275.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/643/00000/9A86E40D-CF2C-E511-AD65-02163E0128FE.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/283F6D7B-602C-E511-8A31-02163E012A2C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/721/00000/FCBDFC75-602C-E511-B68A-02163E014376.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/781/00000/D85C9422-9C2C-E511-B8A0-02163E0118E7.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/402035C7-AC2D-E511-9D83-02163E0133DE.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/44864117-232D-E511-8C15-02163E01463E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/883/00000/CC542F3F-AC2D-E511-B093-02163E014181.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/116/00000/8A04959A-7A30-E511-8ECE-02163E0137FD.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/44AD0FCD-C430-E511-9CE3-02163E0125E8.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/86ABE6C2-4D31-E511-AB00-02163E011A04.root' ] );


secFiles.extend( [
               ] )

