import FWCore.ParameterSet.Config as cms

def makeJetVars(process, JetTag, suff, skipGoodJets, storeProperties, geninfo, SkipTag=cms.VInputTag(), onlyGoodJets=False):
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
            SaveAllJetsId             = True,
            SaveAllJetsPt             = False, # exclude low pt jets from good collection
        )
        setattr(process,"GoodJets"+suff,GoodJets)
        GoodJetsTag = cms.InputTag("GoodJets"+suff)
        process.TreeMaker2.VarsBool.extend(['GoodJets'+suff+':JetID(JetID'+suff+')'])
        if storeProperties>0:
            process.TreeMaker2.VectorRecoCand.extend(['GoodJets'+suff+'(Jets'+suff+')'])
            process.TreeMaker2.VectorBool.extend(['GoodJets'+suff+':JetIDMask(Jets'+suff+'_ID)'])
            if len(SkipTag)>0: process.TreeMaker2.VectorBool.extend(['GoodJets'+suff+':JetLeptonMask(Jets'+suff+'_LeptonMask)'])
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
    if storeProperties>0: process.TreeMaker2.VectorBool.extend(['HTJets'+suff+':SubJetMask(Jets'+suff+'_HTMask)'])
    HTJetsTag = cms.InputTag("HTJets"+suff)
    
    from TreeMaker.Utils.htdouble_cfi import htdouble
    HT = htdouble.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"HT"+suff,HT)
    process.TreeMaker2.VarsDouble.extend(['HT'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.njetint_cfi import njetint
    NJets = njetint.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"NJets"+suff,NJets)
    process.TreeMaker2.VarsInt.extend(['NJets'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.btagint_cfi import btagint
    BTags = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.800)
    )
    setattr(process,"BTags"+suff,BTags)
    process.TreeMaker2.VarsInt.extend(['BTags'+suff])
    
    from TreeMaker.Utils.btagint_cfi import btagint
    BTagsMVA = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedMVAV2BJetTags'),
        BTagCutValue = cms.double(0.185)
    )
    setattr(process,"BTagsMVA"+suff,BTagsMVA)
    process.TreeMaker2.VarsInt.extend(['BTagsMVA'+suff])
    
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
    if storeProperties>0: process.TreeMaker2.VectorBool.extend(['MHTJets'+suff+':SubJetMask(Jets'+suff+'_MHTMask)'])
    MHTJetsTag = cms.InputTag("MHTJets"+suff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+suff,MHT)
    process.TreeMaker2.VarsDouble.extend(['MHT'+suff+':Pt(MHT'+suff+')','MHT'+suff+':Phi(MHTPhi'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTJets      = MHTJetsTag,
    )
    setattr(process,"DeltaPhi"+suff,DeltaPhi)
    process.TreeMaker2.VarsDouble.extend(['DeltaPhi'+suff+':DeltaPhi1(DeltaPhi1'+suff+')','DeltaPhi'+suff+':DeltaPhi2(DeltaPhi2'+suff+')',
                                          'DeltaPhi'+suff+':DeltaPhi3(DeltaPhi3'+suff+')','DeltaPhi'+suff+':DeltaPhi4(DeltaPhi4'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## ISR jets
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        from TreeMaker.Utils.isrjet_cfi import ISRJetProducer
        ISRJets = ISRJetProducer.clone(
            JetTag = GoodJetsTag,
            JetLeptonTag  = cms.InputTag(GoodJetsTag.value()+':JetLeptonMask'),
            GenPartTag = cms.InputTag("prunedGenParticles"),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        setattr(process,"ISRJets"+suff,ISRJets)
        if storeProperties>0:
            process.TreeMaker2.VectorBool.extend(['ISRJets'+suff+':SubJetMask(Jets'+suff+'_ISRMask)'])
            process.TreeMaker2.VarsInt.extend(['ISRJets'+suff+'(NJetsISR'+suff+')'])


    ## ----------------------------------------------------------------------------------------------
    ## Jet properties
    ## ----------------------------------------------------------------------------------------------
    
    if storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetsProperties = jetproperties.clone(
            JetTag       = GoodJetsTag
        )
        # provide extra info where necessary
        JetsProperties.bDiscriminatorMVA = cms.vstring('pfCombinedMVAV2BJetTags')
        if storeProperties==1: 
            JetsProperties.properties = cms.vstring("bDiscriminatorCSV","bDiscriminatorMVA","muonEnergyFraction","partonFlavor","hadronFlavor")
        setattr(process,"JetsProperties"+suff,JetsProperties)
        process.TreeMaker2.VectorDouble.extend(['JetsProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_bDiscriminatorCSV)',
                                                'JetsProperties'+suff+':bDiscriminatorMVA(Jets'+suff+'_bDiscriminatorMVA)',
                                                'JetsProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)'])
        process.TreeMaker2.VectorInt.extend(['JetsProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
                                             'JetsProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)'])
        if storeProperties>1:
            process.TreeMaker2.VectorDouble.extend(['JetsProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                                                    'JetsProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                                                    'JetsProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                                                    'JetsProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
                                                    'JetsProperties'+suff+':jecUnc(Jets'+suff+'_jecUnc)',
                                                    'JetsProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                                                    'JetsProperties'+suff+':qgPtD(Jets'+suff+'_qgPtD)',
                                                    'JetsProperties'+suff+':qgAxis2(Jets'+suff+'_qgAxis2)'])
            process.TreeMaker2.VectorInt.extend(['JetsProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                                                 'JetsProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                                                 'JetsProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                                                 'JetsProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                                                 'JetsProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                                                 'JetsProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                                                 'JetsProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)',
                                                 'JetsProperties'+suff+':qgMult(Jets'+suff+'_qgMult)'])
                                             
    return process
