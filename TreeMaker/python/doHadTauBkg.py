import FWCore.ParameterSet.Config as cms

def makeJetVarsHadTau(process,JetTag,suff,fastsim,storeProperties=0):
    # clone GoodJetsProducer
    GoodJetsForHadTau = process.GoodJets.clone(
        JetTag = JetTag,
        jetPtFilter = cms.double(30),
        invertJetPtFilter = cms.bool(True),
        SaveAllJetsId = cms.bool(True),
        SaveAllJetsPt = cms.bool(False), # save only jets *below* pt cut
        ExcludeLepIsoTrackPhotons = cms.bool(False),
    )
    if fastsim: GoodJetsForHadTau.jetPtFilter = cms.double(20)
    setattr(process,"GoodJetsForHadTau"+suff,GoodJetsForHadTau)
    GoodJetsTag = cms.InputTag("GoodJetsForHadTau"+suff)
    
    process.TreeMaker2.VectorRecoCand.extend(['GoodJetsForHadTau'+suff+'(SoftJets'+suff+')'])
    process.TreeMaker2.VectorBool.extend(['GoodJetsForHadTau'+suff+':JetIDMask(SoftJets'+suff+'_ID)'])
    
    if storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetsProperties = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties   = cms.vstring("jecFactor","jecUnc","bDiscriminatorCSV")
        )
        # provide extra info where necessary
        JetsProperties.jecUnc = cms.vstring("jecUncHadTau")
        setattr(process,"HadTauJetsProperties"+suff,JetsProperties)
        process.TreeMaker2.VectorDouble.extend(['HadTauJetsProperties:jecFactor(SoftJets'+suff+'_jecFactor)','HadTauJetsProperties:jecUnc(SoftJets'+suff+'_jecUnc)','HadTauJetsProperties:bDiscriminatorCSV(SoftJets'+suff+'_bDiscriminatorCSV)'])
    
    return process

def doHadTauBkg(process,geninfo,residual,JetTag,fastsim,recluster):
    if recluster:
        print "Reclustering for hadtau"
        
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

    from TreeMaker.Utils.jetsforhadtauproducer_cfi import JetsForHadTauProducer 
    # this save the jets without considering jet Id. But, also saves jetId in a vector.

    process.JetsForHadTau = JetsForHadTauProducer.clone(
        JetTag                 = JetTag,
        reclusJetTag           = cms.InputTag('patJetsAK4PFCHS'),
        maxJetEta              = cms.double(5.0), 
        MCflag                 = cms.bool(False),
        jetPtCut_analysis      = cms.double(30),
    )
    if geninfo:
        process.JetsForHadTau.MCflag = cms.bool(True)
    if not recluster:
        process.JetsForHadTau.reclusJetTag = JetTag
        process.JetsForHadTau.useReclusteredJets = cms.bool(False)
    JetTagHadTau = cms.InputTag("JetsForHadTau")

    # jet uncertainty variations
    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    
    #JEC uncertainty
    process.jecUncHadTau = JetUncertaintyProducer.clone(
        JetTag = JetTagHadTau,
        jecUncDir = cms.int32(0)
    )
    # add userfloat & update tag
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo
    process, JetTagHadTau = addJetInfo(process, JetTagHadTau, ['jecUncHadTau'], [])
    
    # skip all jet smearing and uncertainties for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    if geninfo:        
        # JEC unc up
        process, JetTagHadTauJECup = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVarsHadTau(process,
            JetTag=JetTagHadTauJECup,
            suff='JECup',
            fastsim=fastsim,
        )
        
        # JEC unc down
        process, JetTagHadTauJECdown = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=-1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVarsHadTau(process,
            JetTag=JetTagHadTauJECdown,
            suff='JECdown',
            fastsim=fastsim,
        )
    
        # JER unc up
        process, JetTagHadTauJERup = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=1
        )
        process = makeJetVarsHadTau(process,
            JetTag=JetTagHadTauJERup,
            suff='JERup',
            fastsim=fastsim,
        )
        
        # JER unc down
        process, JetTagHadTauJERdown = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=-1
        )
        process = makeJetVarsHadTau(process,
            JetTag=JetTagHadTauJERdown,
            suff='JERdown',
            fastsim=fastsim,
        )

        # finally, do central smearing and replace jet tag
        process, JetTagHadTau = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0
        )
    
    process = makeJetVarsHadTau(process,
        JetTag=JetTagHadTau,
        suff='',
        fastsim=fastsim,
        storeProperties=1
    )
    
    return process
