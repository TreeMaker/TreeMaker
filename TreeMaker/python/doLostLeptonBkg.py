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
    
    for type in ['Electron','Muon']:
        self.VectorBool.extend(['LeptonsNew:Id'+type+'MediumID('+type+'s_mediumID)'])
        self.VectorBool.extend(['LeptonsNew:Id'+type+'TightID('+type+'s_tightID)'])
        self.VectorDouble.extend(['LeptonsNew:Id'+type+'MTW('+type+'s_MTW)'])
        self.VectorDouble.extend(['ID'+type+'MiniIso:MiniIso('+type+'s_MiniIso)'])
#    self.VectorDouble.extend(['PTWExtrapolation:MuPTW(Muons_PTW)','PTWExtrapolation:ElecPTW(Electrons_PTW)'])

    for type in ['Electron','Muon','Pion']:
        self.VectorTLorentzVector.extend(['TAP'+type+'Tracks:pfcands(TAP'+type+'Tracks)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandstrkiso(TAP'+type+'Tracks_trkiso)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsmT(TAP'+type+'Tracks_mT)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandspfreliso03chg(TAP'+type+'Tracks_pfRelIso03chg)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsdxypv(TAP'+type+'Tracks_dxypv)'])

    if self.debugtap:
        for type in ['Electron','Muon','Pion']:
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandspfreliso03chg(TAP'+type+'Tracks_pfRelIso03chg)'])
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandspfreliso03all(TAP'+type+'Tracks_pfRelIso03all)'])
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsdzpv(TAP'+type+'Tracks_dzpv)'])
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsdxypv(TAP'+type+'Tracks_dxypv)'])
            self.VectorInt.extend(['TAP'+type+'Tracks:pfcandschg(TAP'+type+'Tracks_charge)'])
            self.VectorInt.extend(['TAP'+type+'Tracks:pfcandsid(TAP'+type+'Tracks_id)'])
    if self.geninfo: # gen information on leptons
        self.VectorRecoCand.extend(['GenLeptons:Muon(GenMuons)','GenLeptons:Electron(GenElectrons)','GenLeptons:Tau(GenTaus)'])
        self.VectorBool.extend(['GenLeptons:TauHadronic(GenTaus_had)'])
    
    return process
