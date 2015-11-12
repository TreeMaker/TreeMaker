import FWCore.ParameterSet.Config as cms

def reclusterZinv(process, cleanedCandidates, suff, SkipTag):
    # do CHS for jet clustering
    cleanedCandidatesCHS = cms.EDFilter("CandPtrSelector",
        src = cleanedCandidates,
        cut = cms.string("fromPV")
    )
    setattr(process,"cleanedCandidatesCHS"+suff,cleanedCandidatesCHS)

    # make the RECO jets 
    from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
    ak4PFJetsClean = ak4PFJets.clone(
        src = cms.InputTag("cleanedCandidatesCHS"+suff),
        doAreaFastjet = True
    )
    setattr(process,"ak4PFJetsClean"+suff,ak4PFJetsClean)

    # turn the RECO jets into PAT jets
    # for a full list & description of parameters see:
    # PhysicsTools/PatAlgos/python/tools/jetTools.py
    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    addJetCollection(
       process,
       labelName = 'AK4PFCLEAN'+suff,
       jetSource = cms.InputTag('ak4PFJetsClean'+suff),
       pfCandidates = cleanedCandidates,
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
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenPartonMatch = cms.bool(False)
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenJetMatch = cms.bool(False)

    # apply pt cut to final jet collection (done in slimmedJets)
    reclusteredJets = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("patJetsAK4PFCLEAN"+suff),
        cut = cms.string("pt>10.")
    )
    setattr(process,'reclusteredJets'+suff,reclusteredJets)

    # isolated tracks
    #from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    #IsolatedElectronTracksVetoClean = trackIsolationFilter.clone(
    #    doTrkIsoVeto        = False,
    #    vertexInputTag      = cms.InputTag("goodVertices"),
    #    pfCandidatesTag     = cleanedCandidates,
    #    dR_ConeSize         = cms.double(0.3),
    #    dz_CutValue         = cms.double(0.1),
    #    minPt_PFCandidate   = cms.double(5.0),
    #    isoCut              = cms.double(0.2),
    #    pdgId               = cms.int32(11),
    #    mTCut               = cms.double(100.),
    #    METTag              = cms.InputTag("METclean"),
    #)
    #setattr(process,"IsolatedElectronTracksVetoClean"+suff,IsolatedElectronTracksVetoClean)

    #IsolatedMuonTracksVetoClean = trackIsolationFilter.clone(
    #    doTrkIsoVeto        = False,
    #    vertexInputTag      = cms.InputTag("goodVertices"),
    #    pfCandidatesTag     = cleanedCandidates,
    #    dR_ConeSize         = cms.double(0.3),
    #    dz_CutValue         = cms.double(0.1),
    #    minPt_PFCandidate   = cms.double(5.0),
    #    isoCut              = cms.double(0.2), 
    #    pdgId               = cms.int32(13),
    #    mTCut               = cms.double(100.),
    #    METTag              = cms.InputTag("METclean"),
    #)
    #setattr(process,"IsolatedMuonTracksVetoClean"+suff,IsolatedMuonTracksVetoClean)

    #process.ZinvClean += getattr(process,"IsolatedElectronTracksVetoClean"+suff)
    #process.ZinvClean += getattr(process,"IsolatedMuonTracksVetoClean"+suff)
    #process.TreeMaker2.VarsInt.extend(['IsolatedElectronTracksVetoClean'+suff+':isoTracks(isoElectronTracksclean'+suff+')'])
    #process.TreeMaker2.VarsInt.extend(['IsolatedMuonTracksVetoClean'+suff+':isoTracks(isoMuonTracksclean'+suff+')'])

    # make the event variables
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(
        process,
        sequence="ZinvClean",
        JetTag = cms.InputTag("reclusteredJets"+suff),
        suff='clean'+suff,
        skipGoodJets=False,
        storeProperties=1,
        SkipTag=SkipTag
    ) 

    return process

def doZinvBkg(process,METTag):
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
                          storeProperties=0
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

    # remove leptons for DY
    process.selectedElectrons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("LeptonsNew:IdIsoElectron"), cut = cms.string('')
    )
    process.electronCleanedCandidates = cms.EDProducer("CandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedElectrons")
    )
    process.selectedMuons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("LeptonsNew:IdIsoMuon"), cut = cms.string('')
    )
    process.leptonCleanedCandidates =  cms.EDProducer("CandPtrProjector",
        src = cms.InputTag("electronCleanedCandidates"), veto = cms.InputTag("selectedMuons")
    )
    
    # make jets for DY
    process = reclusterZinv(
        process,
        cms.InputTag("leptonCleanedCandidates"),
        "DY",
        cms.VInputTag(
            cms.InputTag('IsolatedElectronTracksVeto'),
            cms.InputTag('IsolatedMuonTracksVeto'),
            cms.InputTag('IsolatedPionTracksVeto'),
            cms.InputTag('goodPhotons','bestPhoton'),
        )
    )
    
    # remove photon for GJet
    process.selectedPhotons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("goodPhotons:bestPhoton"), cut = cms.string('')
    )
    process.photonCleanedCandidates =  cms.EDProducer("CandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedPhotons")
    )

    # make jets for GJet
    process = reclusterZinv(
        process,
        cms.InputTag("photonCleanedCandidates"),
        "GJ",
        cms.VInputTag(
            cms.InputTag('LeptonsNew:IdIsoMuon'),
            cms.InputTag('LeptonsNew:IdIsoElectron'),
            cms.InputTag('IsolatedElectronTracksVeto'),
            cms.InputTag('IsolatedMuonTracksVeto'),
            cms.InputTag('IsolatedPionTracksVeto'),
        )
    )

    process.AdditionalSequence += process.ZinvClean
    
    return process
