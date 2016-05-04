# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outfile,
reportfreq=10,
dataset="",
globaltag="",
numevents=1000,
lostlepton=False,
hadtau=False,
applybaseline=False,
doZinv=False,
debugtracks=False,
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False,
QCD=False,
doPDFs=False,
fastsim=False,
signal=False
):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    process.GlobalTag.globaltag = globaltag

    # CMSSW version sniffing
    CMSSWVER = os.getenv("CMSSW_VERSION")
    CMSSWVER_parts = CMSSWVER.split("_")

    # define if mt cut should be applied and the value (less than 0 means no cut)
    mtcut = cms.double(100)
    print "Calculation with mtcut: "+ str(mtcut)

    # log output
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = reportfreq
    process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
#        wantSummary = cms.untracked.bool(True) # off by default
    )

    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numevents)
    )
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(dataset)
    )
    if len(jsonfile)>0: process.source.lumisToProcess = LumiList.LumiList(filename = jsonfile).getVLuminosityBlockRange()

    # output file
    process.TFileService = cms.Service("TFileService",
        fileName = cms.string(outfile+".root")
    )
    # branches for treemaker
    VectorRecoCand       = cms.vstring() 
    VarsDouble           = cms.vstring()
    VarsInt              = cms.vstring()
    VarsBool             = cms.vstring()
    VectorTLorentzVector = cms.vstring()
    VectorDouble         = cms.vstring()
    VectorString         = cms.vstring()
    VectorInt            = cms.vstring()
    VectorBool           = cms.vstring()
    
    # sequence for baseline producers
    process.Baseline = cms.Sequence()

    # configure treemaker
    from TreeMaker.TreeMaker.treeMaker import TreeMaker
    process.TreeMaker2 = TreeMaker.clone(
        TreeName             = cms.string("PreSelection"),
        VectorRecoCand       = VectorRecoCand, 
        VarsDouble           = VarsDouble,
        VarsInt              = VarsInt,
        VarsBool             = VarsBool,
        VectorTLorentzVector = VectorTLorentzVector,
        VectorDouble         = VectorDouble,
        VectorInt            = VectorInt,
        VectorString         = VectorString,
        VectorBool           = VectorBool,
    )

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Standard producers
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## SUSY scan info
    ## ----------------------------------------------------------------------------------------------
    if geninfo :
        # mother and LSP masses for SUSY signal scans
        # branches always added, but only have values for fastsim samples
        # needed for WeightProducer
        from TreeMaker.Utils.susyscan_cfi import SusyScanProducer
        process.SusyScan = SusyScanProducer.clone(
            shouldScan = cms.bool(fastsim and signal),
            debug = cms.bool(False)
        )
        process.Baseline += process.SusyScan
        VarsDouble.extend(['SusyScan:SusyMotherMass','SusyScan:SusyLSPMass'])
    
    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],fastsim and signal)
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string("TreeMaker/Production/test/data/PileupHistograms_1117.root")
        process.Baseline += process.WeightProducer
        VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if doPDFs:
        process.PDFWeights = cms.EDProducer('PDFWeightProducer')
        process.Baseline += process.PDFWeights
        VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights'])
        VectorInt.extend(['PDFWeights:PDFids'])

    ## ----------------------------------------------------------------------------------------------
    ## GenHT for stitching together MC samples
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        process.GenHT = cms.EDProducer('GenHTProducer')
        process.Baseline += process.GenHT
        VarsDouble.extend(['GenHT:genHT'])
    
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
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])
    # also store total number of vertices without quality checks
    process.nAllVertices = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    process.Baseline += process.nAllVertices
    VarsInt.extend(['nAllVertices'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    if geninfo :
        process.genParticles = cms.EDProducer("GenParticlesProducer",
            genCollection = cms.untracked.InputTag("prunedGenParticles"),
            debug = cms.untracked.bool(False)
        )
        process.Baseline += process.genParticles
        VectorTLorentzVector.append("genParticles(GenParticles)")
        VectorInt.append("genParticles:PdgId(GenParticles_PdgId)")
        VectorInt.append("genParticles:Status(GenParticles_Status)")
        VectorInt.append("genParticles:Parent(GenParticles_ParentIdx)")
        VectorInt.append("genParticles:ParentId(GenParticles_ParentId)")

    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------

    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
    
    # QG tagging DB payload
    qgDatabaseVersion = 'v1' # check https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
    process.QGPoolDBESSource = cms.ESSource("PoolDBESSource",CondDBSetup,
        toGet = cms.VPSet(),
        connect = cms.string('frontier://FrontierProd/CMS_COND_PAT_000'),
    )
    for type in ['AK4PFchs','AK4PFchs_antib']:
        process.QGPoolDBESSource.toGet.extend(
            cms.VPSet(
                cms.PSet(
                    record = cms.string('QGLikelihoodRcd'),
                    tag    = cms.string('QGLikelihoodObject_'+qgDatabaseVersion+'_'+type),
                    label  = cms.untracked.string('QGL_'+type)
                )
            )
        )
    
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    JetTag = cms.InputTag('slimmedJets')
    JetAK8Tag = cms.InputTag('slimmedJetsAK8')
    METTag = cms.InputTag('slimmedMETs')
    if len(jecfile)>0:
        #get name of JECs without any directories
        JECera = jecfile.split('/')[-1]
        JECPatch = cms.string('sqlite_file:'+jecfile+'.db')
        if os.getenv('GC_CONF'): 
            JECPatch = cms.string('sqlite_file:../src/'+jecfile+'.db')

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
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK8PFchs"),
                    label  = cms.untracked.string("AK8PFchs")
                ),
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
        
        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
        process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
            src     = cms.InputTag("slimmedJets"),
            levels  = ['L1FastJet',
                      'L2Relative',
                      'L3Absolute'],
            payload = 'AK4PFchs' # Make sure to choose the appropriate levels and payload here!
        )
        if residual: process.patJetCorrFactorsReapplyJEC.levels.append('L2L3Residual')
        
        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
        process.patJetsReapplyJEC = patJetsUpdated.clone(
            jetSource = cms.InputTag("slimmedJets"),
            jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
        )
        
        process.Baseline += process.patJetCorrFactorsReapplyJEC
        process.Baseline += process.patJetsReapplyJEC
        
        JetTag = cms.InputTag('patJetsReapplyJEC')
        
        # also update the corrections for AK8 jets
        process.patJetCorrFactorsReapplyJECAK8 = patJetCorrFactorsUpdated.clone(
            src     = cms.InputTag("slimmedJetsAK8"),
            levels  = ['L1FastJet',
                      'L2Relative',
                      'L3Absolute'],
            payload = 'AK8PFchs' # Make sure to choose the appropriate levels and payload here!
        )
        if residual: process.patJetCorrFactorsReapplyJECAK8.levels.append('L2L3Residual')
        process.patJetsReapplyJECAK8 = patJetsUpdated.clone(
            jetSource = cms.InputTag("slimmedJetsAK8"),
            jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJECAK8"))
        )
        process.Baseline += process.patJetCorrFactorsReapplyJECAK8
        process.Baseline += process.patJetsReapplyJECAK8
        JetAK8Tag = cms.InputTag('patJetsReapplyJECAK8')
        
        # update the MET to account for the new JECs
        # ref: https://github.com/cms-met/cmssw/blob/METCorUnc74X/PhysicsTools/PatAlgos/test/corMETFromMiniAOD.py
        
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
            jetCollUnskimmed=JetTag.value(),
            jetColl=JetTag.value(),
            postfix="Update"
        )
        if not residual: #skip residuals for data if not used
            process.patPFMetT1T2CorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT1T2SmearCorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2CorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2SmearCorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.shiftedPatJetEnDownUpdate.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
            process.shiftedPatJetEnUpUpdate.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
        if hasattr(process,"slimmedMETsUpdate"):
            delattr(getattr(process,"slimmedMETsUpdate"),"caloMET")
        METTag = cms.InputTag('slimmedMETsUpdate','',process.name_())

    ## ----------------------------------------------------------------------------------------------
    ## IsoTracks
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationCounter

    process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("goodVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(11),
        mTCut               = mtcut,
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
        mTCut               = mtcut,
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
        mTCut               = mtcut,
        METTag              = METTag,
    )

    process.Baseline += process.IsolatedElectronTracksVeto
    process.Baseline += process.IsolatedMuonTracksVeto
    process.Baseline += process.IsolatedPionTracksVeto

    VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

    if debugtracks:
        #NB: this increases the runtime and size of ntuples by ~10x
        #do not turn on unless you really want to save all the isotrack quantities!!!
        #just store the full set of isotrack quantities once
        process.IsolatedPionTracksVeto.debug = cms.bool(True)
        VectorTLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(pfcands)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(pfcands_trkiso)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(pfcands_dzpv)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(pfcands_mT)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(pfcands_chg)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(pfcands_id)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## Electrons/Muons
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.leptonproducer_cfi import leptonproducer

    process.LeptonsNew = leptonproducer.clone(
        MuonTag          = cms.InputTag('slimmedMuons'),
        ElectronTag      = cms.InputTag('slimmedElectrons'),
        PrimaryVertex    = cms.InputTag('offlineSlimmedPrimaryVertices'),
        minElecPt        = cms.double(10),
        maxElecEta       = cms.double(2.5),
        minMuPt          = cms.double(10),
        maxMuEta         = cms.double(2.4),
        UseMiniIsolation = cms.bool(True),
        muIsoValue       = cms.double(0.2),
        elecIsoValue     = cms.double(0.1), # only has an effect when used with miniIsolation
        METTag           = METTag, 
    )
    process.Baseline += process.LeptonsNew
    VarsInt.extend(['LeptonsNew(Leptons)'])
    VectorRecoCand.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])
    VectorInt.extend(['LeptonsNew:MuonCharge(MuonCharge)','LeptonsNew:ElectronCharge(ElectronCharge)'])

    process.LeptonsNewTag = leptonproducer.clone(
        MuonTag          = cms.InputTag('slimmedMuons'),
        ElectronTag      = cms.InputTag('slimmedElectrons'),
        PrimaryVertex    = cms.InputTag('offlineSlimmedPrimaryVertices'),
        minElecPt        = cms.double(20),
        maxElecEta       = cms.double(2.5),
        minMuPt          = cms.double(20),
        maxMuEta         = cms.double(2.4),
        UseMiniIsolation = cms.bool(True),
        muIsoValue       = cms.double(0.2),
        elecIsoValue     = cms.double(0.1), # only has an effect when used with miniIsolation
        METTag           = METTag,
    )
    process.Baseline += process.LeptonsNewTag
    VarsInt.extend(['LeptonsNewTag(TagLeptonHighPT)'])

    ## ----------------------------------------------------------------------------------------------
    ## MET Filters
    ## ----------------------------------------------------------------------------------------------
    
    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree
    
    if not fastsim: # MET filters are not run for fastsim samples

        from TreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer
        process.METFilters = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_METFilters"),
        )
        process.Baseline += process.METFilters
        VarsInt.extend(['METFilters'])
        
        #process.CSCTightHaloFilter = filterDecisionProducer.clone(
        #    trigTagArg1 = cms.string('TriggerResults'),
        #    trigTagArg2 = cms.string(''),
        #    trigTagArg3 = cms.string(tagname),
        #    filterName  = cms.string("Flag_CSCTightHaloFilter"),
        #)
        #process.Baseline += process.CSCTightHaloFilter
        #VarsInt.extend(['CSCTightHaloFilter'])
        
        #run beam halo filter from text list of events
        from TreeMaker.Utils.getEventListFilter_cff import getEventListFilter
        process.CSCTightHaloFilter = getEventListFilter(process.source.fileNames[0],"Dec01","csc2015")
        process.Baseline += process.CSCTightHaloFilter
        VarsBool.extend(['CSCTightHaloFilter'])
        
        #process.HBHENoiseFilter = filterDecisionProducer.clone(
        #    trigTagArg1 = cms.string('TriggerResults'),
        #    trigTagArg2 = cms.string(''),
        #    trigTagArg3 = cms.string(tagname),
        #    filterName  = cms.string("Flag_HBHENoiseFilter"),
        #)
        #process.Baseline += process.HBHENoiseFilter
        #VarsInt.extend(['HBHENoiseFilter'])
        
        #rerun HBHE noise filter manually
        process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
        process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
        process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(False) 
        process.HBHENoiseFilterResultProducer.defaultDecision = cms.string("HBHENoiseFilterResultRun2Loose")
        process.Baseline += process.HBHENoiseFilterResultProducer
        VarsBool.extend(['HBHENoiseFilterResultProducer:HBHENoiseFilterResult(HBHENoiseFilter)'])
        #add HBHE iso noise filter
        VarsBool.extend(['HBHENoiseFilterResultProducer:HBHEIsoNoiseFilterResult(HBHEIsoNoiseFilter)'])

        process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
        process.Baseline += process.EcalDeadCellTriggerPrimitiveFilter
        VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])
        
        process.eeBadScFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(tagname),
            filterName  =   cms.string("Flag_eeBadScFilter"),
            )
        process.Baseline += process.eeBadScFilter
        VarsInt.extend(['eeBadScFilter'])
        
        #run eeBadSc4 filter from text list of events
        process.eeBadSc4Filter = getEventListFilter(process.source.fileNames[0],"Dec01","ecalscn1043093")
        process.Baseline += process.eeBadSc4Filter
        VarsBool.extend(['eeBadSc4Filter'])

    ## ----------------------------------------------------------------------------------------------
    ## Triggers
    ## ----------------------------------------------------------------------------------------------

    # The trigger results are saved to the tree as a vector
    # Three vectors are saved:
    # 1) names of the triggers
    # 2) trigger results
    # 3) trigger prescales
    # the indexing of these vectors must match
    # If the version number of the input trigger name is omitted,
    # any matching trigger will be included (default behavior)

    from TreeMaker.Utils.triggerproducer_cfi import triggerProducer
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = cms.vstring( # list of trigger names
            'HLT_PFHT350_PFMET100_NoiseCleaned_v',
            'HLT_PFHT350_PFMET100_JetIdCleaned_v',
            'HLT_PFMET170_NoiseCleaned_v',
            'HLT_PFMET170_JetIdCleaned_v',
            'HLT_PFHT350_v',
            'HLT_PFHT800_v',
            'HLT_PFHT900_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v',
            'HLT_IsoMu17_eta2p1_v',
            'HLT_PFHT350_PFMET120_NoiseCleaned_v',
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v',
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v',
            'HLT_Mu15_IsoVVVL_BTagCSV07_PFHT400_v',
            'HLT_Mu15_IsoVVVL_PFHT600_v',
            'HLT_Ele15_IsoVVVL_PFHT600_v',
            'HLT_Mu45_eta2p1_v',
            'HLT_Mu50_eta2p1_v',
            'HLT_Mu50_v',
            'HLT_Mu55_v',
            'HLT_Photon75_v',
            'HLT_Photon90_v',
            'HLT_Photon90_CaloIdL_PFHT500_v',
            'HLT_DoubleEle8_CaloIdM_Mass8_PFHT300_v',
            'HLT_Ele27_eta2p1_WP85_Gsf_v',
            'HLT_IsoMu20_eta2p1_IterTrk02_v',
            'HLT_DoubleMu8_Mass8_PFHT300_v',
            'HLT_Ele27_WP85_Gsf_v',
            'HLT_IsoMu20_eta2p1_v',
            'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
            'HLT_DoubleMu18NoFiltersNoVtx_v',
            'HLT_Mu20_v',
            'HLT_QuadJet45_TripleCSV0p5_v',
            'HLT_DoubleJet90_Double30_TripleCSV0p5_v',
            'HLT_Ele15_IsoVVVL_PFHT350_v',
            'HLT_Mu15_IsoVVVL_PFHT350_v',
            'HLT_Ele23_WPLoose_Gsf_v',
            'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v',
            'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v',
            'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT250_v',
            'HLT_DoubleMu8_Mass8_PFHT250_v',
            'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v',
            'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',
            'HLT_PFHT750_4JetPt50_v',
            'HLT_PFHT450_SixJet40_PFBTagCSV0p72_v',
            'HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v',
            'HLT_PFHT350_PFMET100_v',
            'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v',
            'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v',
            'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v',
            'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
            'HLT_DiCentralPFJet55_PFMET110_JetIdCleaned_v',
       )
    )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet variables
    ## ----------------------------------------------------------------------------------------------

    # list of clean tags - ignore jet ID for jets matching these objects
    SkipTag = cms.VInputTag(
        cms.InputTag('LeptonsNew:IdIsoMuon'),
        cms.InputTag('LeptonsNew:IdIsoElectron'),
        cms.InputTag('IsolatedElectronTracksVeto'),
        cms.InputTag('IsolatedMuonTracksVeto'),
        cms.InputTag('IsolatedPionTracksVeto'),
    )
    
    from TreeMaker.TreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=JetTag,
                          suff='',
                          skipGoodJets=False,
                          storeProperties=2,
                          SkipTag=SkipTag
    )
    
    # AK8 jet variables - separate instance of jet properties producer
    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsPropertiesAK8 = jetproperties.clone(
        JetTag       = JetAK8Tag,
        BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        QGTag        = cms.InputTag(""),
        AK8          = cms.bool(True)
    )
    process.Baseline += process.JetsPropertiesAK8
    VectorRecoCand.extend([JetAK8Tag.value()+'(JetsAK8)'])
    VectorDouble.extend(['JetsPropertiesAK8:prunedMass(JetsAK8_prunedMass)',
                         'JetsPropertiesAK8:bDiscriminatorSubjet1(JetsAK8_bDiscriminatorSubjet1CSV)',
                         'JetsPropertiesAK8:bDiscriminatorSubjet2(JetsAK8_bDiscriminatorSubjet2CSV)',
                         'JetsPropertiesAK8:NsubjettinessTau1(JetsAK8_NsubjettinessTau1)',
                         'JetsPropertiesAK8:NsubjettinessTau2(JetsAK8_NsubjettinessTau2)',
                         'JetsPropertiesAK8:NsubjettinessTau3(JetsAK8_NsubjettinessTau3)'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet uncertainty variations
    ## ----------------------------------------------------------------------------------------------

    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    
    #JEC unc up
    process.patJetsJECup = JetUncertaintyProducer.clone(
        JetTag = JetTag,
        jecUncDir = cms.int32(1)
    )
    process.Baseline += process.patJetsJECup
    #get the JEC factor and unc from here
    VectorDouble.extend(['patJetsJECup:jecFactor(Jets_jecFactor)','patJetsJECup:jecUnc(Jets_jecUnc)'])
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=cms.InputTag("patJetsJECup"),
                          suff='JECup',
                          skipGoodJets=False,
                          storeProperties=1,
                          SkipTag=SkipTag
    )

    #JEC unc down
    process.patJetsJECdown = JetUncertaintyProducer.clone(
        JetTag = JetTag,
        jecUncDir = cms.int32(-1)
    )
    process.Baseline += process.patJetsJECdown
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=cms.InputTag("patJetsJECdown"),
                          suff='JECdown',
                          skipGoodJets=False,
                          storeProperties=1,
                          SkipTag=SkipTag
    )

    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('HT'),
        CutValue  = cms.double('500'),
    )
    process.MHTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('MHT:Pt'),
        CutValue  = cms.double('200'),
    )
    if applybaseline:
        process.Baseline += process.HTFilter
        #process.Baseline += process.MHTFilter
    
    ## ----------------------------------------------------------------------------------------------
    ## MET
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = METTag,
        GenMETTag = cms.InputTag("slimmedMETs","",tagname), #original collection used deliberately here
        JetTag = cms.InputTag('HTJets'),
        geninfo = cms.untracked.bool(geninfo),
    )
    process.Baseline += process.MET
    VarsDouble.extend(['MET:Pt(METPt)','MET:Phi(METPhi)','MET:CaloPt(CaloMETPt)','MET:CaloPhi(CaloMETPhi)'])
    if geninfo:
        VarsDouble.extend(['MET:GenPt(GenMETPt)','MET:GenPhi(GenMETPhi)'])
        VectorDouble.extend(['MET:PtUp(METPtUp)', 'MET:PtDown(METPtDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    from TreeMaker.Utils.mt2producer_cfi import mt2Producer
    process.Mt2Producer = mt2Producer.clone(
                JetTag  = cms.InputTag('MHTJets'),
                METTag = METTag
        )
    process.Baseline += process.Mt2Producer
    VarsDouble.extend(['Mt2Producer:mt2(MT2)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # sequence for optional producers
    process.AdditionalSequence = cms.Sequence()
    
    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------
    if hadtau:
        from TreeMaker.TreeMaker.doHadTauBkg import doHadTauBkg
        process = doHadTauBkg(process,geninfo,residual,JetTag)

    ## ----------------------------------------------------------------------------------------------
    ## Lost Lepton Background
    ## ----------------------------------------------------------------------------------------------
    if lostlepton:
        from TreeMaker.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
        process = doLostLeptonBkg(process,geninfo,METTag)

    ## ----------------------------------------------------------------------------------------------
    ## Zinv Background
    ## ----------------------------------------------------------------------------------------------
    if doZinv:
        from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg
        process = doZinvBkg(process,tagname,geninfo,residual)

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## QCD DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    if QCD:
        from TreeMaker.TreeMaker.DeltaPhiQCD import DeltaPhiQCD
        process = DeltaPhiQCD(process,geninfo)

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Final steps
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # create the process path
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.WriteTree = cms.Path(
        process.Baseline *
        process.AdditionalSequence *
#        process.dump *
        process.TreeMaker2
    )
    
    return process

