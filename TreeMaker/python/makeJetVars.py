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
        MHTPhi       = cms.InputTag('MHT'+MHTsuff+suff+':Phi'),
    )
    setattr(process,"DeltaPhi"+MHTsuff+suff,DeltaPhi)
    self.VarsDouble.extend(['DeltaPhi'+MHTsuff+suff+':DeltaPhi1(DeltaPhi1'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi2(DeltaPhi2'+MHTsuff+suff+')',
                                          'DeltaPhi'+MHTsuff+suff+':DeltaPhi3(DeltaPhi3'+MHTsuff+suff+')','DeltaPhi'+MHTsuff+suff+':DeltaPhi4(DeltaPhi4'+MHTsuff+suff+')'])
    
    return process

def makeGoodJets(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), jetConeSize=0.4):
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
    GoodJets = GoodJetsProducer.clone()
    TMeras.TM2016.toModify(GoodJets,
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        maxJetEta                 = cms.double(5.0),
        minNconstituents          = cms.int32(1),
        minNneutralsHF            = cms.int32(10),
        minNcharged               = cms.int32(0),
        maxNeutralFraction        = cms.double(0.99),
        maxPhotonFraction         = cms.double(0.99),
        maxPhotonFractionHF       = cms.double(0.90),
        minChargedFraction        = cms.double(0),
        maxChargedEMFraction      = cms.double(0.99),
        jetPtFilter               = cms.double(30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(jetConeSize),
        SkipTag                   = SkipTag,
        SaveAllJetsId             = True,
        SaveAllJetsPt             = False, # exclude low pt jets from good collection
    )
    TMeras.TM2017.toModify(GoodJets,
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        maxJetEta                 = cms.double(5.0),
        minNconstituents          = cms.int32(1),
        minNneutralsHE            = cms.int32(2),
        minNneutralsHF            = cms.int32(10),
        minNcharged               = cms.int32(0),
        maxNeutralFraction        = cms.double(0.90),
        maxNeutralFractionHE      = cms.double(1.00), #Turned off as not needed for the tight WP
        minNeutralFractionHF      = cms.double(0.02),
        maxPhotonFraction         = cms.double(0.90),
        minPhotonFractionHE       = cms.double(0.02),
        maxPhotonFractionHE       = cms.double(0.99),
        maxPhotonFractionHF       = cms.double(0.90),
        minChargedFraction        = cms.double(0.00),
        maxChargedEMFraction      = cms.double(1.00), #Turned off as not needed for the tight WP
        jetPtFilter               = cms.double(170 if jetConeSize==0.8 else 30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(jetConeSize),
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
        process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,SkipTag,0.4)
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

    BTagsDeepCSV = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfDeepCSVDiscriminatorsJetTags:BvsAll'),
        BTagCutValue = cms.double(0.4941 )
    )
    setattr(process,"BTagsDeepCSV"+suff,BTagsDeepCSV)
    self.VarsInt.extend(['BTagsDeepCSV'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT, DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    # MHT, DeltaPhi moved to separate fn (above)
    process = self.makeMHTVars(process, GoodJetsTag, HTJetsTag, storeProperties, suff, "")

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
        JetProperties = jetproperties.clone(
            JetTag       = GoodJetsTag
        )
        # provide extra info where necessary
        if storeProperties==1: 
            JetProperties.properties = cms.vstring("bDiscriminatorCSV","bJetTagDeepCSVprobb","bJetTagDeepCSVprobc",
                                                   "bJetTagDeepCSVprobudsg","bJetTagDeepCSVprobbb","bDiscriminatorDeepCSVBvsAll",
                                                   "bDiscriminatorDeepCSVCvsB","bDiscriminatorDeepCSVCvsL","bJetTagDeepFlavourprobb",
                                                   "bJetTagDeepFlavourprobc","bJetTagDeepFlavourprobg","bJetTagDeepFlavourproblepb",
                                                   "bJetTagDeepFlavourprobbb","bJetTagDeepFlavourprobuds","muonEnergyFraction",
                                                   "chargedHadronEnergyFraction","partonFlavor","hadronFlavor")
        if storeProperties>1 and self.geninfo:
            JetProperties.properties.extend(["jerFactor", "jerFactorUp","jerFactorDown"])
        setattr(process,"JetProperties"+suff,JetProperties)
        self.VectorDouble.extend([
            'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_bDiscriminatorCSV)',
            'JetProperties'+suff+':bJetTagDeepCSVprobb(Jets'+suff+'_bJetTagDeepCSVprobb)',
            'JetProperties'+suff+':bJetTagDeepCSVprobc(Jets'+suff+'_bJetTagDeepCSVprobc)',
            'JetProperties'+suff+':bJetTagDeepCSVprobudsg(Jets'+suff+'_bJetTagDeepCSVprobudsg)',
            'JetProperties'+suff+':bJetTagDeepCSVprobbb(Jets'+suff+'_bJetTagDeepCSVprobbb)',
            'JetProperties'+suff+':bDiscriminatorDeepCSVBvsAll(Jets'+suff+'_bJetTagDeepCSVBvsAll)',
            'JetProperties'+suff+':bDiscriminatorDeepCSVCvsB(Jets'+suff+'_bJetTagDeepCSVCvsB)',
            'JetProperties'+suff+':bDiscriminatorDeepCSVCvsL(Jets'+suff+'_bJetTagDeepCSVCvsL)',
            'JetProperties'+suff+':bJetTagDeepFlavourprobb(Jets'+suff+'_bJetTagDeepFlavourprobb)',
            'JetProperties'+suff+':bJetTagDeepFlavourprobc(Jets'+suff+'_bJetTagDeepFlavourprobc)',
            'JetProperties'+suff+':bJetTagDeepFlavourprobg(Jets'+suff+'_bJetTagDeepFlavourprobg)',
            'JetProperties'+suff+':bJetTagDeepFlavourproblepb(Jets'+suff+'_bJetTagDeepFlavourproblepb)',
            'JetProperties'+suff+':bJetTagDeepFlavourprobbb(Jets'+suff+'_bJetTagDeepFlavourprobbb)',
            'JetProperties'+suff+':bJetTagDeepFlavourprobuds(Jets'+suff+'_bJetTagDeepFlavourprobuds)',
            'JetProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
            'JetProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
        ])
        self.VectorInt.extend([
            'JetProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
            'JetProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)',
        ])
        if storeProperties>1:
            self.VectorDouble.extend([
                'JetProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                'JetProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                'JetProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                'JetProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                'JetProperties'+suff+':electronEnergyFraction(Jets'+suff+'_electronEnergyFraction)',
                'JetProperties'+suff+':hfEMEnergyFraction(Jets'+suff+'_hfEMEnergyFraction)',
                'JetProperties'+suff+':hfHadronEnergyFraction(Jets'+suff+'_hfHadronEnergyFraction)',
                'JetProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
                'JetProperties'+suff+':jecUnc(Jets'+suff+'_jecUnc)',
                'JetProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
            ])
            if self.geninfo:
                self.VectorDouble.extend([
                    'JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)',
                    'JetProperties'+suff+':jerFactorUp(Jets'+suff+'_jerFactorUp)',
                    'JetProperties'+suff+':jerFactorDown(Jets'+suff+'_jerFactorDown)',
                ])

            self.VectorInt.extend([
                'JetProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                'JetProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                'JetProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                'JetProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                'JetProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                'JetProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                'JetProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)',
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
                                             
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

    process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,jetConeSize=0.8)

    if storeProperties>0:
        # AK8 jet variables - separate instance of jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetPropertiesAK8 = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties = cms.vstring(
                "prunedMass"            ,
                "softDropMass"          ,
                "NsubjettinessTau1"     ,
                "NsubjettinessTau2"     ,
                "NsubjettinessTau3"     ,
                "bDiscriminatorCSV"     ,
                "bJetTagDeepCSVprobb"   ,
                "bJetTagDeepCSVprobc"   ,
                "bJetTagDeepCSVprobudsg",
                "bJetTagDeepCSVprobbb"  ,
                "NumBhadrons"           ,
                "NumChadrons"           ,
                "subjets"               ,
            )
        )
        # specify userfloats
        JetPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass')
        JetPropertiesAK8.softDropMass = cms.vstring('SoftDropPuppi') # computed from subjets
        JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi:tau1')
        JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi:tau2')
        JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi:tau3')
        JetPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
        JetPropertiesAK8.bJetTagDeepCSVprobb = cms.vstring('pfDeepCSVJetTags:probb')
        JetPropertiesAK8.bJetTagDeepCSVprobc = cms.vstring('pfDeepCSVJetTags:probc')
        JetPropertiesAK8.bJetTagDeepCSVprobudsg = cms.vstring('pfDeepCSVJetTags:probudsg')
        JetPropertiesAK8.bJetTagDeepCSVprobbb = cms.vstring('pfDeepCSVJetTags:probbb')
        JetPropertiesAK8.subjets = cms.vstring('SoftDropPuppi')
        self.VectorDouble.extend([
                             'JetProperties'+suff+':prunedMass(Jets'+suff+'_prunedMass)',
                             'JetProperties'+suff+':softDropMass(Jets'+suff+'_softDropMass)',
                             'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_doubleBDiscriminator)',
                             'JetProperties'+suff+':bJetTagDeepCSVprobb(Jets'+suff+'_bJetTagDeepCSVprobb)',
                             'JetProperties'+suff+':bJetTagDeepCSVprobc(Jets'+suff+'_bJetTagDeepCSVprobc)',
                             'JetProperties'+suff+':bJetTagDeepCSVprobudsg(Jets'+suff+'_bJetTagDeepCSVprobudsg)',
                             'JetProperties'+suff+':bJetTagDeepCSVprobbb(Jets'+suff+'_bJetTagDeepCSVprobbb)',
                             'JetProperties'+suff+':NsubjettinessTau1(Jets'+suff+'_NsubjettinessTau1)',
                             'JetProperties'+suff+':NsubjettinessTau2(Jets'+suff+'_NsubjettinessTau2)',
                             'JetProperties'+suff+':NsubjettinessTau3(Jets'+suff+'_NsubjettinessTau3)'])
        self.VectorInt.extend(['JetProperties'+suff+':NumBhadrons(Jets'+suff+'_NumBhadrons)',
                          'JetProperties'+suff+':NumChadrons(Jets'+suff+'_NumChadrons)'])
        self.VectorVectorTLorentzVector.extend([
            'JetProperties'+suff+':subjets(Jets'+suff+'_subjets)',
        ])

        if self.semivisible:
            JetPropertiesAK8.properties.extend([
                'overflow',
                'girth',
                'momenthalf',
                'ptD',
                'axismajor',
                'axisminor',
                'multiplicity',
#                'constituents',
            ])
            JetPropertiesAK8.overflow = cms.vstring('BasicSubstructure'+suff+':overflow')
            JetPropertiesAK8.girth = cms.vstring('BasicSubstructure'+suff+':girth')
            JetPropertiesAK8.momenthalf = cms.vstring('BasicSubstructure'+suff+':momenthalf')
            JetPropertiesAK8.ptD = cms.vstring('BasicSubstructure'+suff+':ptD')
            JetPropertiesAK8.axismajor = cms.vstring('BasicSubstructure'+suff+':axismajor')
            JetPropertiesAK8.axisminor = cms.vstring('BasicSubstructure'+suff+':axisminor')
            JetPropertiesAK8.multiplicity = cms.vstring('BasicSubstructure'+suff+':multiplicity')
            self.VectorDouble.extend([
                'JetProperties'+suff+':overflow(Jets'+suff+'_overflow)',
                'JetProperties'+suff+':girth(Jets'+suff+'_girth)',
                'JetProperties'+suff+':momenthalf(Jets'+suff+'_momenthalf)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
            ])
            self.VectorInt.extend([
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
#            self.VectorVectorTLorentzVector.extend([
#                'JetProperties'+suff+':constituents(Jets'+suff+'_constituents)',
#            ])
        setattr(process,"JetProperties"+suff,JetPropertiesAK8)

    return process        
