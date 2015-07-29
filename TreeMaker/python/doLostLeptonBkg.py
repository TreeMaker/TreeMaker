import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(process,geninfo):
    process.LostLepton = cms.Sequence()

    if geninfo:
        process.LostLepton += process.GenLeptons

    process.LostLepton += process.SelectedPFCandidates

    print "Adding LostLepton calculations to final path and tree"
    process.AdditionalSequence += process.LostLepton 
    process.AdditionalSequence += process.SelectedPFElecCandidates
    process.AdditionalSequence += process.SelectedPFMuCandidates
    process.AdditionalSequence += process.SelectedPFPionCandidates

    process.TreeMaker2.VectorRecoCand.extend(['IsolatedElectronTracksVeto','IsolatedMuonTracksVeto','IsolatedPionTracksVeto'])
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdIsoMuon(selectedIDIsoMuons)','LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)','LeptonsNew:IdElectron(selectedIDElectrons)','SelectedPFCandidates'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDIsoMTW(selectedIDIsoMuons_MTW)','LeptonsNew:MuIDMTW(selectedIDMuons_MTW)','LeptonsNew:ElecIDIsoMTW(selectedIDIsoElectrons_MTW)','LeptonsNew:ElecIDMTW(selectedIDElectrons_MTW)'])
    process.TreeMaker2.VectorInt.extend(['SelectedPFCandidates:Charge(SelectedPFCandidates_Charge)','SelectedPFCandidates:Typ(SelectedPFCandidates_Typ)'])
    if geninfo: # gen information on leptons
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:Boson(GenBoson)','GenLeptons:TauDecayCands(TauDecayCands)','GenLeptons:TauNu(GenTauNu)'])
        process.TreeMaker2.VectorInt.extend(['GenLeptons:BosonPDGId(GenBoson_GenBosonPDGId)','GenLeptons:MuonTauDecay(GenMu_GenMuFromTau)','GenLeptons:ElectronTauDecay(GenElec_GenElecFromTau)','GenLeptons:TauHadronic(GenTau_GenTauHad)','GenLeptons:TauDecayCandspdgID(TauDecayCands_pdgID)'])
    # other information on various variables
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNewTag:IdIsoMuon(selectedIDIsoMuonsNoMiniIso)','LeptonsNewTag:IdIsoElectron(selectedIDIsoElectronsNoMiniIso)'])
    process.TreeMaker2.VectorRecoCand.extend(['slimmedElectrons','slimmedMuons'])
    process.TreeMaker2.VectorRecoCand.extend(['SelectedPFElecCandidates','SelectedPFMuCandidates','SelectedPFPionCandidates'])
    
    return process