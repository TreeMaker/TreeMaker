import FWCore.ParameterSet.Config as cms

def reclusterZinv(self, process, cleanedCandidates, suff):
    # skip all jet smearing for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    doJERsmearing = self.geninfo

    ### AK8 detour

    # https://twiki.cern.ch/CMS/JetToolbox
    from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
    listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos','pfImpactParameterTagInfos'] 
    listBtagDiscriminatorsAK8 = [
         'pfBoostedDoubleSecondaryVertexAK8BJetTags',
    ]
    listBtagDiscriminatorsSubjetAK8 = [
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',
    ]
    jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    if self.residual: jecLevels.append("L2L3Residual")
    jetToolbox(process,
        'ak8',
        'jetSequence',
        'noOutput',
        PUMethod = 'Puppi',
        dataTier = 'miniAOD',
        runOnMC = self.geninfo,
        postFix='Clean',
        newPFCollection = True,
        nameNewPFCollection = cleanedCandidates.value(),
        Cut = 'pt>170.',
        addPruning = True,
        addSoftDropSubjets = True,
        addNsub = True,
        maxTau = 3,
        bTagInfos = listBTagInfos, 
        bTagDiscriminators = listBtagDiscriminatorsAK8,
        subjetBTagDiscriminators = listBtagDiscriminatorsSubjetAK8,
        JETCorrLevels = jecLevels,
        subJETCorrLevels = jecLevels,
        addEnergyCorrFunc = False,
        verbosity = 2 if self.verbose else 0,
    )
    JetAK8CleanTag = cms.InputTag("packedPatJetsAK8PFPuppiCleanSoftDrop")

    if doJERsmearing:
        # do central smearing and replace jet tag
        process, _, JetAK8CleanTag = JetDepot(process,
            JetTag=JetAK8CleanTag,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0,
            storeJer=2,
        )
    
    # get puppi-specific multiplicities
    from PhysicsTools.PatAlgos.patPuppiJetSpecificProducer_cfi import patPuppiJetSpecificProducer
    process.puppiSpecificAK8Clean = patPuppiJetSpecificProducer.clone(
        src = JetAK8CleanTag
    )
    # update userfloats (used for jet ID, including ID for JEC/JER variations)
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo
    process, JetAK8CleanTag = addJetInfo(process, JetAK8CleanTag,
        ['puppiSpecificAK8Clean:puppiMultiplicity','puppiSpecificAK8Clean:neutralPuppiMultiplicity','puppiSpecificAK8Clean:neutralHadronPuppiMultiplicity',
         'puppiSpecificAK8Clean:photonPuppiMultiplicity','puppiSpecificAK8Clean:HFHadronPuppiMultiplicity','puppiSpecificAK8Clean:HFEMPuppiMultiplicity'])

    process = self.makeJetVarsAK8(process,
        JetTag=JetAK8CleanTag,
        suff='AK8Clean',
        storeProperties=1,
        doECFs=False, # currently disabled
        doDeepAK8=False, # currently disabled
        doDeepDoubleB=False, # currently disabled
        puppiSpecific="puppiSpecificAK8Clean",
    )

    # update some userfloat names
    process.JetPropertiesAK8Clean.prunedMass = cms.vstring('ak8PFJetsPuppiCleanPrunedMass')
    process.JetPropertiesAK8Clean.softDropMass = cms.vstring('SoftDrop')
    process.JetPropertiesAK8Clean.NsubjettinessTau1 = cms.vstring('NjettinessAK8PuppiClean:tau1')
    process.JetPropertiesAK8Clean.NsubjettinessTau2 = cms.vstring('NjettinessAK8PuppiClean:tau2')
    process.JetPropertiesAK8Clean.NsubjettinessTau3 = cms.vstring('NjettinessAK8PuppiClean:tau3')
    process.JetPropertiesAK8Clean.subjets = cms.vstring('SoftDrop')
    process.JetPropertiesAK8Clean.SJbDiscriminatorCSV = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetPropertiesAK8Clean.neutralHadronPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:neutralHadronPuppiMultiplicity")
    process.JetPropertiesAK8Clean.neutralPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:neutralPuppiMultiplicity")
    process.JetPropertiesAK8Clean.photonPuppiMultiplicity = cms.vstring("puppiSpecificAK8Clean:photonPuppiMultiplicity")
#    process.JetPropertiesAK8Clean.ecfN2b1 = cms.vstring('ak8PFJetsPuppiCleanSoftDropValueMap:nb1AK8PuppiCleanSoftDropN2')
#    process.JetPropertiesAK8Clean.ecfN3b1 = cms.vstring('ak8PFJetsPuppiCleanSoftDropValueMap:nb1AK8PuppiCleanSoftDropN3')
#    process.JetPropertiesAK8Clean.ecfN2b2 = cms.vstring('ak8PFJetsPuppiCleanSoftDropValueMap:nb2AK8PuppiCleanSoftDropN2')
#    process.JetPropertiesAK8Clean.ecfN3b2 = cms.vstring('ak8PFJetsPuppiCleanSoftDropValueMap:nb2AK8PuppiCleanSoftDropN3')

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
    btagDiscs = ['pfCombinedInclusiveSecondaryVertexV2BJetTags','pfDeepCSVDiscriminatorsJetTags:BvsAll']
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
    # turn on/off GEN matching
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenPartonMatch = cms.bool(False)
    getattr(process,'patJetsAK4PFCLEAN'+suff).addGenJetMatch = cms.bool(False)
    # turn off some flags for data
    getattr(process,'patJetsAK4PFCLEAN'+suff).addJetFlavourInfo = cms.bool(self.geninfo)
    getattr(process,'patJetsAK4PFCLEAN'+suff).getJetMCFlavour = cms.bool(self.geninfo)

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
        reapplyJEC=False,
        postfix=postfix,
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

    if doJERsmearing:
        # do central smearing and replace jet tag
        process, _, JetTagClean = JetDepot(process,
            JetTag=JetTagClean,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0,
            storeJer=2,
        )
    
    # make the event variables
    process = self.makeJetVars(
        process,
        JetTag = JetTagClean,
        suff=postfix,
        storeProperties=1,
    )

    from TreeMaker.Utils.metdouble_cfi import metdouble
    METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJets'+postfix)
    )
    setattr(process,"METclean"+suff,METclean)
    self.VarsDouble.extend(['METclean'+suff+':Pt(METclean'+suff+')','METclean'+suff+':Phi(METPhiclean'+suff+')'])
#    self.VarsDouble.extend(['METclean'+suff+':RawPt(RawMETclean'+suff+')','METclean'+suff+':RawPhi(RawMETPhiclean'+suff+')'])

    return process

def doZinvBkg(self,process):
    ## ----------------------------------------------------------------------------------------------
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.photonidisoproducer_cfi import PhotonIDisoProducer
    process.goodPhotons = PhotonIDisoProducer.clone(
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",self.tagname)
    )
    
    ##### add branches for photon studies
    self.VectorRecoCand.append("goodPhotons(Photons)")
    self.VectorDouble.append("goodPhotons:isEB(Photons_isEB)")
    self.VectorDouble.append("goodPhotons:genMatched(Photons_genMatched)")
    self.VectorDouble.append("goodPhotons:hadTowOverEM(Photons_hadTowOverEM)")
    self.VectorBool.append("goodPhotons:hasPixelSeed(Photons_hasPixelSeed)")
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
    
    # if there are no leptons in the event, just remove high-pt photons (GJet)
    # otherwise, just remove leptons (DY)
    process.selectedXons = cms.EDProducer("CandPtrPrefer",
        first = cms.InputTag("selectedLeptons"), second = cms.InputTag("goodPhotons","highpt")
    )
    
    # do the removal
    # if putEmpty is set to true, this will output an empty collection if the "veto" collection is empty
    # this avoids pointless reclustering of an identical candidate collection
    # "clean" branches in the ntuple will not be filled in this case; (e.g. Jetsclean.size()==0)
    # the corresponding non-clean branches should be used instead for those events
    process.cleanedCandidates =  cms.EDProducer("PackedCandPtrProjector",
        src = cms.InputTag("packedPFCandidates"), veto = cms.InputTag("selectedXons"),
        putEmpty = cms.bool(True)
    )
    
    # make reclustered jets
    process = self.reclusterZinv(
        process,
        cms.InputTag("cleanedCandidates"),
        "",
    )
    
    return process
