import FWCore.ParameterSet.Config as cms

def reclusterZinv(self, process, cleanedCandidates, suff):
    
    ### AK8 detour

    # https://twiki.cern.ch/CMS/JetToolbox
    from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
    listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos'] 
    listBtagDiscriminatorsAK8 = [
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',
        'pfBoostedDoubleSecondaryVertexAK8BJetTags'
    ]
    jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    if self.residual: jecLevels.append("L2L3Residual")
    jetToolbox(process,
        'ak8',
        'jetSequence',
        'out',
        PUMethod = 'CHS',
        miniAOD = True,
        runOnMC = self.geninfo,
        postFix='Clean',
        newPFCollection = True,
        nameNewPFCollection = cleanedCandidates.value(),
        Cut = 'pt>170.',
        addPruning = True,
        #addSoftDropSubjets = True,
        addNsub = True,
        maxTau = 3,
        bTagInfos = listBTagInfos, 
        bTagDiscriminators = listBtagDiscriminatorsAK8,
        JETCorrLevels = jecLevels,
        subJETCorrLevels = jecLevels,
    )
    JetAK8CleanTag = cms.InputTag("selectedPatJetsAK8PFCHSClean")

    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = self.makeJetVars(process,
        JetTag=JetAK8CleanTag,
        suff='AK8Clean',
        skipGoodJets=False,
        storeProperties=1,
        onlyGoodJets=True
    )
    
    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsPropertiesAK8Clean = jetproperties.clone(
        JetTag       = JetAK8CleanTag,
        debug = cms.bool(False),
        properties = cms.vstring(
            "prunedMass"    ,
            "NsubjettinessTau1"    ,
            "NsubjettinessTau2"    ,
            "NsubjettinessTau3"    ,
            #"bDiscriminatorSubjet1",
            #"bDiscriminatorSubjet2",
            "bDiscriminatorCSV"    ,
            "NumBhadrons"          ,
            "NumChadrons"          ,
        )
    )
    
    process.JetsPropertiesAK8Clean.prunedMass = cms.vstring('ak8PFJetsCHSCleanPrunedMass')
    process.JetsPropertiesAK8Clean.NsubjettinessTau1 = cms.vstring('NjettinessAK8CHSClean:tau1')
    process.JetsPropertiesAK8Clean.NsubjettinessTau2 = cms.vstring('NjettinessAK8CHSClean:tau2')
    process.JetsPropertiesAK8Clean.NsubjettinessTau3 = cms.vstring('NjettinessAK8CHSClean:tau3')
    #process.JetsPropertiesAK8Clean.bDiscriminatorSubjet1 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    #process.JetsPropertiesAK8Clean.bDiscriminatorSubjet2 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8Clean.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
    self.VectorDouble.extend([
        'JetsPropertiesAK8Clean:prunedMass(JetsAK8Clean_prunedMass)',
        'JetsPropertiesAK8Clean:NsubjettinessTau1(JetsAK8Clean_NsubjettinessTau1)',
        'JetsPropertiesAK8Clean:NsubjettinessTau2(JetsAK8Clean_NsubjettinessTau2)',
        'JetsPropertiesAK8Clean:NsubjettinessTau3(JetsAK8Clean_NsubjettinessTau3)',
        #'JetsPropertiesAK8Clean:bDiscriminatorSubjet1(JetsAK8Clean_bDiscriminatorSubjet1CSV)',
        #'JetsPropertiesAK8Clean:bDiscriminatorSubjet2(JetsAK8Clean_bDiscriminatorSubjet2CSV)',
        'JetsPropertiesAK8Clean:bDiscriminatorCSV(JetsAK8Clean_doubleBDiscriminator)'
    ])
    self.VectorInt.extend([
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
    if self.residual: jecLevels.append("L2L3Residual")
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
        isData=not self.geninfo, # controls gen met
        jetCollUnskimmed='patJetsAK4PFCLEAN'+suff,
        pfCandColl=cleanedCandidates.value(),
        recoMetFromPFCs=True, # to recompute
        reclusterJets=False, # without reclustering
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

    self.VarsInt.extend(['IsolatedElectronTracksVetoClean'+suff+':isoTracks(isoElectronTracksclean'+suff+')'])
    self.VarsInt.extend(['IsolatedMuonTracksVetoClean'+suff+':isoTracks(isoMuonTracksclean'+suff+')'])
    self.VarsInt.extend(['IsolatedPionTracksVetoClean'+suff+':isoTracks(isoPionTracksclean'+suff+')'])

    # skip all jet smearing for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    doJERsmearing = self.geninfo
    
    if doJERsmearing:
        # do central smearing and replace jet tag
        process, JetTagClean = JetDepot(process,
            JetTag=JetTagClean,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0
        )
    
    # make the event variables
    process = self.makeJetVars(
        process,
        JetTag = JetTagClean,
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
    self.VarsDouble.extend(['METclean'+suff+':Pt(METclean'+suff+')','METclean'+suff+':Phi(METPhiclean'+suff+')'])
    
    return process

def doZinvBkg(self,process):
    ## ----------------------------------------------------------------------------------------------
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
        photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
        electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",self.tagname),
        beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot"),
        ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
        genParCollection       = cms.untracked.InputTag("prunedGenParticles"), 
        debug                  = cms.untracked.bool(False)
    )
    
    ##### add branches for photon studies
    self.VectorRecoCand.append("goodPhotons(Photons)")
    self.VectorDouble.append("goodPhotons:isEB(Photons_isEB)")
    self.VectorDouble.append("goodPhotons:genMatched(Photons_genMatched)")
    self.VectorDouble.append("goodPhotons:hadTowOverEM(Photons_hadTowOverEM)")
    self.VectorDouble.append("goodPhotons:hasPixelSeed(Photons_hasPixelSeed)")
    self.VectorDouble.append("goodPhotons:passElectronVeto(Photons_passElectronVeto)")
    self.VectorDouble.append("goodPhotons:pfChargedIso(Photons_pfChargedIso)")
    self.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(Photons_pfChargedIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfGammaIso(Photons_pfGammaIso)")
    self.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(Photons_pfGammaIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfNeutralIso(Photons_pfNeutralIso)")
    self.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(Photons_pfNeutralIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:sigmaIetaIeta(Photons_sigmaIetaIeta)")
    self.VectorBool.append("goodPhotons:nonPrompt(Photons_nonPrompt)")
    self.VectorBool.append("goodPhotons:fullID(Photons_fullID)")
    self.VectorBool.append("goodPhotons:electronFakes(Photons_electronFakes)")
    self.VarsBool.append("goodPhotons:hasGenPromptPhoton(hasGenPromptPhoton)")

    ## add MadGraph-level deltaR between photon or Z and status 23 partons
    if self.geninfo:
        process.madMinPhotonDeltaR = cms.EDProducer("MinDeltaRDouble")
        self.VarsDouble.extend(['madMinPhotonDeltaR:madMinPhotonDeltaR(madMinPhotonDeltaR)'])
        self.VarsInt.extend([   'madMinPhotonDeltaR:madMinDeltaRStatus(madMinDeltaRStatus)'])

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.makeTheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon')
    )
    self.VectorRecoCand.append("makeTheZs:ZCandidates")

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
    process = self.reclusterZinv(
        process,
        cms.InputTag("cleanedCandidates"),
        "",
    )
    
    return process
