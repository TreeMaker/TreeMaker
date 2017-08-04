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
hadtaurecluster=False,
applybaseline=False,
doZinv=False,
debugtracks=False,
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False,
jerfile="",
pufile="",
doPDFs=False,
fastsim=False,
signal=False,
pmssm=False,
scenario=""
):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    process.GlobalTag.globaltag = globaltag

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
        fileNames = cms.untracked.vstring(dataset),
        inputCommands = cms.untracked.vstring('keep *','drop LHERunInfoProduct_*_*_*'),
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
    if geninfo:
        # mother and LSP masses for SUSY signal scans
        # branches always added, but only have values for fastsim samples
        # needed for WeightProducer
        from TreeMaker.Utils.susyscan_cfi import SusyScanProducer
        process.SusyScan = SusyScanProducer.clone(
            shouldScan = cms.bool(fastsim and signal and (not pmssm)),
            debug = cms.bool(False),
            isLHE = cms.bool(False)
        )
        VarsDouble.extend(['SusyScan:SusyMotherMass','SusyScan:SusyLSPMass'])
        
        # pMSSM ID for identifying the pMSSM model point
        from TreeMaker.Utils.pmssm_cfi import PmssmProducer
        process.Pmssm = PmssmProducer.clone(
            shouldScan = cms.bool(pmssm),
            debug = cms.bool(False),
            xsecFilename = cms.string('data/pmssm-xsecs-scan1.txt'),
        )
        VarsDouble.extend(['Pmssm:PmssmId'])


    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],fastsim and signal, pmssm)
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string(pufile)
        VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if geninfo and doPDFs:
        process.PDFWeights = cms.EDProducer('PDFWeightProducer')
        VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights'])
        VectorInt.extend(['PDFWeights:PDFids'])

    ## ----------------------------------------------------------------------------------------------
    ## GenHT for stitching together MC samples
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        process.MadHT = cms.EDProducer('GenHTProducer')
        # called madHT, i.e. MadGraph, to distinguish from GenHT from GenJets
        VarsDouble.extend(['MadHT:genHT(madHT)'])
    
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
    VarsInt.extend(['NVtx'])
    # also store total number of vertices without quality checks
    process.nAllVertices = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    VarsInt.extend(['nAllVertices'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    if geninfo :
        process.genParticles = cms.EDProducer("GenParticlesProducer",
            genCollection = cms.untracked.InputTag("prunedGenParticles"),
            debug = cms.untracked.bool(False)
        )
        VectorTLorentzVector.append("genParticles(GenParticles)")
        VectorInt.append("genParticles:PdgId(GenParticles_PdgId)")
        VectorInt.append("genParticles:Status(GenParticles_Status)")
        VectorInt.append("genParticles:Parent(GenParticles_ParentIdx)")
        VectorInt.append("genParticles:ParentId(GenParticles_ParentId)")
        
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
        VectorRecoCand.append("genTops(GenTops)")
        VarsDouble.append("genTops:weight(GenTopWeight)")

    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------

    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
    
    # default miniAOD tags
    JetTag = cms.InputTag('slimmedJets')
    JetAK8Tag = cms.InputTag('slimmedJetsAK8')
    METTag = cms.InputTag('slimmedMETs')
    if scenario=="2016ReMiniAOD03Feb": METTag = cms.InputTag('slimmedMETsMuEGClean')
    
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
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
        
        levels  = ['L1FastJet','L2Relative','L3Absolute']
        if residual: levels.append('L2L3Residual')
        
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
            jetCorrections = ('AK8PFchs', levels, 'None')
        )
        
        JetAK8Tag = cms.InputTag('updatedPatJetsAK8UpdatedJEC')
        
        # update the MET to account for the new JECs
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )
        METTag = cms.InputTag('slimmedMETs','',process.name_())
    else:
        # pointless run of MET tool because it is barely functional
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )

    # keep jets before any further modifications for hadtau
    JetTagBeforeSmearing = JetTag
    # JEC uncertainty - after JECs are updated
    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    process.jecUnc = JetUncertaintyProducer.clone(
        JetTag = JetTag,
        jecUncDir = cms.int32(0)
    )
    _infosToAdd = ['jecUnc']
    if geninfo:
        # JER factors - central, up, down
        from TreeMaker.Utils.smearedpatjet_cfi import SmearedPATJetProducer
        process.jerFactor = SmearedPATJetProducer.clone(
            src = JetTag,
            variation = cms.int32(0),
            store_factor = cms.bool(True)
        )
        process.jerFactorUp = SmearedPATJetProducer.clone(
            src = JetTag,
            variation = cms.int32(1),
            store_factor = cms.bool(True)
        )
        process.jerFactorDown = SmearedPATJetProducer.clone(
            src = JetTag,
            variation = cms.int32(-1),
            store_factor = cms.bool(True)
        )
        _infosToAdd.extend(['jerFactor','jerFactorUp','jerFactorDown'])
    # add userfloat & update tag
    from TreeMaker.TreeMaker.addJetInfo import addJetInfo
    process, JetTag = addJetInfo(process, JetTag, _infosToAdd, [])

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

    VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

    if debugtracks:
        #NB: this increases the runtime and size of ntuples by ~10x
        #do not turn on unless you really want to save all the isotrack quantities!!!
        #just store the full set of isotrack quantities once
        process.IsolatedPionTracksVeto.debug = cms.bool(True)
        VectorTLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(PFCands)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(PFCands_trkiso)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(PFCands_dzpv)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(PFCands_mT)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(PFCands_charge)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(PFCands_id)'])
    
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
    VectorRecoCand.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])
    VectorInt.extend(['LeptonsNew:MuonCharge(Muons_charge)','LeptonsNew:ElectronCharge(Electrons_charge)'])

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
        
        process.CSCTightHaloFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_CSCTightHalo2015Filter"),
        )
        VarsInt.extend(['CSCTightHaloFilter'])
        
        process.globalTightHalo2016Filter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_globalTightHalo2016Filter"),
        )
        VarsInt.extend(['globalTightHalo2016Filter'])
        
        process.HBHENoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_HBHENoiseFilter"),
        )
        VarsInt.extend(['HBHENoiseFilter'])
        
        process.HBHEIsoNoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_HBHENoiseIsoFilter"),
        )
        VarsInt.extend(['HBHEIsoNoiseFilter'])
        
        process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
        VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])
        
        process.eeBadScFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(tagname),
            filterName  =   cms.string("Flag_eeBadScFilter"),
        )
        VarsInt.extend(['eeBadScFilter'])
        
        # some filters need to be rerun
        process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
        process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
        process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadChargedCandidateFilter.taggingMode = True
        VarsBool.extend(['BadChargedCandidateFilter'])
        
        process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
        process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
        process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadPFMuonFilter.taggingMode = True
        VarsBool.extend(['BadPFMuonFilter'])
        
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
    from TreeMaker.TreeMaker.triggerNameList import triggerNameList as _triggerNameList
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = _triggerNameList
    )
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    
    if not geninfo:
        from TreeMaker.Utils.prescaleweightproducer_cfi import prescaleweightProducer
        process.PrescaleWeightProducer = prescaleweightProducer.clone()
        VarsDouble.extend(['PrescaleWeightProducer:weight(PrescaleWeightHT)'])
        VarsDouble.extend(['PrescaleWeightProducer:ht(HTOnline)'])
        VarsDouble.extend(['PrescaleWeightProducer:mht(MHTOnline)'])

    
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
    if len(jerfile)>0:
        #get name of JERs without any directories
        JERera = jerfile.split('/')[-1]
        JERPatch = cms.string('sqlite_file:'+jerfile+'.db')
        if os.getenv('GC_CONF'): 
            JERPatch = cms.string('sqlite_file:../src/'+jerfile+'.db')
    
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
    
    if geninfo:
        # JEC unc up
        process, JetTagJECup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVars(process,
                              JetTag=JetTagJECup,
                              suff='JECup',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              scenario=scenario,
                              SkipTag=SkipTag
        )
        
        # JEC unc down
        process, JetTagJECdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=-1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVars(process,
                              JetTag=JetTagJECdown,
                              suff='JECdown',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              scenario=scenario,
                              SkipTag=SkipTag
        )

        # JER unc up
        process, JetTagJERup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=1
        )
        process = makeJetVars(process,
                              JetTag=JetTagJERup,
                              suff='JERup',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              scenario=scenario,
                              SkipTag=SkipTag
        )
        
        # JER unc down
        process, JetTagJERdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=-1
        )
        process = makeJetVars(process,
                              JetTag=JetTagJERdown,
                              suff='JERdown',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              scenario=scenario,
                              SkipTag=SkipTag
        )

        # finally, do central smearing and replace jet tag
        process, JetTag = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0
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
    process, JetTag = addJetInfo(process, JetTag, ['QGTagger:qgLikelihood','QGTagger:ptD', 'QGTagger:axis2'], ['QGTagger:mult'])
    
    process = makeJetVars(process,
                          JetTag=JetTag,
                          suff='',
                          skipGoodJets=False,
                          storeProperties=2,
                          geninfo=geninfo,
                          fastsim=fastsim,
                          scenario=scenario,
                          SkipTag=SkipTag
    )
    
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
    
    # add discriminator and update tag
    process, JetAK8Tag = addJetInfo(process, JetAK8Tag, [], [], cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTags")))
    
    # apply jet ID
    process = makeJetVars(process,
        JetTag=JetAK8Tag,
        suff='AK8',
        skipGoodJets=False,
        storeProperties=1,
        geninfo=geninfo,
        fastsim=fastsim,
        scenario=scenario,
        onlyGoodJets=True
    )
    
    # AK8 jet variables - separate instance of jet properties producer
    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsPropertiesAK8 = jetproperties.clone(
        JetTag       = JetAK8Tag,
        properties = cms.vstring(
            "prunedMass"    ,
            "NsubjettinessTau1"    ,
            "NsubjettinessTau2"    ,
            "NsubjettinessTau3"    ,
            "bDiscriminatorSubjet1",
            "bDiscriminatorSubjet2",
            "bDiscriminatorCSV"    ,
            "NumBhadrons"          ,
            "NumChadrons"          ,
        )
    )
    #specify userfloats
    process.JetsPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSPrunedMass')
    process.JetsPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8:tau1')
    process.JetsPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8:tau2')
    process.JetsPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8:tau3')
    process.JetsPropertiesAK8.bDiscriminatorSubjet1 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8.bDiscriminatorSubjet2 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
    #VectorRecoCand.extend([JetAK8Tag.value()+'(JetsAK8)'])
    VectorDouble.extend(['JetsPropertiesAK8:prunedMass(JetsAK8_prunedMass)',
                         'JetsPropertiesAK8:bDiscriminatorSubjet1(JetsAK8_bDiscriminatorSubjet1CSV)',
                         'JetsPropertiesAK8:bDiscriminatorSubjet2(JetsAK8_bDiscriminatorSubjet2CSV)',
                         'JetsPropertiesAK8:bDiscriminatorCSV(JetsAK8_doubleBDiscriminator)',
                         'JetsPropertiesAK8:NsubjettinessTau1(JetsAK8_NsubjettinessTau1)',
                         'JetsPropertiesAK8:NsubjettinessTau2(JetsAK8_NsubjettinessTau2)',
                         'JetsPropertiesAK8:NsubjettinessTau3(JetsAK8_NsubjettinessTau3)'])
    VectorInt.extend(['JetsPropertiesAK8:NumBhadrons(JetsAK8_NumBhadrons)',
                      'JetsPropertiesAK8:NumChadrons(JetsAK8_NumChadrons)'])

    ## ----------------------------------------------------------------------------------------------
    ## GenJet variables
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        # store all genjets
        VectorRecoCand.extend ( [ 'slimmedGenJets(GenJets)' ] )
    
        from TreeMaker.Utils.subJetSelection_cfi import SubGenJetSelection
        
        process.GenHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        VectorBool.extend(['GenHTJets:SubJetMask(GenJets_HTMask)'])
        
        # make gen HT
        from TreeMaker.Utils.htdouble_cfi import htdouble
        process.GenHT = htdouble.clone(
            JetTag = cms.InputTag("GenHTJets"),
        )
        VarsDouble.extend(['GenHT'])
        
        process.GenMHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(5.0),
        )
        VectorBool.extend(['GenMHTJets:SubJetMask(GenJets_MHTMask)'])
        
        # make gen MHT
        from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
        process.GenMHT = mhtdouble.clone(
            JetTag  = cms.InputTag('GenMHTJets'),
        )
        VarsDouble.extend(['GenMHT:Pt(GenMHT)','GenMHT:Phi(GenMHTPhi)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    # sequence for baseline filters
    process.Baseline = cms.Sequence()
    from TreeMaker.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('HT'),
        CutValue  = cms.double(500),
    )
    process.MHTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('MHT:Pt'),
        CutValue  = cms.double(200),
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
    VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)','MET:CaloPt(CaloMET)','MET:CaloPhi(CaloMETPhi)','MET:PFCaloPtRatio(PFCaloMETRatio)'])
    if geninfo:
        VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    from TreeMaker.Utils.mt2producer_cfi import mt2Producer
    process.Mt2Producer = mt2Producer.clone(
                JetTag  = cms.InputTag('MHTJets'),
                METTag = METTag
        )
    VarsDouble.extend(['Mt2Producer:mt2(MT2)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------
    if hadtau:
        from TreeMaker.TreeMaker.doHadTauBkg import doHadTauBkg
        dorecluster = False
        if hadtaurecluster==0: dorecluster = False
        elif hadtaurecluster==1: dorecluster = ("TTJets" in process.source.fileNames[0] or "WJets" in process.source.fileNames[0])
        elif hadtaurecluster==2: dorecluster = geninfo
        elif hadtaurecluster==3: dorecluster = True
        process = doHadTauBkg(process,geninfo,residual,JetTagBeforeSmearing,fastsim,dorecluster)

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
        process = doZinvBkg(process,tagname,geninfo,residual,fastsim,scenario)

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

