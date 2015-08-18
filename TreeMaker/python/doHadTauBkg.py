import FWCore.ParameterSet.Config as cms

def doHadTauBkg(process,is74X,geninfo,residual,JetTag):
    process.load("RecoJets.JetProducers.ak4PFJets_cfi")
    from JetMETCorrections.Configuration.JetCorrectionServices_cff import ak4PFCHSL1FastL2L3,ak4PFCHSL1Fastjet,ak4PFCHSL2Relative,ak4PFCHSL3Absolute

    #do projections
    process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
    # no idea while doArea is false by default, but it's True in RECO so we have to set it
    process.ak4PFJetsCHS = process.ak4PFJets.clone(src = 'pfCHS', doAreaFastjet = True)

    if geninfo:
        process.load("RecoJets.JetProducers.ak4GenJets_cfi")
        process.ak4GenJets = process.ak4GenJets.clone(src = 'packedGenParticles', rParam = 0.4)

    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    jetCorrectionLevels = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'Type-2')
    if residual: jetCorrectionLevels = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'], 'Type-2')
    if is74X:
        addJetCollection(
            process,
            postfix            = "",
            labelName          = 'AK4PFCHS',
            jetSource          = cms.InputTag('ak4PFJetsCHS'),
            pfCandidates       = cms.InputTag('packedPFCandidates'),
            pvSource           = cms.InputTag('offlineSlimmedPrimaryVertices'),  # 74x
            svSource           = cms.InputTag('slimmedSecondaryVertices'),       # 74x
            elSource           = cms.InputTag('slimmedElectrons'),
            muSource           = cms.InputTag('slimmedMuons'),
            jetCorrections     = jetCorrectionLevels,
            btagDiscriminators = [ 'pfCombinedInclusiveSecondaryVertexV2BJetTags' ],  # 74x
            genJetCollection   = cms.InputTag('ak4GenJets'),
            genParticles       = cms.InputTag('prunedGenParticles'),
            algo               = 'AK',
            rParam             = 0.4
        )
    else:
        addJetCollection(
            process,
            postfix            = "",
            labelName          = 'AK4PFCHS',
            jetSource          = cms.InputTag('ak4PFJetsCHS'),
            pfCandidates       = cms.InputTag('packedPFCandidates'),
            trackSource        = cms.InputTag('unpackedTracksAndVertices'),           # 72x
            pvSource           = cms.InputTag('unpackedTracksAndVertices'),              # 72x
            svSource           = cms.InputTag('unpackedTracksAndVertices','secondary'),  # 72x
            jetCorrections     = jetCorrectionLevels,
            btagDiscriminators = [ 'combinedInclusiveSecondaryVertexV2BJetTags' ],  # 72x
            genJetCollection   = cms.InputTag('ak4GenJets'),
            algo               = 'AK',
            rParam             = 0.4
        )
    # end of if is74X:

    # adjust MC matching
    process.patJetsAK4PFCHS.getJetMCFlavour   = False
    process.patJetsAK4PFCHS.addGenPartonMatch = False
    process.patJetsAK4PFCHS.addGenJetMatch    = False
    if geninfo:
        process.patJetsAK4PFCHS.getJetMCFlavour   = True
        process.patJetsAK4PFCHS.addGenPartonMatch = True
        process.patJetsAK4PFCHS.addGenJetMatch    = True
        process.patJetGenJetMatchAK4PFCHS.matched = "ak4GenJets"
        process.patJetPartonMatchAK4PFCHS.matched = "prunedGenParticles"
        process.patJetPartons.particles           = "prunedGenParticles"
        process.patJetPartons.skipFirstN          = cms.uint32(0) # do not skip first 6 particles, we already pruned some!
        process.patJetPartons.acceptNoDaughters   = cms.bool(True) # as we drop intermediate stuff, we need to accept quarks with no siblings

    # adjust PV used for Jet Corrections
    process.patJetCorrFactorsAK4PFCHS.primaryVertices = "offlineSlimmedPrimaryVertices"

    # recreate tracks and pv for btagging
    process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')
    process.options.allowUnscheduled = cms.untracked.bool(True) # in case we forgot something :)

    from TreeMaker.Utils.jetsforhadtauproducer_cfi import JetsForHadTauProducer 
    # this save the jets without considering jet Id. But, also saves jetId in a vector.

    process.JetsForHadTau = JetsForHadTauProducer.clone(
        JetTag                 = JetTag,
        reclusJetTag           = cms.InputTag('patJetsAK4PFCHS'),
        maxJetEta              = cms.double(5.0), 
        maxMuFraction          = cms.double(2), 
        minNConstituents       = cms.double(2),       
        maxNeutralFraction     = cms.double(0.90),
        maxPhotonFraction      = cms.double(0.95),
        minChargedMultiplicity = cms.double(0), 
        minChargedFraction     = cms.double(0),     
        maxChargedEMFraction   = cms.double(0.99), 
        MCflag                 = cms.bool(False)
    )

    if geninfo:
        process.JetsForHadTau.MCflag = cms.bool(True)
        
    process.AdditionalSequence += process.JetsForHadTau
    process.TreeMaker2.VectorRecoCand.extend(['JetsForHadTau:Jet(slimJet)'])
    process.TreeMaker2.VectorInt.extend(['JetsForHadTau:JetFlag(slimJet_slimJetID)'])
    
    return process