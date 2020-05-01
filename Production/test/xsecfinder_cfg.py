# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
name = parameters.value("name","")
redir = parameters.value("redir","root://cmsxrootd.fnal.gov/")
numevents = int(parameters.value("numevents", 1e6))

# handle site name usage
if redir[0]=="T":
    redir = "root://cmsxrootd.fnal.gov//store/test/xrootd/"+redir

import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

# use specified numevents
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(numevents) )

# get all input files
readFiles = getattr(__import__("TreeMaker.Production."+name+"_cff",fromlist=["readFiles"]),"readFiles")
process.source = cms.Source("PoolSource",
    fileNames = readFiles,
)

# log output
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

# temporary redirector fix
for f,val in enumerate(process.source.fileNames):
    if process.source.fileNames[f][0:6]=="/store":
        process.source.fileNames[f] = redir+process.source.fileNames[f]

process.xsec = cms.EDAnalyzer("GenXSecAnalyzer")

process.p = cms.Path(process.xsec)
