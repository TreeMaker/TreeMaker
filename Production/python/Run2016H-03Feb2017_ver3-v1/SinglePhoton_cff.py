import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/060A7A39-27EB-E611-BE1F-7845C4FC3983.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/088D2FB1-3DEB-E611-B95D-3417EBE6453D.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/4448FFA1-30EB-E611-8478-848F69FD2520.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/5477D26A-37EB-E611-93BC-001D09FDD7D1.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/6AEE69A9-3DEB-E611-9CE1-008CFAFC0500.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/942BF339-44EB-E611-95F2-008CFAFC02A8.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/A26BBA63-37EB-E611-9ED2-008CFAFC0500.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/AC3AA2AB-3DEB-E611-8D66-3417EBE644B9.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/B0450BBB-3DEB-E611-8A80-7845C4FBB6A4.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/E28F269E-08EC-E611-BB84-7845C4F9162D.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/03Feb2017_ver3-v1/80000/EE906F3F-44EB-E611-8A77-008CFA008D0C.root',
] )
