import FWCore.ParameterSet.Config as cms

def addJetInfo(process, JetTag, userFloats=[], userInts=[], btagDiscrs=cms.VInputTag(), suff=""):
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
    if len(btagDiscrs)>0:
        patJetsAuxiliary.discriminatorSources = btagDiscrs
        patJetsAuxiliary.addBTagInfo = cms.bool(True)
    setattr(process,JetTagOut.value(),patJetsAuxiliary)
    
    return (process, JetTagOut)