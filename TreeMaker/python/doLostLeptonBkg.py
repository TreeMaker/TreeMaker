import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(self,process,METTag):
    if self.geninfo:
        from TreeMaker.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
        process.GenLeptons = genLeptonRecoCand.clone(
            PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
            pfCandsTag  = cms.InputTag('packedPFCandidates')
        )

    from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter

    process.TAPElectronTracks = trackIsolationFilter.clone(
            doTrkIsoVeto        = False,
            vertexInputTag      = cms.InputTag("goodVertices"),
            pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
            ElectronTag         = cms.InputTag("LeptonsNew:IsoTrkVetoElectron"),
            MuonTag             = cms.InputTag("LeptonsNew:IsoTrkVetoMuon"),
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
            ElectronTag         = cms.InputTag("LeptonsNew:IsoTrkVetoElectron"),
            MuonTag             = cms.InputTag("LeptonsNew:IsoTrkVetoMuon"),
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
            ElectronTag         = cms.InputTag("LeptonsNew:IsoTrkVetoElectron"),
            MuonTag             = cms.InputTag("LeptonsNew:IsoTrkVetoMuon"),
            dR_ConeSize         = cms.double(0.3),
            dz_CutValue         = cms.double(0.1),
            minPt_PFCandidate   = cms.double(10.0),
            isoCut              = cms.double(-1.),
            pdgId               = cms.int32(211),
            mTCut               = 0.,
            METTag              = METTag
            )
    
    for type in ['Electron','Muon']:
        self.VectorBool.extend(['LeptonsNew:Id'+type+'MediumID('+type+'s_mediumID)'])
        self.VectorBool.extend(['LeptonsNew:Id'+type+'TightID('+type+'s_tightID)'])
        self.VectorDouble.extend(['LeptonsNew:Id'+type+'MTW('+type+'s_MTW)'])
        self.VectorDouble.extend(['LeptonsNew:Id'+type+'Iso('+type+'s_iso)'])

    for type in ['Electron','Muon','Pion']:
        self.VectorLorentzVector.extend(['TAP'+type+'Tracks:pfcands(TAP'+type+'Tracks)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandstrkiso(TAP'+type+'Tracks_trkiso)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsmT(TAP'+type+'Tracks_mT)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandspfreliso03chg(TAP'+type+'Tracks_pfRelIso03chg)'])
        self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsdxypv(TAP'+type+'Tracks_dxypv)'])
        self.VectorBool.extend(['TAP'+type+'Tracks:pfcandsleptonmatch(TAP'+type+'Tracks_leptonMatch)'])

    if self.debugtap:
        for type in ['Electron','Muon','Pion']:
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandspfreliso03all(TAP'+type+'Tracks_pfRelIso03all)'])
            self.VectorDouble.extend(['TAP'+type+'Tracks:pfcandsdzpv(TAP'+type+'Tracks_dzpv)'])
            self.VectorInt.extend(['TAP'+type+'Tracks:pfcandschg(TAP'+type+'Tracks_charge)'])
            self.VectorInt.extend(['TAP'+type+'Tracks:pfcandsid(TAP'+type+'Tracks_id)'])
    if self.geninfo: # gen information on leptons
        self.VectorRecoCand.extend(['GenLeptons:Muon(GenMuons)','GenLeptons:Electron(GenElectrons)','GenLeptons:Tau(GenTaus)'])
        self.VectorBool.extend(['GenLeptons:TauHadronic(GenTaus_had)'])
    
    return process
