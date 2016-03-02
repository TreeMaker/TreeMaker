import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

for i in xrange(0,20):
    readFiles.extend(['/store/user/lpcsusyhad/SusyRA2Analysis2015/T5HH/T5HH_1200_950_batch%s_MiniAODv2.root'%(i+1)])

secFiles.extend( [
               ] )