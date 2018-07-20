# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(self,process):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
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
        # mother and LSP masses for SUSY signal scans
        # branches always added, but only have values for fastsim samples
        # needed for WeightProducer
        from TreeMaker.Utils.susyscan_cfi import SusyScanProducer
        process.SusyScan = SusyScanProducer.clone(
            shouldScan = cms.bool(self.fastsim and self.signal and (not self.pmssm)),
            debug = cms.bool(False),
            isLHE = cms.bool(False)
        )
        self.VarsDouble.extend(['SusyScan:SusyMotherMass','SusyScan:SusyLSPMass'])
        
        # pMSSM ID for identifying the pMSSM model point
        from TreeMaker.Utils.pmssm_cfi import PmssmProducer
        process.Pmssm = PmssmProducer.clone(
            shouldScan = cms.bool(self.pmssm),
            debug = cms.bool(False),
            xsecFilename = cms.string('data/pmssm-xsecs-scan1.txt'),
        )
        self.VarsDouble.extend(['Pmssm:PmssmId'])


    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],self.fastsim and self.signal, self.pmssm)
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string(self.pufile)
        self.VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        self.VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo and self.doPDFs:
        process.PDFWeights = cms.EDProducer('PDFWeightProducer')
        self.VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights'])
        self.VectorInt.extend(['PDFWeights:PDFids'])

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

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    if self.geninfo:
        process.genParticles = cms.EDProducer("GenParticlesProducer",
            genCollection = cms.InputTag("prunedGenParticles"),
            debug = cms.bool(False),
            childIds = cms.vint32(1,2,3,4,5,11,12,13,14,15,16,22),
            parentIds = cms.vint32(
                1,2,6,23,24,25,
                1000021,1000022,1000023,1000024,1000025,1000035,1000037,1000039,
                1000001,1000002,1000003,1000004,1000005,1000006,
                2000001,2000002,2000003,2000004,2000005,2000006,
                4900023,4900101,4900111,4900211,
                5000001,5000002,
            ),
            keepIds = cms.vint32(6,23,24,25),
            keepFirst = cms.bool(True),
        )
        # store gluons for signals with Higgs
        if "T5qqqqZH" in process.source.fileNames[0]: process.genParticles.childIds.append(21)
        self.VectorTLorentzVector.append("genParticles(GenParticles)")
        self.VectorInt.append("genParticles:PdgId(GenParticles_PdgId)")
        self.VectorInt.append("genParticles:Status(GenParticles_Status)")
        self.VectorInt.append("genParticles:Parent(GenParticles_ParentIdx)")
        self.VectorInt.append("genParticles:ParentId(GenParticles_ParentId)")
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

    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------

    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
    
    # default miniAOD tags
    JetTag = cms.InputTag('slimmedJets')
    JetAK8Tag = cms.InputTag('slimmedJetsAK8')
    METTag = cms.InputTag('slimmedMETs')
    
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
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PF"),
                    label  = cms.untracked.string("AK4PF")
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
        
        updateJetCollection(
            process,
            jetSource = cms.InputTag('slimmedJets'),
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK4PFchs', levels, 'None')
        )
        
        JetTag = cms.InputTag('updatedPatJetsUpdatedJEC')
        
        # also update the corrections for AK8 jets
        updateJetCollection(
            process,
            jetSource = cms.InputTag('slimmedJetsAK8'),
            labelName = 'AK8',
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK8PFPuppi', levels, 'None')
        )
        
        JetAK8Tag = cms.InputTag('updatedPatJetsAK8UpdatedJEC')
        
        # update the MET to account for the new JECs
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not self.geninfo, # controls gen met
            reapplyJEC=False,
            fixEE2017=self.doMETfix,
        )
        METTag = cms.InputTag('slimmedMETs','',process.name_())

        # additional run to keep orig values
        if self.doMETfix:
            runMetCorAndUncFromMiniAOD(
                process,
                isData=not self.geninfo, # controls gen met
                reapplyJEC=False,
                postfix="Orig"
            )
            METTagOrig = cms.InputTag('slimmedMETsOrig')
            MHTJetTagExt = cms.InputTag("PFCandidateJetsWithEEnoise","jets","process.name_())
        else:
            METTagOrig = None
            MHTJetTagExt = None

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
    from TreeMaker.Utils.leptonproducer_cfi import leptonproducer
    process.LeptonsNew = leptonproducer.clone(
        elecIsoValue       = cms.double(0.1), # only has an effect when used with miniIsolation
        UseMiniIsolation   = cms.bool(True),
        METTag             = METTag  ,
        rhoCollection      = cms.InputTag("fixedGridRhoFastjetCentralNeutral")  
    )
    TMeras.TM2017.toModify(process.LeptonsNew,
        # barrel electrons
        eb_ieta_cut        = cms.vdouble(0.0128,  0.0105,  0.0105,  0.0104),
        eb_deta_cut        = cms.vdouble(0.00523, 0.00387, 0.00365, 0.00353),
        eb_dphi_cut        = cms.vdouble(0.159,   0.0716,  0.0588,  0.0499),
        eb_hovere_cut      = cms.vdouble(0.05,    0.05,    0.026,   0.026),
        eb_ooeminusoop_cut = cms.vdouble(0.193,   0.129,   0.0327,  0.0278),
        eb_d0_cut          = cms.vdouble(0.05,    0.05,    0.05,    0.05),
        eb_dz_cut          = cms.vdouble(0.10,    0.10,    0.10,    0.10),
        eb_misshits_cut    = cms.vint32 (2,       1,       1,       1),
        # endcap electrons
        ee_ieta_cut        = cms.vdouble(0.0445,  0.0356,  0.0309,  0.0305),
        ee_deta_cut        = cms.vdouble(0.00984, 0.0072,  0.00625, 0.00567),
        ee_dphi_cut        = cms.vdouble(0.157,   0.147,   0.0355,  0.0165),
        ee_hovere_cut      = cms.vdouble(0.05,    0.0414,  0.026,   0.026),
        ee_ooeminusoop_cut = cms.vdouble(0.0962,  0.0875,  0.0335,  0.0158),
        ee_d0_cut          = cms.vdouble(0.10,    0.10,    0.10,    0.10),
        ee_dz_cut          = cms.vdouble(0.20,    0.20,    0.20,    0.20),
        ee_misshits_cut    = cms.vint32 (3,       1,       1,       1),
        # common electrons
        hovere_constant    = cms.bool(False),
        electronEAValues   = cms.vdouble(0.1566, 0.1626, 0.1073, 0.0854, 0.1051, 0.1204, 0.1524),
            # Newer values exist at https://github.com/lsoffi/cmssw/blob/CMSSW_9_2_X_TnP/RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt,
            #  but the SUSY group says to use the older values as of 04/17/2018 (https://twiki.cern.ch/twiki/bin/view/CMS/SUSLeptonSF#Electrons).
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
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        saveHLTObj = cms.bool("SingleElectron" in process.source.fileNames[0]),
        triggerNameList = _triggerNameList
    )
    self.VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales','TriggerProducer:TriggerVersion'])
    self.VectorString.extend(['TriggerProducer:TriggerNames'])
    if "SingleElectron" in process.source.fileNames[0]:
        self.VectorTLorentzVector.extend(['TriggerProducer:HLTElectronObjects'])

    if not self.geninfo:
        from TreeMaker.Utils.prescaleweightproducer_cfi import prescaleweightProducer
        process.PrescaleWeightProducer = prescaleweightProducer.clone()
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
            ),
        )

        process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')

    # skip all jet smearing and uncertainties for data
    from TreeMaker.TreeMaker.JetDepot import JetDepot
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo

    if self.geninfo and self.systematics:
        # JEC unc up
        process, JetTagJECupTmp, JetTagJECup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=1,
            storeJec=True, # get JER unc value (in intermediate tag Tmp)
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get JER smearing factor w/ JEC variation
        )
        process = self.makeJetVars(process,
            JetTag=JetTagJECup,
            suff='JECup',
            skipGoodJets=False,
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JEC",
        )
        
        # JEC unc down
        process, _, JetTagJECdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=-1,
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get JER smearing factor w/ JEC variation
        )
        process = self.makeJetVars(process,
            JetTag=JetTagJECdown,
            suff='JECdown',
            skipGoodJets=False,
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JEC",
        )

        # JER unc up
        process, _, JetTagJERup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=1,
            storeJer=1,
        )
        process = self.makeJetVars(process,
            JetTag=JetTagJERup,
            suff='JERup',
            skipGoodJets=False,
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JER",
        )
        
        # JER unc down
        process, _, JetTagJERdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=-1,
            storeJer=1,
        )
        process = self.makeJetVars(process,
            JetTag=JetTagJERdown,
            suff='JERdown',
            skipGoodJets=False,
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JER",
        )

        # append factors to central collection
        process, JetTag = addJetInfo(process, JetTag, [JetTagJECupTmp.value(),JetTagJERup.value(),JetTagJERdown.value()], [])

    if self.geninfo:
        # finally, do central smearing and replace jet tag
        process, _, JetTag = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get central jet smearing factor
        )
        
    ## ----------------------------------------------------------------------------------------------
    ## Jet variables
    ## ----------------------------------------------------------------------------------------------

    # get updated QG training
    QGPatch = cms.string('sqlite_file:data/QGL_80X.db')
    if os.getenv('GC_CONF'): 
        QGPatch = cms.string('sqlite_file:../src/data/QGL_80X.db')

    process.qgdb = cms.ESSource("PoolDBESSource",CondDBSetup,
        connect = QGPatch,
        toGet   = cms.VPSet(
            cms.PSet(
                record = cms.string('QGLikelihoodRcd'),
                tag    = cms.string('QGLikelihoodObject_80X_AK4PFchs'),
                label  = cms.untracked.string('QGL_AK4PFchs')
            ),
            cms.PSet(
                record = cms.string('QGLikelihoodRcd'),
                tag    = cms.string('QGLikelihoodObject_80X_AK4PFchs_antib'),
                label  = cms.untracked.string('QGL_AK4PFchs_antib')
            ),
        )
    )
    process.es_prefer_qg = cms.ESPrefer("PoolDBESSource","qgdb")
    
    # get QG tagging discriminant
    process.QGTagger = cms.EDProducer('QGTagger',
        srcJets	            = JetTag,
        jetsLabel           = cms.string('QGL_AK4PFchs'),
        srcRho              = cms.InputTag('fixedGridRhoFastjetAll'),		
        srcVertexCollection	= cms.InputTag('offlinePrimaryVerticesWithBS'),
        useQualityCuts	    = cms.bool(False)
    )
    
    # add userfloats & update tag
    process, JetTag = addJetInfo(process, JetTag, ['QGTagger:qgLikelihood','QGTagger:ptD', 'QGTagger:axis2', 'QGTagger:axis1'], ['QGTagger:mult'])
    
    process = self.makeJetVars(process,
        JetTag=JetTag,
        suff='',
        skipGoodJets=False,
        storeProperties=2,
        SkipTag=SkipTag,
        MHTJetTagExt = MHTJetTagExt,
    )
    if self.geninfo and self.systematics:
        process.JetProperties.properties.extend(["jerFactorUp","jerFactorDown","jecUnc"])
        process.JetProperties.jerFactorUp = cms.vstring(JetTagJERup.value())
        process.JetProperties.jerFactorDown = cms.vstring(JetTagJERdown.value())
        process.JetProperties.jecUnc = cms.vstring(JetTagJECupTmp.value())
        self.VectorDouble.extend([
            'JetProperties:jecUnc(Jets_jecUnc)',
            'JetProperties:jerFactorUp(Jets_jerFactorUp)',
            'JetProperties:jerFactorDown(Jets_jerFactorDown)',
        ])

    # get QG tagging discriminant for subjets
    SubjetTag = cms.InputTag('slimmedJetsAK8PFPuppiSoftDropPacked:SubJets')
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
            OldName = cms.string("SoftDropPuppi"),
            NewName = cms.string("SoftDropPuppiUpdated"),
        )
    )
    JetAK8Tag = JetAK8TagSJU
    
    # get double b-tagger (w/ miniAOD customizations)
    process.load("RecoBTag.ImpactParameter.pfImpactParameterAK8TagInfos_cfi")
    process.pfImpactParameterAK8TagInfos.primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.pfImpactParameterAK8TagInfos.candidates = cms.InputTag("packedPFCandidates")
    process.pfImpactParameterAK8TagInfos.jets = JetAK8Tag
    process.load("RecoBTag.SecondaryVertex.pfInclusiveSecondaryVertexFinderAK8TagInfos_cfi")
    process.pfInclusiveSecondaryVertexFinderAK8TagInfos.extSVCollection = cms.InputTag("slimmedSecondaryVertices")
    process.pfInclusiveSecondaryVertexFinderAK8TagInfos.trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfos")
    process.load("RecoBTag.SecondaryVertex.pfBoostedDoubleSVAK8TagInfos_cfi")
    process.load("RecoBTag.SecondaryVertex.candidateBoostedDoubleSecondaryVertexAK8Computer_cfi")
    process.load("RecoBTag.SecondaryVertex.pfBoostedDoubleSecondaryVertexAK8BJetTags_cfi")

    _floatsAK8 = []
    if self.deepAK8:
        from TreeMaker.Utils.deepak8producer_cfi import DeepAK8Producer
        process.deepAK8 = DeepAK8Producer.clone(
            JetAK8 = JetAK8Tag
        )
        _floatsAK8 = ['deepAK8:tDiscriminatorDeep','deepAK8:wDiscriminatorDeep','deepAK8:zDiscriminatorDeep','deepAK8:hDiscriminatorDeep']

    # add discriminator and update tag
    process, JetAK8Tag = addJetInfo(process, JetAK8Tag, _floatsAK8, [], cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTags")))

    # apply jet ID and get properties
    process = self.makeJetVarsAK8(process,
        JetTag=JetAK8Tag,
        suff='AK8',
        storeProperties=2,
    )    

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
    
        # store all AK8 genjets
        self.VectorRecoCand.extend ( [ 'slimmedGenJetsAK8(GenJetsAK8)' ] )

        # substructure for genjets
        from RecoJets.Configuration.RecoGenJets_cff import ak8GenJetsNoNu
        from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
        process.ak8GenJetsPruned = ak8GenJetsNoNu.clone(
            SubJetParameters,
            usePruning = cms.bool(True),
            useExplicitGhosts = cms.bool(True),
            writeCompound = cms.bool(True),
            jetCollInstanceName=cms.string("SubJets"),
            jetPtMin = 170.,
            doAreaFastjet = cms.bool(False),
            src = cms.InputTag("packedGenParticles"),
        )
        process.ak8GenJetsSoftDrop = ak8GenJetsNoNu.clone(
            useSoftDrop = cms.bool(True),
            zcut = cms.double(0.1),
            beta = cms.double(0.0),
            R0   = cms.double(0.5),
            useExplicitGhosts = cms.bool(True),
            writeCompound = cms.bool(True),
            jetCollInstanceName=cms.string("SubJets"),
            jetPtMin = 170.,
            src = cms.InputTag("packedGenParticles"),
        )

        process.ak8GenJetProperties = cms.EDProducer("GenJetProperties",
            GenJetTag = cms.InputTag("slimmedGenJetsAK8"),
            PrunedGenJetTag = cms.InputTag("ak8GenJetsPruned"),
            SoftDropGenJetTag = cms.InputTag("ak8GenJetsSoftDrop"),
            distMax = cms.double(0.8),
        )
        self.VectorDouble.extend([
            'ak8GenJetProperties:prunedMass(GenJetsAK8_prunedMass)',
            'ak8GenJetProperties:softDropMass(GenJetsAK8_softDropMass)',
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
    )
    self.VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)','MET:CaloPt(CaloMET)','MET:CaloPhi(CaloMETPhi)','MET:PFCaloPtRatio(PFCaloMETRatio)','MET:Significance(METSignificance)'])
    if self.geninfo:
        self.VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        self.VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    if self.doMETfix:
        process.METOrig = process.MET.clone(
            METTag = METTagOrig
        )
        self.VarsDouble.extend(['METOrig:Pt(METOrig)','METOrig:Phi(METPhiOrig)'])

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
            GenTag = cms.InputTag("prunedGenParticles"),
            DarkIDs = cms.vuint32(4900211),
        )
        self.VarsDouble.extend([
            'HiddenSector:MJJ(MJJ_AK8)',
            'HiddenSector:Mmc(Mmc_AK8)',
            'HiddenSector:MT(MT_AK8)',
            'HiddenSector:DeltaPhi1(DeltaPhi1_AK8)',
            'HiddenSector:DeltaPhi2(DeltaPhi2_AK8)',
            'HiddenSector:DeltaPhiMin(DeltaPhiMin_AK8)',
        ])

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

    return process

