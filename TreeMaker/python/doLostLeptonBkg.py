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
    process.IsoElectronTrackMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('IsolatedElectronTracksVeto'), 
        LeptonType = cms.string('track'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IsoElectronTrackMiniIso
    process.IsoMuonTrackMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('IsolatedMuonTracksVeto'), 
        LeptonType = cms.string('track'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IsoMuonTrackMiniIso
    process.IsoPionTrackMiniIso = isolationproducer.clone(
        LeptonTag = cms.InputTag('IsolatedPionTracksVeto'), 
        LeptonType = cms.string('track'),
        PFCandTag = cms.InputTag('packedPFCandidates'),
        JetTag = cms.InputTag('HTJets')
    )    
    process.LostLepton += process.IsoPionTrackMiniIso
    
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
    process.TreeMaker2.VectorDouble.extend(['IsolatedElectronTracksVeto:pfcandsmT(IsolatedElectronTracksVeto_MTW)','IsolatedMuonTracksVeto:pfcandsmT(IsolatedMuonTracksVeto_MTW)','IsolatedPionTracksVeto:pfcandsmT(IsolatedPionTracksVeto_MTW)'])
    # may eventually save track isolation, activity
    # process.TreeMaker2.VectorDouble.extend(['IsoElectronTrackMiniIso:MiniIso(IsolatedElectronTracksVeto_MiniIso)','IsoMuonTrackMiniIso:MiniIso(IsolatedMuonTracksVeto_MiniIso)','IsoPionTrackMiniIso:MiniIso(IsolatedPionTracksVeto_MiniIso)'])
    # process.TreeMaker2.VectorDouble.extend(['IsoElectronTrackMiniIso:MT2Activity(IsolatedElectronTracksVeto_MT2Activity)','IsoMuonTrackMiniIso:MT2Activity(IsolatedMuonTracksVeto_MT2Activity)','IsoPionTrackMiniIso:MT2Activity(IsolatedPionTracksVeto_MT2Activity)'])
    process.TreeMaker2.VectorBool.extend(['LeptonsNew:ElecIDMedium(selectedIDElectrons_mediumID)', 'LeptonsNew:ElecIDIsoMedium(selectedIDIsoElectrons_mediumID)'])
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdElectron(selectedIDElectrons)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDMTW(selectedIDMuons_MTW)','LeptonsNew:ElecIDMTW(selectedIDElectrons_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MiniIso(selectedIDMuons_MiniIso)','IDElectronMiniIso:MiniIso(selectedIDElectrons_MiniIso)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:RA2Activity(selectedIDMuons_RA2Activity)','IDElectronMiniIso:RA2Activity(selectedIDElectrons_RA2Activity)'])
    process.TreeMaker2.VectorDouble.extend(['IDMuonMiniIso:MT2Activity(selectedIDMuons_MT2Activity)','IDElectronMiniIso:MT2Activity(selectedIDElectrons_MT2Activity)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDIsoMTW(selectedIDIsoMuons_MTW)','LeptonsNew:ElecIDIsoMTW(selectedIDIsoElectrons_MTW)'])
    process.TreeMaker2.VectorDouble.extend(['PTWExtrapolation:MuPTW(selectedIDIsoMuons_PTW)','PTWExtrapolation:ElecPTW(selectedIDIsoElectrons_PTW)'])
    process.TreeMaker2.VectorDouble.extend(['IDIsoMuonMiniIso:RA2Activity(selectedIDIsoMuons_RA2Activity)','IDIsoElectronMiniIso:RA2Activity(selectedIDIsoElectrons_RA2Activity)'])
    process.TreeMaker2.VectorDouble.extend(['IDIsoMuonMiniIso:MT2Activity(selectedIDIsoMuons_MT2Activity)','IDIsoElectronMiniIso:MT2Activity(selectedIDIsoElectrons_MT2Activity)'])
    if geninfo: # gen information on leptons
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:Muon(GenMus)','GenLeptons:Electron(GenEls)','GenLeptons:Tau(GenTaus)'])
        process.TreeMaker2.VectorDouble.extend(['GenMuonMiniIso:RA2Activity(GenMu_RA2Activity)','GenElectronMiniIso:RA2Activity(GenElec_RA2Activity)', 'GenTauMiniIso:RA2Activity(GenTau_RA2Activity)'])
        process.TreeMaker2.VectorDouble.extend(['GenMuonMiniIso:MT2Activity(GenMu_MT2Activity)','GenElectronMiniIso:MT2Activity(GenElec_MT2Activity)', 'GenTauMiniIso:MT2Activity(GenTau_MT2Activity)'])
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:TauDecayCands(TauDecayCands)','GenLeptons:TauNu(GenTauNu)'])
        process.TreeMaker2.VectorInt.extend(['GenLeptons:MuonTauDecay(GenMu_GenMuFromTau)','GenLeptons:ElectronTauDecay(GenElec_GenElecFromTau)','GenLeptons:TauHadronic(GenTau_GenTauHad)','GenLeptons:TauDecayCandspdgID(TauDecayCands_pdgID)'])

    
    return process
