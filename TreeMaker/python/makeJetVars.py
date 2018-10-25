import FWCore.ParameterSet.Config as cms
from TreeMaker.TreeMaker.addJetInfo import addJetInfo

def makeGoodJets(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), jetConeSize=0.4):
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
    GoodJets = GoodJetsProducer.clone(
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
    TMeras.TM2017.toModify(GoodJets,
        maxNeutralFraction        = cms.double(0.90),
        maxNeutralFractionHE      = cms.double(1.00), #Turned off as not needed for the tight WP
        minNeutralFractionHF      = cms.double(0.02),
        maxPhotonFraction         = cms.double(0.90),
        minPhotonFractionHE       = cms.double(0.02),
        maxPhotonFractionHE       = cms.double(0.99),
        maxChargedEMFraction      = cms.double(1.00), #Turned off as not needed for the tight WP
    )
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
def makeJetVars(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), onlyGoodJets=False, systType="", MHTJetTagExt=None):
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
    MHTJets = SubJetSelection.clone(
        JetTag = MHTJetTagExt if MHTJetTagExt is not None else JetTag,
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    setattr(process,"MHTJets"+suff,MHTJets)
    if storeProperties>0: self.VectorBool.extend(['MHTJets'+suff+':SubJetMask(Jets'+suff+'_MHT'+'Mask)'])
    MHTJetsTag = cms.InputTag("MHTJets"+suff)
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    MHT = mhtdouble.clone(
        JetTag  = MHTJetsTag,
    )
    setattr(process,"MHT"+suff,MHT)
    self.VarsDouble.extend(['MHT'+suff+':Pt(MHT'+suff+')','MHT'+suff+':Phi(MHTPhi'+suff+')'])
    
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = HTJetsTag,
        MHTPhi       = cms.InputTag('MHT'+suff+':Phi'),
    )
    setattr(process,"DeltaPhi"+suff,DeltaPhi)
    self.VarsDouble.extend(['DeltaPhi'+suff+':DeltaPhi1(DeltaPhi1'+suff+')','DeltaPhi'+suff+':DeltaPhi2(DeltaPhi2'+suff+')',
                            'DeltaPhi'+suff+':DeltaPhi3(DeltaPhi3'+suff+')','DeltaPhi'+suff+':DeltaPhi4(DeltaPhi4'+suff+')'])

    # keep orig MHT, dphi values if ext tag was given
    if MHTJetTagExt is not None:
        MHTJetsOrig = MHTJets.clone(
            JetTag = JetTag,
        )
        setattr(process,"MHTJets"+suff+"Orig",MHTJetsOrig)
        if storeProperties>0: self.VectorBool.extend(['MHTJets'+suff+'Orig:SubJetMask(Jets'+suff+'_MHTOrig'+'Mask)'])
        MHTJetsTagOrig = cms.InputTag("MHTJets"+suff+"Orig")
    
        MHTOrig = mhtdouble.clone(
            JetTag  = MHTJetsTagOrig,
        )
        setattr(process,"MHT"+suff+"Orig",MHTOrig)
        self.VarsDouble.extend(['MHT'+suff+'Orig:Pt(MHT'+suff+'Orig)','MHT'+suff+'Orig:Phi(MHTPhi'+suff+'Orig)'])
        
        DeltaPhiOrig = DeltaPhi.clone(
            MHTPhi       = cms.InputTag('MHT'+suff+'Orig:Phi'),
        )
        setattr(process,"DeltaPhi"+suff+"Orig",DeltaPhiOrig)
        self.VarsDouble.extend(['DeltaPhi'+suff+'Orig:DeltaPhi1(DeltaPhi1'+suff+'Orig)','DeltaPhi'+suff+'Orig:DeltaPhi2(DeltaPhi2'+suff+'Orig)',
                                'DeltaPhi'+suff+'Orig:DeltaPhi3(DeltaPhi3'+suff+'Orig)','DeltaPhi'+suff+'Orig:DeltaPhi4(DeltaPhi4'+suff+'Orig)'])
    else:
        MHTJetsTagOrig = None

    # extra HT version using MHT collection w/ |eta| < 5, to filter forward beam halo events
    HT5 = htdouble.clone(
        JetTag = MHTJetsTagOrig if MHTJetsTagOrig is not None else MHTJetsTag,
    )
    setattr(process,"HT5"+suff,HT5)
    self.VarsDouble.extend(['HT5'+suff])

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
            JetProperties.properties = cms.vstring("bDiscriminatorCSV","bJetTagDeepCSVprobb","bJetTagDeepCSVprobc",
                                                   "bJetTagDeepCSVprobudsg","bJetTagDeepCSVprobbb","bDiscriminatorDeepCSVBvsAll",
                                                   "bDiscriminatorDeepCSVCvsB","bDiscriminatorDeepCSVCvsL","bJetTagDeepFlavourprobb",
                                                   "bJetTagDeepFlavourprobc","bJetTagDeepFlavourprobg","bJetTagDeepFlavourproblepb",
                                                   "bJetTagDeepFlavourprobbb","bJetTagDeepFlavourprobuds","muonEnergyFraction",
                                                   "chargedHadronEnergyFraction","partonFlavor","hadronFlavor")
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
            JetProperties.properties.extend(["jecFactor"])
            self.VectorDouble.extend([
                'JetProperties'+suff+':chargedEmEnergyFraction(Jets'+suff+'_chargedEmEnergyFraction)',
                'JetProperties'+suff+':neutralEmEnergyFraction(Jets'+suff+'_neutralEmEnergyFraction)',
                'JetProperties'+suff+':neutralHadronEnergyFraction(Jets'+suff+'_neutralHadronEnergyFraction)',
                'JetProperties'+suff+':photonEnergyFraction(Jets'+suff+'_photonEnergyFraction)',
                'JetProperties'+suff+':electronEnergyFraction(Jets'+suff+'_electronEnergyFraction)',
                'JetProperties'+suff+':hfEMEnergyFraction(Jets'+suff+'_hfEMEnergyFraction)',
                'JetProperties'+suff+':hfHadronEnergyFraction(Jets'+suff+'_hfHadronEnergyFraction)',
                'JetProperties'+suff+':qgLikelihood(Jets'+suff+'_qgLikelihood)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                'JetProperties'+suff+':jecFactor(Jets'+suff+'_jecFactor)',
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
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])
                                             
    return process

# AK8 storeProperties levels:
# 0 = ID scalar from goodJets (+ origIndex,jerFactor for syst)
# 1 = 0 + 4vecs, most properties
# 2 = 1 + subjet properties + extra substructure
# 3 = 2 + constituents (large)
# SkipTag is not used, but just there to make interfaces consistent
def makeJetVarsAK8(self, process, JetTag, suff, storeProperties, SkipTag=cms.VInputTag(), systType="", doDeepAK8=True, doDoubleB=True, CandTag=cms.InputTag("packedPFCandidates")):
    # select good jets before anything else - eliminates bad AK8 jets (low pT, no constituents stored, etc.)
    process, GoodJetsTag = self.makeGoodJets(process,JetTag,suff,storeProperties,jetConeSize=0.8)

    # anything to be computed for AK8 jets
    ak8floats = []
    ak8ints = []
    ak8tags = cms.VInputTag()

    if storeProperties>0 and doDoubleB:
        # get double b-tagger (w/ miniAOD customizations)
        from RecoBTag.ImpactParameter.pfImpactParameterAK8TagInfos_cfi import pfImpactParameterAK8TagInfos
        pfImpactParameterAK8TagInfosMod = pfImpactParameterAK8TagInfos.clone(
            primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
            candidates = CandTag,
            jets = GoodJetsTag,
        )
        setattr(process,"pfImpactParameterAK8TagInfos"+suff,pfImpactParameterAK8TagInfosMod)
        from RecoBTag.SecondaryVertex.pfInclusiveSecondaryVertexFinderAK8TagInfos_cfi import pfInclusiveSecondaryVertexFinderAK8TagInfos
        pfInclusiveSecondaryVertexFinderAK8TagInfosMod = pfInclusiveSecondaryVertexFinderAK8TagInfos.clone(
            extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
            trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfos"+suff),
        )
        setattr(process,"pfInclusiveSecondaryVertexFinderAK8TagInfos"+suff,pfInclusiveSecondaryVertexFinderAK8TagInfosMod)
        from RecoBTag.SecondaryVertex.pfBoostedDoubleSVAK8TagInfos_cfi import pfBoostedDoubleSVAK8TagInfos
        pfBoostedDoubleSVAK8TagInfosMod = pfBoostedDoubleSVAK8TagInfos.clone(
            svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfos"+suff),
        )
        setattr(process,"pfBoostedDoubleSVAK8TagInfos"+suff,pfBoostedDoubleSVAK8TagInfosMod)
        from RecoBTag.SecondaryVertex.candidateBoostedDoubleSecondaryVertexAK8Computer_cfi import candidateBoostedDoubleSecondaryVertexAK8Computer
        candidateBoostedDoubleSecondaryVertexAK8ComputerMod = candidateBoostedDoubleSecondaryVertexAK8Computer.clone()
        setattr(process,"candidateBoostedDoubleSecondaryVertexAK8Computer"+suff,candidateBoostedDoubleSecondaryVertexAK8ComputerMod)
        from RecoBTag.SecondaryVertex.pfBoostedDoubleSecondaryVertexAK8BJetTags_cfi import pfBoostedDoubleSecondaryVertexAK8BJetTags
        pfBoostedDoubleSecondaryVertexAK8BJetTagsMod = pfBoostedDoubleSecondaryVertexAK8BJetTags.clone(
            jetTagComputer = cms.string("candidateBoostedDoubleSecondaryVertexAK8Computer"+suff),
            tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfos"+suff)),
        )
        setattr(process,"pfBoostedDoubleSecondaryVertexAK8BJetTags"+suff,pfBoostedDoubleSecondaryVertexAK8BJetTagsMod)
        ak8tags.append(cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTags"+suff))

    if storeProperties>0 and self.deepAK8 and doDeepAK8:
        from TreeMaker.Utils.deepak8producer_cfi import DeepAK8Producer, DeepAK8DecorrelProducer
        deepAK8 = DeepAK8Producer.clone(
            JetAK8 = GoodJetsTag
        )
        setattr(process,"deepAK8"+suff,deepAK8)
        ak8floats.extend([
            'deepAK8'+suff+':tDiscriminatorDeep',
            'deepAK8'+suff+':wDiscriminatorDeep',
            'deepAK8'+suff+':zDiscriminatorDeep',
            'deepAK8'+suff+':hDiscriminatorDeep'
        ])
        deepAK8decorrel = DeepAK8DecorrelProducer.clone(
            JetAK8 = GoodJetsTag
        )
        setattr(process,"deepAK8decorrel"+suff,deepAK8decorrel)
        ak8floats.extend([
            'deepAK8decorrel'+suff+':tDiscriminatorDeep',
            'deepAK8decorrel'+suff+':wDiscriminatorDeep',
            'deepAK8decorrel'+suff+':zDiscriminatorDeep',
            'deepAK8decorrel'+suff+':hDiscriminatorDeep'
        ])

    # get more substructure
    if self.semivisible and storeProperties>1:
        from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness
        NjettinessBeta1 = Njettiness.clone(
            src = GoodJetsTag,
            cone = cms.double(0.8),
            storeAxes = cms.bool(True),
            Njets = cms.vuint32(1),
            beta = cms.double(1.0)
        )
        setattr(process,"NjettinessBeta1"+suff,NjettinessBeta1)
        NjettinessBeta2 = NjettinessBeta1.clone(
            beta = cms.double(2.0)
        )
        setattr(process,"NjettinessBeta2"+suff,NjettinessBeta2)
        BasicSubstructure = cms.EDProducer("BasicSubstructureProducer",
            JetTag = GoodJetsTag
        )
        setattr(process,"BasicSubstructure"+suff,BasicSubstructure)
        QGTagger = process.QGTagger.clone(
            srcJets = GoodJetsTag
        )
        setattr(process,"QGTagger"+suff,QGTagger)
        ak8floats.extend([
            'BasicSubstructure'+suff+':overflow',
            'BasicSubstructure'+suff+':girth',
            'BasicSubstructure'+suff+':momenthalf',
            'BasicSubstructure'+suff+':ptdrlog',
            'NjettinessBeta1'+suff+':tau1etaAxis1',
            'NjettinessBeta1'+suff+':tau1phiAxis1',
            'NjettinessBeta2'+suff+':tau1etaAxis1',
            'NjettinessBeta2'+suff+':tau1phiAxis1',
            'QGTagger'+suff+':ptD',
            'QGTagger'+suff+':axis1',
            'QGTagger'+suff+':axis2',
        ])
        ak8ints.extend([
            'QGTagger'+suff+':mult',
        ])

    # add discriminator and update tag
    if len(ak8floats)>0 or len(ak8ints)>0 or len(ak8tags)>0:
        process, GoodJetsTag = addJetInfo(process, GoodJetsTag, ak8floats, ak8ints, ak8tags)

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
                "prunedMass"            ,
                "softDropMass"          ,
                "NsubjettinessTau1"     ,
                "NsubjettinessTau2"     ,
                "NsubjettinessTau3"     ,
                "ecfN2b1"               ,
                "ecfN2b2"               ,
                "ecfN3b1"               ,
                "ecfN3b2"               ,
                "bDiscriminatorCSV"     ,
                "bJetTagDeepCSVprobb"   ,
                "bJetTagDeepCSVprobc"   ,
                "bJetTagDeepCSVprobudsg",
                "bJetTagDeepCSVprobbb"  ,
                "NumBhadrons"           ,
                "NumChadrons"           ,
                "subjets"               ,
                "SJbDiscriminatorCSV"   ,
            )
        )
        # specify userfloats
        JetPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass')
        JetPropertiesAK8.softDropMass = cms.vstring('SoftDropPuppi') # computed from subjets
        JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi:tau1')
        JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi:tau2')
        JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi:tau3')
        JetPropertiesAK8.ecfN2b1 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2')
        JetPropertiesAK8.ecfN2b2 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN2')
        JetPropertiesAK8.ecfN3b1 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3')
        JetPropertiesAK8.ecfN3b2 = cms.vstring('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN3')
        JetPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
        JetPropertiesAK8.subjets = cms.vstring('SoftDropPuppi')
        JetPropertiesAK8.SJbDiscriminatorCSV = cms.vstring('SoftDropPuppi','pfCombinedInclusiveSecondaryVertexV2BJetTags')
        self.VectorDouble.extend([
            'JetProperties'+suff+':prunedMass(Jets'+suff+'_prunedMass)',
            'JetProperties'+suff+':softDropMass(Jets'+suff+'_softDropMass)',
            'JetProperties'+suff+':bDiscriminatorCSV(Jets'+suff+'_doubleBDiscriminator)',
            'JetProperties'+suff+':NsubjettinessTau1(Jets'+suff+'_NsubjettinessTau1)',
            'JetProperties'+suff+':NsubjettinessTau2(Jets'+suff+'_NsubjettinessTau2)',
            'JetProperties'+suff+':NsubjettinessTau3(Jets'+suff+'_NsubjettinessTau3)',
            'JetProperties'+suff+':ecfN2b1(Jets'+suff+'_ecfN2b1)',
            'JetProperties'+suff+':ecfN2b2(Jets'+suff+'_ecfN2b2)',
            'JetProperties'+suff+':ecfN3b1(Jets'+suff+'_ecfN3b1)',
            'JetProperties'+suff+':ecfN3b2(Jets'+suff+'_ecfN3b2)',
        ])
        self.VectorInt.extend([
            'JetProperties'+suff+':NumBhadrons(Jets'+suff+'_NumBhadrons)',
            'JetProperties'+suff+':NumChadrons(Jets'+suff+'_NumChadrons)'
        ])
        self.VectorVectorTLorentzVector.extend([
            'JetProperties'+suff+':subjets(Jets'+suff+'_subjets)',
        ])
        self.VectorVectorDouble.extend([
            'JetProperties'+suff+':SJbDiscriminatorCSV(Jets'+suff+'_subjets_bDiscriminatorCSV)',
        ])

        if self.deepAK8 and doDeepAK8:
            JetPropertiesAK8.properties.extend([
                "tDiscriminatorDeep",
                "wDiscriminatorDeep",
                "zDiscriminatorDeep",
                "hDiscriminatorDeep",
                "tDiscriminatorDeepDecorrel",
                "wDiscriminatorDeepDecorrel",
                "zDiscriminatorDeepDecorrel",
                "hDiscriminatorDeepDecorrel",
            ])
            JetPropertiesAK8.tDiscriminatorDeep = cms.vstring('deepAK8'+suff+':tDiscriminatorDeep')
            JetPropertiesAK8.wDiscriminatorDeep = cms.vstring('deepAK8'+suff+':wDiscriminatorDeep')
            JetPropertiesAK8.zDiscriminatorDeep = cms.vstring('deepAK8'+suff+':zDiscriminatorDeep')
            JetPropertiesAK8.hDiscriminatorDeep = cms.vstring('deepAK8'+suff+':hDiscriminatorDeep')
            JetPropertiesAK8.tDiscriminatorDeepDecorrel = cms.vstring('deepAK8decorrel'+suff+':tDiscriminatorDeep')
            JetPropertiesAK8.wDiscriminatorDeepDecorrel = cms.vstring('deepAK8decorrel'+suff+':wDiscriminatorDeep')
            JetPropertiesAK8.zDiscriminatorDeepDecorrel = cms.vstring('deepAK8decorrel'+suff+':zDiscriminatorDeep')
            JetPropertiesAK8.hDiscriminatorDeepDecorrel = cms.vstring('deepAK8decorrel'+suff+':hDiscriminatorDeep')
            self.VectorDouble.extend([
                'JetProperties'+suff+':tDiscriminatorDeep(Jets'+suff+'_tDiscriminatorDeep)',
                'JetProperties'+suff+':wDiscriminatorDeep(Jets'+suff+'_wDiscriminatorDeep)',
                'JetProperties'+suff+':zDiscriminatorDeep(Jets'+suff+'_zDiscriminatorDeep)',
                'JetProperties'+suff+':hDiscriminatorDeep(Jets'+suff+'_hDiscriminatorDeep)',
                'JetProperties'+suff+':tDiscriminatorDeepDecorrel(Jets'+suff+'_tDiscriminatorDeepDecorrel)',
                'JetProperties'+suff+':wDiscriminatorDeepDecorrel(Jets'+suff+'_wDiscriminatorDeepDecorrel)',
                'JetProperties'+suff+':zDiscriminatorDeepDecorrel(Jets'+suff+'_zDiscriminatorDeepDecorrel)',
                'JetProperties'+suff+':hDiscriminatorDeepDecorrel(Jets'+suff+'_hDiscriminatorDeepDecorrel)',
            ])

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
            # extra stuff for subjets
            JetPropertiesAK8.properties.extend(["SJptD", "SJaxismajor", "SJaxisminor", "SJmultiplicity"])
            JetPropertiesAK8.SJptD = cms.vstring('SoftDropPuppiUpdated','QGTaggerSubjets:ptD')
            JetPropertiesAK8.SJaxismajor = cms.vstring('SoftDropPuppiUpdated','QGTaggerSubjets:axis1')
            JetPropertiesAK8.SJaxisminor = cms.vstring('SoftDropPuppiUpdated','QGTaggerSubjets:axis2')
            JetPropertiesAK8.SJmultiplicity = cms.vstring('SoftDropPuppiUpdated','QGTaggerSubjets:mult')
            self.VectorVectorDouble.extend([
                'JetProperties'+suff+':SJptD(Jets'+suff+'_subjets_ptD)',
                'JetProperties'+suff+':SJaxismajor(Jets'+suff+'_subjets_axismajor)',
                'JetProperties'+suff+':SJaxisminor(Jets'+suff+'_subjets_axisminor)',
            ])
            self.VectorVectorInt.extend([
                'JetProperties'+suff+':SJmultiplicity(Jets'+suff+'_subjets_multiplicity)',
            ])

        if self.semivisible and storeProperties>1:
            JetPropertiesAK8.properties.extend([
                'overflow',
                'girth',
                'momenthalf',
                'ptD',
                'axismajor',
                'axisminor',
                'multiplicity',
                'ptdrlog',
                'lean',
            ])
            JetPropertiesAK8.overflow = cms.vstring('BasicSubstructure'+suff+':overflow')
            JetPropertiesAK8.girth = cms.vstring('BasicSubstructure'+suff+':girth')
            JetPropertiesAK8.momenthalf = cms.vstring('BasicSubstructure'+suff+':momenthalf')
            JetPropertiesAK8.ptD = cms.vstring('QGTagger'+suff+':ptD')
            JetPropertiesAK8.axismajor = cms.vstring('QGTagger'+suff+':axis1')
            JetPropertiesAK8.axisminor = cms.vstring('QGTagger'+suff+':axis2')
            JetPropertiesAK8.multiplicity = cms.vstring('QGTagger'+suff+':mult')
            JetPropertiesAK8.ptdrlog = cms.vstring('BasicSubstructure'+suff+':ptdrlog')
            JetPropertiesAK8.lean = cms.vstring(
                'NjettinessBeta1'+suff+':tau1etaAxis1',
                'NjettinessBeta1'+suff+':tau1phiAxis1',
                'NjettinessBeta2'+suff+':tau1etaAxis1',
                'NjettinessBeta2'+suff+':tau1phiAxis1',
            )
            self.VectorDouble.extend([
                'JetProperties'+suff+':overflow(Jets'+suff+'_overflow)',
                'JetProperties'+suff+':girth(Jets'+suff+'_girth)',
                'JetProperties'+suff+':momenthalf(Jets'+suff+'_momenthalf)',
                'JetProperties'+suff+':ptD(Jets'+suff+'_ptD)',
                'JetProperties'+suff+':axismajor(Jets'+suff+'_axismajor)',
                'JetProperties'+suff+':axisminor(Jets'+suff+'_axisminor)',
                'JetProperties'+suff+':ptdrlog(Jets'+suff+'_ptdrlog)',
                'JetProperties'+suff+':lean(Jets'+suff+'_lean)',
            ])
            self.VectorInt.extend([
                'JetProperties'+suff+':multiplicity(Jets'+suff+'_multiplicity)',
            ])

            if storeProperties>2:
                JetPropertiesAK8.properties.extend(['constituents'])
                self.VectorVectorTLorentzVector.extend([
                    'JetProperties'+suff+':constituents(Jets'+suff+'_constituents)',
                ])
        setattr(process,"JetProperties"+suff,JetPropertiesAK8)

    return process        

