import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/604/00000/865C217E-992A-E511-8FD4-02163E0127DF.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/612/00000/DE1D52B8-AB2A-E511-AF79-02163E0134CC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/628/00000/404908F7-B52A-E511-AC9A-02163E013830.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/638/00000/0E9B99F5-F62A-E511-A7F4-02163E01299A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/642/00000/363CBB73-E82A-E511-B93B-02163E0133A4.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/643/00000/26E24212-942C-E511-953D-02163E012044.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/643/00000/34B19403-A62C-E511-BC66-02163E0124CC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/716/00000/BCC3BD84-2F2C-E511-96D3-02163E011B19.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/721/00000/284B19B0-462C-E511-9BDF-02163E011861.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/781/00000/501608D5-AD2C-E511-949F-02163E01420D.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/883/00000/2E44F5B7-4E2D-E511-85FC-02163E012377.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/883/00000/ACE0E713-362D-E511-ADA8-02163E01360E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/102/00000/C860A95B-D92F-E511-A473-02163E01241A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/116/00000/6EFB7390-7A30-E511-901E-02163E014462.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/126/00000/9C91DDFD-D930-E511-852E-02163E0125E8.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/488/00000/325394A3-EE35-E511-9CB5-02163E01287D.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/489/00000/8E84B579-3434-E511-96BF-02163E014543.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/490/00000/8E01C5EB-3534-E511-9010-02163E012283.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/492/00000/5EF62604-4734-E511-8F20-02163E011836.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/496/00000/6C14625C-CC35-E511-9B77-02163E014241.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/499/00000/A4D30E76-CD35-E511-9195-02163E0137FD.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/252/501/00000/B42326CF-CA35-E511-8C98-02163E0118F2.root' ] );


secFiles.extend( [
               ] )

