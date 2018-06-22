import FWCore.ParameterSet.Config as cms

def JetDepot(process, JetTag, jecUncDir=0, storeJec=False, doSmear=True, jerUncDir=0, storeJer=0):
    # starting value
    # for now, assume JECs have already been updated
    JetTagOut = JetTag
    
    ## ----------------------------------------------------------------------------------------------
    ## JEC uncertainty variations
    ## ----------------------------------------------------------------------------------------------

    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer

    if jecUncDir!=0:
        #JEC unc up or down
        patJetsJEC = JetUncertaintyProducer.clone(
            JetTag = JetTagOut,
            jecUncDir = cms.int32(jecUncDir),
            storeUnc = cms.bool(storeJec),
        )
        dir = "up" if jecUncDir>0 else "down"
        JetTagOut = cms.InputTag(JetTagOut.value()+"JEC"+dir)
        setattr(process,JetTagOut.value(),patJetsJEC)

    JetTagOutTmp = JetTagOut

    ## ----------------------------------------------------------------------------------------------
    ## JER smearing + uncertainty variations
    ## ----------------------------------------------------------------------------------------------
    
    from TreeMaker.Utils.smearedpatjet_cfi import SmearedPATJetProducer
    
    if doSmear:
        patSmearedJets = SmearedPATJetProducer.clone(
            src = JetTagOut,
            variation = cms.int32(jerUncDir),
            store_factor = cms.uint32(storeJer),
        )
        dir = "" if jerUncDir==0 else ("up" if jerUncDir>0 else "down")
        JetTagOut = cms.InputTag(JetTagOut.value()+"JER"+dir)
        setattr(process,JetTagOut.value(),patSmearedJets)
    
    return (process, JetTagOutTmp, JetTagOut)
