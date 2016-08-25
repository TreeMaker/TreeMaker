import FWCore.ParameterSet.Config as cms

def addJetInfo(process, JetTag, userFloats, userInts, suff=""):
    # add userfloats to jet collection
    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJets as patJetsUpdated

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
    
    return (process, JetTagOut)