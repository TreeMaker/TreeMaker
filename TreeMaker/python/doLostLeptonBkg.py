import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(process,geninfo):
    process.LostLepton = cms.Sequence()

    if geninfo:
        process.LostLepton += process.GenLeptons

    from TreeMaker.Utils.isolationproducer_cfi import isolationproducer
    process.IDMuonMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdMuon'),
        LeptonType = cms.string('muon'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IDMuonMiniIso
    process.IDElectronMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdElectron'), 
        LeptonType = cms.string('electron'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )
    process.IDIsoMuonMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdIsoMuon'), 
        LeptonType = cms.string('muon'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IDIsoMuonMiniIso
    process.IDIsoElectronMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdIsoElectron'), 
        LeptonType = cms.string('electron'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IDIsoElectronMiniIso

    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationCounter

    process.TAPElectronTracks = trackIsolationFilter.clone(
            doTrkIsoVeto        = False,
            vertexInputTag      = cms.InputTag("goodVertices"),
            pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
            dR_ConeSize         = cms.double(0.3),
            dz_CutValue         = cms.double(0.1),
            minPt_PFCandidate   = cms.double(5.0),
            isoCut              = cms.double(-1.),
            pdgId               = cms.int32(11),
            mTCut               = 0.,
            METTag              = "slimmedMETs"
            )

    process.TAPMuonTracks = trackIsolationFilter.clone(
            doTrkIsoVeto        = False,
            vertexInputTag      = cms.InputTag("goodVertices"),
            pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
            dR_ConeSize         = cms.double(0.3),
            dz_CutValue         = cms.double(0.1),
            minPt_PFCandidate   = cms.double(5.0),
            isoCut              = cms.double(-1.), 
            pdgId               = cms.int32(13),
            mTCut               = 0.,
            METTag              = "slimmedMETs"
            )

    ## process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
    ##     doTrkIsoVeto        = False,
    ##     vertexInputTag      = cms.InputTag("goodVertices"),
    ##     pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
    ##     dR_ConeSize         = cms.double(0.3),
    ##     dz_CutValue         = cms.double(0.1),
    ##     minPt_PFCandidate   = cms.double(5.0),
    ##     isoCut              = cms.double(0.2), 
    ##     pdgId               = cms.int32(13),
    ##     mTCut               = mtcut,
    ##     METTag              = METTag,
    ##     )

    process.TAPPionTracks = trackIsolationFilter.clone(
            doTrkIsoVeto        = False,
            vertexInputTag      = cms.InputTag("goodVertices"),
            pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
            dR_ConeSize         = cms.double(0.3),
            dz_CutValue         = cms.double(0.1),
            minPt_PFCandidate   = cms.double(10.0),
            isoCut              = cms.double(-1.),
            pdgId               = cms.int32(211),
            mTCut               = 0.,
            METTag              = "slimmedMETs"
            )
    process.LostLepton += process.TAPElectronTracks
    process.LostLepton += process.TAPMuonTracks
    process.LostLepton += process.TAPPionTracks
    
    
    if geninfo:
        process.GenMuonMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Muon'), 
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
        )    
        process.LostLepton += process.GenMuonMiniIso
        process.GenElectronMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Electron'), 
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
        )    
        process.LostLepton += process.GenElectronMiniIso
        process.GenTauMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Tau'), 
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
        )    
        process.LostLepton += process.GenTauMiniIso      
    
        
    from TreeMaker.Utils.extrapolationproducer_cfi import extrapolationproducer
    process.PTWExtrapolation = extrapolationproducer.clone(
        MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'), # these are the leptons that pass ID and isolation
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron')
    )
    process.LostLepton += process.PTWExtrapolation
        
    print "Adding LostLepton calculations to final path and tree"
    process.AdditionalSequence += process.LostLepton
    
    process.TreeMaker2.VectorRecoCand.extend(['IsolatedElectronTracksVeto','IsolatedMuonTracksVeto','IsolatedPionTracksVeto'])
    # may eventually save track isolation, activity
    process.TreeMaker2.VectorBool.extend(['LeptonsNew:ElecIDMedium(selectedIDElectrons_mediumID)', 'LeptonsNew:ElecIDIsoMedium(selectedIDIsoElectrons_mediumID)'])
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdElectron(selectedIDElectrons)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDMTW(selectedIDMuons_MTW)','LeptonsNew:ElecIDMTW(selectedIDElectrons_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MiniIso(selectedIDMuons_MiniIso)','IDElectronMiniIso:MiniIso(selectedIDElectrons_MiniIso)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MT2Activity(selectedIDMuons_MT2Activity)','IDElectronMiniIso:MT2Activity(selectedIDElectrons_MT2Activity)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDIsoMTW(selectedIDIsoMuons_MTW)','LeptonsNew:ElecIDIsoMTW(selectedIDIsoElectrons_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['PTWExtrapolation:MuPTW(selectedIDIsoMuons_PTW)','PTWExtrapolation:ElecPTW(selectedIDIsoElectrons_PTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDIsoMuonMiniIso:MT2Activity(selectedIDIsoMuons_MT2Activity)','IDIsoElectronMiniIso:MT2Activity(selectedIDIsoElectrons_MT2Activity)'])
    process.TreeMaker2.VarsInt.extend(['TAPElectronTracks:isoTracks(nTAPElectronTracks)'])
    process.TreeMaker2.VarsInt.extend(['TAPMuonTracks:isoTracks(nTAPMuonTracks)'])
    process.TreeMaker2.VarsInt.extend(['TAPPionTracks:isoTracks(nTAPPionTracks)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPElectronTracks:pfcands(TAPElectronTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandstrkiso(TAPElectronTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandsactivity(TAPElectronTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandsmT(TAPElectronTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPElectronTracks:pfcandschg(TAPElectronTracks_chg)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPMuonTracks:pfcands(TAPMuonTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandstrkiso(TAPMuonTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandsactivity(TAPMuonTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandsmT(TAPMuonTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPMuonTracks:pfcandschg(TAPMuonTracks_chg)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPPionTracks:pfcands(TAPPionTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandstrkiso(TAPPionTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandsactivity(TAPPionTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandsmT(TAPPionTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPPionTracks:pfcandschg(TAPPionTracks_chg)'])
    if geninfo: # gen information on leptons
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:Muon(GenMus)','GenLeptons:Electron(GenEls)','GenLeptons:Tau(GenTaus)'])
        process.TreeMaker2.VectorDouble.extend(['GenMuonMiniIso:MT2Activity(GenMu_MT2Activity)','GenElectronMiniIso:MT2Activity(GenElec_MT2Activity)', 'GenTauMiniIso:MT2Activity(GenTau_MT2Activity)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonGenRecoD3(GenMu_RecoTrkd3)','GenLeptons:ElectronGenRecoD3(GenElec_RecoTrkd3)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonTrkIso(GenMu_RecoTrkIso)','GenLeptons:ElectronTrkIso(GenElec_RecoTrkIso)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonTrkAct(GenMu_RecoTrkAct)','GenLeptons:ElectronTrkAct(GenElec_RecoTrkAct)'])
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:TauDecayCands(TauDecayCands)','GenLeptons:TauNu(GenTauNu)'])
        process.TreeMaker2.VectorInt.extend(['GenLeptons:MuonTauDecay(GenMu_GenMuFromTau)','GenLeptons:ElectronTauDecay(GenElec_GenElecFromTau)','GenLeptons:TauHadronic(GenTau_GenTauHad)','GenLeptons:TauDecayCandspdgID(TauDecayCands_pdgID)', 'GenLeptons:TauDecayCandsmomInd(TauDecayCands_momInd)'])
        process.TreeMaker2.VectorTLorentzVector.extend(['GenLeptons:TauLeadTrk(GenTauLeadTrk)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:TauLeadTrkGenRecoD3(GenTauLeadRecoTrkd3)', 'GenLeptons:TauLeadTrkIso(GenTauLeadRecoTrkIso)', 'GenLeptons:TauLeadTrkAct(GenTauLeadRecoTrkAct)'])

    
    return process
