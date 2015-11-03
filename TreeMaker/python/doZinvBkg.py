import FWCore.ParameterSet.Config as cms

def doZinvBkg(process,METTag, doZinv_photon, doZinv_leptons):
    ##### add branches for photon studies
    process.TreeMaker2.VectorDouble.append("goodPhotons:isEB(photon_isEB)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:genMatched(photon_genMatched)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hadTowOverEM(photon_hadTowOverEM)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hasPixelSeed(photon_hasPixelSeed)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:passElectronVeto(photon_passElectronVeto)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIso(photon_pfChargedIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(photon_pfChargedIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIso(photon_pfGammaIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(photon_pfGammaIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIso(photon_pfNeutralIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(photon_pfNeutralIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:sigmaIetaIeta(photon_sigmaIetaIeta)")
    process.TreeMaker2.VectorBool.append("goodPhotons:nonPrompt(photon_nonPrompt)")
    process.TreeMaker2.VectorRecoCand.append("slimmedPhotons(photonCands)")
    
    process.ZinvClean = cms.Sequence()

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.makeTheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon')
    )
    process.ZinvClean += process.makeTheZs
    process.TreeMaker2.VectorRecoCand.append("makeTheZs:ZCandidates")
    
    from TreeMaker.Utils.jetcleaner_cfi import JetCleaner
    process.cleanTheJets = JetCleaner.clone(
       JetTag      = cms.InputTag('GoodJets'),
       ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
       ElectronR   = cms.double(0.4),
       MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon'),
       MuonR       = cms.double(0.4),
       PhotonTag   = cms.InputTag('goodPhotons', 'bestPhoton'),
       PhotonR     = cms.double(0.4)
    )
    process.ZinvClean += process.cleanTheJets
    
    CleanJetsTag = cms.InputTag('cleanTheJets', 'GoodJetsclean')
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(process,
                          sequence="ZinvClean",
                          JetTag=CleanJetsTag,
                          suff='clean',
                          skipGoodJets=True,
                          storeProperties=False,
                          ZinvSkipPhoton = False,
                          ZinvSkipLeptons = False
   )

    from TreeMaker.Utils.metdouble_cfi import metdouble
    process.METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJetsclean'),
       cleanTag = cms.untracked.VInputTag(
           cms.InputTag('LeptonsNew:IdIsoElectron'),
           cms.InputTag('LeptonsNew:IdIsoMuon'),
           cms.InputTag('goodPhotons', 'bestPhoton')
       )
    )
    process.ZinvClean += process.METclean
    process.TreeMaker2.VarsDouble.extend(['METclean:Pt(METPtclean)','METclean:Phi(METPhiclean)'])
    
    ###
    # do the new cleaning
    ###

    # turn on unscheduled mode
    process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True)
    )

    # remove leptons only
    if (doZinv_leptons and ~doZinv_photon):
        print "removing leptons only"
        process.selectedElectrons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("LeptonsNew:IdIsoElectron"), cut = cms.string('')
        )
        process.tempCandidates = cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedElectrons")
        )
        process.selectedMuons = cms.EDFilter("CandPtrSelector",
            src = cms.InputTag("LeptonsNew:IdIsoMuon"), cut = cms.string('')
        )
        process.cleanedCandidates =  cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("tempCandidates"), veto = cms.InputTag("selectedMuons")
        )
    
    # remove photon only
    if (~doZinv_leptons and doZinv_photon):
        print "removing bestPhoton only"
        process.selectedPhotons = cms.EDFilter("CandPtrSelector",
            src = cms.InputTag("goodPhotons:bestPhoton"), cut = cms.string('')
        )
        process.cleanedCandidates =  cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedPhotons")
        )

    # remove leptons and photon
    if (doZinv_leptons and doZinv_photon) :
        print "removing both leptons and bestPhoton"
        process.selectedElectrons = cms.EDFilter("CandPtrSelector",
            src = cms.InputTag("LeptonsNew:IdIsoElectron"), cut = cms.string('')
        )
        process.tempCandidates1 = cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedElectrons")
        )
        process.selectedMuons = cms.EDFilter("CandPtrSelector",
            src = cms.InputTag("LeptonsNew:IdIsoMuon"), cut = cms.string('')
        )
        process.tempCandidates2 =  cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("tempCandidates1"), veto = cms.InputTag("selectedMuons")
        )
        process.selectedPhotons = cms.EDFilter("CandPtrSelector",
            src = cms.InputTag("goodPhotons:bestPhoton"), cut = cms.string('')
        )
        process.cleanedCandidates =  cms.EDProducer("CandPtrProjector",
            src = cms.InputTag("tempCandidates2"), veto = cms.InputTag("selectedMuons")
        )

    # do CHS for jet clustering
    process.cleanedCandidatesCHS = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("cleanedCandidates"),
        cut = cms.string("fromPV")
    )

    # make the RECO jets 
    from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
    process.ak4PFJetsClean = ak4PFJets.clone(
        src = cms.InputTag("cleanedCandidatesCHS"),
        doAreaFastjet = True
    )

    # turn the RECO jets into PAT jets
    # for a full list & description of parameters see:
    # PhysicsTools/PatAlgos/python/tools/jetTools.py
    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    addJetCollection(
       process,
       labelName = 'AK4PFCLEAN',
       jetSource = cms.InputTag('ak4PFJetsClean'),
       pfCandidates = cms.InputTag('cleanedCandidates'),
       pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
       svSource = cms.InputTag('slimmedSecondaryVertices'),
       algo = 'AK',
       rParam = 0.4,
       getJetMCFlavour = True, # seems to be enough for hadronFlavour()
       #genJetCollection = cms.InputTag('slimmedGenJets'),
       genParticles = cms.InputTag('prunedGenParticles'), # likely needed for hadronFlavour()....
       jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
       btagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    )
    # turn on/off GEN matching (different than hadronFlavour()?)
    process.patJetsAK4PFCLEAN.addGenPartonMatch = cms.bool(False)
    process.patJetsAK4PFCLEAN.addGenJetMatch = cms.bool(False)

    # apply pt cut to final jet collection (done in slimmedJets)
    process.reclusteredJets = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("patJetsAK4PFCLEAN"),
        cut = cms.string("pt>10.")
    )

    # isolated tracks
    #from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    #process.IsolatedElectronTracksVetocleanv2 = trackIsolationFilter.clone(
    #    doTrkIsoVeto        = False,
    #    vertexInputTag      = cms.InputTag("goodVertices"),
    #    pfCandidatesTag     = cms.InputTag("cleanedCandidates"),
    #    dR_ConeSize         = cms.double(0.3),
    #    dz_CutValue         = cms.double(0.1),
    #    minPt_PFCandidate   = cms.double(5.0),
    #    isoCut              = cms.double(0.2),
    #    pdgId               = cms.int32(11),
    #    mTCut               = cms.double(100.),
    #    METTag              = cms.InputTag("METclean"),
    #)

    #process.IsolatedMuonTracksVetocleanv2 = trackIsolationFilter.clone(
    #    doTrkIsoVeto        = False,
    #    vertexInputTag      = cms.InputTag("goodVertices"),
    #    pfCandidatesTag     = cms.InputTag("cleanedCandidates"),
    #    dR_ConeSize         = cms.double(0.3),
    #    dz_CutValue         = cms.double(0.1),
    #    minPt_PFCandidate   = cms.double(5.0),
    #    isoCut              = cms.double(0.2), 
    #    pdgId               = cms.int32(13),
    #    mTCut               = cms.double(100.),
    #    METTag              = cms.InputTag("METclean"),
    #)

    #process.ZinvClean += process.IsolatedElectronTracksVetocleanv2
    #process.ZinvClean += process.IsolatedMuonTracksVetocleanv2
    #process.TreeMaker2.VarsInt.extend(['IsolatedElectronTracksVetocleanv2:isoTracks(isoElectronTrackscleanv2)'])
    #process.TreeMaker2.VarsInt.extend(['IsolatedMuonTracksVetocleanv2:isoTracks(isoMuonTrackscleanv2)'])

    # make the event variables
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(
        process,
        sequence="ZinvClean",
        JetTag = cms.InputTag("reclusteredJets"),
        suff='cleanv2',
        skipGoodJets=False,
        storeProperties=False,
        ZinvSkipPhoton = cms.bool(doZinv_photon),
        ZinvSkipLeptons = cms.bool(doZinv_leptons)
    )

    process.AdditionalSequence += process.ZinvClean
    
    return process
