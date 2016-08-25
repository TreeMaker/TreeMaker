import FWCore.ParameterSet.Config as cms

def JetDepot(process, JetTag, jecUncDir=0, doSmear=True, jerUncDir=0):
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
            jecUncDir = cms.int32(jecUncDir)
        )
        dir = "up" if jecUncDir>0 else "down"
        JetTagOut = cms.InputTag(JetTagOut.value()+"JEC"+dir)
        setattr(process,JetTagOut.value(),patJetsJEC)

    ## ----------------------------------------------------------------------------------------------
    ## JER smearing + uncertainty variations
    ## ----------------------------------------------------------------------------------------------
    
    if doSmear:
        patSmearedJets = cms.EDProducer("SmearedPATJetProducer",
            src = JetTagOut,
            enabled = cms.bool(True),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            skipGenMatching = cms.bool(False),
            # Read from GT
            algopt = cms.string('AK4PFchs_pt'),
            algo = cms.string('AK4PFchs'),
            # Gen jet matching
            genJets = cms.InputTag("slimmedGenJets"),
            dRMax = cms.double(0.2),
            dPtMaxFactor = cms.double(3),
            variation = cms.int32(jerUncDir),
            seed = cms.uint32(37428479),
        )
        dir = "" if jerUncDir==0 else ("up" if jerUncDir>0 else "down")
        JetTagOut = cms.InputTag(JetTagOut.value()+"JER"+dir)
        setattr(process,JetTagOut.value(),patSmearedJets)
    
    return (process, JetTagOut)
