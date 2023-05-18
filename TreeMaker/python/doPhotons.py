import FWCore.ParameterSet.Config as cms

def doPhotonVars(self,process):
    from TreeMaker.TreeMaker.TMEras import TMeras
    from TreeMaker.Utils.photonidisoproducer_cfi import PhotonIDisoProducer
    process.goodPhotons = PhotonIDisoProducer.clone(
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",self.tagname)
    )
    from TreeMaker.Utils.EgammaPostRecoTools import setupEgammaPostRecoSeq 
    phoPostRecoEra = cms.PSet(value = cms.string(""))
    TMeras.TMUL2018.toModify(phoPostRecoEra, value = "2018-UL")
    TMeras.TMUL2017.toModify(phoPostRecoEra, value = "2017-UL")
    TMeras.TMUL2016.toModify(phoPostRecoEra, value = "2016postVFP-UL")
    TMeras.TMUL2016APV.toModify(phoPostRecoEra,value ="2016preVFP-UL")
    setupEgammaPostRecoSeq(process,era=phoPostRecoEra.value.value()),
                           runVID=True,
                           eleIDModules=['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
                                        'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',
                                         'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
                                         'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff'],
                           phoIDModules=['RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V2_cff',
                                         'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_94X_V2_cff']
    )
    self.VectorRecoCand.append("goodPhotons(Photons)")
    self.VectorDouble.append("goodPhotons:isEB(Photons_isEB)")
    self.VectorDouble.append("goodPhotons:genMatched(Photons_genMatched)")
    self.VectorDouble.append("goodPhotons:hadTowOverEM(Photons_hadTowOverEM)")
    self.VectorBool.append("goodPhotons:hasPixelSeed(Photons_hasPixelSeed)")
    self.VectorDouble.append("goodPhotons:passElectronVeto(Photons_passElectronVeto)")
    self.VectorDouble.append("goodPhotons:pfChargedIso(Photons_pfChargedIso)")
    self.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(Photons_pfChargedIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfGammaIso(Photons_pfGammaIso)")
    self.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(Photons_pfGammaIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:pfNeutralIso(Photons_pfNeutralIso)")
    self.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(Photons_pfNeutralIsoRhoCorr)")
    self.VectorDouble.append("goodPhotons:sigmaIetaIeta(Photons_sigmaIetaIeta)")
    self.VectorBool.append("goodPhotons:nonPrompt(Photons_nonPrompt)")
    self.VectorBool.append("goodPhotons:fullID(Photons_fullID)")
    self.VectorBool.append("goodPhotons:electronFakes(Photons_electronFakes)")
    self.VarsBool.append("goodPhotons:hasGenPromptPhoton(hasGenPromptPhoton)")
    self.VectorDouble.append("goodPhotons:mvaValuesIDFall17V2(Photons_mvaValuesID)")
    self.VectorInt.append("goodPhotons:cutBasedIDFall17V2(Photons_cutBasedID)")

    ## add MadGraph-level deltaR between photon or Z and status 23 partons
    if self.geninfo:
        process.madMinPhotonDeltaR = cms.EDProducer("MinDeltaRDouble")
        self.VarsDouble.extend(['madMinPhotonDeltaR:madMinPhotonDeltaR(madMinPhotonDeltaR)'])
        self.VarsInt.extend([   'madMinPhotonDeltaR:madMinDeltaRStatus(madMinDeltaRStatus)'])

    return process
