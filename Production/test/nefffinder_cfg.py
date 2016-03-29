# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
name = parameters.value("name","")
nstart = parameters.value("nstart",0)
nfiles = parameters.value("nfiles",-1)

import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("Demo",eras.Run2_25ns)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = "74X_mcRun2_asymptotic_v2"

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# this inputs the input files
if nfiles==-1:
    process.load("TreeMaker.Production."+name+"_cff")
else:
    readFiles = getattr(__import__("TreeMaker.Production."+name+"_cff",fromlist=["readFiles"]),"readFiles")
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(readFiles[nstart:(nstart+nfiles)])
    )

#temporary redirector fix
for f,val in enumerate(process.source.fileNames):
    if process.source.fileNames[f][0:6]=="/store":
        process.source.fileNames[f] = "root://cmsxrootd.fnal.gov/"+process.source.fileNames[f]

process.demo = cms.EDAnalyzer('NeffFinder',
    name = cms.string(name)
)

process.p = cms.Path(process.demo)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
