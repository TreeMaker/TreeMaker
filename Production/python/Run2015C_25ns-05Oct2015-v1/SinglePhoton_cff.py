import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/042C4A0D-5E74-E511-B545-0026189438FA.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/1814B910-5E74-E511-8C97-0025905A60AA.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/20556714-5E74-E511-98F1-0025905B85AE.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/2433BA11-5E74-E511-B591-0025905B8562.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/363DCC10-5E74-E511-BBA0-0025905A6092.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/3C8C1A03-5F74-E511-8937-0025905964C4.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/40FE7F13-5F74-E511-9C3A-002618943880.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/447FE10F-5E74-E511-AAEA-0025905A60FE.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/5636C4EA-5E74-E511-8ADF-003048FF86CA.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/A41A580C-5E74-E511-A13B-00261894382D.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/AAEC8C30-5F74-E511-8D1A-0025905A6118.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/D6271DDA-5E74-E511-AABF-0025905A48C0.root',
       '/store/data/Run2015C_25ns/SinglePhoton/MINIAOD/05Oct2015-v1/30000/EA81AE2F-5F74-E511-9BE5-0025905B85D6.root' ] );


secFiles.extend( [
               ] )

