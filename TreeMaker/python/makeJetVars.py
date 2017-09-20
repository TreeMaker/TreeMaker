import FWCore.ParameterSet.Config as cms
from TreeMaker.TreeMaker.addJetInfo import addJetInfo

def makeMHTVars(self, process, JetTag, HTJetsTag, storeProperties, suff, MHTsuff):
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    MHTJets = SubJetSelection.clone(
        JetTag = JetTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    setattr(process,"MHTJets"+MHTsuff+suff,MHTJets)
    if storeProperties>0: self.VectorBool.extend(['MHTJets'+MHTsuff+suff+':SubJetMask(Jets'+suff+'_MHT'+MHTsuff+'Mask)'])
    MHTJetsTag = cms.InputTag("MHTJets"+MHTsuff+suff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+MHTsuff+suff,MHT)
    self.VarsDouble.extend(['MHT'+MHTsuff+suff+':Pt(MHT'+MHTsuff+suff+')','MHT'+MHTsuff+suff+':Phi(MHTPhi'+MHTsuff+suff+')'])
    
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTJets      = MHTJetsTag,
    )
    setattr(process,"DeltaPhi"+MHTsuff+suff,DeltaPhi)
    self.VarsDouble.extend(['DeltaPhi'+MHTsuff+suff+':DeltaPhi1(DeltaPhi1'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi2(DeltaPhi2'+MHTsuff+suff+')',
                                          'DeltaPhi'+MHTsuff+suff+':DeltaPhi3(DeltaPhi3'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi4(DeltaPhi4'+MHTsuff+suff+')'])
    
    return process

def makeGoodJets(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag()):
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
    if self.fastsim: GoodJets.jetPtFilter = cms.double(20)
    setattr(process,"GoodJets"+suff,GoodJets)
    GoodJetsTag = cms.InputTag("GoodJets"+suff)
    self.VarsBool.extend(['GoodJets'+suff+':JetID(JetID'+suff+')'])
    if storeProperties>0:
        self.VectorRecoCand.extend(['GoodJets'+suff+'(Jets'+suff+')'])
        self.VectorBool.extend(['GoodJets'+suff+':JetIDMask(Jets'+suff+'_ID)'])
        if len(SkipTag)>0: self.VectorBool.extend(['GoodJets'+suff+':JetLeptonMask(Jets'+suff+'_LeptonMask)'])
    return (process,GoodJetsTag)


def makeJetVars(self, process, JetTag, suff, skipGoodJets, storeProperties, SkipTag=cms.VInputTag(), onlyGoodJets=False):
    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
    if skipGoodJets:
        GoodJetsTag = JetTag
    else:
        process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,SkipTag)
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
    if storeProperties>0: self.VectorBool.extend(['HTJets'+suff+':SubJetMask(Jets'+suff+'_HTMask)'])
    HTJetsTag = cms.InputTag("HTJets"+suff)
    
    from TreeMaker.Utils.htdouble_cfi import htdouble
    HT = htdouble.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"HT"+suff,HT)
    self.VarsDouble.extend(['HT'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.njetint_cfi import njetint
    NJets = njetint.clone(
        JetTag = HTJetsTag,
    )
    setattr(process,"NJets"+suff,NJets)
    self.VarsInt.extend(['NJets'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.btagint_cfi import btagint
    BTags = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.8484)
    )
    setattr(process,"BTags"+suff,BTags)
    self.VarsInt.extend(['BTags'+suff])
    
    from TreeMaker.Utils.btagint_cfi import btagint
    BTagsMVA = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfCombinedMVAV2BJetTags'),
        BTagCutValue = cms.double(0.4432)
    )
    setattr(process,"BTagsMVA"+suff,BTagsMVA)
    self.VarsInt.extend(['BTagsMVA'+suff])

    ## ----------------------------------------------------------------------------------------------
    ## MHT, DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    # MHT, DeltaPhi moved to separate fn (above) because of stupid egamma slew corrections
    MHTOrig = ""
    if self.scenario=="2016ReMiniAOD03Feb":
        MHTOrig = "Orig"
        from TreeMaker.Utils.patjetfix_cfi import patjetfix
        PatJetFix = patjetfix.clone(
            jets = GoodJetsTag
        )
        setattr(process,"PatJetFix"+suff,PatJetFix)
        process = self.makeMHTVars(process, cms.InputTag("PatJetFix"+suff), HTJetsTag, storeProperties, suff, "")
    process = self.makeMHTVars(process, GoodJetsTag, HTJetsTag, storeProperties, suff, MHTOrig)

    ## ----------------------------------------------------------------------------------------------
    ## ISR jets
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
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
            self.VectorBool.extend(['ISRJets'+suff+':SubJetMask(Jets'+suff+'_ISRMask)'])
            self.VarsInt.extend(['ISRJets'+suff+'(NJetsISR'+suff+')'])

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
            JetsProperties.properties = cms.vstring("bDiscriminatorCSV","bDiscriminatorMVA","muonEnergyFraction","chargedHadronEnergyFraction","partonFlavor","hadronFlavor")
        if storeProperties>1 and self.geninfo:
            JetsProperties.properties.extend(["jerFactor", "jerFactorUp","jerFactorDown"])
        setattr(process,"JetsProperties"+suff,JetsProperties)
        self.VectorDouble.extend(['JetsProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_bDiscriminatorCSV)',
                                                'JetsProperties'+suff+':bDiscriminatorMVA(Jets'+suff+'_bDiscriminatorMVA)',
                                                'JetsProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
                                                'JetsProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',])
        self.VectorInt.extend(['JetsProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
                                             'JetsProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)'])
        if storeProperties>1:
            self.VectorDouble.extend(['JetsProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                                                    'JetsProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                                                    'JetsProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                                                    'JetsProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
                                                    'JetsProperties'+suff+':jecUnc(Jets'+suff+'_jecUnc)',
                                                    'JetsProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                                                    'JetsProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                                                    'JetsProperties'+suff+':axisminor(Jets'+suff+'_axisminor)'])
            if self.geninfo:
                self.VectorDouble.extend(['JetsProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)',
                                                        'JetsProperties'+suff+':jerFactorUp(Jets'+suff+'_jerFactorUp)',
                                                        'JetsProperties'+suff+':jerFactorDown(Jets'+suff+'_jerFactorDown)'])

            self.VectorInt.extend(['JetsProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                                                 'JetsProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                                                 'JetsProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                                                 'JetsProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                                                 'JetsProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                                                 'JetsProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                                                 'JetsProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)',
                                                 'JetsProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)'])
                                             
    return process

def makeJetVarsAK8(self, process, JetTag, suff, storeProperties):
    # get more substructure
    if self.semivisible:
        BasicSubstructure = cms.EDProducer("BasicSubstructureProducer",
            JetTag = JetTag
        )
        setattr(process,"BasicSubstructure"+suff,BasicSubstructure)
        ak8floats = [
            'BasicSubstructure'+suff+':overflow',
            'BasicSubstructure'+suff+':girth',
            'BasicSubstructure'+suff+':momenthalf',
            'BasicSubstructure'+suff+':ptD',
            'BasicSubstructure'+suff+':axismajor',
            'BasicSubstructure'+suff+':axisminor',
        ]
        ak8ints = [
            'BasicSubstructure'+suff+':multiplicity',
        ]
    
        # add discriminator and update tag
        process, JetTag = addJetInfo(process, JetTag, ak8floats, ak8ints)

    process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties)

    if storeProperties>0:
        # AK8 jet variables - separate instance of jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetsPropertiesAK8 = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties = cms.vstring(
                "prunedMass"    ,
                "NsubjettinessTau1"    ,
                "NsubjettinessTau2"    ,
                "NsubjettinessTau3"    ,
#                "bDiscriminatorSubjet1",
#                "bDiscriminatorSubjet2",
                "bDiscriminatorCSV"    ,
                "NumBhadrons"          ,
                "NumChadrons"          ,
            )
        )
        # specify userfloats
        JetsPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSPrunedMass')
        JetsPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8:tau1')
        JetsPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8:tau2')
        JetsPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8:tau3')
#        JetsPropertiesAK8.bDiscriminatorSubjet1 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
#        JetsPropertiesAK8.bDiscriminatorSubjet2 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
        JetsPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
        self.VectorDouble.extend(['JetsProperties'+suff+':prunedMass(Jets'+suff+'_prunedMass)',
#                             'JetsProperties'+suff+':bDiscriminatorSubjet1(Jets'+suff+'_bDiscriminatorSubjet1CSV)',
#                             'JetsProperties'+suff+':bDiscriminatorSubjet2(Jets'+suff+'_bDiscriminatorSubjet2CSV)',
                             'JetsProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_doubleBDiscriminator)',
                             'JetsProperties'+suff+':NsubjettinessTau1(Jets'+suff+'_NsubjettinessTau1)',
                             'JetsProperties'+suff+':NsubjettinessTau2(Jets'+suff+'_NsubjettinessTau2)',
                             'JetsProperties'+suff+':NsubjettinessTau3(Jets'+suff+'_NsubjettinessTau3)'])
        self.VectorInt.extend(['JetsProperties'+suff+':NumBhadrons(Jets'+suff+'_NumBhadrons)',
                          'JetsProperties'+suff+':NumChadrons(Jets'+suff+'_NumChadrons)'])
        if self.semivisible:
            JetsPropertiesAK8.properties.extend([
                'overflow',
                'girth',
                'momenthalf',
                'ptD',
                'axismajor',
                'axisminor',
                'multiplicity',
                'constituents',
            ])
            JetsPropertiesAK8.overflow = cms.vstring('BasicSubstructure'+suff+':overflow')
            JetsPropertiesAK8.girth = cms.vstring('BasicSubstructure'+suff+':girth')
            JetsPropertiesAK8.momenthalf = cms.vstring('BasicSubstructure'+suff+':momenthalf')
            JetsPropertiesAK8.ptD = cms.vstring('BasicSubstructure'+suff+':ptD')
            JetsPropertiesAK8.axismajor = cms.vstring('BasicSubstructure'+suff+':axismajor')
            JetsPropertiesAK8.axisminor = cms.vstring('BasicSubstructure'+suff+':axisminor')
            JetsPropertiesAK8.multiplicity = cms.vstring('BasicSubstructure'+suff+':multiplicity')
            self.VectorDouble.extend([
                'JetsProperties'+suff+':overflow(Jets'+suff+'_overflow)',
                'JetsProperties'+suff+':girth(Jets'+suff+'_girth)',
                'JetsProperties'+suff+':momenthalf(Jets'+suff+'_momenthalf)',
                'JetsProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetsProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                'JetsProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
            ])
            self.VectorInt.extend([
                'JetsProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
            self.VectorVectorTLorentzVector.extend([
                'JetsProperties'+suff+':constituents(Jets'+suff+'_constituents)',
            ])
        setattr(process,"JetsProperties"+suff,JetsPropertiesAK8)

        return process        
