import FWCore.ParameterSet.Config as cms

def addJetInfo(process, sequence, JetTag, is74X, userFloats, userInts, suff=""):
    if hasattr(process,sequence):
        theSequence = getattr(process,sequence)
    else:
        print "Unknown sequence: "+sequence
        return

    # add userfloats to jet collection
    if is74X: from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
    else: from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJets as patJetsUpdated

    # default suffix
    if len(suff)==0: suff = "Auxiliary"
    
    JetTagOut = cms.InputTag(JetTag.value()+suff)
    patJetsAuxiliary = patJetsUpdated.clone(
        jetSource = JetTag,
        addJetCorrFactors = cms.bool(False),
        addBTagInfo = cms.bool(False)
    )
    patJetsAuxiliary.userData.userFloats.src += userFloats
    patJetsAuxiliary.userData.userInts.src += userInts
    setattr(process,JetTagOut.value(),patJetsAuxiliary)
    theSequence += getattr(process,JetTagOut.value())
    
    return (process, JetTagOut)