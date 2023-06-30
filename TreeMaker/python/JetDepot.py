import FWCore.ParameterSet.Config as cms

def JetDepot(process, JetTag, jecUncDir=0, storeJec=False, doSmear=True, jerUncDir=0, storeJer=0):
    # starting value
    # for now, assume JECs have already been updated
    JetTagOut = JetTag
    
    ## ----------------------------------------------------------------------------------------------
    ## JEC uncertainty variations
    ## ----------------------------------------------------------------------------------------------

    from TreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer

    if jecUncDir!=0 or storeJec:
        #JEC unc up or down
        patJetsJEC = JetUncertaintyProducer.clone(
            JetTag = JetTagOut,
            jecUncDir = cms.int32(jecUncDir),
            storeUnc = cms.bool(storeJec),
        )
        dir = "up" if jecUncDir>0 else "down" if jecUncDir<0 else "unc"
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

from TreeMaker.TreeMaker.addJetInfo import addJetInfo

def JetVariations(self, process, JetTag, SkipTag=cms.VInputTag(), suff='', puppiSpecific='puppiSpecificAK8', vars='makeJetVars'):
        makeJetVarsFn = getattr(self,vars)

        # JEC unc up
        process, JetTagJECTmp, JetTagJECup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=1,
            storeJec=True, # get JEC unc value (in intermediate tag Tmp)
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get JER smearing factor w/ JEC variation
        )
        process = makeJetVarsFn(process,
            JetTag=JetTagJECup,
            suff=suff+'JECup',
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JEC",
            puppiSpecific=puppiSpecific,
        )
        
        # JEC unc down
        process, _, JetTagJECdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=-1,
            doSmear=True,
            jerUncDir=0,
            storeJer=2, # get JER smearing factor w/ JEC variation
        )
        process = makeJetVarsFn(process,
            JetTag=JetTagJECdown,
            suff=suff+'JECdown',
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JEC",
            puppiSpecific=puppiSpecific,
        )

        # JER unc up
        process, _, JetTagJERup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=1,
            storeJer=1,
        )
        process = makeJetVarsFn(process,
            JetTag=JetTagJERup,
            suff=suff+'JERup',
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JER",
            puppiSpecific=puppiSpecific,
        )
        
        # JER unc down
        process, _, JetTagJERdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=-1,
            storeJer=1,
        )
        process = makeJetVarsFn(process,
            JetTag=JetTagJERdown,
            suff=suff+'JERdown',
            storeProperties=0,
            SkipTag=SkipTag,
            systType="JER",
            puppiSpecific=puppiSpecific,
        )

        # append factors to central collection
        process, JetTag = addJetInfo(process, JetTag, [JetTagJECTmp.value(),JetTagJERup.value(),JetTagJERdown.value()], [])

        return (process, JetTagJECTmp, JetTagJECup, JetTagJECdown, JetTagJERup, JetTagJERdown, JetTag)
