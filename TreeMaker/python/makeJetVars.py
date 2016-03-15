import FWCore.ParameterSet.Config as cms

def makeJetVars(process, sequence, JetTag, suff, skipGoodJets, storeProperties, SkipTag=cms.VInputTag(), onlyGoodJets=False):
    if hasattr(process,sequence):
        theSequence = getattr(process,sequence)
    else:
        print "Unknown sequence: "+sequence
        return

    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
    if skipGoodJets:
        GoodJetsTag = JetTag
    else:
        from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
        GoodJets = GoodJetsProducer.clone(
            TagMode                   = cms.bool(True),
            JetTag                    = JetTag,
            maxJetEta                 = cms.double(5.0),
            minNconstituents          = cms.int32(1),
            minNneutrals              = cms.int32(10),
            minNcharged               = cms.int32(0),
            maxNeutralFraction        = cms.double(0.99),
            maxPhotonFraction         = cms.double(0.99),
            maxPhotonFractionHF       = cms.double(0.90),
            minChargedFraction        = cms.double(0),
            maxChargedEMFraction      = cms.double(0.99),
            jetPtFilter               = cms.double(30),
            ExcludeLepIsoTrackPhotons = cms.bool(True),
            JetConeSize               = cms.double(0.4),
            SkipTag                   = SkipTag,
            SaveAllJets               = True
        )
        setattr(process,"GoodJets"+suff,GoodJets)
        theSequence += getattr(process,"GoodJets"+suff)
        GoodJetsTag = cms.InputTag("GoodJets"+suff)
        process.TreeMaker2.VarsBool.extend(['GoodJets'+suff+':JetID(JetID'+suff+')'])
        if storeProperties>0:
            process.TreeMaker2.VectorRecoCand.extend(['GoodJets'+suff+'(Jets'+suff+')'])
            process.TreeMaker2.VectorBool.extend(['GoodJets'+suff+':JetIDMask(Jets'+suff+'_ID)'])
        if onlyGoodJets:
            return process
    
    ## ----------------------------------------------------------------------------------------------
    ## HT
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    HTJets = SubJetSelection.clone(
        JetTag = GoodJetsTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(2.4),
    )
    setattr(process,"HTJets"+suff,HTJets)
    theSequence += getattr(process,"HTJets"+suff)
    if storeProperties>0: process.TreeMaker2.VectorBool.extend(['HTJets'+suff+':SubJetMask(HTJetsMask'+suff+')'])
    HTJetsTag = cms.InputTag("HTJets"+suff)
    
    from TreeMaker.Utils.htdouble_cfi import htdouble
    HT = htdouble.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"HT"+suff,HT)
    theSequence += getattr(process,"HT"+suff)
    process.TreeMaker2.VarsDouble.extend(['HT'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.njetint_cfi import njetint
    NJets = njetint.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"NJets"+suff,NJets)
    theSequence += getattr(process,"NJets"+suff)
    process.TreeMaker2.VarsInt.extend(['NJets'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.btagint_cfi import btagint
    BTags = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.890)
    )
    setattr(process,"BTags"+suff,BTags)
    theSequence += getattr(process,"BTags"+suff)
    process.TreeMaker2.VarsInt.extend(['BTags'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    MHTJets = SubJetSelection.clone(
        JetTag = GoodJetsTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    setattr(process,"MHTJets"+suff,MHTJets)
    theSequence += getattr(process,"MHTJets"+suff)
    if storeProperties>0: process.TreeMaker2.VectorBool.extend(['MHTJets'+suff+':SubJetMask(MHTJetsMask'+suff+')'])
    MHTJetsTag = cms.InputTag("MHTJets"+suff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+suff,MHT)
    theSequence += getattr(process,"MHT"+suff)
    process.TreeMaker2.VarsDouble.extend(['MHT'+suff+':Pt(MHT'+suff+')','MHT'+suff+':Phi(MHT_Phi'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTJets      = MHTJetsTag,
    )
    setattr(process,"DeltaPhi"+suff,DeltaPhi)
    theSequence += getattr(process,"DeltaPhi"+suff)
    process.TreeMaker2.VarsDouble.extend(['DeltaPhi'+suff+':DeltaPhi1(DeltaPhi1'+suff+')','DeltaPhi'+suff+':DeltaPhi2(DeltaPhi2'+suff+')',
                                          'DeltaPhi'+suff+':DeltaPhi3(DeltaPhi3'+suff+')','DeltaPhi'+suff+':DeltaPhi4(DeltaPhi4'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet properties
    ## ----------------------------------------------------------------------------------------------
    
    if storeProperties>0:
        # get QG tagging discriminant
        QGTagger = cms.EDProducer('QGTagger',
            srcJets	            = GoodJetsTag,
            jetsLabel           = cms.string('QGL_AK4PFchs'),
            srcRho              = cms.InputTag('fixedGridRhoFastjetAll'),		
            srcVertexCollection	= cms.InputTag('offlinePrimaryVerticesWithBS'),
            useQualityCuts	    = cms.bool(False)
        )
        setattr(process,"QGTagger"+suff,QGTagger)
        theSequence += getattr(process,"QGTagger"+suff)
        QGTag = cms.InputTag("QGTagger"+suff,"qgLikelihood")
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetsProperties = jetproperties.clone(
            JetTag       = GoodJetsTag,
            BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
            QGTag        = QGTag
        )
        setattr(process,"JetsProperties"+suff,JetsProperties)
        theSequence += getattr(process,"JetsProperties"+suff)
        process.TreeMaker2.VectorDouble.extend(['JetsProperties'+suff+':bDiscriminatorUser(Jets'+suff+'_bDiscriminatorCSV)'])
        process.TreeMaker2.VectorInt.extend(['JetsProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
                                             'JetsProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)'])
        if storeProperties>1:
            process.TreeMaker2.VectorDouble.extend(['JetsProperties'+suff+':bDiscriminatorMVA(Jets'+suff+'_bDiscriminatorMVA)',
                                                    'JetsProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                                                    'JetsProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
                                                    'JetsProperties'+suff+':jetArea(Jets'+suff+'_jetArea)',
                                                    'JetsProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                                                    'JetsProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                                                    'JetsProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)'])
            process.TreeMaker2.VectorInt.extend(['JetsProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                                                 'JetsProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                                                 'JetsProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                                                 'JetsProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                                                 'JetsProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                                                 'JetsProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                                                 'JetsProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)'])
                                             
    return process
