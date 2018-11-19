# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
name = parameters.value("name","")
redir = parameters.value("redir","root://cmsxrootd.fnal.gov/")

# handle site name usage
if redir[0]=="T":
    redir = "root://cmsxrootd.fnal.gov//store/test/xrootd/"+redir

import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

# only need one event to get run info
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

# this selects the first input file
readFiles = getattr(__import__("TreeMaker.Production."+name+"_cff",fromlist=["readFiles"]),"readFiles")
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(readFiles[0])
)

# log output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.categories.append('TreeMaker')
process.MessageLogger.cerr.TreeMaker = cms.untracked.PSet(
    optionalPSet = cms.untracked.bool(True),
    limit = cms.untracked.int32(10000000),
)

# temporary redirector fix
for f,val in enumerate(process.source.fileNames):
    if process.source.fileNames[f][0:6]=="/store":
        process.source.fileNames[f] = redir+process.source.fileNames[f]

process.PdfFinder = cms.EDAnalyzer('PdfFinder')

process.p = cms.Path(process.PdfFinder)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
