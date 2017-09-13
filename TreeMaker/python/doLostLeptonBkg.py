import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(self,process,METTag):
    if self.geninfo:
        from TreeMaker.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
        process.GenLeptons = genLeptonRecoCand.clone(
            PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
            pfCandsTag  = cms.InputTag('packedPFCandidates')
        )

    from TreeMaker.Utils.isolationproducer_cfi import isolationproducer
    process.IDMuonMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdMuon'),
        LeptonType = cms.string('muon'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )
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
    process.IDIsoElectronMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('LeptonsNew:IdIsoElectron'), 
        LeptonType = cms.string('electron'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
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
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
            JetTag = cms.InputTag('HTJets')
        )
        process.GenElectronMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Electron'), 
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
            JetTag = cms.InputTag('HTJets')
        )
        process.GenTauMiniIso = isolationproducer.clone(
            LeptonTag = cms.InputTag('GenLeptons:Tau'), 
            LeptonType = cms.string('gen'),
            PFCandTag = cms.InputTag('packedPFCandidates'),
            JetTag = cms.InputTag('HTJets')
        )

    from TreeMaker.Utils.extrapolationproducer_cfi import extrapolationproducer
    process.PTWExtrapolation = extrapolationproducer.clone(
        MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'), # these are the leptons that pass ID and isolation
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron')
    )
    
    # may eventually save track isolation, activity
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdMuon(MuonsNoIso)','LeptonsNew:IdElectron(ElectronsNoIso)'])
    process.TreeMaker2.VectorBool.extend(['LeptonsNew:IdMuonTightID(MuonsNoIso_tightID)','LeptonsNew:IdIsoMuonTightID(Muons_tightID)'])
    process.TreeMaker2.VectorBool.extend(['LeptonsNew:IdElectronMediumID(ElectronsNoIso_mediumID)','LeptonsNew:IdIsoElectronMediumID(Electrons_mediumID)'])
    process.TreeMaker2.VectorBool.extend(['LeptonsNew:IdElectronTightID(ElectronsNoIso_tightID)','LeptonsNew:IdIsoElectronTightID(Electrons_tightID)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDMTW(MuonsNoIso_MTW)','LeptonsNew:ElecIDMTW(ElectronsNoIso_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MiniIso(MuonsNoIso_MiniIso)','IDElectronMiniIso:MiniIso(ElectronsNoIso_MiniIso)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MT2Activity(MuonsNoIso_MT2Activity)','IDElectronMiniIso:MT2Activity(ElectronsNoIso_MT2Activity)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDIsoMTW(Muons_MTW)','LeptonsNew:ElecIDIsoMTW(Electrons_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['PTWExtrapolation:MuPTW(Muons_PTW)','PTWExtrapolation:ElecPTW(Electrons_PTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDIsoMuonMiniIso:MT2Activity(Muons_MT2Activity)','IDIsoElectronMiniIso:MT2Activity(Electrons_MT2Activity)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPElectronTracks:pfcands(TAPElectronTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandstrkiso(TAPElectronTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandsactivity(TAPElectronTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPElectronTracks:pfcandsmT(TAPElectronTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPElectronTracks:pfcandschg(TAPElectronTracks_charge)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPMuonTracks:pfcands(TAPMuonTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandstrkiso(TAPMuonTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandsactivity(TAPMuonTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPMuonTracks:pfcandsmT(TAPMuonTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPMuonTracks:pfcandschg(TAPMuonTracks_charge)'])
    process.TreeMaker2.VectorTLorentzVector.extend(['TAPPionTracks:pfcands(TAPPionTracks)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandstrkiso(TAPPionTracks_trkiso)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandsactivity(TAPPionTracks_activity)'])
    process.TreeMaker2.VectorDouble.extend(['TAPPionTracks:pfcandsmT(TAPPionTracks_mT)'])
    process.TreeMaker2.VectorInt.extend(['TAPPionTracks:pfcandschg(TAPPionTracks_charge)'])
    if self.geninfo: # gen information on leptons
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:Muon(GenMuons)','GenLeptons:Electron(GenElectrons)','GenLeptons:Tau(GenTaus)'])
        process.TreeMaker2.VectorDouble.extend(['GenMuonMiniIso:MT2Activity(GenMuons_MT2Activity)','GenElectronMiniIso:MT2Activity(GenElectrons_MT2Activity)', 'GenTauMiniIso:MT2Activity(GenTaus_MT2Activity)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonGenRecoD3(GenMuons_RecoTrkd3)','GenLeptons:ElectronGenRecoD3(GenElectrons_RecoTrkd3)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonTrkIso(GenMuons_RecoTrkIso)','GenLeptons:ElectronTrkIso(GenElectrons_RecoTrkIso)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:MuonTrkAct(GenMuons_RecoTrkAct)','GenLeptons:ElectronTrkAct(GenElectrons_RecoTrkAct)'])
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:TauNu(GenTaus_Nu)'])
        process.TreeMaker2.VectorInt.extend(['GenLeptons:TauNProngs(GenTaus_NProngs)','GenLeptons:TauNNHads(GenTaus_NNeutralHadrons)'])
        process.TreeMaker2.VectorBool.extend(['GenLeptons:MuonTauDecay(GenMuons_fromTau)','GenLeptons:ElectronTauDecay(GenElectrons_fromTau)','GenLeptons:TauHadronic(GenTaus_had)'])
        process.TreeMaker2.VectorTLorentzVector.extend(['GenLeptons:TauLeadTrk(GenTaus_LeadTrk)'])
        process.TreeMaker2.VectorDouble.extend(['GenLeptons:TauLeadTrkGenRecoD3(GenTaus_LeadRecoTrkd3)', 'GenLeptons:TauLeadTrkIso(GenTaus_LeadRecoTrkIso)', 'GenLeptons:TauLeadTrkAct(GenTaus_LeadRecoTrkAct)'])

    
    return process
