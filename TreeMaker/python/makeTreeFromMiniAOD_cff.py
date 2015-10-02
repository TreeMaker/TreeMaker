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
tagandprobe=False,
applybaseline=False,
doZinv=False,
debugtracks=False,
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False,
QCD=False,
IncludeBEff=True,
AddBtagSF=False,
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
    is74X = False
    if int(CMSSWVER_parts[1])==7 and int(CMSSWVER_parts[2])>=4:
        is74X = True
        print "Configuring for 74X"

    # define if mt cut should be applied and the value (less than 0 means no cut)
    mtcut = cms.double(100)
    if tagandprobe:
        mtcut=-100
        print "Doing tagandprobe"
    print "Calculation with mtcut: "+ str(mtcut)

    # log output
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = reportfreq
    process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
        wantSummary = cms.untracked.bool(True)
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
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
    process.WeightProducer = getWeightProducer(process.source.fileNames[0])
    process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
    process.WeightProducer.PU                         = cms.int32(0) # PU S10 3 for S10 2 for S7
    process.WeightProducer.FileNamePUDataDistribution = cms.string("./data/pu_weights_7_4_25ns_testShifts.root")
    process.Baseline += process.WeightProducer
    VarsDouble.extend(['WeightProducer:weight(Weight)'])

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
        process.genParticles = cms.EDProducer("genParticlesProducer",
            genCollection = cms.untracked.InputTag("prunedGenParticles"),
            debug = cms.untracked.bool(False)
        )
        process.Baseline += process.genParticles
        ## JACK--do we really need to save all of these?
        VectorTLorentzVector.append("genParticles(genParticles)")
        VectorInt.append("genParticles:PDGid(genParticles_PDGid)")
        #VectorInt.append("genParticles:parent(genParticles_parent)")
        

    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------
    
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    JetTag = cms.InputTag('slimmedJets')
    METTag = cms.InputTag('slimmedMETs')
    if len(jecfile)>0:
        #get name of JECs without any directories
        JECera = jecfile.split('/')[-1]
        JECPatch = cms.string('sqlite_file:'+jecfile+'.db')
        if os.getenv('GC_CONF'): 
            JECPatch = cms.string('sqlite_file:../src/'+jecfile+'.db')

        process.load("CondCore.DBCommon.CondDBCommon_cfi")
        from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
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
                )
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
        
        # update the MET to account for the new JECs
        # ref: https://github.com/cms-met/cmssw/blob/METCorUnc74X/PhysicsTools/PatAlgos/test/corMETFromMiniAOD.py
        
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )
        if not residual: #skip residuals for data if not used
            process.patPFMetT1T2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT1T2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.shiftedPatJetEnDown.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
            process.shiftedPatJetEnUp.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
            
        METTag = cms.InputTag('slimmedMETs','',process.name_())

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
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
        photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
        electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",tagname),
        beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot","","RECO"),
        ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
        debug                  = cms.untracked.bool(False)
    )
    process.Baseline += process.goodPhotons
    # good photon tag is InputTag('goodPhotons','bestPhoton')
    VectorRecoCand.append("goodPhotons:bestPhoton")
    VarsInt.append("goodPhotons:NumPhotons")

    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        maxJetEta                 = cms.double(5.0),
        maxMuFraction             = cms.double(2),
        minNConstituents          = cms.double(2),
        maxNeutralFraction        = cms.double(0.90),
        maxPhotonFraction         = cms.double(0.95),
        minChargedMultiplicity    = cms.double(0),
        minChargedFraction        = cms.double(0),
        maxChargedEMFraction      = cms.double(0.99),
        jetPtFilter               = cms.double(30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(0.4),
        MuonTag                   = cms.InputTag('LeptonsNew:IdIsoMuon'),
        ElecTag                   = cms.InputTag('LeptonsNew:IdIsoElectron'),
        IsoElectronTrackTag       = cms.InputTag('IsolatedElectronTracksVeto'),
        IsoMuonTrackTag           = cms.InputTag('IsolatedMuonTracksVeto'),
        IsoPionTrackTag           = cms.InputTag('IsolatedPionTracksVeto'),
        PhotonTag                 = cms.InputTag('goodPhotons','bestPhoton'),
    )
    process.Baseline += process.GoodJets
    VarsBool.extend(['GoodJets(JetID)'])

    ## ----------------------------------------------------------------------------------------------
    ## MET Filters
    ## ----------------------------------------------------------------------------------------------
    
    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree

    from TreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer
    process.METFilters = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(tagname),
        filterName  = cms.string("Flag_METFilters"),
    )
    process.Baseline += process.METFilters
    VarsInt.extend(['METFilters'])

    process.CSCTightHaloFilter = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(tagname),
        filterName  = cms.string("Flag_CSCTightHaloFilter"),
    )
    process.Baseline += process.CSCTightHaloFilter
    VarsInt.extend(['CSCTightHaloFilter'])

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
    process.Baseline += process.HBHENoiseFilterResultProducer
    VarsBool.extend(['HBHENoiseFilterResultProducer:HBHENoiseFilterResult(HBHENoiseFilter)'])

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
            'HLT_PFMET170_NoiseCleaned_v',
            'HLT_PFMET170_NoiseCleaned_v',
            'HLT_PFHT350_v',
            'HLT_PFHT800_v',
            'HLT_PFHT900_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v',
            'HLT_IsoMu17_eta2p1_v',
            'HLT_PFHT350_PFMET120_NoiseCleaned_v',
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v',
            'HLT_Mu15_IsoVVVL_BTagCSV07_PFHT400_v',
            'HLT_Mu15_IsoVVVL_PFHT600_v',
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
        )
    )
    process.Baseline += process.TriggerProducer
    VectorBool.extend(['TriggerProducer:TriggerPass'])
    VectorInt.extend(['TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])

    ## ----------------------------------------------------------------------------------------------
    ## HT
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    process.HTJets = SubJetSelection.clone(
        JetTag = cms.InputTag('GoodJets'),
        MinPt  = cms.double(30),
        MaxEta = cms.double(2.4),
    )
    process.Baseline += process.HTJets
    
    from TreeMaker.Utils.htdouble_cfi import htdouble
    process.HT = htdouble.clone(
        JetTag = cms.InputTag('HTJets'),
    )
    process.Baseline += process.HT
    VarsDouble.extend(['HT'])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.njetint_cfi import njetint
    process.NJets = njetint.clone(
        JetTag = cms.InputTag('HTJets'),
    )
    process.Baseline += process.NJets
    VarsInt.extend(['NJets'])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.btagint_cfi import btagint
    process.BTags = btagint.clone(
        JetTag       = cms.InputTag('HTJets'),
        BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.814)
    )
    if is74X:
        process.BTags.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')
        process.BTags.BTagCutValue = cms.double(0.890)
    process.Baseline += process.BTags
    VarsInt.extend(['BTags'])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    process.MHTJets = SubJetSelection.clone(
        JetTag = cms.InputTag('GoodJets'),
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    process.Baseline += process.MHTJets
    
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    process.MHT = mhtdouble.clone(
        JetTag  = cms.InputTag('MHTJets'),
    )
    process.Baseline += process.MHT
    VarsDouble.extend(['MHT:Pt(MHT)','MHT:Phi(MHT_Phi)'])
    
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
    ## DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    process.DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = cms.InputTag('HTJets'),
        MHTJets      = cms.InputTag("MHTJets"),
    )
    process.Baseline += process.DeltaPhi
    VarsDouble.extend(['DeltaPhi:DeltaPhi1','DeltaPhi:DeltaPhi2','DeltaPhi:DeltaPhi3'])
    
    ## ----------------------------------------------------------------------------------------------
    ## MET
    ## ----------------------------------------------------------------------------------------------
    from TreeMaker.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = METTag,
        GenMETTag = cms.InputTag("slimmedMETs","","PAT"), #deliberately hardcoded
        JetTag = cms.InputTag('HTJets'),
        geninfo = cms.untracked.bool(geninfo),
    )
    process.Baseline += process.MET
    VarsDouble.extend(['MET:minDeltaPhiN','MET:DeltaPhiN1','MET:DeltaPhiN2','MET:DeltaPhiN3','MET:Pt(METPt)','MET:Phi(METPhi)'])
    if geninfo:
        VarsDouble.extend(['MET:GenPt(GenMETPt)','MET:GenPhi(GenMETPhi)'])

    ## ----------------------------------------------------------------------------------------------
    ## Jet properties
    ## ----------------------------------------------------------------------------------------------
    
    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsProperties = jetproperties.clone(
        JetTag       = cms.InputTag('GoodJets'),
        BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
        METTag       = METTag,
    )
    if is74X: process.JetsProperties.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.Baseline += process.JetsProperties
    process.TreeMaker2.VectorRecoCand.extend(['GoodJets(Jets)'])
    process.TreeMaker2.VectorDouble.extend(['JetsProperties:bDiscriminatorUser(Jets_bDiscriminatorCSV)',
                                            'JetsProperties:bDiscriminatorMVA(Jets_bDiscriminatorMVA)',
                                            'JetsProperties:chargedEmEnergyFraction(Jets_chargedEmEnergyFraction)',
                                            'JetsProperties:chargedHadronEnergyFraction(Jets_chargedHadronEnergyFraction)',
                                            'JetsProperties:jetArea(Jets_jetArea)',
                                            'JetsProperties:muonEnergyFraction(Jets_muonEnergyFraction)',
                                            'JetsProperties:neutralEmEnergyFraction(Jets_neutralEmEnergyFraction)',
                                            'JetsProperties:photonEnergyFraction(Jets_photonEnergyFraction)'])
    process.TreeMaker2.VectorInt.extend(['JetsProperties:chargedHadronMultiplicity(Jets_chargedHadronMultiplicity)',
                                         'JetsProperties:electronMultiplicity(Jets_electronMultiplicity)',
                                         'JetsProperties:muonMultiplicity(Jets_muonMultiplicity)',
                                         'JetsProperties:neutralHadronMultiplicity(Jets_neutralHadronMultiplicity)',
                                         'JetsProperties:photonMultiplicity(Jets_photonMultiplicity)',
                                         'JetsProperties:flavor(Jets_flavor)'])
    if IncludeBEff:
    	process.bTaggingEffAnalyzerAK5PF = cms.EDAnalyzer('BTaggingEffAnalyzer',
        	JetsTag            = cms.InputTag('HTJets'),
        	DiscriminatorTag   = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        	DiscriminatorValue = cms.double(0.890),
        	PtNBins            = cms.int32(100),
        	PtMin              = cms.double(0.),
        	PtMax              = cms.double(1000.),
        	EtaNBins           = cms.int32(60),
        	EtaMin             = cms.double(-3.),
        	EtaMax             = cms.double(3.)
    	)
   	process.Baseline += process.bTaggingEffAnalyzerAK5PF
    if AddBtagSF:
	process.BTagScale=cms.EDProducer('BTagScale',
		JetsTag            = cms.InputTag('HTJets'),
		BTagEffInput   =cms.string('./data/test_run_RA2AnalysisTree.root'),
		CSVTag=cms.string('./data/CSVv2.csv'),
		
		)
	process.Baseline += process.BTagScale
	VarsDouble.extend(['BTagScale:BTagProb0', 'BTagScale:BTagProb1', 'BTagScale:BTagProb2', 'BTagScale:BTagProb3'])
#	VarsDouble.extend(['BTagScale:BTagProb0ShiftUp', 'BTagScale:BTagProb1ShiftUp','BTagScale:BTagProb2ShiftUp', 'BTagScale:BTagProb3ShiftUp'])
#	VarsDouble.extend(['BTagScale:BTagProb0ShiftDown', 'BTagScale:BTagProb1ShiftDown','BTagScale:BTagProb2ShiftDown', 'BTagScale:BTagProb3ShiftDown'])
	
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
        process = doHadTauBkg(process,is74X,geninfo,residual,JetTag)

    ## ----------------------------------------------------------------------------------------------
    ## Shared processes for lost lepton, tag and probe
    ## ----------------------------------------------------------------------------------------------
    if lostlepton or tagandprobe:
        from TreeMaker.TreeMaker.doProcessesForLLTP import doProcessesForLLTP
        process = doProcessesForLLTP(process,geninfo)
    
    ## ----------------------------------------------------------------------------------------------
    ## Tag And Probe
    ## ----------------------------------------------------------------------------------------------
    if tagandprobe:
        from TreeMaker.TreeMaker.doTagAndProbe import doTagAndProbe
        process = doTagAndProbe(process,geninfo,METTag)

    ## ----------------------------------------------------------------------------------------------
    ## Lost Lepton Background
    ## ----------------------------------------------------------------------------------------------
    if lostlepton:
        from TreeMaker.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
        process = doLostLeptonBkg(process,geninfo)

    ## ----------------------------------------------------------------------------------------------
    ## Zinv Background
    ## ----------------------------------------------------------------------------------------------
    if doZinv:
        from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg
        process = doZinvBkg(process,is74X,METTag)

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## QCD DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    if QCD:
        from TreeMaker.TreeMaker.DeltaPhiQCD import DeltaPhiQCD
        process = DeltaPhiQCD(process,is74X,geninfo)

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

