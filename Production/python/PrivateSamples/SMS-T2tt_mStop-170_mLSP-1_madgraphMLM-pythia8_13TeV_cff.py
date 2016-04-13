import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

for i in xrange(0,500):
    readFiles.extend(['/store/group/phys_susy/LHE/private_samples/FSPremix74X/SMS-T2tt/SMS-T2tt_mStop-170/SMS-T2tt_mStop-170_mLSP-1_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_b%s.root'%(i)])

secFiles.extend( [
               ] )