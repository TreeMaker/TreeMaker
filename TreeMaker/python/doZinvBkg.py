import FWCore.ParameterSet.Config as cms

def reclusterZinv(process, geninfo, residual, cleanedCandidates, suff, fastsim):
    
    ### AK8 detour

    # https://twiki.cern.ch/CMS/JetToolbox
    from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
    listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos'] 
    listBtagDiscriminatorsAK8 = [
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',
        'pfBoostedDoubleSecondaryVertexAK8BJetTags'
    ]
    jetToolbox(process,
        'ak8',
        'jetSequence',
        'out',
        PUMethod = 'Puppi',
        miniAOD = True,
        runOnMC = geninfo,
        newPFCollection = True,
        nameNewPFCollection = 'cleanedCandidates',
        Cut = 'pt>170.',
        addSoftDrop = True,
        addSoftDropSubjets = True,
        addNsub = True,
        bTagInfos = listBTagInfos, 
        bTagDiscriminators = listBtagDiscriminatorsAK8, 
    )
    JetAK8CleanTag = cms.InputTag("packedPatJetsAK8PFPuppiSoftDrop")

    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    makeJetVars(process,
        JetTag=JetAK8CleanTag,
        suff='AK8Clean',
        skipGoodJets=False,
        storeProperties=1,
        geninfo=geninfo,
        fastsim=fastsim,
        onlyGoodJets=True
    )
    
    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsPropertiesAK8Clean = jetproperties.clone(
        JetTag       = JetAK8CleanTag,
        debug = cms.bool(False),
        properties = cms.vstring(
            "PuppiSoftDropMass"    ,
            "NsubjettinessTau1"    ,
            "NsubjettinessTau2"    ,
            "NsubjettinessTau3"    ,
            "bDiscriminatorSubjet1",
            "bDiscriminatorSubjet2",
            "bDiscriminatorCSV"    ,
            "NumBhadrons"          ,
            "NumChadrons"          ,
        )
    )
    
    process.JetsPropertiesAK8Clean.PuppiSoftDropMass = cms.vstring('SoftDrop')
    process.JetsPropertiesAK8Clean.NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi:tau1')
    process.JetsPropertiesAK8Clean.NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi:tau2')
    process.JetsPropertiesAK8Clean.NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi:tau3')
    process.JetsPropertiesAK8Clean.bDiscriminatorSubjet1 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8Clean.bDiscriminatorSubjet2 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8Clean.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
    process.TreeMaker2.VectorDouble.extend([
        'JetsPropertiesAK8Clean:PuppiSoftDropMass(JetsAK8Clean_puppiSoftDropMass)',
        'JetsPropertiesAK8Clean:NsubjettinessTau1(JetsAK8Clean_NsubjettinessTau1)',
        'JetsPropertiesAK8Clean:NsubjettinessTau2(JetsAK8Clean_NsubjettinessTau2)',
        'JetsPropertiesAK8Clean:NsubjettinessTau3(JetsAK8Clean_NsubjettinessTau3)',
        'JetsPropertiesAK8Clean:bDiscriminatorSubjet1(JetsAK8Clean_bDiscriminatorSubjet1CSV)',
        'JetsPropertiesAK8Clean:bDiscriminatorSubjet2(JetsAK8Clean_bDiscriminatorSubjet2CSV)',
        'JetsPropertiesAK8Clean:bDiscriminatorCSV(JetsAK8Clean_doubleBDiscriminator)'
    ])
    process.TreeMaker2.VectorInt.extend([
        'JetsPropertiesAK8Clean:NumBhadrons(JetsAK8Clean_NumBhadrons)',
        'JetsPropertiesAK8Clean:NumChadrons(JetsAK8Clean_NumChadrons)'
    ])

    ### end AK8 detour

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
    btagDiscs = ['pfCombinedInclusiveSecondaryVertexV2BJetTags','pfCombinedMVAV2BJetTags']
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
       btagDiscriminators = btagDiscs,
       muSource = cms.InputTag("slimmedMuons"),
       elSource = cms.InputTag("slimmedElectrons")
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
    JetTagClean = cms.InputTag("reclusteredJets"+suff)

    # recalculate MET from cleaned candidates and reclustered jets
    postfix="clean"+suff
    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    runMetCorAndUncFromMiniAOD(
        process,
        isData=not geninfo, # controls gen met
        jetCollUnskimmed='patJetsAK4PFCLEAN'+suff,
        pfCandColl=cleanedCandidates.value(),
        repro80X=True, # to recompute without reclustering
        postfix=postfix
    )
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

    process.TreeMaker2.VarsInt.extend(['IsolatedElectronTracksVetoClean'+suff+':isoTracks(isoElectronTracksclean'+suff+')'])
    process.TreeMaker2.VarsInt.extend(['IsolatedMuonTracksVetoClean'+suff+':isoTracks(isoMuonTracksclean'+suff+')'])
    process.TreeMaker2.VarsInt.extend(['IsolatedPionTracksVetoClean'+suff+':isoTracks(isoPionTracksclean'+suff+')'])

    # skip all jet smearing for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    doJERsmearing = geninfo
    
    if doJERsmearing:
        # do central smearing and replace jet tag
        process, JetTagClean = JetDepot(process,
            JetTag=JetTagClean,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0
        )
    
    # make the event variables
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(
        process,
        JetTag = JetTagClean,
        suff=postfix,
        skipGoodJets=False,
        storeProperties=1,
        geninfo=geninfo,
        fastsim=fastsim
    )

    from TreeMaker.Utils.metdouble_cfi import metdouble
    METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJets'+postfix)
    )
    setattr(process,"METclean"+suff,METclean)
    process.TreeMaker2.VarsDouble.extend(['METclean'+suff+':Pt(METclean'+suff+')','METclean'+suff+':Phi(METPhiclean'+suff+')'])
    
    return process

def doZinvBkg(process,tagname,geninfo,residual,fastsim):
    ## ----------------------------------------------------------------------------------------------
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
        photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
        electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",tagname),
        beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot"),
        ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
        genParCollection = cms.untracked.InputTag("prunedGenParticles"), 
        debug                  = cms.untracked.bool(False)
    )
    
    ##### add branches for photon studies
    process.TreeMaker2.VectorRecoCand.append("goodPhotons(Photons)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:isEB(Photons_isEB)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:genMatched(Photons_genMatched)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hadTowOverEM(Photons_hadTowOverEM)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hasPixelSeed(Photons_hasPixelSeed)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:passElectronVeto(Photons_passElectronVeto)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIso(Photons_pfChargedIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(Photons_pfChargedIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIso(Photons_pfGammaIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(Photons_pfGammaIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIso(Photons_pfNeutralIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(Photons_pfNeutralIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:sigmaIetaIeta(Photons_sigmaIetaIeta)")
    process.TreeMaker2.VectorBool.append("goodPhotons:nonPrompt(Photons_nonPrompt)")
    process.TreeMaker2.VectorBool.append("goodPhotons:fullID(Photons_fullID)")
    process.TreeMaker2.VectorBool.append("goodPhotons:electronFakes(Photons_electronFakes)")
    process.TreeMaker2.VarsBool.append("goodPhotons:hasGenPromptPhoton(hasGenPromptPhoton)")

    ## add MadGraph-level deltaR between photon or Z and status 23 partons
    if geninfo:
        process.madMinPhotonDeltaR = cms.EDProducer("MinDeltaRDouble")
        process.TreeMaker2.VarsDouble.extend(['madMinPhotonDeltaR:madMinPhotonDeltaR(madMinPhotonDeltaR)'])
        process.TreeMaker2.VarsInt.extend([   'madMinPhotonDeltaR:madMinDeltaRStatus(madMinDeltaRStatus)'])

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.makeTheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon')
    )
    process.TreeMaker2.VectorRecoCand.append("makeTheZs:ZCandidates")

    ###
    # do the new cleaning
    ###

    # combine leptons
    process.selectedLeptons = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("LeptonsNew:IdIsoElectron","LeptonsNew:IdIsoMuon")
    )
    
    # if there are no leptons in the event, just remove photons (GJet)
    # otherwise, just remove leptons (DY)
    process.selectedXons = cms.EDProducer("CandPtrPrefer",
        first = cms.InputTag("selectedLeptons"), second = cms.InputTag("goodPhotons")
    )
    
    # do the removal
    process.cleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedXons")
    )
    
    # make reclustered jets
    process = reclusterZinv(
        process,
        geninfo,
        residual,
        cms.InputTag("cleanedCandidates"),
        "",
        fastsim
    )
    
    return process
