import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(self,process,METTag):
    if self.geninfo:
        from TreeMaker.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
        process.GenLeptons = genLeptonRecoCand.clone(
            PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
            pfCandsTag  = cms.InputTag('packedPFCandidates')
        )

    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.isolationproducer_cfi import isolationproducer
    process.IDMuonMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdMuon'),
        LeptonType = cms.string('muon')
    )
    electronEAValuesLocal = cms.vdouble(0.1566, 0.1626, 0.1073, 0.0854, 0.1051, 0.1204, 0.1524)
    muonEAValuesLocal     = cms.vdouble(0.0735, 0.0619, 0.0465, 0.0433, 0.0577)
    (TMeras.TM2017 | TMeras.TM2018).toModify(process.IDMuonMiniIso,
        electronEAValues = electronEAValuesLocal,
        muonEAValues     = muonEAValuesLocal
    )
    process.IDElectronMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdElectron'), 
        LeptonType = cms.string('electron')
    )
    (TMeras.TM2017 | TMeras.TM2018).toModify(process.IDElectronMiniIso,
        electronEAValues = electronEAValuesLocal,
        muonEAValues     = muonEAValuesLocal
    )

    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

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
            METTag              = METTag
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
            METTag              = METTag
            )

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
            METTag              = METTag
            )

    if self.geninfo:
        process.GenMuonMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Muon'), 
            LeptonType = cms.string('gen')
        )
        (TMeras.TM2017 | TMeras.TM2018).toModify(process.GenMuonMiniIso,
            electronEAValues = electronEAValuesLocal,
            muonEAValues     = muonEAValuesLocal
        )
        process.GenElectronMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Electron'), 
            LeptonType = cms.string('gen')
        )
        (TMeras.TM2017 | TMeras.TM2018).toModify(process.GenElectronMiniIso,
            electronEAValues = electronEAValuesLocal,
            muonEAValues     = muonEAValuesLocal
        )
        process.GenTauMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Tau'), 
            LeptonType = cms.string('gen')
        )
        (TMeras.TM2017 | TMeras.TM2018).toModify(process.GenTauMiniIso,
            electronEAValues = electronEAValuesLocal,
            muonEAValues     = muonEAValuesLocal
        )

#    from TreeMaker.Utils.extrapolationproducer_cfi import extrapolationproducer
#    process.PTWExtrapolation = extrapolationproducer.clone(
#        MuonTag = cms.InputTag('LeptonsNew:IdMuon'), # these are the leptons that pass ID
#        ElectronTag = cms.InputTag('LeptonsNew:IdElectron')
#    )
    
    # may eventually save track isolation, activity
    self.VectorBool.extend(['LeptonsNew:IdMuonTightID(Muons_tightID)'])
    self.VectorBool.extend(['LeptonsNew:IdElectronMediumID(Electrons_mediumID)'])
    self.VectorBool.extend(['LeptonsNew:IdElectronTightID(Electrons_tightID)'])
    self.VectorDouble.extend(['LeptonsNew:IdMuonMTW(Muons_MTW)','LeptonsNew:IdElectronMTW(Electrons_MTW)'])
    self.VectorDouble.extend(['IDMuonMiniIso:MiniIso(Muons_MiniIso)','IDElectronMiniIso:MiniIso(Electrons_MiniIso)'])
    self.VectorDouble.extend(['IDMuonMiniIso:MT2Activity(Muons_MT2Activity)','IDElectronMiniIso:MT2Activity(Electrons_MT2Activity)'])
#    self.VectorDouble.extend(['PTWExtrapolation:MuPTW(Muons_PTW)','PTWExtrapolation:ElecPTW(Electrons_PTW)'])
    self.VectorTLorentzVector.extend(['TAPElectronTracks:pfcands(TAPElectronTracks)'])
    self.VectorDouble.extend(['TAPElectronTracks:pfcandstrkiso(TAPElectronTracks_trkiso)'])
    self.VectorDouble.extend(['TAPElectronTracks:pfcandsactivity(TAPElectronTracks_activity)'])
    self.VectorDouble.extend(['TAPElectronTracks:pfcandsmT(TAPElectronTracks_mT)'])
    self.VectorInt.extend(['TAPElectronTracks:pfcandschg(TAPElectronTracks_charge)'])
    self.VectorTLorentzVector.extend(['TAPMuonTracks:pfcands(TAPMuonTracks)'])
    self.VectorDouble.extend(['TAPMuonTracks:pfcandstrkiso(TAPMuonTracks_trkiso)'])
    self.VectorDouble.extend(['TAPMuonTracks:pfcandsactivity(TAPMuonTracks_activity)'])
    self.VectorDouble.extend(['TAPMuonTracks:pfcandsmT(TAPMuonTracks_mT)'])
    self.VectorInt.extend(['TAPMuonTracks:pfcandschg(TAPMuonTracks_charge)'])
    self.VectorTLorentzVector.extend(['TAPPionTracks:pfcands(TAPPionTracks)'])
    self.VectorDouble.extend(['TAPPionTracks:pfcandstrkiso(TAPPionTracks_trkiso)'])
    self.VectorDouble.extend(['TAPPionTracks:pfcandsactivity(TAPPionTracks_activity)'])
    self.VectorDouble.extend(['TAPPionTracks:pfcandsmT(TAPPionTracks_mT)'])
    self.VectorInt.extend(['TAPPionTracks:pfcandschg(TAPPionTracks_charge)'])
    if self.geninfo: # gen information on leptons
        self.VectorRecoCand.extend(['GenLeptons:Muon(GenMuons)','GenLeptons:Electron(GenElectrons)','GenLeptons:Tau(GenTaus)'])
        self.VectorDouble.extend(['GenMuonMiniIso:MT2Activity(GenMuons_MT2Activity)','GenElectronMiniIso:MT2Activity(GenElectrons_MT2Activity)', 'GenTauMiniIso:MT2Activity(GenTaus_MT2Activity)'])
        self.VectorDouble.extend(['GenLeptons:MuonGenRecoD3(GenMuons_RecoTrkd3)','GenLeptons:ElectronGenRecoD3(GenElectrons_RecoTrkd3)'])
        self.VectorDouble.extend(['GenLeptons:MuonTrkIso(GenMuons_RecoTrkIso)','GenLeptons:ElectronTrkIso(GenElectrons_RecoTrkIso)'])
        self.VectorDouble.extend(['GenLeptons:MuonTrkAct(GenMuons_RecoTrkAct)','GenLeptons:ElectronTrkAct(GenElectrons_RecoTrkAct)'])
        self.VectorRecoCand.extend(['GenLeptons:TauNu(GenTaus_Nu)'])
        self.VectorInt.extend(['GenLeptons:TauNProngs(GenTaus_NProngs)','GenLeptons:TauNNHads(GenTaus_NNeutralHadrons)'])
        self.VectorBool.extend(['GenLeptons:MuonTauDecay(GenMuons_fromTau)','GenLeptons:ElectronTauDecay(GenElectrons_fromTau)','GenLeptons:TauHadronic(GenTaus_had)'])
        self.VectorTLorentzVector.extend(['GenLeptons:TauLeadTrk(GenTaus_LeadTrk)'])
        self.VectorDouble.extend(['GenLeptons:TauLeadTrkGenRecoD3(GenTaus_LeadRecoTrkd3)', 'GenLeptons:TauLeadTrkIso(GenTaus_LeadRecoTrkIso)', 'GenLeptons:TauLeadTrkAct(GenTaus_LeadRecoTrkAct)'])

    
    return process
