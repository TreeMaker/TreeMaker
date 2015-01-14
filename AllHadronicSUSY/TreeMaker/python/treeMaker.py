import FWCore.ParameterSet.Config as cms

TreeMaker = cms.EDProducer(
'TreeMaker',
# Name of the output tree
TreeName          = cms.string('RA2Tree'),
## might help if something isn working wilil produce couts
debug = cms.bool(False),
# list of reco candidate objects eg leptons: For each reco cand collection the pt eta phi e and Tlorentzvector will be stored in arrays. In addition optional float int or bool variables can be stored
# syntax example:  VarsRecoCand = cms.vstring('selectedIDIsoMuons(selectedIDIsoMuonsName)|Isolation(F_NameOfIsolationInTreeisolation)|Jup(b_nameofJup)|wwww(F)','selectedIDMuons','selectedRecoIsoElec','selectedRecoElec'),
# selectedIDIsoMuons would be the tag of the reco candiate 
# (selectedIDIsoMuonsName ) optoinal naming in the tree if not defined tag name will be used
# separated with | addition variables int float or bool defined by: TagName(typ) always needed optional TagName(typ_NameInTree) 
VarsTLoretzVector = cms.vstring(),
VarsString = cms.vstring(),
VarsDouble = cms.vstring(),
VarsInt = cms.vstring(),
VarsBool = cms.vstring(),
VarsRecoCand = cms.vstring(),
VectorDouble = cms.vstring(),
VectorInt = cms.vstring(),
VectorBool = cms.vstring(),
VectorString = cms.vstring(),
VectorTLorentzVector = cms.vstring(),
)
