# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os,re

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
        inputCommands = cms.untracked.vstring('keep *','drop LHERunInfoProduct_*_*_*'),
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
        TreeName                   = cms.string(self.treename),
        VectorRecoCand             = self.VectorRecoCand,
        VarsDouble                 = self.VarsDouble,
        VarsInt                    = self.VarsInt,
        VarsBool                   = self.VarsBool,
        VectorTLorentzVector       = self.VectorTLorentzVector,
        VectorDouble               = self.VectorDouble,
        VectorInt                  = self.VectorInt,
        VectorString               = self.VectorString,
        VectorBool                 = self.VectorBool,
        VectorVectorBool           = self.VectorVectorBool,
        VectorVectorInt            = self.VectorVectorInt,
        VectorVectorDouble         = self.VectorVectorDouble,
        VectorVectorString         = self.VectorVectorString,
        VectorVectorTLorentzVector = self.VectorVectorTLorentzVector,
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
        self.VarsDouble.extend(['SignalScan:SusyMotherMass','SignalScan:SusyLSPMass'])
        self.VectorDouble.extend(['SignalScan:SignalParameters'])
        # set scan type ("None" by default, producer does nothing)
        if self.signal:
            if "PMSSM" in self.sample: process.SignalScan.signalType = "pMSSM"
            elif self.fastsim: process.SignalScan.signalType = "SUSY"
            elif "SVJ" in self.sample and "Scan" in self.sample: process.SignalScan.signalType = "SVJ"

    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],process.SignalScan.signalType!="None")
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string(self.pufile)
        process.WeightProducer.FileNamePUMCDistribution = cms.string(self.wrongpufile)
        process.WeightProducer.SampleName = cms.string(self.sample)
        self.VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        self.VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo and self.doPDFs:
        from TreeMaker.Utils.pdfweightproducer_cfi import PDFWeightProducer
        process.PDFWeights = PDFWeightProducer.clone(
            recalculatePDFs = cms.bool(self.signal),
            recalculateScales = cms.bool(False),
            normalize = (not "SVJ" in self.sample), # skip normalization only for SVJ signals
            pdfSetName = cms.string("NNPDF31_lo_as_0130"),
        )
        if "SVJ" in self.sample: # skip trying to get scale and PDF weights for SVJ signals
            process.PDFWeights.nScales = 0
            process.PDFWeights.nPDFs = 0
            process.PDFWeights.nEM = 2
            process.PDFWeights.recalculateScales = True
        TMeras.TM2016.toModify(process.PDFWeights, pdfSetName = cms.string("NNPDF23_lo_as_0130_qed"))
        self.VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights','PDFWeights:PSweights'])

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
    process.NVtx = primaryvertices.clone(
        VertexCollection  = cms.InputTag('goodVertices'),
    )
    self.VarsInt.extend(['NVtx'])
    # also store total number of vertices without quality checks
    process.nAllVertices = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    self.VarsInt.extend(['nAllVertices'])
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
                    4900021,4900023,4900101,4900102,4900111,4900113,4900211,4900213,51,52,53,
                    5000001,5000002,
                ),
                # Other settings
                keepIds = cms.vint32(),
                keepFirst = cms.bool(False),
                keepMinimal = cms.bool(True),
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
                    4900021,4900023,4900101,4900102,4900111,4900113,4900211,4900213,51,52,53,
                    5000001,5000002,
                ),
                keepIds = cms.vint32(6,23,24,25),
                keepFirst = cms.bool(True),
                keepMinimal = cms.bool(False),
            )
            # store gluons for signals with Higgs
            if "T5qqqqZH" in process.source.fileNames[0]: process.genParticles.childIds.append(21)
        self.VectorTLorentzVector.append("genParticles(GenParticles)")
        self.VectorInt.append("genParticles:PdgId(GenParticles_PdgId)")
        self.VectorInt.append("genParticles:Status(GenParticles_Status)")
        self.VectorInt.append("genParticles:Parent(GenParticles_ParentIdx)")
        self.VectorInt.append("genParticles:ParentId(GenParticles_ParentId)")
        if not self.saveMinimalGenParticles:
            self.VectorBool.append("genParticles:TTFlag(GenParticles_TTFlag)")

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

        #Event weight to fix FastSim pre-UL bug
        if self.fastsim:
            process.FastSimWeightPR31285To36122 = cms.EDProducer("FastSimWeightPR31285To36122",
                genCollection = cms.InputTag("prunedGenParticles"),
                genJetTag = cms.InputTag('slimmedGenJets'),
                recJetTag = cms.InputTag("slimmedJets")
            )
            self.VarsDouble.append("FastSimWeightPR31285To36122")

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

    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup

    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    if len(self.jecfile)>0:
        #get name of JECs without any directories
        JECera = self.jecfile.split('/')[-1]
        JECPatch = cms.string('sqlite_file:'+self.jecfile+'.db')

        process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
            connect = JECPatch,
            toGet   = cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PFchs"),
                    label  = cms.untracked.string("AK4PFchs")
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
        TMeras.TM80X.toModify(ak4updates,
            discrs = cms.vstring(
                ['pfDeepCSVJetTags:'+x for x in ['probb','probc','probudsg','probbb']] +
                ['pfDeepCSVDiscriminatorsJetTags:'+x for x in ['BvsAll','CvsB','CvsL']]
            )
        )

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
            ak8updates.extend(["pfDeepBoostedDiscriminatorsJetTags:"+x for x in ["TvsQCD","WvsQCD","ZvsQCD","HbbvsQCD"]])
            ak8updates.extend(["pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:"+x for x in ["TvsQCD","WvsQCD","ZHbbvsQCD"]])

        if self.deepDoubleB:
            ak8updates.extend(['pfDeepDoubleBJetTags:'+x for x in ['probQ','probH']])

        if TMeras.TM80X.isChosen():
            # use jet toolbox to rerun puppi, recluster AK8 jets, and compute substructure variables
            # do not add discriminators here, several issues
            from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
            jetToolbox(process,
                'ak8',
                'jetSequence',
                'out',
                PUMethod = 'Puppi',
                miniAOD = True,
                runOnMC = self.geninfo,
                postFix = '94Xlike',
                Cut = 'pt>170.',
                addPruning = True,
                addSoftDropSubjets = True,
                addNsub = True,
                maxTau = 3,
                subjetBTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
                JETCorrLevels = levels,
                subJETCorrLevels = levels,
                addEnergyCorrFunc = False,
                associateTask = False,
                verbosity = 2 if self.verbose else 0,
            )

            JetAK8Tag = cms.InputTag("packedPatJetsAK8PFPuppi94XlikeSoftDrop")
            SubjetTag = cms.InputTag("selectedPatJetsAK8PFPuppi94XlikeSoftDropPacked:SubJets")
            SubjetName = cms.string("SoftDrop")

        if self.tchannel:
            # recluster AK8 jets to remove pT cut
            # this also produces a reclustered AK8 GenJet collection w/ no pT cut
            from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
            jetToolbox(process,
                'ak8',
                'jetSequence',
                'out',
                PUMethod = 'Puppi',
                miniAOD = True,
                runOnMC = self.geninfo,
                postFix = 'NoCut',
                addPruning = True,
                addSoftDropSubjets = True,
                addNsub = True,
                maxTau = 3,
                subjetBTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
                JETCorrLevels = levels,
                subJETCorrLevels = levels,
                addEnergyCorrFunc = True,
                associateTask = False,
                verbosity = 2 if self.verbose else 0,
            )

            JetAK8Tag = cms.InputTag("packedPatJetsAK8PFPuppiNoCutSoftDrop")
            SubjetTag = cms.InputTag("selectedPatJetsAK8PFPuppiNoCutSoftDropPacked:SubJets")
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

        # update the MET to account for the new JECs
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not self.geninfo, # controls gen met
            jetCollUnskimmed=JetTag,
            reapplyJEC=False,
            fixEE2017=self.doMETfix,
        )
        METTag = cms.InputTag('slimmedMETs','',process.name_())

        # additional run to keep orig values
        if self.doMETfix:
            runMetCorAndUncFromMiniAOD(
                process,
                isData=not self.geninfo, # controls gen met
                jetCollUnskimmed=JetTag,
                reapplyJEC=False,
                postfix="Orig",
                computeMETSignificance=False,
            )
            METTagOrig = cms.InputTag('slimmedMETsOrig')
        else:
            METTagOrig = None

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
        self.VectorTLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(PFCands)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(PFCands_trkiso)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(PFCands_dzpv)'])
        self.VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(PFCands_mT)'])
        self.VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(PFCands_charge)'])
        self.VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(PFCands_id)'])

    ## ----------------------------------------------------------------------------------------------
    ## Electrons/Muons
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.EgammaPostRecoTools import setupEgammaPostRecoSeq
    elePostRecoEra = cms.PSet(value = cms.string(""))
    TMeras.TM2018.toModify(elePostRecoEra, value = "2018-Prompt")
    TMeras.TM2017.toModify(elePostRecoEra, value = "2017-Nov17ReReco")
    TMeras.TM80X.toModify(elePostRecoEra, value = "2016-Legacy")
    if len(elePostRecoEra.value.value())>0:
        process = setupEgammaPostRecoSeq(process, runVID=False, era=elePostRecoEra.value.value())
    from TreeMaker.Utils.leptonproducer_cfi import leptonproducer
    process.LeptonsNew = leptonproducer.clone(
        elecIsoValue       = cms.double(0.1), # only has an effect when used with miniIsolation
        UseMiniIsolation   = cms.bool(True),
        METTag             = METTag  ,
        rhoCollection      = cms.InputTag("fixedGridRhoFastjetCentralNeutral")
    )
    # from: https://indico.cern.ch/event/732971/contributions/3022843/attachments/1658685/2656462/eleIdTuning.pdf
    (TMeras.TM2017 | TMeras.TM2018).toModify(process.LeptonsNew,
        # barrel electrons
        eb_ieta_cut        = cms.vdouble(0.0126,  0.0112,  0.0106,  0.0104),
        eb_deta_cut        = cms.vdouble(0.00463, 0.00377, 0.0032,  0.00255),
        eb_dphi_cut        = cms.vdouble(0.148,   0.0884,  0.0547,  0.022),
        eb_hovere_cut      = cms.vdouble(0.05,    0.05,    0.046,   0.026),
        eb_hovere_cut2     = cms.vdouble(1.16,    1.16,    1.16,    1.15),
        eb_hovere_cut3     = cms.vdouble(0.0324,  0.0324,  0.0324,  0.0324),
        eb_ooeminusoop_cut = cms.vdouble(0.209,   0.193,   0.184,   0.159),
        eb_d0_cut          = cms.vdouble(0.05,    0.05,    0.05,    0.05),
        eb_dz_cut          = cms.vdouble(0.10,    0.10,    0.10,    0.10),
        eb_misshits_cut    = cms.vint32 (2,       1,       1,       1),
        # endcap electrons
        ee_ieta_cut        = cms.vdouble(0.0457,  0.0425,  0.0387,  0.0353),
        ee_deta_cut        = cms.vdouble(0.00814, 0.00674, 0.00632, 0.00501),
        ee_dphi_cut        = cms.vdouble(0.19,    0.169,   0.0394,  0.0236),
        ee_hovere_cut      = cms.vdouble(0.05,    0.0441,  0.0275,  0.0188),
        ee_hovere_cut2     = cms.vdouble(2.54,    2.54,    2.52,    2.06),
        ee_hovere_cut3     = cms.vdouble(0.183,   0.183,   0.183,   0.183),
        ee_ooeminusoop_cut = cms.vdouble(0.132,   0.111,   0.0721,  0.0197),
        ee_d0_cut          = cms.vdouble(0.10,    0.10,    0.10,    0.10),
        ee_dz_cut          = cms.vdouble(0.20,    0.20,    0.20,    0.20),
        ee_misshits_cut    = cms.vint32 (3,       1,       1,       1),
        # common electrons
        hovere_constant    = cms.bool(False),
        # from: https://github.com/cms-sw/cmssw/blob/1fbada01f097fbd446e7a431140f83bc9f5a0ff0/RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt
        electronEAValues   = cms.vdouble(0.1440, 0.1562, 0.1032, 0.0859, 0.1116, 0.1321, 0.1654),
    )
    TMeras.TM2017.toModify(process.LeptonsNew,
        # new collection from reco tool (to get user floats)
        ElectronTag = cms.InputTag('slimmedElectrons','',process.name_()),
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

        # some filters need to be rerun
        from RecoMET.METFilters.ecalBadCalibFilter_cfi import ecalBadCalibFilter
        process.ecalBadCalibReducedFilter = ecalBadCalibFilter.clone(
            EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
            ecalMinEt = cms.double(50.),
            baddetEcal = cms.vuint32([
                872439604,872422825,872420274,872423218,
                872423215,872416066,872435036,872439336,
                872420273,872436907,872420147,872439731,
                872436657,872420397,872439732,872439339,
                872439603,872422436,872439861,872437051,
                872437052,872420649,872422436,872421950,
                872437185,872422564,872421566,872421695,
                872421955,872421567,872437184,872421951,
                872421694,872437056,872437057,872437313
            ]),
            taggingMode = cms.bool(True),
        )
        process.ecalBadCalibReducedExtraFilter = process.ecalBadCalibReducedFilter.clone(
            baddetEcal = cms.vuint32([
                872439604,872422825,872420274,872423218,
                872423215,872416066,872435036,872439336,
                872420273,872436907,872420147,872439731,
                872436657,872420397,872439732,872439339,
                872439603,872422436,872439861,872437051,
                872437052,872420649,872421950,872437185,
                872422564,872421566,872421695,872421955,
                872421567,872437184,872421951,872421694,
                872437056,872437057,872437313,872438182,
                872438951,872439990,872439864,872439609,
                872437181,872437182,872437053,872436794,
                872436667,872436536,872421541,872421413,
                872421414,872421031,872423083,872421439
            ])
        )
        self.VarsBool.extend(['ecalBadCalibReducedFilter','ecalBadCalibReducedExtraFilter'])

        process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
        process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
        process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadChargedCandidateFilter.taggingMode = True
        self.VarsBool.extend(['BadChargedCandidateFilter'])

        process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
        process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
        process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadPFMuonFilter.taggingMode = True
        self.VarsBool.extend(['BadPFMuonFilter'])

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
    self.VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales','TriggerProducer:TriggerVersion'])
    self.VectorString.extend(['TriggerProducer:TriggerNames'])
    if "SingleElectron" in process.source.fileNames[0] or "EGamma" in process.source.fileNames[0]:
        process.TriggerProducer.saveHLTObj = cms.bool(True)
        process.TriggerProducer.saveHLTObjPath = cms.string("HLT_Ele27_WPTight_Gsf_v")
        process.TriggerProducer.saveHLTObjName = cms.string("HLTElectronObjects")
        self.VectorTLorentzVector.extend(['TriggerProducer:HLTElectronObjects'])
    elif "SingleMuon" in process.source.fileNames[0]:
        process.TriggerProducer.saveHLTObj = cms.bool(True)
        process.TriggerProducer.saveHLTObjPath = cms.string("HLT_Mu50_v")
        process.TriggerProducer.saveHLTObjName = cms.string("HLTMuonObjects")
        self.VectorTLorentzVector.extend(['TriggerProducer:HLTMuonObjects'])

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
        JERPatch = cms.string('sqlite_file:'+self.jerfile+'.db')

        process.jer = cms.ESSource("PoolDBESSource",CondDBSetup,
            connect = JERPatch,
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

    # get updated QG training
    QGPatch = cms.string('sqlite_file:data/QGL_cmssw8020_v2.db')

    process.qgdb = cms.ESSource("PoolDBESSource",CondDBSetup,
        connect = QGPatch,
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
        SkipTag=SkipTag,
        METfix=self.doMETfix,
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
        doECFs = not TMeras.TM80X.isChosen(), # temporarily disabled
    )
    TMeras.TM80X.toModify(process.JetPropertiesAK8,
        NsubjettinessTau1 = cms.vstring('NjettinessAK8Puppi94Xlike:tau1'),
        NsubjettinessTau2 = cms.vstring('NjettinessAK8Puppi94Xlike:tau2'),
        NsubjettinessTau3 = cms.vstring('NjettinessAK8Puppi94Xlike:tau3'),
#        ecfN2b1 = cms.vstring('ak8PFJetsPuppi94XlikeSoftDropValueMap:nb1AK8Puppi94XlikeSoftDropN2'),
#        ecfN2b2 = cms.vstring('ak8PFJetsPuppi94XlikeSoftDropValueMap:nb2AK8Puppi94XlikeSoftDropN2'),
#        ecfN3b1 = cms.vstring('ak8PFJetsPuppi94XlikeSoftDropValueMap:nb1AK8Puppi94XlikeSoftDropN3'),
#        ecfN3b2 = cms.vstring('ak8PFJetsPuppi94XlikeSoftDropValueMap:nb2AK8Puppi94XlikeSoftDropN3'),
        prunedMass = cms.vstring('ak8PFJetsPuppi94XlikePrunedMass'),
        softDropMass = cms.vstring('SoftDrop'),
        subjets = cms.vstring('SoftDrop'),
        SJbDiscriminatorCSV = cms.vstring('SoftDrop', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    )
    if self.tchannel:
        process.JetPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8PuppiNoCut:tau1')
        process.JetPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8PuppiNoCut:tau2')
        process.JetPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8PuppiNoCut:tau3')
        process.JetPropertiesAK8.ecfN2b1 = cms.vstring('ak8PFJetsPuppiNoCutSoftDropValueMap:nb1AK8PuppiNoCutSoftDropN2')
        process.JetPropertiesAK8.ecfN2b2 = cms.vstring('ak8PFJetsPuppiNoCutSoftDropValueMap:nb2AK8PuppiNoCutSoftDropN2')
        process.JetPropertiesAK8.ecfN3b1 = cms.vstring('ak8PFJetsPuppiNoCutSoftDropValueMap:nb1AK8PuppiNoCutSoftDropN3')
        process.JetPropertiesAK8.ecfN3b2 = cms.vstring('ak8PFJetsPuppiNoCutSoftDropValueMap:nb2AK8PuppiNoCutSoftDropN3')
        process.JetPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsPuppiNoCutPrunedMass')
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

    ## ----------------------------------------------------------------------------------------------
    ## GenJet variables
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        # store all genjets
        self.VectorRecoCand.extend ( [ 'slimmedGenJets(GenJets)' ] )

        from TreeMaker.Utils.subJetSelection_cfi import SubGenJetSelection

        process.GenHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        self.VectorBool.extend(['GenHTJets:SubJetMask(GenJets_HTMask)'])

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
        self.VectorBool.extend(['GenMHTJets:SubJetMask(GenJets_MHTMask)'])

        # make gen MHT
        from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
        process.GenMHT = mhtdouble.clone(
            JetTag  = cms.InputTag('GenMHTJets'),
        )
        self.VarsDouble.extend(['GenMHT:Pt(GenMHT)','GenMHT:Phi(GenMHTPhi)'])

        # substructure for genjets
        from RecoJets.Configuration.RecoGenJets_cff import ak8GenJetsNoNu as ak8GenJetsNoNuDefault
        from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
        process.ak8GenJetsPruned = ak8GenJetsNoNuDefault.clone(
            SubJetParameters,
            usePruning = cms.bool(True),
            useExplicitGhosts = cms.bool(True),
            writeCompound = cms.bool(True),
            jetCollInstanceName=cms.string("SubJets"),
            jetPtMin = 0. if self.tchannel else 170.,
            doAreaFastjet = cms.bool(False),
            src = GenParticlesForJetTag,
        )
        process.ak8GenJetsSoftDrop = ak8GenJetsNoNuDefault.clone(
            useSoftDrop = cms.bool(True),
            zcut = cms.double(0.1),
            beta = cms.double(0.0),
            R0   = cms.double(0.5),
            useExplicitGhosts = cms.bool(True),
            writeCompound = cms.bool(True),
            jetCollInstanceName=cms.string("SubJets"),
            jetPtMin = 0. if self.tchannel else 170.,
            src = GenParticlesForJetTag,
        )

        process.ak8GenJetProperties = cms.EDProducer("GenJetProperties",
            GenJetTag = GenJetAK8Tag,
            PrunedGenJetTag = cms.InputTag("ak8GenJetsPruned"),
            SoftDropGenJetTag = cms.InputTag("ak8GenJetsSoftDrop"),
            distMax = cms.double(0.8),
            jetPtFilter = cms.double(0. if self.tchannel else 150),
        )
        self.VectorDouble.extend([
            'ak8GenJetProperties:prunedMass(GenJetsAK8_prunedMass)',
            'ak8GenJetProperties:softDropMass(GenJetsAK8_softDropMass)',
        ])
        self.VectorInt.extend([
            'ak8GenJetProperties:multiplicity(GenJetsAK8_multiplicity)',
        ])
        # store AK8 genjets above pt cut
        self.VectorRecoCand.extend (['ak8GenJetProperties(GenJetsAK8)'])

    ## ----------------------------------------------------------------------------------------------
    ## Prefiring weights
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.L1ECALNonPrefiringProbProducer_cfi import L1ECALNonPrefiringProbProducer
    prefiringDataEra = cms.PSet(value = cms.string(""))
    TMeras.TM2016.toModify(prefiringDataEra, value = "2016BtoH")
    TMeras.TM2017.toModify(prefiringDataEra, value = "2017BtoF")
    if len(prefiringDataEra.value.value())>0:
        process.L1ECALNonPrefiringProbProducer = L1ECALNonPrefiringProbProducer.clone(
            TheJets = JetTag,
            DataEra = prefiringDataEra.value,
            L1Maps = cms.string('data/L1PrefiringMaps_new.root'),
        )
        self.VarsDouble.extend([
            'L1ECALNonPrefiringProbProducer:NonPrefiringProb',
            'L1ECALNonPrefiringProbProducer:NonPrefiringProbUp',
            'L1ECALNonPrefiringProbProducer:NonPrefiringProbDown',
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
        JetTag = cms.InputTag('HTJets'),
        geninfo = cms.untracked.bool(self.geninfo),
        InfTagAK8 = JetAK8TagInf,
    )
    self.VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)','MET:CaloPt(CaloMET)','MET:CaloPhi(CaloMETPhi)','MET:PFCaloPtRatio(PFCaloMETRatio)','MET:Significance(METSignificance)'])
#    self.VarsDouble.extend(['MET:RawPt(RawMET)','MET:RawPhi(RawMETPhi)'])
    if self.geninfo:
        self.VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        self.VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    if self.doMETfix:
        process.METOrig = process.MET.clone(
            METTag = METTagOrig
        )
        self.VarsDouble.extend(['METOrig:Pt(METOrig)','METOrig:Phi(METPhiOrig)'])
#        self.VarsDouble.extend(['METOrig:RawPt(RawMETOrig)','METOrig:RawPhi(RawMETPhiOrig)'])
        if self.geninfo:
            self.VectorDouble.extend(['METOrig:PtUp(METOrigUp)', 'METOrig:PtDown(METOrigDown)', 'METOrig:PhiUp(METPhiOrigUp)', 'MET:PhiDown(METPhiOrigDown)'])

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
            JetTag = JetAK8Tag,
            MetTag = METTag,
            GenMetTag = cms.InputTag("genMetTrue"),
            GenTag = cms.InputTag("prunedGenParticles"),
            GenJetTag = GenJetAK8Tag,
            coneSize = cms.double(0.8),
            DarkStableIDs = cms.vuint32(51,52,53),
            DarkQuarkIDs = cms.vuint32(4900101),
            DarkMediatorIDs = cms.vuint32(4900023),
            DarkHadronIDs = cms.vuint32(4900111,4900113,4900211,4900213),
            DarkGluonIDs = cms.vuint32(4900021),
            SMQuarkIDs = cms.vuint32(1,2,3,4,5,6),
        )
        if self.tchannel:
            process.HiddenSector.DarkQuarkIDs = [4900101,4900102]
            process.HiddenSector.DarkMediatorIDs = [4900001,4900002,4900003,4900004,4900005,4900006]
        self.VarsDouble.extend([
            'HiddenSector:MJJ(MJJ_AK8)',
            'HiddenSector:Mmc(Mmc_AK8)',
            'HiddenSector:MT(MT_AK8)',
            'HiddenSector:GenMT2(GenMT2_AK8)',
            'HiddenSector:DeltaPhi1(DeltaPhi1_AK8)',
            'HiddenSector:DeltaPhi2(DeltaPhi2_AK8)',
            'HiddenSector:DeltaPhiMin(DeltaPhiMin_AK8)',
        ])
        if self.geninfo:
            self.VectorBool.extend([
                'HiddenSector:isHV(JetsAK8_isHV)'
            ])
            if self.tchannel:
                self.VectorInt.extend([
                    'HiddenSector:hvCategory(GenJetsAK8_hvCategory)',
                    'HiddenSector:MT2JetsID(GenJetsAK8_MT2JetsID)',
                    'HiddenSector:genIndex(JetsAK8_genIndex)'
                ])
                self.VectorDouble.extend([
                    'HiddenSector:darkPtFrac(GenJetsAK8_darkPtFrac)'
                ])
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
