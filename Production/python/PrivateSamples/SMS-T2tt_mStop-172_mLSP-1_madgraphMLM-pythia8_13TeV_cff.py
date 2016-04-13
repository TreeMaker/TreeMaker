import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

missing = [204,212,216,220,224,228,261]

for i in xrange(0,500):
    if i in missing: continue
    readFiles.extend(['/store/group/phys_susy/LHE/private_samples/FSPremix74X/SMS-T2tt/SMS-T2tt_mStop-172/SMS-T2tt_mStop-172_mLSP-1_2bd_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_b%s.root'%(i+1)])

secFiles.extend( [
               ] )