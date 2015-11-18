import FWCore.ParameterSet.Config as cms

def reclusterZinv(process, geninfo, residual, jecuncfile, cleanedCandidates, suff):
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
    jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    if residual: jecLevels.append("L2L3Residual")
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
       jetCorrections = ('AK4PFchs', jecLevels, 'None'),
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

    # recalculate MET from cleaned candidates and reclustered jets
    postfix="clean"+suff
    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    runMetCorAndUncFromMiniAOD(
        process,
        isData=not geninfo, # controls gen met
        jetCollUnskimmed="reclusteredJets"+suff,
        jetColl='patJetsAK4PFCLEAN'+suff,
        pfCandColl=cleanedCandidates.value(),
        repro74X=True, # to recompute without reclustering
        jecUncFile=jecuncfile,
        postfix=postfix
    )
    if not residual: #skip residuals for data if not used
            getattr(process,"patPFMetT1T2Corr"+postfix).jetCorrLabelRes = cms.InputTag("L3Absolute")
            getattr(process,"patPFMetT1T2SmearCorr"+postfix).jetCorrLabelRes = cms.InputTag("L3Absolute")
            getattr(process,"patPFMetT2Corr"+postfix).jetCorrLabelRes = cms.InputTag("L3Absolute")
            getattr(process,"patPFMetT2SmearCorr"+postfix).jetCorrLabelRes = cms.InputTag("L3Absolute")
            getattr(process,"shiftedPatJetEnDown"+postfix).jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
            getattr(process,"shiftedPatJetEnUp"+postfix).jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
    if hasattr(process,"slimmedMETs"+postfix):
        delattr(getattr(process,"slimmedMETs"+postfix),"caloMET")
    METTag = cms.InputTag('slimmedMETs'+postfix)
    
    # isolated tracks
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    IsolatedElectronTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(11),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedElectronTracksVetoClean"+suff,IsolatedElectronTracksVetoClean)

    IsolatedMuonTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2), 
        pdgId               = cms.int32(13),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedMuonTracksVetoClean"+suff,IsolatedMuonTracksVetoClean)
    
    IsolatedPionTracksVetoClean = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cleanedCandidates,
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(10.0),
        isoCut              = cms.double(0.1),
        pdgId               = cms.int32(211),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )
    setattr(process,"IsolatedPionTracksVetoClean"+suff,IsolatedPionTracksVetoClean)

    process.ZinvClean += getattr(process,"IsolatedElectronTracksVetoClean"+suff)
    process.ZinvClean += getattr(process,"IsolatedMuonTracksVetoClean"+suff)
    process.ZinvClean += getattr(process,"IsolatedPionTracksVetoClean"+suff)
    process.TreeMaker2.VarsInt.extend(['IsolatedElectronTracksVetoClean'+suff+':isoTracks(isoElectronTracksclean'+suff+')'])
    process.TreeMaker2.VarsInt.extend(['IsolatedMuonTracksVetoClean'+suff+':isoTracks(isoMuonTracksclean'+suff+')'])
    process.TreeMaker2.VarsInt.extend(['IsolatedPionTracksVetoClean'+suff+':isoTracks(isoPionTracksclean'+suff+')'])

    # make the event variables
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(
        process,
        sequence="ZinvClean",
        JetTag = cms.InputTag("reclusteredJets"+suff),
        suff=postfix,
        skipGoodJets=False,
        storeProperties=1,
    )

    from TreeMaker.Utils.metdouble_cfi import metdouble
    METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJets'+postfix)
    )
    setattr(process,"METclean"+suff,METclean)
    process.ZinvClean += getattr(process,"METclean"+suff)
    process.TreeMaker2.VarsDouble.extend(['METclean'+suff+':Pt(METPtclean'+suff+')','METclean'+suff+':Phi(METPhiclean'+suff+')'])
    
    return process

def doZinvBkg(process,JetTag,METTag,geninfo,residual,jecuncfile):
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
    process.TreeMaker2.VarsInt.append("goodPhotons:NumPhotonsLoose")
    process.TreeMaker2.VectorRecoCand.append("goodPhotons:bestPhotonLoose")
    
    process.ZinvClean = cms.Sequence()

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.makeTheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon')
    )
    process.ZinvClean += process.makeTheZs
    process.TreeMaker2.VectorRecoCand.append("makeTheZs:ZCandidates")

    ###
    # do the old cleaning
    ###
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    
    # redo goodjets, skipping photon
    OldSkipTag = cms.VInputTag(
        cms.InputTag('LeptonsNew:IdIsoMuon'),
        cms.InputTag('LeptonsNew:IdIsoElectron'),
        cms.InputTag('IsolatedElectronTracksVeto'),
        cms.InputTag('IsolatedMuonTracksVeto'),
        cms.InputTag('IsolatedPionTracksVeto'),
        cms.InputTag('goodPhotons', 'bestPhoton'),
    )
    process = makeJetVars(process,
                          sequence="ZinvClean",
                          JetTag=JetTag,
                          suff='clean',
                          skipGoodJets=False,
                          storeProperties=0,
                          SkipTag=OldSkipTag,
                          onlyGoodJets=True
    )
    
    from TreeMaker.Utils.jetcleaner_cfi import JetCleaner
    process.cleanTheJets = JetCleaner.clone(
       JetTag      = cms.InputTag('GoodJetsclean'),
       ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
       ElectronR   = cms.double(0.4),
       MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon'),
       MuonR       = cms.double(0.4),
       PhotonTag   = cms.InputTag('goodPhotons', 'bestPhoton'),
       PhotonR     = cms.double(0.4)
    )
    process.ZinvClean += process.cleanTheJets
    process.TreeMaker2.VectorRecoCand.extend(['cleanTheJets:GoodJetsclean(Jetsclean)'])
    
    CleanJetsTag = cms.InputTag('cleanTheJets', 'GoodJetsclean')
    process = makeJetVars(process,
                          sequence="ZinvClean",
                          JetTag=CleanJetsTag,
                          suff='clean',
                          skipGoodJets=True,
                          storeProperties=1,
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
    process.ZinvClean += process.selectedElectrons
    process.electronCleanedCandidates = cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedElectrons")
    )
    process.ZinvClean += process.electronCleanedCandidates
    process.selectedMuons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("LeptonsNew:IdIsoMuon"), cut = cms.string('')
    )
    process.ZinvClean += process.selectedMuons
    process.leptonCleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("electronCleanedCandidates"), veto = cms.InputTag("selectedMuons")
    )
    process.ZinvClean += process.leptonCleanedCandidates
    
    # make jets for DY
    process = reclusterZinv(
        process,
        geninfo,
        residual,
        jecuncfile,
        cms.InputTag("leptonCleanedCandidates"),
        "DY",
    )
    
    # remove photon for GJet
    process.selectedPhotons = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("goodPhotons:bestPhoton"), cut = cms.string('')
    )
    process.ZinvClean += process.selectedPhotons
    process.photonCleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedPhotons")
    )
    process.ZinvClean += process.photonCleanedCandidates

    # make jets for GJet
    process = reclusterZinv(
        process,
        geninfo,
        residual,
        jecuncfile,
        cms.InputTag("photonCleanedCandidates"),
        "GJ",
    )
    
    # remove photon for GJet purity studies (loose ID/iso)
    process.selectedPhotonsLoose = cms.EDFilter("CandPtrSelector",
        src = cms.InputTag("goodPhotons:bestPhotonLoose"), cut = cms.string('')
    )
    process.ZinvClean += process.selectedPhotonsLoose
    process.loosePhotonCleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedPhotonsLoose")
    )
    process.ZinvClean += process.loosePhotonCleanedCandidates

    # make jets for GJet
    process = reclusterZinv(
        process,
        geninfo,
        residual,
        jecuncfile,
        cms.InputTag("loosePhotonCleanedCandidates"),
        "GJloose",
    )

    process.AdditionalSequence += process.ZinvClean
    
    return process
