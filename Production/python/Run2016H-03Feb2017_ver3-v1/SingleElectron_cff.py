import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/02973E99-69EC-E611-9913-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/04C8C9AF-62EC-E611-AB90-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/061E21A6-62EC-E611-96C1-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/1A933E99-69EC-E611-870A-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/1E797AAC-62EC-E611-BB8B-E0071B740D90.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/2291F6A5-62EC-E611-A658-24BE05C63681.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/26891437-71EC-E611-B246-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/324501AF-62EC-E611-9D0B-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/346B00AB-62EC-E611-8830-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/5405C6AD-62EC-E611-B257-E0071B7A5540.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/5C9C3E99-69EC-E611-9C82-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/64573F99-69EC-E611-A264-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/7620AF3C-71EC-E611-A7BF-B8CA3A709648.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/76963E99-69EC-E611-B9B5-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/76CA6AA4-62EC-E611-9E7A-24BE05C60641.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/945A0C76-69EC-E611-B7AB-5065F3820341.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/9A512238-71EC-E611-8ECB-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/9E963E99-69EC-E611-AF5F-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/A8963E99-69EC-E611-9E3D-5065F381A2F1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/ACA473A4-62EC-E611-8169-5065F381E151.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/AE3C57A4-62EC-E611-A05F-24BE05C33C71.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/CC4098A5-62EC-E611-A77C-24BE05CECBE1.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/CED322A9-62EC-E611-AC9D-A0000420FE80.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/F237C6A5-62EC-E611-874C-24BE05C64601.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/F682F9AA-62EC-E611-BBDC-E0071B749C40.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/F6FE86AB-62EC-E611-A141-E0071B7A9800.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/FC973E99-69EC-E611-8854-5065F381A2F1.root',
] )
