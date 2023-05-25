# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os,re
from itertools import chain

def transformJetSeq(self, process, baseModule, transformModules, jetType):
    transformProperties = [
        "jetCollInstanceName","jetPtMin","useMassDropTagger","useFiltering","useDynamicFiltering","useTrimming","usePruning",
        "useCMSBoostedTauSeedingAlgorithm","useKtPruning","useConstituentSubtraction","useSoftDrop","correctShape","muCut",
        "yCut","rFilt","rFiltFactor","trimPtFracMin","zcut","rcut_factor","csRho_EtaMax","csRParam","beta","R0","gridMaxRapidity",
        "gridSpacing","subjetPtMin","muMin","muMax","yMin","yMax","dRMin","dRMax","maxDepth","nFilt",
    ]

    transformPSets = []
    for transformName,transformModule in transformModules.iteritems():
        transform = getattr(process, transformModule)
        transformPSets.append(cms.PSet(
            **{p:getattr(transform, p) for p in transformProperties if hasattr(transform,p)}
        ))
        transformPSets[-1].name = cms.string(transformName)
        collName = getattr(transformPSets[-1],transformProperties[0],cms.string("")).value()
        delattr(process, transformModule)
        setattr(process, transformModule, cms.EDAlias(
                **{baseModule: cms.VPSet(
                    cms.PSet(type = cms.string("recoBasicJets"), fromProductInstance = cms.string(transformName), toProductInstance = cms.string("")),
                    cms.PSet(type = cms.string(jetType), fromProductInstance = cms.string(transformName+collName), toProductInstance = cms.string(collName)),
                )}
            )
        )

    base = getattr(process, baseModule)
    # skip the first two that are also used in base clustering
    for p in transformProperties[2:]:
        if hasattr(base,p): delattr(base,p)
    base.doBaseClustering = cms.bool(True)
    base.jetTransforms = cms.VPSet(transformPSets)
    # has to be done here because area definition happens in VirtualJetProducer constructor before FastjetJetProducer constructor
    if len(transformPSets)>0: base.useExplicitGhosts = cms.bool(True)

    setattr(process, baseModule, base)

    return process

def makeTreeFromMiniAOD(self,process):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
    from TreeMaker.TreeMaker.TMEras import TMeras
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(self.numevents)
    )
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(self.readFiles),
    )
    if len(self.jsonfile)>0: process.source.lumisToProcess = LumiList.LumiList(filename = self.jsonfile).getVLuminosityBlockRange()

    # output file
    process.TFileService = cms.Service("TFileService",
        fileName = cms.string(self.outfile+".root"),
        closeFileFast = cms.untracked.bool(True),
    )

    # configure treemaker
    from TreeMaker.TreeMaker.treeMaker import TreeMaker
    process.TreeMaker2 = TreeMaker.clone(
        TreeName                       = cms.string(self.treename),
        VectorRecoCand                 = self.VectorRecoCand,
        VarsXYZVector                  = self.VarsXYZVector,
        VarsXYZPoint                   = self.VarsXYZPoint,
        VarsDouble                     = self.VarsDouble,
        VarsInt                        = self.VarsInt,
        VarsBool                       = self.VarsBool,
        VectorLorentzVector            = self.VectorLorentzVector,
        VectorXYZVector                = self.VectorXYZVector,
        VectorXYZPoint                 = self.VectorXYZPoint,
        VectorFloat                    = self.VectorFloat,
        VectorDouble                   = self.VectorDouble,
        VectorInt                      = self.VectorInt,
        VectorString                   = self.VectorString,
        VectorBool                     = self.VectorBool,
        VectorVectorBool               = self.VectorVectorBool,
        VectorVectorInt                = self.VectorVectorInt,
        VectorVectorDouble             = self.VectorVectorDouble,
        VectorVectorString             = self.VectorVectorString,
        VectorVectorLorentzVector      = self.VectorVectorLorentzVector,
        VectorVectorXYZVector          = self.VectorVectorXYZVector,
        VectorVectorXYZPoint           = self.VectorVectorXYZVector,
        AssocVectorVectorBool          = self.AssocVectorVectorBool,
        AssocVectorVectorInt           = self.AssocVectorVectorInt,
        AssocVectorVectorDouble        = self.AssocVectorVectorDouble,
        AssocVectorVectorString        = self.AssocVectorVectorString,
        AssocVectorVectorLorentzVector = self.AssocVectorVectorLorentzVector,
        AssocVectorVectorXYZVector     = self.AssocVectorVectorXYZVector,
        AssocVectorVectorXYZPoint      = self.AssocVectorVectorXYZVector,
        TitleMap                       = self.TitleMap,
        nestedVectors                  = self.nestedVectors,
        storeOffsets                   = self.storeOffsets,
        splitLevel                     = self.splitLevel,
        saveFloat                      = self.saveFloat,
    )

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Standard producers
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## SUSY scan info
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        # parameters from signal scans (e.g. mother and LSP masses for SUSY SMS)
        # branches always added, but only have values for scan samples
        # needed for WeightProducer
        from TreeMaker.Utils.signalscan_cfi import SignalScanProducer
        process.SignalScan = SignalScanProducer.clone(
            debug = cms.bool(False),
            isLHE = cms.bool(False)
        )
        self.VectorDouble.extend(['SignalScan:SignalParameters'])
        # set scan type ("None" by default, producer does nothing)
        if self.signal:
            if "PMSSM" in self.sample: process.SignalScan.signalType = "pMSSM"
            elif self.fastsim: process.SignalScan.signalType = "SUSY"
            elif "SVJ" in self.sample and "Scan" in self.sample: process.SignalScan.signalType = "SVJ"
            elif self.scan: process.SignalScan.signalType = "SUSY"

    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],process.SignalScan.signalType!="None")
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string(self.pufile)
        process.WeightProducer.SampleName = cms.string(self.sample)
        self.VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        self.VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo and self.doPDFs:
        # use new code from https://github.com/cms-sw/cmssw/pull/32167 to parse & organize weights
        from GeneratorInterface.Core.genWeights_cfi import genWeights
        from GeneratorInterface.Core.lheWeights_cfi import lheWeights
        process.lheWeights = lheWeights.clone(
            failIfInvalidXML = False
        )
        process.genWeights = genWeights.clone(
            allowUnassociatedWeights = True
        )

        from TreeMaker.Utils.pdfweightproducer_cfi import PDFWeightProducer
        process.PDFWeights = PDFWeightProducer.clone()
        from TreeMaker.Utils.pdfrecalculator_cfi import PDFRecalculator
        process.PDFRecalculator = PDFRecalculator.clone(
            recalculatePDFs = cms.bool(self.signal),
            recalculateScales = cms.bool(False),
            pdfSetName = cms.string("NNPDF31_nnlo_as_0118_mc_hessian_pdfas"),
        )
        if "madgraph" in self.sample.lower():
            process.PDFRecalculator.recalculateScales = False
            process.PDFRecalculator.recalculatePDFs = False
        elif "SVJ" in self.sample: # skip trying to get scale and PDF weights for SVJ signals
            process.PDFWeights.storeScales = False
            process.PDFWeights.storePDFs = False
            process.PDFRecalculator.nEM = 2
            process.PDFRecalculator.recalculateScales = True
        elif "EMJ" in self.sample: # skip trying to get scale and PDF weights for EMJ signals
            process.PDFWeights.storeScales = False
            process.PDFWeights.storePDFs = False
            process.PDFRecalculator.nQCD = 2
            process.PDFRecalculator.nEM = 0
            process.PDFRecalculator.recalculateScales = True
        # want to recalculate PDFs for these even though madgraph
        if any(s in self.sample for s in ["RPV", "SYY", "SHH"]):
            process.PDFWeights.storePDFs = False
            process.PDFRecalculator.recalculatePDFs = True

        # handle different sources for weight outputs
        if process.PDFRecalculator.recalculatePDFs:
            self.VectorFloat.extend(['PDFRecalculator:PDFweights'])
        else:
            self.VectorFloat.extend(['PDFWeights:PDFweights'])
        if process.PDFRecalculator.recalculateScales:
            self.VectorFloat.extend(['PDFRecalculator:ScaleWeights'])
        else:
            self.VectorFloat.extend(['PDFWeights:ScaleWeights'])
        self.VectorFloat.extend(['PDFWeights:PSweights'])

    ## ----------------------------------------------------------------------------------------------
    ## GenHT for stitching together MC samples
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        process.MadHT = cms.EDProducer('GenHTProducer')
        # called madHT, i.e. MadGraph, to distinguish from GenHT from GenJets
        self.VarsDouble.extend(['MadHT:genHT(madHT)'])

    ## ----------------------------------------------------------------------------------------------
    ## PrimaryVertices
    ## ----------------------------------------------------------------------------------------------
    process.goodVertices = cms.EDFilter("VertexSelector",
        src = cms.InputTag("offlineSlimmedPrimaryVertices"),
        cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
        filter = cms.bool(False)
    )
    from TreeMaker.Utils.primaryvertices_cfi import primaryvertices
    process.primaryVertices = primaryvertices.clone(
        VertexCollection     = cms.InputTag('offlineSlimmedPrimaryVertices'),
        GoodVertexCollection = cms.InputTag('goodVertices'),
        saveVertices         = cms.bool(self.emerging),
    )
    self.VarsInt.extend(['primaryVertices:NVtx(NVtx)','primaryVertices:nAllVertices(nAllVertices)'])
    # also store rho for PU comparisons
    self.VarsDouble.extend(['fixedGridRhoFastjetAll'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        if self.saveMinimalGenParticles:
            process.genParticles = cms.EDProducer("GenParticlesProducer",
                genCollection = cms.InputTag("prunedGenParticles"),
                debug = cms.bool(False),
                # Particles we want to save from the decay chain of the tops
                childIds = cms.vint32(1,2,3,4,5,11,12,13,14,15,16,24),
                # Particles we want to save the last copy from the hard scatter
                parentIds = cms.vint32(
                    6,22,23,24,25,
                    1000021,1000022,1000023,1000024,1000025,1000035,1000037,1000039,
                    1000001,1000002,1000003,1000004,1000005,1000006,
                    2000001,2000002,2000003,2000004,2000005,2000006,
                    4900001,4900002,4900003,4900004,4900005,4900006,
                    4900021,4900023,4900101,4900102,4900103,4900111,4900113,4900211,4900213,51,52,53,
                    5000001,5000002,
                ),
                # Other settings
                keepIds = cms.vint32(),
                keepFirst = cms.bool(False),
                keepMinimal = cms.bool(True),
                saveVtx = cms.bool(self.emerging),
            )
        else:
            process.genParticles = cms.EDProducer("GenParticlesProducer",
                genCollection = cms.InputTag("prunedGenParticles"),
                debug = cms.bool(False),
                childIds = cms.vint32(1,2,3,4,5,11,12,13,14,15,16,22),
                parentIds = cms.vint32(
                    1,2,6,23,24,25,
                    1000021,1000022,1000023,1000024,1000025,1000035,1000037,1000039,
                    1000001,1000002,1000003,1000004,1000005,1000006,
                    2000001,2000002,2000003,2000004,2000005,2000006,
                    4900001,4900002,4900003,4900004,4900005,4900006,
                    4900021,4900023,4900101,4900102,4900103,4900111,4900113,4900211,4900213,51,52,53,
                    5000001,5000002,
                ),
                keepIds = cms.vint32(6,23,24,25),
                keepFirst = cms.bool(True),
                keepMinimal = cms.bool(False),
                saveVtx = cms.bool(self.emerging),
            )
            # store gluons for signals with Higgs
            if "T5qqqqZH" in process.source.fileNames[0]: process.genParticles.childIds.append(21)
        self.VectorLorentzVector.append("genParticles(GenParticles)")
        self.VectorInt.append("genParticles:Charge(GenParticles_Charge)")
        self.VectorInt.append("genParticles:PdgId(GenParticles_PdgId)")
        self.VectorInt.append("genParticles:Status(GenParticles_Status)")
        self.VectorInt.append("genParticles:Parent(GenParticles_ParentIdx)")
        self.VectorInt.append("genParticles:ParentId(GenParticles_ParentId)")
        if not self.saveMinimalGenParticles:
            self.VectorBool.append("genParticles:TTFlag(GenParticles_TTFlag)")
        if self.emerging:
            self.VectorInt.append("genParticles:VtxIdx(GenParticles_vertexIdx)")
            self.VectorXYZPoint.append("genParticles:GenVtx(GenVertices)")
        
        if self.saveGenTops:
            # for ttbar pT reweighting
            # params from: https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting#Run_2_strategy
            process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
            process.initSubset.src = cms.InputTag("prunedGenParticles")
            process.decaySubset.src = cms.InputTag("prunedGenParticles")
            process.decaySubset.runMode = cms.string("Run2")
            process.genTops = cms.EDProducer("GenTopProducer",
                genEvent = cms.InputTag("genEvt"),
                a = cms.double(0.0615),
                b = cms.double(-0.0005)
            )
            self.VectorRecoCand.append("genTops(GenTops)")
            self.VarsDouble.append("genTops:weight(GenTopWeight)")

    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------

    # default miniAOD tags
    JetTag = cms.InputTag("slimmedJets")
    METTag = cms.InputTag('slimmedMETs')
    # get rid of the pointless low-pt AK8 jets ASAP
    # also get rid of jets w/ inf constituents (CutParser doesn't support isinf or bitwise operations, so use this hack)
    process.slimmedJetsAK8Good = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("slimmedJetsAK8"),
        cut = cms.string("isPFJet && abs(daughter(0).energy)!=exp(1000)"),
    )
    JetAK8Tag = cms.InputTag('slimmedJetsAK8Good')
    process.slimmedJetsAK8Inf = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("slimmedJetsAK8"),
        cut = cms.string("isPFJet && abs(daughter(0).energy)==exp(1000)"),
    )
    JetAK8TagInf = cms.InputTag('slimmedJetsAK8Inf')
    SubjetTag = cms.InputTag('slimmedJetsAK8PFPuppiSoftDropPacked:SubJets')
    SubjetName = cms.string("SoftDropPuppi")
    GenJetAK8Tag = cms.InputTag('slimmedGenJetsAK8')
    GenParticlesForJetTag = cms.InputTag("packedGenParticlesForJetsNoNu")

    process.load("CondCore.CondDB.CondDB_cfi")

    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    if len(self.jecfile)>0:
        #get name of JECs without any directories
        JECera = self.jecfile.split('/')[-1]
        process.CondDB.connect = cms.string('sqlite_file:'+self.jecfile+'.db')

        process.jec = cms.ESSource("PoolDBESSource",process.CondDB,
            toGet   = cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PFchs"),
                    label  = cms.untracked.string("AK4PFchs")
                ),
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PFPuppi"),
                    label  = cms.untracked.string("AK4PFPuppi")
                ),
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK8PFPuppi"),
                    label  = cms.untracked.string("AK8PFPuppi")
                ),
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")

        levels  = ['L1FastJet','L2Relative','L3Absolute']
        if self.residual: levels.append('L2L3Residual')
        
        from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

        # rerun DeepCSV on AK4 jets for 2016 80X MC
        ak4updates = cms.PSet(discrs = cms.vstring())

        updateJetCollection(
            process,
            jetSource = JetTag,
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK4PFchs', levels, 'None'),
            btagDiscriminators = ak4updates.discrs.value() if len(ak4updates.discrs.value())>0 else ['None'],
            printWarning = bool(self.verbose),
        )

        JetTag = cms.InputTag('updatedPatJetsUpdatedJEC' if len(ak4updates.discrs.value())==0 else 'updatedPatJetsTransientCorrectedUpdatedJEC')

        # select double b-tagger
        ak8updates = []
        ak8updates.append("pfBoostedDoubleSecondaryVertexAK8BJetTags")

        if self.deepAK8:
            DeepAK8Tags = ["ZvsQCD","ZbbvsQCD","TvsQCD","WvsQCD","HbbvsQCD"]
            DeepAK8TagsDecorrel = ["ZvsQCD","ZbbvsQCD","bbvsLight","TvsQCD","WvsQCD","HbbvsQCD","ZHbbvsQCD"]
            ak8updates.extend(["pfDeepBoostedDiscriminatorsJetTags:"+x for x in DeepAK8Tags])
            ak8updates.extend(["pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:"+x for x in DeepAK8TagsDecorrel])

        if self.deepDoubleB:
            ak8updates.extend(['pfMassIndependentDeepDoubleBvLJetTags:probHbb'])

        if self.tchannel:
            # recluster AK8 jets to remove pT cut
            # this also produces a reclustered AK8 GenJet collection w/ no pT cut
            from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
            jetToolbox(process,
                'ak8',
                'jetSequence',
                'noOutput',
                PUMethod = 'Puppi',
                useExistingWeights=True,
                dataTier='miniAOD',
                runOnMC = self.geninfo,
                Cut = 'pt>10.',
                postFix = 'LowCut',
                addPruning = False,
                addSoftDropSubjets = True,
                addNsub = True,
                maxTau = 4,
                bTagDiscriminators = None, # can't use ak8updates here because "pfDeepBoostedJetTagInfos only supports running via updateJetCollection"
                subjetBTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
                JETCorrLevels = levels,
                subJETCorrLevels = levels,
                addEnergyCorrFunc = True,
                ecfBeta = [1.0,2.0],
                verbosity = 2 if self.verbose else 0,
            )

            # todo: revamp jet toolbox to handle this
            if self.geninfo and not self.doZinv: # calling jet toolbox again for ak8 would break after this, so skip it
                process = self.transformJetSeq(process, "ak8GenJetsNoNu", {"SoftDrop":"ak8GenJetsNoNuSoftDrop"}, "recoGenJets")
            process.ak8PFJetsPuppiLowCutSoftDrop.jetPtMin = cms.double(10) # to match central clustering
            process = self.transformJetSeq(process, "ak8PFJetsPuppiLowCut", {"SoftDrop":"ak8PFJetsPuppiLowCutSoftDrop"}, "recoPFJets")

            JetAK8Tag = cms.InputTag("packedPatJetsAK8PFPuppiLowCutSoftDrop")
            SubjetTag = cms.InputTag("selectedPatJetsAK8PFPuppiLowCutSoftDropPacked:SubJets")
            SubjetName = cms.string("SoftDrop")
            GenJetAK8Tag = cms.InputTag("ak8GenJetsNoNu")

        # update the corrections for AK8 jets
        # and add any extra discriminators
        updateJetCollection(
            process,
            jetSource = JetAK8Tag,
            labelName = 'AK8',
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK8PFPuppi', levels, 'None'),
            pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
            svSource = cms.InputTag('slimmedSecondaryVertices'),
            rParam = 0.8,
            btagDiscriminators = ak8updates if len(ak8updates)>0 else ['None'],
            printWarning = bool(self.verbose),
        )

        # remove (or reduce) pt cut to avoid default values for some jets
        if self.deepAK8:
            process.pfDeepBoostedJetTagInfosAK8UpdatedJEC.min_jet_pt = cms.double(150 if self.tchannel else 0)

        JetAK8Tag = cms.InputTag('updatedPatJetsTransientCorrectedAK8UpdatedJEC')
 
        # update the corrections for the subjets from the AK8 jets
        # the references from the AK8 jets to the subjets will be fixed later on
        updateJetCollection(
            process,
            jetSource = SubjetTag,
            labelName = 'slimmedJetsAK8PFPuppiSoftDropPackedSubJets',
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK4PFPuppi', levels, 'None'),
            pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
            svSource = cms.InputTag('slimmedSecondaryVertices'),
            rParam = 0.4,
            btagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
            printWarning = bool(self.verbose),
        )

        SubjetTag = cms.InputTag('updatedPatJetsTransientCorrectedSlimmedJetsAK8PFPuppiSoftDropPackedSubJetsUpdatedJEC')
       
        # update the MET to account for the new JECs
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not self.geninfo, # controls gen met
            jetCollUnskimmed=JetTag,
            reapplyJEC=False,
        )
        METTag = cms.InputTag('slimmedMETs','',process.name_())

    # keep jets before any further modifications for hadtau
    JetTagBeforeSmearing = JetTag

    ## ----------------------------------------------------------------------------------------------
    ## IsoTracks
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(11),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )

    process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(13),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )

    process.IsolatedPionTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(10.0),
        isoCut              = cms.double(0.1),
        pdgId               = cms.int32(211),
        mTCut               = cms.double(100.),
        METTag              = METTag,
    )

    self.VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    self.VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    self.VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

    if self.debugtracks:
        # NB: this increases the runtime and size of ntuples by ~10x
        # do not turn on unless you really want to save all the isotrack quantities!!!
        # just store the full set of isotrack quantities once
        process.IsolatedPionTracksVeto.debug = cms.bool(True)
        self.VectorLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(PFCands)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(PFCands_trkiso)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandspfreliso03chg(PFCands_pfRelIso03chg)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandspfreliso03all(PFCands_pfRelIso03all)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(PFCands_dzpv)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdxypv(PFCands_dxypv)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(PFCands_mT)'])
        self.VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(PFCands_charge)'])
        self.VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(PFCands_id)'])

    ## ----------------------------------------------------------------------------------------------
    ## Electrons/Muons
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.leptonproducer_cfi import leptonproducer
    process.LeptonsNew = leptonproducer.clone(
        elecIsoValue       = cms.double(0.1), # only has an effect when used with miniIsolation
        UseMiniIsolation   = cms.bool(True),
        METTag             = METTag,
        rhoCollection      = cms.InputTag("fixedGridRhoFastjetAll")
    )
    self.VectorRecoCand.extend(['LeptonsNew:IdMuon(Muons)','LeptonsNew:IdElectron(Electrons)'])
    self.VectorInt.extend(['LeptonsNew:IdMuonCharge(Muons_charge)','LeptonsNew:IdElectronCharge(Electrons_charge)'])
    self.VectorBool.extend(['LeptonsNew:IdMuonPassIso(Muons_passIso)','LeptonsNew:IdElectronPassIso(Electrons_passIso)'])
    self.VarsInt.extend(['LeptonsNew:IdIsoMuonNum(NMuons)','LeptonsNew:IdIsoElectronNum(NElectrons)'])

    ## ----------------------------------------------------------------------------------------------
    ## MET Filters
    ## ----------------------------------------------------------------------------------------------

    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree

    if not self.fastsim: # MET filters are not run for fastsim samples

        from TreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer

        process.PrimaryVertexFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_goodVertices"),
        )
        self.VarsInt.extend(['PrimaryVertexFilter'])

        process.CSCTightHaloFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_CSCTightHalo2015Filter"),
        )
        self.VarsInt.extend(['CSCTightHaloFilter'])

        process.globalTightHalo2016Filter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_globalTightHalo2016Filter"),
        )
        self.VarsInt.extend(['globalTightHalo2016Filter'])

        process.globalSuperTightHalo2016Filter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_globalSuperTightHalo2016Filter"),
        )
        self.VarsInt.extend(['globalSuperTightHalo2016Filter'])

        process.HBHENoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_HBHENoiseFilter"),
        )
        self.VarsInt.extend(['HBHENoiseFilter'])

        process.HBHEIsoNoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_HBHENoiseIsoFilter"),
        )
        self.VarsInt.extend(['HBHEIsoNoiseFilter'])

        process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
        self.VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])

        process.EcalDeadCellBoundaryEnergyFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(self.tagname),
            filterName  = cms.string("Flag_EcalDeadCellBoundaryEnergyFilter"),
        )
        self.VarsInt.extend(['EcalDeadCellBoundaryEnergyFilter'])

        process.eeBadScFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(self.tagname),
            filterName  =   cms.string("Flag_eeBadScFilter"),
        )
        self.VarsInt.extend(['eeBadScFilter'])

        process.ecalBadCalibFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(self.tagname),
            filterName  =   cms.string("Flag_ecalBadCalibFilter"),
        )
        self.VarsInt.extend(['ecalBadCalibFilter'])

        process.hfNoisyHitsFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(self.tagname),
            filterName  =   cms.string("Flag_hfNoisyHitsFilter"),
        )
        self.VarsInt.extend(['hfNoisyHitsFilter'])

        process.BadChargedCandidateFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(self.tagname),
            filterName  =   cms.string("Flag_BadChargedCandidateFilter"),
        )
        self.VarsInt.extend(['BadChargedCandidateFilter'])

        process.BadPFMuonFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(self.tagname),
            filterName  =   cms.string("Flag_BadPFMuonFilter"),
        )
        self.VarsInt.extend(['BadPFMuonFilter'])

        # https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2#Recipe_for_BadPFMuonDz_filter_in
        # Not in MiniAODv1 but in MiniAODv2, so cannot rely on getting from TriggerResults
        process.load('RecoMET.METFilters.BadPFMuonDzFilter_cfi')
        process.BadPFMuonDzFilter.vtx = cms.InputTag("offlineSlimmedPrimaryVertices")
        process.BadPFMuonDzFilter.muons = cms.InputTag("slimmedMuons")
        process.BadPFMuonDzFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadPFMuonDzFilter.taggingMode = True
        process.BadPFMuonDzFilter.minDzBestTrack = cms.double(0.5)
        self.VarsBool.extend(['BadPFMuonDzFilter'])

    ## ----------------------------------------------------------------------------------------------
    ## Triggers
    ## ----------------------------------------------------------------------------------------------

    # The trigger results are saved to the tree as a vector
    # Four vectors are saved:
    # 1) names of the triggers
    # 2) trigger results
    # 3) trigger prescales
    # 4) trigger versions
    # the indexing of these vectors must match
    # If the version number of the input trigger name is omitted,
    # any matching trigger will be included (default behavior)

    from TreeMaker.Utils.triggerproducer_cfi import triggerProducer
    from TreeMaker.TreeMaker.triggerNameList import triggerNameList as _triggerNameList
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string(self.hlttagname),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        saveHLTObj = cms.bool(False),
        triggerNameList = _triggerNameList
    )
    _joinedTriggerNameList = ','.join(_triggerNameList)
    _TriggerBranchesList = ['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales','TriggerProducer:TriggerVersion']
    self.VectorInt.extend(_TriggerBranchesList)
    self.TitleMap.extend(list(chain.from_iterable([[x,_joinedTriggerNameList] for x in _TriggerBranchesList])))

    if "SingleElectron" in process.source.fileNames[0] or "EGamma" in process.source.fileNames[0]:
        process.TriggerProducer.saveHLTObj = cms.bool(True)
        process.TriggerProducer.saveHLTObjPath = cms.string("HLT_Ele27_WPTight_Gsf_v")
        process.TriggerProducer.saveHLTObjName = cms.string("HLTElectronObjects")
        self.VectorLorentzVector.extend(['TriggerProducer:HLTElectronObjects'])
    elif "SingleMuon" in process.source.fileNames[0]:
        process.TriggerProducer.saveHLTObj = cms.bool(True)
        process.TriggerProducer.saveHLTObjPath = cms.string("HLT_Mu50_v")
        process.TriggerProducer.saveHLTObjName = cms.string("HLTMuonObjects")
        self.VectorLorentzVector.extend(['TriggerProducer:HLTMuonObjects'])

    if not self.geninfo:
        from TreeMaker.Utils.prescaleweightproducer_cfi import prescaleweightProducer
        process.PrescaleWeightProducer = prescaleweightProducer.clone()
        process.PrescaleWeightProducer.bits.setProcessName(self.hlttagname)
        self.VarsDouble.extend(['PrescaleWeightProducer:weight(PrescaleWeightHT)'])
        self.VarsDouble.extend(['PrescaleWeightProducer:ht(HTOnline)'])
        self.VarsDouble.extend(['PrescaleWeightProducer:mht(MHTOnline)'])


    ## ----------------------------------------------------------------------------------------------
    ## JER smearing, various uncertainties
    ## ----------------------------------------------------------------------------------------------

    # list of clean tags - ignore jet ID for jets matching these objects
    SkipTag = cms.VInputTag(
        cms.InputTag('LeptonsNew:IdIsoMuon'),
        cms.InputTag('LeptonsNew:IdIsoElectron'),
        cms.InputTag('IsolatedElectronTracksVeto'),
        cms.InputTag('IsolatedMuonTracksVeto'),
        cms.InputTag('IsolatedPionTracksVeto'),
    )

    # get the JERs (disabled by default)
    # this requires the user to download the .db file from this github
    # https://github.com/cms-jet/JRDatabase
    if len(self.jerfile)>0:
        #get name of JERs without any directories
        JERera = self.jerfile.split('/')[-1]
        process.CondDB.connect = cms.string('sqlite_file:'+self.jerfile+'.db')
    
        process.jer = cms.ESSource("PoolDBESSource",process.CondDB,
            toGet = cms.VPSet(
                cms.PSet(
                    record = cms.string('JetResolutionRcd'),
                    tag    = cms.string('JR_'+JERera+'_PtResolution_AK4PFchs'),
                    label  = cms.untracked.string('AK4PFchs_pt')
                ),
                cms.PSet(
                    record = cms.string('JetResolutionScaleFactorRcd'),
                    tag    = cms.string('JR_'+JERera+'_SF_AK4PFchs'),
                    label  = cms.untracked.string('AK4PFchs')
                ),
                cms.PSet(
                    record = cms.string('JetResolutionRcd'),
                    tag    = cms.string('JR_'+JERera+'_PtResolution_AK8PFPuppi'),
                    label  = cms.untracked.string('AK8PFPuppi_pt')
                ),
                cms.PSet(
                    record = cms.string('JetResolutionScaleFactorRcd'),
                    tag    = cms.string('JR_'+JERera+'_SF_AK8PFPuppi'),
                    label  = cms.untracked.string('AK8PFPuppi')
                ),
            ),
        )

        process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')

    # skip all jet smearing and uncertainties for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo

    # AK4 jet uncertainties
    if self.geninfo and self.systematics:
        process, JetTagJECTmp, JetTagJECup, JetTagJECdown, JetTagJERup, JetTagJERdown, JetTag = self.JetVariations(process, JetTag, SkipTag)
    elif not self.geninfo:
        # get JEC unc for data
        process, JetTagJECTmp, _ = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            storeJec=True, # get JEC unc value (in intermediate tag Tmp)
            doSmear=False,
        )
        # append unc to central collection
        process, JetTag = addJetInfo(process, JetTag, [JetTagJECTmp.value()], [])

    if self.geninfo:
        # finally, do central smearing and replace jet tag
        process, _, JetTag = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get central jet smearing factor
        )

    # get puppi-specific multiplicities
    from PhysicsTools.PatAlgos.patPuppiJetSpecificProducer_cfi import patPuppiJetSpecificProducer
    process.puppiSpecificAK8 = patPuppiJetSpecificProducer.clone(
        src = JetAK8Tag
    )
    # update userfloats (used for jet ID, including ID for JEC/JER variations)
    process, JetAK8Tag = addJetInfo(process, JetAK8Tag,
        ['puppiSpecificAK8:puppiMultiplicity','puppiSpecificAK8:neutralPuppiMultiplicity','puppiSpecificAK8:neutralHadronPuppiMultiplicity',
         'puppiSpecificAK8:photonPuppiMultiplicity','puppiSpecificAK8:HFHadronPuppiMultiplicity','puppiSpecificAK8:HFEMPuppiMultiplicity'])

    # AK8 jet uncertainties
    if self.geninfo and self.systematics:
        process, JetAK8TagJECTmp, JetAK8TagJECup, JetAK8TagJECdown, JetAK8TagJERup, JetAK8TagJERdown, JetAK8Tag = self.JetVariations(process, JetAK8Tag, SkipTag, suff="AK8", vars="makeJetVarsAK8")
    elif not self.geninfo:
        # get JEC unc for data
        process, JetAK8TagJECTmp, _ = JetDepot(process,
            JetTag=JetAK8Tag,
            jecUncDir=0,
            storeJec=True, # get JEC unc value (in intermediate tag Tmp)
            doSmear=False,
        )
        # append unc to central collection
        process, JetAK8Tag = addJetInfo(process, JetAK8Tag, [JetAK8TagJECTmp.value()], [])

    if self.geninfo:
        # finally, do central smearing and replace jet tag
        process, _, JetAK8Tag = JetDepot(process,
            JetTag=JetAK8Tag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get central jet smearing factor
        )

    ## ----------------------------------------------------------------------------------------------
    ## Jet variables
    ## ----------------------------------------------------------------------------------------------

    if self.doQG:
        # get updated QG training
        process.CondDB.connect = cms.string('sqlite_file:'+os.environ['CMSSW_BASE']+'/src/TreeMaker/Production/test/data/QGL_cmssw8020_v2.db')

        process.qgdb = cms.ESSource("PoolDBESSource",process.CondDB,
            toGet   = cms.VPSet(
                cms.PSet(
                    record = cms.string('QGLikelihoodRcd'),
                    tag    = cms.string('QGLikelihoodObject_cmssw8020_v2_AK4PFchs'),
                    label  = cms.untracked.string('QGL_AK4PFchs')
                ),
                cms.PSet(
                    record = cms.string('QGLikelihoodRcd'),
                    tag    = cms.string('QGLikelihoodObject_cmssw8020_v2_AK4PFchs_antib'),
                    label  = cms.untracked.string('QGL_AK4PFchs_antib')
                ),
            )
        )
        process.es_prefer_qg = cms.ESPrefer("PoolDBESSource","qgdb")

        # get QG tagging discriminant
        process.QGTagger = cms.EDProducer('QGTagger',
            srcJets             = JetTag,
            jetsLabel           = cms.string('QGL_AK4PFchs'),
            srcRho              = cms.InputTag('fixedGridRhoFastjetAll'),
            srcVertexCollection = cms.InputTag('offlinePrimaryVerticesWithBS'),
            useQualityCuts      = cms.bool(False)
        )

        # add userfloats & update tag

        process, JetTag = addJetInfo(process, JetTag, ['QGTagger:qgLikelihood','QGTagger:ptD', 'QGTagger:axis2', 'QGTagger:axis1'], ['QGTagger:mult'])

    process = self.makeJetVars(process,
        JetTag=JetTag,
        suff='',
        storeProperties=2,
        SkipTag=SkipTag
    )

    if self.systematics:
        process.JetProperties.properties.extend(["jecUnc"])
        process.JetProperties.jecUnc = cms.vstring(JetTagJECTmp.value())
        self.VectorDouble.extend([
            'JetProperties:jecUnc(Jets_jecUnc)',
        ])
    if self.geninfo and self.systematics:
        process.JetProperties.properties.extend(["jerFactorUp","jerFactorDown"])
        process.JetProperties.jerFactorUp = cms.vstring(JetTagJERup.value())
        process.JetProperties.jerFactorDown = cms.vstring(JetTagJERdown.value())
        self.VectorDouble.extend([
            'JetProperties:jerFactorUp(Jets_jerFactorUp)',
            'JetProperties:jerFactorDown(Jets_jerFactorDown)',
        ])

    if self.doQG:
        # get QG tagging discriminant for subjets
        process.QGTaggerSubjets = process.QGTagger.clone(
            srcJets = SubjetTag
        )

        # add userfloats & update subjet tag
        process, SubjetTag = addJetInfo(process, SubjetTag,
            ['QGTaggerSubjets:qgLikelihood','QGTaggerSubjets:ptD', 'QGTaggerSubjets:axis2', 'QGTaggerSubjets:axis1'], ['QGTaggerSubjets:mult'])
        # update subjets in jet coll
        JetAK8TagSJU = cms.InputTag(JetAK8Tag.value()+'SJUpdate')
        setattr(process, JetAK8TagSJU.value(),
            cms.EDProducer('SubjetUpdater',
                JetTag = JetAK8Tag,
                SubjetTag = SubjetTag,
                OldName = SubjetName,
                NewName = cms.string("SoftDropPuppiUpdated"),
            )
        )
        JetAK8Tag = JetAK8TagSJU

    # apply jet ID and get properties
    process = self.makeJetVarsAK8(process,
        JetTag=JetAK8Tag,
        suff='AK8',
        storeProperties=2,
    )
    if self.tchannel:
        process.JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8PuppiLowCut:tau1')
        process.JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8PuppiLowCut:tau2')
        process.JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8PuppiLowCut:tau3')
        process.JetPropertiesAK8.NsubjettinessTau4 = cms.vstring('NjettinessAK8PuppiLowCut:tau4')
        process.JetPropertiesAK8.ecfN2b1 = cms.vstring('ak8PFJetsPuppiLowCutSoftDropValueMap:nb1AK8PuppiLowCutSoftDropN2')
        process.JetPropertiesAK8.ecfN2b2 = cms.vstring('ak8PFJetsPuppiLowCutSoftDropValueMap:nb2AK8PuppiLowCutSoftDropN2')
        process.JetPropertiesAK8.ecfN3b1 = cms.vstring('ak8PFJetsPuppiLowCutSoftDropValueMap:nb1AK8PuppiLowCutSoftDropN3')
        process.JetPropertiesAK8.ecfN3b2 = cms.vstring('ak8PFJetsPuppiLowCutSoftDropValueMap:nb2AK8PuppiLowCutSoftDropN3')
        process.JetPropertiesAK8.softDropMass = cms.vstring('SoftDrop')
        process.JetPropertiesAK8.subjets = cms.vstring('SoftDrop')
        process.JetPropertiesAK8.SJbDiscriminatorCSV = cms.vstring('SoftDrop', 'pfCombinedInclusiveSecondaryVertexV2BJetTags')
    if self.systematics:
        process.JetPropertiesAK8.properties.extend(["jecUnc"])
        process.JetPropertiesAK8.jecUnc = cms.vstring(JetAK8TagJECTmp.value())
        self.VectorDouble.extend([
            'JetPropertiesAK8:jecUnc(JetsAK8_jecUnc)',
        ])
    if self.geninfo and self.systematics:
        process.JetPropertiesAK8.properties.extend(["jerFactorUp","jerFactorDown"])
        process.JetPropertiesAK8.jerFactorUp = cms.vstring(JetAK8TagJERup.value())
        process.JetPropertiesAK8.jerFactorDown = cms.vstring(JetAK8TagJERdown.value())
        self.VectorDouble.extend([
            'JetPropertiesAK8:jerFactorUp(JetsAK8_jerFactorUp)',
            'JetPropertiesAK8:jerFactorDown(JetsAK8_jerFactorDown)',
        ])

    # record final jet collections (AK4 excluded by default)
    if self.jetsconstituents>2:
        self.JetsTags.extend([JetTag])
        self.JetsNames.extend(["Jets"])
    self.JetsTags.extend([JetAK8Tag])
    self.JetsNames.extend(["JetsAK8"])

    ## ----------------------------------------------------------------------------------------------
    ## GenJet variables
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        # store all genjets
        from TreeMaker.Utils.genjetproperties_cfi import genjetproperties
        if self.emerging:
            process.genJetProperties = genjetproperties.clone(
                GenJetTag = cms.InputTag("slimmedGenJets"),
                doHV = cms.bool(True),
            )
            self.VectorRecoCand.extend(['genJetProperties(GenJets)'])
            self.VectorInt.extend(['genJetProperties:multiplicity(GenJets_multiplicity)'])
            self.VectorInt.extend(['genJetProperties:nHVAncestors(GenJets_nHVAncestors)'])
        else:
            self.VectorRecoCand.extend(['slimmedGenJets(GenJets)'])

        from TreeMaker.Utils.subJetSelection_cfi import SubGenJetSelection

        process.GenHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )

        # make gen HT
        from TreeMaker.Utils.htdouble_cfi import htdouble
        process.GenHT = htdouble.clone(
            JetTag = cms.InputTag("GenHTJets"),
        )
        self.VarsDouble.extend(['GenHT'])

        process.GenMHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(5.0),
        )

        # make gen MHT
        from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
        process.GenMHT = mhtdouble.clone(
            JetTag  = cms.InputTag('GenMHTJets'),
        )
        self.VarsDouble.extend(['GenMHT:Pt(GenMHT)','GenMHT:Phi(GenMHTPhi)'])

        # substructure for genjets
        from RecoJets.Configuration.RecoGenJets_cff import ak8GenJetsNoNu as ak8GenJetsNoNuDefault
        from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
        process.ak8GenJetsSoftDrop = ak8GenJetsNoNuDefault.clone(
            jetTransforms = cms.VPSet(cms.PSet(
                useSoftDrop = cms.bool(True),
                zcut = cms.double(0.1),
                beta = cms.double(0.0),
                R0   = cms.double(0.5),
                jetCollInstanceName=cms.string("SubJets"),
                jetPtMin = cms.double(0. if self.tchannel else 170.),
            )),
            src = GenParticlesForJetTag,
            doBaseClustering = cms.bool(False),
        )

        process.ak8GenJetProperties = genjetproperties.clone(
            GenJetTag = GenJetAK8Tag,
            SoftDropGenJetTag = cms.InputTag("ak8GenJetsSoftDrop"),
            distMax = cms.double(0.8),
            jetPtFilter = cms.double(0. if self.tchannel else 150),
            doHV = cms.bool(True if self.emerging else False),
        )
        if self.tchannel or self.doZinv:
            # avoid doing this twice
            process.ak8GenJetProperties.SoftDropGenJetTag = cms.InputTag("ak8GenJetsNoNuSoftDrop")
        self.VectorDouble.extend([
            'ak8GenJetProperties:softDropMass(GenJetsAK8_softDropMass)',
        ])
        self.VectorInt.extend([
            'ak8GenJetProperties:multiplicity(GenJetsAK8_multiplicity)',
        ])
        if self.emerging:
            self.VectorInt.extend([
                'ak8GenJetProperties:nHVAncestors(GenJetsAK8_nHVAncestors)'
            ])
        # store AK8 genjets above pt cut
        self.VectorRecoCand.extend (['ak8GenJetProperties(GenJetsAK8)'])

    ## ----------------------------------------------------------------------------------------------
    ## Prefiring weights
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.L1NonPrefiringProbProducer_cfi import L1NonPrefiringProbProducer

    process.L1NonPrefiringProbProducer = L1NonPrefiringProbProducer.clone(
        TheJets = JetTag,
        DataEraECAL = cms.string("UL2016postVFP"),
        DataEraMuon = cms.string("2016postVFP"),
        L1MapsECAL = cms.string(os.environ['CMSSW_BASE']+'/src/TreeMaker/Production/test/data/L1PrefiringMaps.root'),
        L1ParamsMuon = cms.string(os.environ['CMSSW_BASE']+'/src/TreeMaker/Production/test/data/L1MuonPrefiringParameterizations.root'),
    )

    TMeras.TMUL2016APV.toModify(process.L1NonPrefiringProbProducer, DataEraECAL = "UL2016preVFP", DataEraMuon = "2016preVFP")
    TMeras.TMUL2017.toModify(process.L1NonPrefiringProbProducer, DataEraECAL = "UL2017BtoF", DataEraMuon = "20172018")
    TMeras.TMUL2018.toModify(process.L1NonPrefiringProbProducer, DataEraECAL = "None", DataEraMuon = "20172018")

    self.VarsDouble.extend([
        'L1NonPrefiringProbProducer:NonPrefiringProb',
        'L1NonPrefiringProbProducer:NonPrefiringProbUp',
        'L1NonPrefiringProbProducer:NonPrefiringProbDown',
        'L1NonPrefiringProbProducer:NonPrefiringProbECAL',
        'L1NonPrefiringProbProducer:NonPrefiringProbECALUp',
        'L1NonPrefiringProbProducer:NonPrefiringProbECALDown',
        'L1NonPrefiringProbProducer:NonPrefiringProbMuon',
        'L1NonPrefiringProbProducer:NonPrefiringProbMuonUp',
        'L1NonPrefiringProbProducer:NonPrefiringProbMuonDown',
    ])


    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    # sequence for baseline filters
    process.Baseline = cms.Sequence()
    from TreeMaker.Utils.doublefilter_cfi import DoubleFilter
    if self.applybaseline:
        process.HTFilter = DoubleFilter.clone(
            DoubleTag = cms.InputTag('HT'),
            CutValue  = cms.double(500),
        )
        process.MHTFilter = DoubleFilter.clone(
            DoubleTag = cms.InputTag('MHT:Pt'),
            CutValue  = cms.double(200),
        )
        process.Baseline += process.HTFilter
        #process.Baseline += process.MHTFilter

    ## ----------------------------------------------------------------------------------------------
    ## MET
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = METTag,
        GenMETTag = cms.InputTag("slimmedMETs","",self.tagname), #original collection used deliberately here
        geninfo = cms.untracked.bool(self.geninfo),
        InfTagAK8 = JetAK8TagInf,
    )
    self.VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)','MET:CaloPt(CaloMET)','MET:CaloPhi(CaloMETPhi)','MET:PFCaloPtRatio(PFCaloMETRatio)','MET:Significance(METSignificance)'])
#    self.VarsDouble.extend(['MET:RawPt(RawMET)','MET:RawPhi(RawMETPhi)'])
    if self.geninfo:
        self.VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        self.VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    if self.doMT2:
        from TreeMaker.Utils.mt2producer_cfi import mt2Producer
        process.Mt2Producer = mt2Producer.clone(
                    JetTag  = cms.InputTag('MHTJets'),
                    METTag = METTag
            )
        self.VarsDouble.extend(['Mt2Producer:mt2(MT2)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------
    if self.hadtau:
        dorecluster = False
        if self.hadtaurecluster==0: dorecluster = False
        elif self.hadtaurecluster==1: dorecluster = ("TTJets" in process.source.fileNames[0] or "WJets" in process.source.fileNames[0])
        elif self.hadtaurecluster==2: dorecluster = geninfo
        elif self.hadtaurecluster==3: dorecluster = True
        process = self.doHadTauBkg(process,JetTagBeforeSmearing,dorecluster)

    ## ----------------------------------------------------------------------------------------------
    ## Lost Lepton Background
    ## ----------------------------------------------------------------------------------------------
    if self.lostlepton:
        process = self.doLostLeptonBkg(process,METTag)

    ## ----------------------------------------------------------------------------------------------
    ## Zinv Background
    ## ----------------------------------------------------------------------------------------------
    if self.doZinv:
        from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg
        process = self.doZinvBkg(process)

    ## ----------------------------------------------------------------------------------------------
    ## Semi-visible jets
    ## ----------------------------------------------------------------------------------------------
    if self.semivisible:
        process.HiddenSector = cms.EDProducer("HiddenSectorProducer",
            signal = cms.bool(self.signal and "SVJ" in self.sample),
            JetTag = JetAK8Tag,
            MetTag = METTag,
            GenMetTag = cms.InputTag("genMetTrue"),
            GenTag = cms.InputTag("prunedGenParticles"),
            GenJetTag = GenJetAK8Tag,
            coneSize = cms.double(0.8),
            DarkStableIDs = cms.vuint32(51,52,53),
            DarkQuarkIDs = cms.vuint32(4900101,4900102),
            DarkSMediatorIDs = cms.vuint32(4900023),
            DarkTMediatorIDs = cms.vuint32(4900001,4900002,4900003,4900004,4900005,4900006),
            DarkHadronIDs = cms.vuint32(4900111,4900113,4900211,4900213),
            DarkGluonIDs = cms.vuint32(4900021),
            SMQuarkIDs = cms.vuint32(1,2,3,4,5,6),
        )
        self.VarsDouble.extend([
            'HiddenSector:MJJ(MJJ_AK8)',
            'HiddenSector:Mmc(Mmc_AK8)',
            'HiddenSector:MT(MT_AK8)',
            'HiddenSector:GenMT2(GenMT2_AK8)',
            'HiddenSector:DeltaPhi1(DeltaPhi1_AK8)',
            'HiddenSector:DeltaPhi2(DeltaPhi2_AK8)',
            'HiddenSector:DeltaPhiMin(DeltaPhiMin_AK8)',
        ])
        if self.geninfo and process.HiddenSector.signal:
            self.VectorBool.extend([
                'HiddenSector:isHV(JetsAK8_isHV)'
            ])
            self.VectorInt.extend([
                'HiddenSector:hvCategory(GenJetsAK8_hvCategory)',
                'HiddenSector:MT2JetsID(GenJetsAK8_MT2JetsID)',
                'HiddenSector:genIndex(JetsAK8_genIndex)'
            ])
            self.VectorDouble.extend([
                'HiddenSector:darkPtFrac(GenJetsAK8_darkPtFrac)'
            ])
    ## ----------------------------------------------------------------------------------------------
    ## Photon information
    ## ----------------------------------------------------------------------------------------------
    if self.doPhotons:
        from TreeMaker.TreeMaker.doPhotons import doPhotonVars
        process = self.doPhotonVars(process)

    ## ----------------------------------------------------------------------------------------------
    ## Emerging jets
    ## ----------------------------------------------------------------------------------------------
    if self.emerging:
        self.VectorXYZPoint.extend(['primaryVertices:vtxposition(PrimaryVertices)'])
        self.VectorDouble.extend([
            'primaryVertices:vtxtime(PrimaryVertices_time)',
            'primaryVertices:vtxndof(PrimaryVertices_ndof)',
            'primaryVertices:vtxchi2(PrimaryVertices_chi2)',
            'primaryVertices:vtxxError(PrimaryVertices_xError)',
            'primaryVertices:vtxyError(PrimaryVertices_yError)',
            'primaryVertices:vtxzError(PrimaryVertices_zError)',
            'primaryVertices:vtxtError(PrimaryVertices_tError)',
        ])
        self.VectorBool.extend([
            'primaryVertices:vtxisValid(PrimaryVertices_isValid)',
            'primaryVertices:vtxisFake(PrimaryVertices_isFake)',
            'primaryVertices:vtxisGood(PrimaryVertices_isGood)',
        ])        
        self.VectorInt.extend(['primaryVertices:vtxntracks(PrimaryVertices_nTracks)'])

        process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
        from TreeMaker.Utils.candidateTrackMaker_cfi import candidateTrackFilter
        process.trackFilter = candidateTrackFilter.clone(
            storedVerticesTag = cms.InputTag("primaryVertices","vtxref"),
        )
        self.VectorXYZVector.extend(['trackFilter:trks(Tracks)'])
        self.VectorXYZPoint.extend(['trackFilter:trksreferencepoint(Tracks_referencePoint)'])
        self.VectorBool.extend(['trackFilter:trksmatchedtopfcand(Tracks_matchedToPFCandidate)',])
        self.VectorDouble.extend([
            'trackFilter:trksdzpv(Tracks_dzPV0)',
            'trackFilter:trksdzerrorpv(Tracks_dzErrorPV0)',
            'trackFilter:trksdxypv(Tracks_dxyPV0)',
            'trackFilter:trksdxyerrorpv(Tracks_dxyErrorPV0)',
            'trackFilter:trksnormalizedchi2(Tracks_normalizedChi2)',
            'trackFilter:trkspterror(Tracks_ptError)',
            'trackFilter:trksetaerror(Tracks_etaError)',
            'trackFilter:trksphierror(Tracks_phiError)',
            'trackFilter:trksqoverperror(Tracks_qoverpError)',
            'trackFilter:trksip2d(Tracks_IP2DPV0)',
            'trackFilter:trksip2dsig(Tracks_IP2DSigPV0)',
            'trackFilter:trksip3d(Tracks_IP3DPV0)',
            'trackFilter:trksip3dsig(Tracks_IP3DSigPV0)',
            'trackFilter:pfcandsenergy(Tracks_pfEnergy)',
            'trackFilter:pfcandsdzassociatedpv(Tracks_dzAssociatedPV)',
            'trackFilter:vtxsumtrackpt2(PrimaryVertices_sumTrackPt2)',
        ])
        self.VectorInt.extend([
            'trackFilter:trkschg(Tracks_charge)',
            'trackFilter:trksfound(Tracks_foundHits)',
            'trackFilter:trkslost(Tracks_lostHits)',
            'trackFilter:trksquality(Tracks_quality)',
            'trackFilter:trksipsign(Tracks_IPSign)',
            'trackFilter:pfcandspdgid(Tracks_pdgId)',
            'trackFilter:pfcandsnumberofhits(Tracks_numberOfHits)',
            'trackFilter:pfcandsnumberofpixelhits(Tracks_numberOfPixelHits)',
            'trackFilter:pfcandsfirsthit(Tracks_firstHit)',
            'trackFilter:pfcandsfrompv(Tracks_fromPV0)',
            'trackFilter:pfcandspvassociationquality(Tracks_pvAssociationQuality)',
            'trackFilter:pfcandsvtxidx(Tracks_vertexIdx)',
        ])
        self.VectorVectorInt.extend([
            'trackFilter:trkshitpattern(Tracks_hitPattern)',
        ])


    ## ----------------------------------------------------------------------------------------------
    ## AK15 jets
    ## ----------------------------------------------------------------------------------------------

    if self.boostedsemivisible:

        from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
        jetToolbox(process,
            'ak15',
            'jetSequence',
            'noOutput',
            PUMethod = 'Puppi',
            useExistingWeights=True,
            dataTier = 'miniAOD',
            runOnMC = self.geninfo,
            Cut = 'pt>20.',
            addPruning = False, # different from AK8
            addSoftDrop = True,
            addSoftDropSubjets = True,
            addNsub = True,
            maxTau = 4,
            subjetBTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
            addEnergyCorrFunc = True,
            ecfType = ["N","M","C","D"],
            ecfBeta = [1.0,2.0],
            # use default pt cut for 3-jet ECFs: effectively disable them
            verbosity = 2 if self.verbose else 0,
            # 
            JETCorrPayload = 'AK8PFPuppi',
            subJETCorrPayload = 'AK4PFPuppi',
            JETCorrLevels = levels,
            subJETCorrLevels = levels,
        )

        JetAK15Tag = cms.InputTag("packedPatJetsAK15PFPuppiSoftDrop")
        subJetAK15Tag = cms.InputTag("selectedPatJetsAK15PFPuppiSoftDropPacked:SubJets")

        # get puppi-specific multiplicities
        from PhysicsTools.PatAlgos.patPuppiJetSpecificProducer_cfi import patPuppiJetSpecificProducer
        process.puppiSpecificAK15 = patPuppiJetSpecificProducer.clone(
            src = JetAK15Tag
        )

        # alternate softdrop parameters
        process.ak15PFJetsPuppiSoftDropBeta1 = process.ak15PFJetsPuppiSoftDrop.clone(
            beta = cms.double(1.0),
        )
        process.ak15PFJetsPuppiSoftDropMassBeta1 = process.ak15PFJetsPuppiSoftDropMass.clone(
            src = JetAK15Tag,
            matched = cms.InputTag("ak15PFJetsPuppiSoftDropBeta1")
        )

        if self.geninfo:
            process = self.transformJetSeq(process, "ak15GenJetsNoNu", {"SoftDrop":"ak15GenJetsNoNuSoftDrop"}, "recoGenJets")
        process = self.transformJetSeq(process, "ak15PFJetsPuppi", {"SoftDrop":"ak15PFJetsPuppiSoftDrop", "SoftDropBeta1":"ak15PFJetsPuppiSoftDropBeta1"}, "recoPFJets")

        # update userfloats (used for jet ID, including ID for JEC/JER variations)
        process, JetAK15Tag = addJetInfo(
            process, JetAK15Tag,
            [
                'puppiSpecificAK15:puppiMultiplicity',
                'puppiSpecificAK15:neutralPuppiMultiplicity',
                'puppiSpecificAK15:neutralHadronPuppiMultiplicity',
                'puppiSpecificAK15:photonPuppiMultiplicity',
                'puppiSpecificAK15:HFHadronPuppiMultiplicity',
                'puppiSpecificAK15:HFEMPuppiMultiplicity',
                'ak15PFJetsPuppiSoftDropMassBeta1',
            ]
        )

        process = self.makeJetVarsAK8(
            process,
            JetTag=JetAK15Tag,
            suff='AK15',
            storeProperties=2,
            puppiSpecific = 'puppiSpecificAK15',
            subjetTag = 'SoftDrop',
            doECFs = True,
        )

        _omit_AK15 = ["jecFactorSubjets", "SJptD", "SJaxismajor", "SJaxisminor", "SJmultiplicity", "jerFactor", "origIndex", "ecfN3b1", "ecfN3b2"]
        process.JetPropertiesAK15.properties = [x for x in process.JetPropertiesAK15.properties if x not in _omit_AK15]
        for branchlist in [self.VectorDouble, self.VectorInt, self.AssocVectorVectorDouble, self.AssocVectorVectorInt]:
            branchlist.setValue([x for x in branchlist if not ("AK15" in x and any([y in x for y in _omit_AK15]))])

        # more ECFs
        _all_ECFs = ["ecfN2b1","ecfN2b2","ecfC2b1","ecfC2b2","ecfM2b1","ecfM2b2","ecfD2b1","ecfD2b2"]
        process.JetPropertiesAK15.properties.extend(_all_ECFs[2:]) # N-types already included
        self.VectorDouble.extend(['JetPropertiesAK15:{0}(JetsAK15_{0})'.format(_ecf) for _ecf in _all_ECFs[2:]])
        for _ecf in _all_ECFs:
            _ecfT = _ecf[3:5]
            _ecfB = _ecf[6]
            setattr(process.JetPropertiesAK15,
                _ecf,
                cms.vstring('ak15PFJetsPuppiSoftDropValueMap:{}b{}AK15PuppiSoftDrop{}'.format(_ecfT[0].lower(),_ecfB,_ecfT))
            )

        process.JetPropertiesAK15.NsubjettinessTau1 = cms.vstring('NjettinessAK15Puppi:tau1')
        process.JetPropertiesAK15.NsubjettinessTau2 = cms.vstring('NjettinessAK15Puppi:tau2')
        process.JetPropertiesAK15.NsubjettinessTau3 = cms.vstring('NjettinessAK15Puppi:tau3')
        process.JetPropertiesAK15.NsubjettinessTau4 = cms.vstring('NjettinessAK15Puppi:tau4')

        process.JetPropertiesAK15.neutralHadronPuppiMultiplicity = cms.vstring("puppiSpecificAK15:neutralHadronPuppiMultiplicity")
        process.JetPropertiesAK15.neutralPuppiMultiplicity = cms.vstring("puppiSpecificAK15:neutralPuppiMultiplicity")
        process.JetPropertiesAK15.photonPuppiMultiplicity = cms.vstring("puppiSpecificAK15:photonPuppiMultiplicity")

        process.JetPropertiesAK15.properties.append("msd")
        process.JetPropertiesAK15.msd = cms.vstring("ak15PFJetsPuppiSoftDropMassBeta1")
        self.VectorDouble.extend([
            'JetPropertiesAK15:msd(JetsAK15_softDropMassBeta1)'
        ])

        # record final jet collection
        self.JetsTags.append(JetAK15Tag)
        self.JetsNames.append("JetsAK15")

        # store AK15 genjets
        if self.geninfo:
            self.VectorRecoCand.extend(['ak15GenJetsNoNu(GenJetsAK15)'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet constituents
    ## ----------------------------------------------------------------------------------------------
    if self.jetsconstituents>0 and len(self.JetsTags)>0:
        process.JetsConstituents = cms.EDProducer("JetsConstituents",
            suffix = cms.string("ConstituentsIndex"),
            JetsTags = cms.VInputTag(self.JetsTags),
            JetsNames = cms.vstring(self.JetsNames),
            # puppi retains order of input candidate collection, so rekeying not needed here
            CandTag = cms.InputTag("packedPFCandidates"),
            properties = cms.vstring("PdgId","PuppiWeight"),
        )
        self.VectorLorentzVector.append("JetsConstituents")
        self.VectorInt.append("JetsConstituents:PdgId(JetsConstituents_PdgId)")
        self.VectorDouble.append("JetsConstituents:PuppiWeight(JetsConstituents_PuppiWeight)")
        if self.jetsconstituents>1:
            process.JetsConstituents.properties.extend(['dz','dxy','dzsig','dxysig'])
            self.VectorDouble.extend([
                "JetsConstituents:dz(JetsConstituents_dz)",
                "JetsConstituents:dxy(JetsConstituents_dxy)",
                "JetsConstituents:dzsig(JetsConstituents_dzsig)",
                "JetsConstituents:dxysig(JetsConstituents_dxysig)",
            ])
        self.VectorVectorInt.extend(["JetsConstituents:{}{}({}{})".format(JetsName,process.JetsConstituents.suffix.value(),JetsName,"_constituentsIndex") for JetsName in self.JetsNames])

    ## ----------------------------------------------------------------------------------------------
    ## Gen particles for jets
    ## ----------------------------------------------------------------------------------------------
    # overwrite NoNu collection, account for SVJ DM particles
    # (do this at the very end to ensure changes aren't overwritten by JetToolbox)
    if self.geninfo:
        setattr(process,GenParticlesForJetTag.value(),
            cms.EDFilter("CandPtrSelector",
                src = cms.InputTag("packedGenParticles"),
                cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16 && abs(pdgId) != 51 && abs(pdgId) != 52 && abs(pdgId) != 53"),
            )
        )

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Final steps
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # dump everything into a task so it can run unscheduled
    process.myTask = cms.Task()
    process.myTask.add(*[getattr(process,prod) for prod in process.producers_()])
    process.myTask.add(*[getattr(process,filt) for filt in process.filters_()])
    # create the process path
    process.WriteTree = cms.Path(
        process.Baseline *
        process.TreeMaker2
    )
    process.WriteTree.associate(process.myTask)

    ## ----------------------------------------------------------------------------------------------
    ## Branch control
    ## ----------------------------------------------------------------------------------------------

    # apply branch inclusion/exclusion, if enabled
    # must be done last
    if len(self.includeBranches)>0 or len(self.excludeBranches)>0:
        # same algorithm from class TreeObject in TreeMaker.h
        def branchName(b):
            pos1 = b.find('(')
            pos2 = b.find(')')
            pos3 = b.find(':')
            # case 3/4
            if pos1!=-1 and pos2!=-1:
                return b[pos1+1:pos2]
            # case 2
            elif pos3!=-1:
                return b[pos3+1:]
            # case 1
            else:
                return b
        if self.exactBranches:
            def branchCheck(b, patterns):
                return any(branchName(b)==pattern for pattern in patterns)
        else:
            def branchCheck(b, patterns):
                return any(regex.match(branchName(b)) for regex in patterns)
        def branchInclude(b, patterns):
            return branchCheck(b, patterns)
        def branchExclude(b, patterns):
            return not branchCheck(b, patterns)

        branches, action = (self.includeBranches, branchInclude) if len(self.includeBranches)>0 else (self.excludeBranches, branchExclude)
        patterns = branches if self.exactBranches else [re.compile(b) for b in branches]

        for branchList in self.branchLists:
            allBranches = getattr(self,branchList).value()
            selBranches = [b for b in allBranches if action(b, patterns)]
            setattr(self,branchList,cms.vstring(selBranches))
            setattr(process.TreeMaker2,branchList,getattr(self,branchList))

    return process
