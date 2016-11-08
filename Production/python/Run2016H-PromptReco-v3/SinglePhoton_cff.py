import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/036/00000/726BEBFC-619F-E611-862A-02163E0121A2.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/036/00000/7E6411C8-619F-E611-830B-02163E014796.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/036/00000/BED78E14-629F-E611-83AE-FA163E43A076.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/036/00000/D4C00724-629F-E611-B52E-02163E011E3B.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/037/00000/4481B3C9-D09F-E611-BF9D-02163E011DEE.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/037/00000/504B56AE-C39F-E611-9106-FA163EF898AE.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/037/00000/908620EF-B09F-E611-BC13-02163E011FFE.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/037/00000/BCB11034-B69F-E611-A2DA-02163E014603.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/038/00000/EE064B51-B99F-E611-BC26-02163E013575.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/039/00000/18AAD053-8C9F-E611-B7D0-02163E011C54.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/040/00000/2C9502A5-969F-E611-A93D-FA163ECACAA7.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/041/00000/0867AE2E-9F9F-E611-8389-02163E012713.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/042/00000/6201171A-939F-E611-A767-FA163EDCABCB.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/043/00000/0E0B503B-C49F-E611-AD8A-FA163EE31817.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/043/00000/D0807051-BA9F-E611-BA9A-02163E013712.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/044/00000/BA6F2C1A-BC9F-E611-973E-02163E014374.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/068/00000/082BE00C-949F-E611-92AC-02163E014632.root',
] )
