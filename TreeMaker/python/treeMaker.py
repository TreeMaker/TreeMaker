import FWCore.ParameterSet.Config as cms

TreeMaker = cms.EDAnalyzer(
'TreeMaker',
# Name of the output tree
TreeName = cms.string('RA2Tree'),
#default: output RecoCands as vector<math::PtEtaPhiELorentzVector>
#switches to vector<double> pt, eta, phi, energy if false
doLorentz = cms.bool(True),
#branches are sorted alphabetically by default
sortBranches = cms.bool(True),
#debug the InputTag to branch mapping by printing the mapping to the log
debugTitles = cms.bool(False),
#default: output vector<vector<T>>
#switches to vector<T> values, vector<int> skips
nestedVectors = cms.bool(True),
#if storing nested vectors, stores counts rather than offsets
storeOffsets = cms.bool(False),
#split level for the TBranches
splitLevel = cms.int32(0),
#convert doubles to floats in output
saveFloat = cms.bool(False),
# list of reco candidate objects: for each reco cand collection, the math::LorentzVector will be stored in a vector.
VarsBool = cms.vstring(),
VarsInt = cms.vstring(),
VarsFloat = cms.vstring(),
VarsString = cms.vstring(),
VarsLorentzVector = cms.vstring(),
VarsXYZVector = cms.vstring(),
VarsXYZPoint = cms.vstring(),
VectorBool = cms.vstring(),
VectorInt = cms.vstring(),
VectorFloat = cms.vstring(),
VectorString = cms.vstring(),
VectorLorentzVector = cms.vstring(),
VectorXYZVector = cms.vstring(),
VectorXYZPoint = cms.vstring(),
VectorVectorBool = cms.vstring(),
VectorVectorInt = cms.vstring(),
VectorVectorDouble = cms.vstring(),
VectorVectorString = cms.vstring(),
VectorVectorLorentzVector = cms.vstring(),
VectorVectorXYZVector = cms.vstring(),
VectorVectorXYZPoint = cms.vstring(),
AssocVectorVectorBool = cms.vstring(),
AssocVectorVectorInt = cms.vstring(),
AssocVectorVectorDouble = cms.vstring(),
AssocVectorVectorString = cms.vstring(),
AssocVectorVectorLorentzVector = cms.vstring(),
AssocVectorVectorXYZVector = cms.vstring(),
AssocVectorVectorXYZPoint = cms.vstring(),
VectorRecoCand = cms.vstring(),
TitleMap = cms.vstring(),
)
