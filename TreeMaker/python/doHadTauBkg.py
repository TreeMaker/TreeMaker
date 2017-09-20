import FWCore.ParameterSet.Config as cms

def makeJetVarsHadTau(self,process,JetTag,suff,storeProperties=0):
    # clone GoodJetsProducer
    GoodJetsForHadTau = process.GoodJets.clone(
        JetTag = JetTag,
        jetPtFilter = cms.double(30),
        invertJetPtFilter = cms.bool(True),
        SaveAllJetsId = cms.bool(True),
        SaveAllJetsPt = cms.bool(False), # save only jets *below* pt cut
        ExcludeLepIsoTrackPhotons = cms.bool(False),
    )
    if self.fastsim: GoodJetsForHadTau.jetPtFilter = cms.double(20)
    setattr(process,"GoodJetsForHadTau"+suff,GoodJetsForHadTau)
    GoodJetsTag = cms.InputTag("GoodJetsForHadTau"+suff)
    
    self.VectorRecoCand.extend(['GoodJetsForHadTau'+suff+'(SoftJets'+suff+')'])
    self.VectorBool.extend(['GoodJetsForHadTau'+suff+':JetIDMask(SoftJets'+suff+'_ID)'])
    
    if storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetProperties = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties   = cms.vstring("jecFactor","jecUnc","bDiscriminatorCSV")
        )
        if self.geninfo:
            JetProperties.properties.extend(["jerFactor", "jerFactorUp","jerFactorDown"])
        # provide extra info where necessary
        JetProperties.jecUnc = cms.vstring("jecUncHadTau")
        JetProperties.jerFactor = cms.vstring("jerFactorHadTau")
        JetProperties.jerFactorUp = cms.vstring("jerFactorUpHadTau")
        JetProperties.jerFactorDown = cms.vstring("jerFactorDownHadTau")
        setattr(process,"HadTauJetProperties"+suff,JetsProperties)
        self.VectorDouble.extend(['HadTauJetProperties:jecFactor(SoftJets'+suff+'_jecFactor)',
                                                'HadTauJetProperties:jecUnc(SoftJets'+suff+'_jecUnc)',
                                                'HadTauJetProperties:bDiscriminatorCSV(SoftJets'+suff+'_bDiscriminatorCSV)'])
        if self.geninfo:
            self.VectorDouble.extend(['HadTauJetProperties:jerFactor(SoftJets'+suff+'_jerFactor)',
                                                    'HadTauJetProperties:jerFactorUp(SoftJets'+suff+'_jerFactorUp)',
                                                    'HadTauJetProperties:jerFactorDown(SoftJets'+suff+'_jerFactorDown)'])
    
    return process

def doHadTauBkg(self,process,JetTag,recluster):
    if recluster:
        print "Reclustering for hadtau"
        
        process.load("RecoJets.JetProducers.ak4PFJets_cfi")
        from JetMETCorrections.Configuration.JetCorrectionServices_cff import ak4PFCHSL1FastL2L3,ak4PFCHSL1Fastjet,ak4PFCHSL2Relative,ak4PFCHSL3Absolute

        #do projections
        process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
        # no idea while doArea is false by default, but it's True in RECO so we have to set it
        process.ak4PFJetsCHS = process.ak4PFJets.clone(src = 'pfCHS', doAreaFastjet = True)

        if self.geninfo:
            process.load("RecoJets.JetProducers.ak4GenJets_cfi")
            process.ak4GenJets = process.ak4GenJets.clone(src = 'packedGenParticles', rParam = 0.4)

        from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
        jetCorrectionLevels = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'Type-2')
        if self.residual: jetCorrectionLevels = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'], 'Type-2')
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
        if self.geninfo:
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
        MCflag                 = cms.bool(self.geninfo),
        useReclusteredJets     = cms.bool(recluster),
        requireLeptonMatch     = cms.bool(False)
    )
    JetTagHadTau = cms.InputTag("JetsForHadTau")

    # jet uncertainty variations
    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    
    # JEC uncertainty
    process.jecUncHadTau = JetUncertaintyProducer.clone(
        JetTag = JetTagHadTau,
        jecUncDir = cms.int32(0)
    )
    _infosToAddHadTau = ['jecUncHadTau']
    if self.geninfo:
        # JER factors - central, up, down
        from TreeMaker.Utils.smearedpatjet_cfi import SmearedPATJetProducer
        process.jerFactorHadTau = SmearedPATJetProducer.clone(
            src = JetTagHadTau,
            variation = cms.int32(0),
            store_factor = cms.bool(True)
        )
        process.jerFactorUpHadTau = SmearedPATJetProducer.clone(
            src = JetTagHadTau,
            variation = cms.int32(1),
            store_factor = cms.bool(True)
        )
        process.jerFactorDownHadTau = SmearedPATJetProducer.clone(
            src = JetTagHadTau,
            variation = cms.int32(-1),
            store_factor = cms.bool(True)
        )
        _infosToAddHadTau.extend(['jerFactorHadTau','jerFactorUpHadTau','jerFactorDownHadTau'])
    # add userfloats & update tag
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo
    process, JetTagHadTau = addJetInfo(process, JetTagHadTau, _infosToAddHadTau, [])
    
    # skip all jet smearing and uncertainties for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    if self.geninfo:        
        # do central smearing and replace jet tag
        process, JetTagHadTau = JetDepot(process,
            JetTag=JetTagHadTau,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0
        )
    
    process = self.makeJetVarsHadTau(process,
        JetTag=JetTagHadTau,
        suff='',
        storeProperties=1
    )
    
    return process
