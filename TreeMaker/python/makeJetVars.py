import FWCore.ParameterSet.Config as cms
from TreeMaker.TreeMaker.addJetInfo import addJetInfo

def makeMHTVars(self, process, JetTag, HTJetsTag, storeProperties, suff, MHTsuff, MaxEta=5.0):
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    MHTJets = SubJetSelection.clone(
        JetTag = JetTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(MaxEta),
    )
    setattr(process,"MHTJets"+suff+MHTsuff,MHTJets)
    if storeProperties>1: self.VectorBool.extend(['MHTJets'+suff+MHTsuff+':SubJetMask(Jets'+suff+'_MHT'+MHTsuff+'Mask)'])
    MHTJetsTag = cms.InputTag("MHTJets"+suff+MHTsuff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+suff+MHTsuff,MHT)
    self.VarsDouble.extend(['MHT'+suff+MHTsuff+':Pt(MHT'+suff+MHTsuff+')','MHT'+suff+MHTsuff+':Phi(MHTPhi'+suff+MHTsuff+')'])

    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTPhi       = cms.InputTag('MHT'+suff+MHTsuff+':Phi'),
    )
    setattr(process,"DeltaPhi"+suff+MHTsuff,DeltaPhi)
    self.VarsDouble.extend(['DeltaPhi'+suff+MHTsuff+':DeltaPhi1(DeltaPhi1'+suff+MHTsuff+')','DeltaPhi'+suff+MHTsuff+':DeltaPhi2(DeltaPhi2'+suff+MHTsuff+')',
                                          'DeltaPhi'+suff+MHTsuff+':DeltaPhi3(DeltaPhi3'+suff+MHTsuff+')','DeltaPhi'+suff+MHTsuff+':DeltaPhi4(DeltaPhi4'+suff+MHTsuff+')'])
    
    return process, MHTJetsTag

def makeGoodJets(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), jetConeSize=0.4, puppiSpecific=""):
    from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer,GoodJetsPuppiProducer
    GoodJets = (GoodJetsPuppiProducer if jetConeSize==0.8 else GoodJetsProducer).clone(
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        jetPtFilter               = cms.double(170 if jetConeSize==0.8 else 30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(jetConeSize),
        SkipTag                   = SkipTag,
        SaveAllJetsId             = cms.bool(True),
        # keep lower-pt central jets in case they fluctuate up in systematic collections (for all)
        SaveAllJetsPt             = cms.bool(True),
        # keep all eta jets to preserve ordering
        maxJetEta                 = cms.double(-1),
    )
    if len(puppiSpecific)>0: GoodJets.puppiPrefix = puppiSpecific
    setattr(process,"GoodJets"+suff,GoodJets)
    GoodJetsTag = cms.InputTag("GoodJets"+suff)
    self.VarsBool.extend(['GoodJets'+suff+':JetID(JetID'+suff+')'])
    if storeProperties>0:
        self.VectorRecoCand.extend(['GoodJets'+suff+'(Jets'+suff+')'])
        self.VectorBool.extend(['GoodJets'+suff+':JetIDMask(Jets'+suff+'_ID)'])
        if len(SkipTag)>0: self.VectorBool.extend(['GoodJets'+suff+':JetLeptonMask(Jets'+suff+'_LeptonMask)'])
    return (process,GoodJetsTag)

# AK4 storeProperties levels:
# 0 = scalars (+ origIndex,jerFactor for syst)
# 1 = 0 + 4vecs, masks, minimal set of properties
# 2 = all properties
def makeJetVars(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), onlyGoodJets=False, systType=""):
    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
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
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.btagint_cfi import btagint

    BTagsDeepCSV = btagint.clone(
        JetTag       = HTJetsTag,
        BTagInputTag = cms.string('pfDeepCSVDiscriminatorsJetTags:BvsAll'),
        BTagCutValue = cms.double(0.5847) # https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16postVFP#AK4_b_tagging
    )
    # Medium DeepCSV UL WPs from:
    
    # https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16preVFP#AK4_b_tagging
    # https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL18#AK4_b_tagging
    # https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL17#AK4_b_tagging
    (TMeras.TMUL2016APV).toModify(BTagsDeepCSV,BTagCutValue = cms.double(0.6001))
    (TMeras.TMUL2017).toModify(BTagsDeepCSV,BTagCutValue = cms.double(0.4506))
    (TMeras.TMUL2018).toModify(BTagsDeepCSV,BTagCutValue = cms.double(0.4168))
    setattr(process,"BTagsDeepCSV"+suff,BTagsDeepCSV)
    self.VarsInt.extend(['BTagsDeepCSV'+suff])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT, DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    process, MHTJetsTag = self.makeMHTVars(process, JetTag, HTJetsTag, storeProperties, suff, "")

    # extra HT version using MHT collection w/ |eta| < 5, to filter forward beam halo events
    HT5 = htdouble.clone(
        JetTag = MHTJetsTag,
    )
    setattr(process,"HT5"+suff,HT5)
    self.VarsDouble.extend(['HT5'+suff])

    ## ----------------------------------------------------------------------------------------------
    ## ISR jets
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo and storeProperties!=1:
        from TreeMaker.Utils.isrjet_cfi import ISRJetProducer
        ISRJets = ISRJetProducer.clone(
            JetTag = GoodJetsTag,
            JetLeptonTag  = cms.InputTag(GoodJetsTag.value()+':JetLeptonMask'),
            GenPartTag = cms.InputTag("prunedGenParticles"),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        setattr(process,"ISRJets"+suff,ISRJets)
        self.VarsInt.extend(['ISRJets'+suff+'(NJetsISR'+suff+')'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet properties
    ## ----------------------------------------------------------------------------------------------
    if storeProperties==0:
        # for systematics
        JetProperties = cms.EDProducer("JetProperties",
            JetTag = GoodJetsTag,
            debug = cms.bool(False),
            properties = cms.vstring("origIndex"),
        )
        if systType=="JEC":
            JetProperties.properties.append("jerFactor")
            JetProperties.jerFactor = cms.vstring("jerFactor")
            JetProperties.origIndex = cms.vstring("jecOrigIndex")
            self.VectorDouble.extend(['JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)'])
        elif systType=="JER":
            JetProperties.origIndex = cms.vstring("jerOrigIndex")
        setattr(process,"JetProperties"+suff,JetProperties)
        self.VectorInt.extend(['JetProperties'+suff+':origIndex(Jets'+suff+'_origIndex)'])
    elif storeProperties>0:
        # make jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetProperties = jetproperties.clone(
            JetTag       = GoodJetsTag
        )

        # provide extra info where necessary
        if storeProperties==1:
            btaggers = ["bDiscriminatorCSV","bDiscriminatorDeepCSVBvsAll"]
            flavors = ["partonFlavor","hadronFlavor"]
            JetProperties.properties = cms.vstring(*(btaggers+flavors))
        setattr(process,"JetProperties"+suff,JetProperties)
        self.VectorDouble.extend([
            'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_bDiscriminatorCSV)',
            'JetProperties'+suff+':bDiscriminatorDeepCSVBvsAll(Jets'+suff+'_bJetTagDeepCSVBvsAll)',
        ])
        self.VectorInt.extend([
            'JetProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
            'JetProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)',
        ])
        if storeProperties>1:
            JetProperties.properties.extend(["jecFactor"])
            self.VectorDouble.extend([
                'JetProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
                'JetProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
                'JetProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                'JetProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                'JetProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                'JetProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                'JetProperties'+suff+':electronEnergyFraction(Jets'+suff+'_electronEnergyFraction)',
                'JetProperties'+suff+':hfEMEnergyFraction(Jets'+suff+'_hfEMEnergyFraction)',
                'JetProperties'+suff+':hfHadronEnergyFraction(Jets'+suff+'_hfHadronEnergyFraction)',
                'JetProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
                'JetProperties'+suff+':bJetTagDeepFlavourprobb(Jets'+suff+'_bJetTagDeepFlavourprobb)',
                'JetProperties'+suff+':bJetTagDeepFlavourprobbb(Jets'+suff+'_bJetTagDeepFlavourprobbb)',
                'JetProperties'+suff+':bJetTagDeepFlavourproblepb(Jets'+suff+'_bJetTagDeepFlavourproblepb)',
                'JetProperties'+suff+':bJetTagDeepFlavourprobc(Jets'+suff+'_bJetTagDeepFlavourprobc)',
                'JetProperties'+suff+':bJetTagDeepFlavourprobg(Jets'+suff+'_bJetTagDeepFlavourprobg)',
                'JetProperties'+suff+':bJetTagDeepFlavourprobuds(Jets'+suff+'_bJetTagDeepFlavourprobuds)',
                'JetProperties'+suff+':bJetTagDeepCSVprobb(Jets'+suff+'_bJetTagDeepCSVprobb)',
                'JetProperties'+suff+':bJetTagDeepCSVprobbb(Jets'+suff+'_bJetTagDeepCSVprobbb)',
                'JetProperties'+suff+':bJetTagDeepCSVprobc(Jets'+suff+'_bJetTagDeepCSVprobc)',
                'JetProperties'+suff+':bJetTagDeepCSVprobudsg(Jets'+suff+'_bJetTagDeepCSVprobudsg)',
            ])
            if self.geninfo:
                JetProperties.properties.extend(["jerFactor"])
                JetProperties.jerFactor = cms.vstring("jerFactor")
                self.VectorDouble.extend([
                    'JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)',
                ])
                if self.systematics:
                    # account for central JER smearing
                    JetProperties.properties.extend(["origIndex"])
                    JetProperties.origIndex = cms.vstring("jerOrigIndex")
                    self.VectorInt.extend(['JetProperties'+suff+':origIndex(Jets'+suff+'_origIndex)'])

            self.VectorInt.extend([
                'JetProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                'JetProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                'JetProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                'JetProperties'+suff+':neutralHadronMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                'JetProperties'+suff+':photonMultiplicity(Jets'+suff+'_photonMultiplicity)',
                'JetProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
                'JetProperties'+suff+':neutralMultiplicity(Jets'+suff+'_neutralMultiplicity)',
            ])

            if self.doQG:
                JetProperties.properties.extend(["qgLikelihood","ptD","axisminor","axismajor","multiplicity"])
                JetProperties.qgLikelihood = cms.vstring('QGTagger:qgLikelihood')
                JetProperties.ptD = cms.vstring('QGTagger:ptD')
                JetProperties.axisminor = cms.vstring('QGTagger:axis2')
                JetProperties.axismajor = cms.vstring('QGTagger:axis1')
                JetProperties.multiplicity = cms.vstring('QGTagger:mult')
                self.VectorDouble.extend([
                    'JetProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                    'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                    'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                    'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                ])
                self.VectorInt.extend([
                    'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
                ])

    return process

# AK8 storeProperties levels:
# 0 = ID scalar from goodJets (+ origIndex,jerFactor for syst)
# 1 = 0 + 4vecs, most properties
# 2 = 1 + subjet properties + extra substructure
# 3 = 2 + constituents (large)
# SkipTag is not used, but just there to make interfaces consistent
def makeJetVarsAK8(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), systType="", doECFs=True, doDeepAK8=True, doDeepDoubleB=True, CandTag=cms.InputTag("packedPFCandidates"),puppiSpecific="", subjetTag='SoftDropPuppiUpdated'):
    # select good jets before anything else - eliminates bad AK8 jets (low pT, no constituents stored, etc.)
    process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,jetConeSize=0.8,puppiSpecific=puppiSpecific)

    # anything to be computed for AK8 jets
    ak8floats = []
    ak8ints = []

    # get more substructure
    if self.semivisible and storeProperties>1:
        BasicSubstructure = cms.EDProducer("BasicSubstructureProducer",
            JetTag = GoodJetsTag
        )
        setattr(process,"BasicSubstructure"+suff,BasicSubstructure)
        ak8floats.extend([
            'BasicSubstructure'+suff+':girth',
        ])

        if self.doQG:
            QGTagger = process.QGTagger.clone(
                srcJets = GoodJetsTag
            )
            setattr(process,"QGTagger"+suff,QGTagger)
            ak8floats.extend([
                'QGTagger'+suff+':ptD',
                'QGTagger'+suff+':axis1',
                'QGTagger'+suff+':axis2',
            ])
            ak8ints.extend([
                'QGTagger'+suff+':mult',
            ])

    # add discriminator and update tag
    if len(ak8floats)>0 or len(ak8ints)>0:
        process, GoodJetsTag = addJetInfo(process, GoodJetsTag, ak8floats, ak8ints)

    if storeProperties==0:
        # for systematics
        JetPropertiesAK8 = cms.EDProducer("JetProperties",
            JetTag = GoodJetsTag,
            debug = cms.bool(False),
            properties = cms.vstring("origIndex"),
        )
        if systType=="JEC":
            JetPropertiesAK8.properties.append("jerFactor")
            JetPropertiesAK8.jerFactor = cms.vstring("jerFactor")
            JetPropertiesAK8.origIndex = cms.vstring("jecOrigIndex")
            self.VectorDouble.extend(['JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)'])
        elif systType=="JER":
            JetPropertiesAK8.origIndex = cms.vstring("jerOrigIndex")
        setattr(process,"JetProperties"+suff,JetPropertiesAK8)
        self.VectorInt.extend(['JetProperties'+suff+':origIndex(Jets'+suff+'_origIndex)'])
    elif storeProperties>0:
        # AK8 jet variables - separate instance of jet properties producer
        from TreeMaker.Utils.jetproperties_cfi import jetproperties
        JetPropertiesAK8 = jetproperties.clone(
            JetTag       = GoodJetsTag,
            properties = cms.vstring(
                "softDropMass"          ,
                "bDiscriminatorCSV"     ,
                "subjets"               ,
                "SJbDiscriminatorCSV"   ,
            )
        )
        # specify userfloats
        JetPropertiesAK8.softDropMass = cms.vstring(subjetTag) # computed from subjets
        JetPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
        JetPropertiesAK8.subjets = cms.vstring(subjetTag)
        self.VectorDouble.extend([
            'JetProperties'+suff+':softDropMass(Jets'+suff+'_softDropMass)',
            'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_doubleBDiscriminator)',
        ])
        self.VectorVectorLorentzVector.extend([
            'JetProperties'+suff+':subjets(Jets'+suff+'_subjets)',
        ])

        if doECFs:
            JetPropertiesAK8.properties.extend([
                "ecfN2b1",
                "ecfN2b2",
                "ecfN3b1",
                "ecfN3b2",
            ])
            JetPropertiesAK8.ecfN2b1 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2')
            JetPropertiesAK8.ecfN2b2 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN2')
            JetPropertiesAK8.ecfN3b1 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3')
            JetPropertiesAK8.ecfN3b2 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN3')
            self.VectorDouble.extend([
                'JetProperties'+suff+':ecfN2b1(Jets'+suff+'_ecfN2b1)',
                'JetProperties'+suff+':ecfN2b2(Jets'+suff+'_ecfN2b2)',
                'JetProperties'+suff+':ecfN3b1(Jets'+suff+'_ecfN3b1)',
                'JetProperties'+suff+':ecfN3b2(Jets'+suff+'_ecfN3b2)',
            ])

        if self.deepAK8 and doDeepAK8:
            JetPropertiesAK8.properties.extend([                  
                "pfDeepBoostedDiscriminatorsJetTagsTvsQCD",
                "pfDeepBoostedDiscriminatorsJetTagsWvsQCD",
                "pfDeepBoostedDiscriminatorsJetTagsZvsQCD",
                "pfDeepBoostedDiscriminatorsJetTagsHbbvsQCD",
                "pfDeepBoostedDiscriminatorsJetTagsZbbvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsTvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsWvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsHbbvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZHbbvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZbbvsQCD",
                "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsbbvsLight",
            ])
            JetPropertiesAK8.pfDeepBoostedDiscriminatorsJetTagsTvsQCD = cms.vstring("pfDeepBoostedDiscriminatorsJetTags:TvsQCD")
            JetPropertiesAK8.pfDeepBoostedDiscriminatorsJetTagsWvsQCD = cms.vstring("pfDeepBoostedDiscriminatorsJetTags:WvsQCD")
            JetPropertiesAK8.pfDeepBoostedDiscriminatorsJetTagsZvsQCD = cms.vstring("pfDeepBoostedDiscriminatorsJetTags:ZvsQCD")
            JetPropertiesAK8.pfDeepBoostedDiscriminatorsJetTagsHbbvsQCD = cms.vstring("pfDeepBoostedDiscriminatorsJetTags:HbbvsQCD")
            JetPropertiesAK8.pfDeepBoostedDiscriminatorsJetTagsZbbvsQCD = cms.vstring("pfDeepBoostedDiscriminatorsJetTags:ZbbvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsTvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsWvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsHbbvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:HbbvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZHbbvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZbbvsQCD = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZbbvsQCD")
            JetPropertiesAK8.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsbbvsLight = cms.vstring("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight")
            self.VectorDouble.extend([
                'JetProperties'+suff+':pfDeepBoostedDiscriminatorsJetTagsTvsQCD(Jets'+suff+'_DeepTagTvsQCD)',
                'JetProperties'+suff+':pfDeepBoostedDiscriminatorsJetTagsWvsQCD(Jets'+suff+'_DeepTagWvsQCD)',
                'JetProperties'+suff+':pfDeepBoostedDiscriminatorsJetTagsZvsQCD(Jets'+suff+'_DeepTagZvsQCD)',
                'JetProperties'+suff+':pfDeepBoostedDiscriminatorsJetTagsHbbvsQCD(Jets'+suff+'_DeepTagHbbvsQCD)',
                'JetProperties'+suff+':pfDeepBoostedDiscriminatorsJetTagsZbbvsQCD(Jets'+suff+'_DeepTagZbbvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsTvsQCD(Jets'+suff+'_DeepMassDecorrelTagTvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsWvsQCD(Jets'+suff+'_DeepMassDecorrelTagWvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZvsQCD(Jets'+suff+'_DeepMassDecorrelTagZvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsHbbvsQCD(Jets'+suff+'_DeepMassDecorrelTagHbbvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZHbbvsQCD(Jets'+suff+'_DeepMassDecorrelTagZHbbvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsZbbvsQCD(Jets'+suff+'_DeepMassDecorrelTagZbbvsQCD)',
                'JetProperties'+suff+':pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsbbvsLight(Jets'+suff+'_DeepMassDecorrelTagbbvsLight)',
            ])

        if self.deepDoubleB and doDeepDoubleB:
            JetPropertiesAK8.properties.extend(["pfMassIndependentDeepDoubleBvLJetTagsProbHbb"])
            JetPropertiesAK8.pfMassIndependentDeepDoubleBvLJetTagsProbHbb = cms.vstring('pfMassIndependentDeepDoubleBvLJetTags:probHbb')
            self.VectorDouble.extend(['JetProperties'+suff+':pfMassIndependentDeepDoubleBvLJetTagsProbHbb(Jets'+suff+'_pfMassIndependentDeepDoubleBvLJetTagsProbHbb)'])

        if storeProperties>1:
            JetPropertiesAK8.properties.extend(["jecFactor"])
            self.VectorDouble.extend([
                'JetProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
            ])
            if self.geninfo:
                JetPropertiesAK8.properties.extend(["jerFactor"])
                JetPropertiesAK8.jerFactor = cms.vstring("jerFactor")
                self.VectorDouble.extend([
                    'JetProperties'+suff+':jerFactor(Jets'+suff+'_jerFactor)',
                ])
                if self.systematics:
                    # account for central JER smearing
                    JetPropertiesAK8.properties.extend(["origIndex"])
                    JetPropertiesAK8.origIndex = cms.vstring("jerOrigIndex")
                    self.VectorInt.extend(['JetProperties'+suff+':origIndex(Jets'+suff+'_origIndex)'])
            # nsubjettiness and num hadrons
            JetPropertiesAK8.properties.extend([
                "NsubjettinessTau1"     ,
                "NsubjettinessTau2"     ,
                "NsubjettinessTau3"     ,
                "NumBhadrons"           ,
                "NumChadrons"           ,
                "partonFlavor"          ,
                "hadronFlavor"          ,
            ])
            JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi:tau1')
            JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi:tau2')
            JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi:tau3')
            self.VectorDouble.extend([
                'JetProperties'+suff+':NsubjettinessTau1(Jets'+suff+'_NsubjettinessTau1)',
                'JetProperties'+suff+':NsubjettinessTau2(Jets'+suff+'_NsubjettinessTau2)',
                'JetProperties'+suff+':NsubjettinessTau3(Jets'+suff+'_NsubjettinessTau3)',
            ])
            self.VectorInt.extend([
                'JetProperties'+suff+':NumBhadrons(Jets'+suff+'_NumBhadrons)',
                'JetProperties'+suff+':NumChadrons(Jets'+suff+'_NumChadrons)',
                'JetProperties'+suff+':partonFlavor(Jets'+suff+'_partonFlavor)',
                'JetProperties'+suff+':hadronFlavor(Jets'+suff+'_hadronFlavor)',
            ])

            # fractions and multiplicities (use puppi versions for neutral mults)
            JetPropertiesAK8.properties.extend([
                'chargedHadronMultiplicity',
                'neutralHadronPuppiMultiplicity',
                'electronMultiplicity',
                'photonPuppiMultiplicity',
                'muonMultiplicity',
                'chargedMultiplicity',
                'neutralPuppiMultiplicity',
                'chargedHadronEnergyFraction',
                'neutralHadronEnergyFraction',
                'chargedEmEnergyFraction',
                'neutralEmEnergyFraction',
                'electronEnergyFraction',
                'photonEnergyFraction',
                'muonEnergyFraction',
                'hfEMEnergyFraction',
                'hfHadronEnergyFraction',
            ])
            JetPropertiesAK8.neutralHadronPuppiMultiplicity = cms.vstring("puppiSpecificAK8:neutralHadronPuppiMultiplicity")
            JetPropertiesAK8.neutralPuppiMultiplicity = cms.vstring("puppiSpecificAK8:neutralPuppiMultiplicity")
            JetPropertiesAK8.photonPuppiMultiplicity = cms.vstring("puppiSpecificAK8:photonPuppiMultiplicity")
            self.VectorDouble.extend([
                'JetProperties'+suff+':muonEnergyFraction(Jets'+suff+'_muonEnergyFraction)',
                'JetProperties'+suff+':chargedHadronEnergyFraction(Jets'+suff+'_chargedHadronEnergyFraction)',
                'JetProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                'JetProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                'JetProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                'JetProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                'JetProperties'+suff+':electronEnergyFraction(Jets'+suff+'_electronEnergyFraction)',
                'JetProperties'+suff+':hfEMEnergyFraction(Jets'+suff+'_hfEMEnergyFraction)',
                'JetProperties'+suff+':hfHadronEnergyFraction(Jets'+suff+'_hfHadronEnergyFraction)',
                'JetProperties'+suff+':neutralHadronPuppiMultiplicity(Jets'+suff+'_neutralHadronMultiplicity)',
                'JetProperties'+suff+':photonPuppiMultiplicity(Jets'+suff+'_photonMultiplicity)',
                'JetProperties'+suff+':neutralPuppiMultiplicity(Jets'+suff+'_neutralMultiplicity)',
            ])
            self.VectorInt.extend([
                'JetProperties'+suff+':chargedHadronMultiplicity(Jets'+suff+'_chargedHadronMultiplicity)',
                'JetProperties'+suff+':electronMultiplicity(Jets'+suff+'_electronMultiplicity)',
                'JetProperties'+suff+':muonMultiplicity(Jets'+suff+'_muonMultiplicity)',
                'JetProperties'+suff+':chargedMultiplicity(Jets'+suff+'_chargedMultiplicity)',
            ])

            # extra stuff for subjets
            JetPropertiesAK8.properties.extend(["jecFactorSubjets"])
            JetPropertiesAK8.jecFactorSubjets = cms.vstring(subjetTag)
            JetPropertiesAK8.SJbDiscriminatorCSV = cms.vstring(subjetTag,'pfCombinedInclusiveSecondaryVertexV2BJetTags')
            self.AssocVectorVectorDouble.extend([
                'JetProperties'+suff+':jecFactorSubjets(Jets'+suff+'_subjets_jecFactor)',
            ])
            if self.doQG:
                JetPropertiesAK8.properties.extend(["SJptD", "SJaxismajor", "SJaxisminor", "SJmultiplicity"])
                JetPropertiesAK8.SJptD = cms.vstring(subjetTag,'QGTaggerSubjets:ptD')
                JetPropertiesAK8.SJaxismajor = cms.vstring(subjetTag,'QGTaggerSubjets:axis1')
                JetPropertiesAK8.SJaxisminor = cms.vstring(subjetTag,'QGTaggerSubjets:axis2')
                JetPropertiesAK8.SJmultiplicity = cms.vstring(subjetTag,'QGTaggerSubjets:mult')
                self.AssocVectorVectorDouble.extend([
                    'JetProperties'+suff+':SJptD(Jets'+suff+'_subjets_ptD)',
                    'JetProperties'+suff+':SJaxismajor(Jets'+suff+'_subjets_axismajor)',
                    'JetProperties'+suff+':SJaxisminor(Jets'+suff+'_subjets_axisminor)',
                ])
                self.AssocVectorVectorInt.extend([
                    'JetProperties'+suff+':SJmultiplicity(Jets'+suff+'_subjets_multiplicity)',
                ])

        if self.semivisible and storeProperties>1:
            JetPropertiesAK8.properties.extend([
                'girth',
            ])
            JetPropertiesAK8.girth = cms.vstring('BasicSubstructure'+suff+':girth')
            self.VectorDouble.extend([
                'JetProperties'+suff+':girth(Jets'+suff+'_girth)',
            ])

            if self.doQG:
                JetPropertiesAK8.properties.extend([
                    'ptD',
                    'axismajor',
                    'axisminor',
                    'multiplicity',
                ])
                JetPropertiesAK8.ptD = cms.vstring('QGTagger'+suff+':ptD')
                JetPropertiesAK8.axismajor = cms.vstring('QGTagger'+suff+':axis1')
                JetPropertiesAK8.axisminor = cms.vstring('QGTagger'+suff+':axis2')
                JetPropertiesAK8.multiplicity = cms.vstring('QGTagger'+suff+':mult')
                self.VectorDouble.extend([
                    'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                    'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                    'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                ])
                self.VectorInt.extend([
                    'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
                ])

            if storeProperties>2:
                JetPropertiesAK8.properties.extend(['constituents'])
                self.VectorVectorLorentzVector.extend([
                    'JetProperties'+suff+':constituents(Jets'+suff+'_constituents)',
                ])

        if self.debugsubjets and storeProperties>1:
            JetPropertiesAK8.GenSubjetTag = cms.InputTag('slimmedGenJetsAK8SoftDropSubJets')
            JetPropertiesAK8.properties.extend(["SJresponse"])
            JetPropertiesAK8.SJresponse = cms.vstring(subjetTag)
            self.AssocVectorVectorDouble.extend([
                'JetProperties'+suff+':SJresponse(Jets'+suff+'_subjets_response)',
            ])

        setattr(process,"JetProperties"+suff,JetPropertiesAK8)

    return process        

