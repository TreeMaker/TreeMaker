import FWCore.ParameterSet.Config as cms

def doLostLeptonBkg(process,geninfo):
    process.LostLepton = cms.Sequence()

    if geninfo:
        process.LostLepton += process.GenLeptons


    print "Adding LostLepton calculations to final path and tree"
    process.AdditionalSequence += process.LostLepton
    
    process.TreeMaker2.VectorRecoCand.extend(['IsolatedElectronTracksVeto','IsolatedMuonTracksVeto','IsolatedPionTracksVeto'])
    process.TreeMaker2.VectorDouble.extend(['IsolatedElectronTracksVeto:pfcandsmT(IsolatedElectronTracksVeto_MTW)','IsolatedMuonTracksVeto:pfcandsmT(IsolatedMuonTracksVeto_MTW)','IsolatedPionTracksVeto:pfcandsmT(IsolatedPionTracksVeto_MTW)'])
    process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdIsoMuon(selectedIDIsoMuons)','LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)','LeptonsNew:IdElectron(selectedIDElectrons)'])
    process.TreeMaker2.VectorDouble.extend(['LeptonsNew:MuIDIsoMTW(selectedIDIsoMuons_MTW)','LeptonsNew:MuIDMTW(selectedIDMuons_MTW)','LeptonsNew:ElecIDIsoMTW(selectedIDIsoElectrons_MTW)','LeptonsNew:ElecIDMTW(selectedIDElectrons_MTW)'])
    if geninfo: # gen information on leptons
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:Muon(GenMus)','GenLeptons:Electron(GenEls)','GenLeptons:Tau(GenTaus)'])
        process.TreeMaker2.VectorRecoCand.extend(['GenLeptons:TauDecayCands(TauDecayCands)','GenLeptons:TauNu(GenTauNu)'])
        process.TreeMaker2.VectorInt.extend(['GenLeptons:MuonTauDecay(GenMu_GenMuFromTau)','GenLeptons:ElectronTauDecay(GenElec_GenElecFromTau)','GenLeptons:TauHadronic(GenTau_GenTauHad)','GenLeptons:TauDecayCandspdgID(TauDecayCands_pdgID)'])

    
    return process
