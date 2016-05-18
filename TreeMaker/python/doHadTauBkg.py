import FWCore.ParameterSet.Config as cms

def makeJetVarsHadTau(process,sequence,JetTag,suff,storeProperties=0):
    if hasattr(process,sequence):
        theSequence = getattr(process,sequence)
    else:
        print "Unknown sequence: "+sequence
        return

    # clone GoodJetsProducer
    GoodJetsForHadTau = process.GoodJets.clone(
        JetTag = JetTag,
        jetPtFilter = cms.double(0),
        SaveAllJets = cms.bool(True),
        ExcludeLepIsoTrackPhotons = cms.bool(False),
    )
    setattr(process,"GoodJetsForHadTau"+suff,GoodJetsForHadTau)
    theSequence += getattr(process,"GoodJetsForHadTau"+suff)
    GoodJetsTag = cms.InputTag("GoodJetsForHadTau"+suff)
    
    process.TreeMaker2.VectorRecoCand.extend(['GoodJetsForHadTau'+suff+'(softJets'+suff+')'])
    process.TreeMaker2.VectorBool.extend(['GoodJetsForHadTau'+suff+':JetIDMask(softJets'+suff+'_ID)'])
    
    if storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetsProperties = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties   = cms.vstring("jecFactor","jecUnc")
        )
        # provide extra info where necessary
        JetsProperties.jecUnc = cms.vstring("jecUncHadTau")
        setattr(process,"HadTauJetsProperties"+suff,JetsProperties)
        theSequence += getattr(process,"HadTauJetsProperties"+suff)
        process.TreeMaker2.VectorDouble.extend(['HadTauJetsProperties:jecFactor(softJets'+suff+'_jecFactor)','HadTauJetsProperties:jecUnc(softJets'+suff+'_jecUnc)'])
    
    return process

def doHadTauBkg(process,geninfo,residual,JetTag,is74X):
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
        MCflag                 = cms.bool(False)
    )
    if geninfo:
        process.JetsForHadTau.MCflag = cms.bool(True)
    process.AdditionalSequence += process.JetsForHadTau
    JetTagHadTau = cms.InputTag("JetsForHadTau")

    # jet uncertainty variations
    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    
    #JEC uncertainty
    process.jecUncHadTau = JetUncertaintyProducer.clone(
        JetTag = JetTagHadTau,
        jecUncDir = cms.int32(0)
    )
    process.AdditionalSequence += process.jecUncHadTau
    
    #add userfloats to jet collection
    if is74X: from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
    else: from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJets as patJetsUpdated
    process.JetsForHadTauAuxiliary = patJetsUpdated.clone(
        jetSource = JetTagHadTau,
        addJetCorrFactors = cms.bool(False),
        addBTagInfo = cms.bool(False)
    )
    process.JetsForHadTauAuxiliary.userData.userFloats.src += ['jecUncHadTau']
    process.AdditionalSequence += process.JetsForHadTauAuxiliary
    JetTagHadTau = cms.InputTag('JetsForHadTauAuxiliary')
    
    process = makeJetVarsHadTau(process,
        sequence="AdditionalSequence",
        JetTag=JetTagHadTau,
        suff='',
        storeProperties=1
    )

    #JEC unc up
    process.JetsForHadTauJECup = JetUncertaintyProducer.clone(
        JetTag = JetTagHadTau,
        jecUncDir = cms.int32(1)
    )
    process.AdditionalSequence += process.JetsForHadTauJECup
    process = makeJetVarsHadTau(process,
        sequence="AdditionalSequence",
        JetTag=cms.InputTag("JetsForHadTauJECup"),
        suff='JECup',
    )

    #JEC unc down
    process.JetsForHadTauJECdown = JetUncertaintyProducer.clone(
        JetTag = JetTagHadTau,
        jecUncDir = cms.int32(-1)
    )
    process.AdditionalSequence += process.JetsForHadTauJECdown
    process = makeJetVarsHadTau(process,
        sequence="AdditionalSequence",
        JetTag=cms.InputTag("JetsForHadTauJECdown"),
        suff='JECdown',
    )
    
    return process
