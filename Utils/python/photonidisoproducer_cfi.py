import FWCore.ParameterSet.Config as cms

PhotonIDisoProducer = cms.EDProducer("PhotonIDisoProducer",
    photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
    electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
    conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions"),
    beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot"),
    ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    genParCollection       = cms.untracked.InputTag("prunedGenParticles"), 
    effArEtaLow            = cms.vdouble(0.,     1.000,  1.479,  2.0,    2.2,    2.3,     2.4), #lower boundaries of |eta| in effective area(EA) calculation
    effArEtaHigh           = cms.vdouble(1.,     1.479,  2.000,  2.2,    2.3,    2.4,     99.), #upper boundaries of |eta| in effective area(EA) calculation
    effArChHad             = cms.vdouble(0.0385, 0.0468, 0.0435, 0.0378, 0.0338, 0.0314,  0.0269),#EA for charged hadrons in diiferent |eta| ranges
    effArNuHad             = cms.vdouble(0.0636, 0.1103, 0.0759, 0.0236, 0.0151, 0.00007, 0.0132),#EA for neutral hadrons in diiferent |eta| ranges
    effArGamma             = cms.vdouble(0.1240, 0.1093, 0.0631, 0.0779, 0.0999, 0.1155,  0.1373),#EA for photons(gamma) in diiferent |eta| ranges
    hadTowOverEm_EB_cut    = cms.double(0.105), #H/E cut in EB
    hadTowOverEm_EE_cut    = cms.double(0.029), #H/E cut in EE
    sieie_EB_cut           = cms.double(0.0103), #Sigma ieta_ieta cut in EB
    sieie_EE_cut           = cms.double(0.0276), #Sigma ieta_ieta cut in EE
    pfChIsoRhoCorr_EB_cut  = cms.double(2.839), #Pho corrected PF charged ISO in EB
    pfChIsoRhoCorr_EE_cut  = cms.double(2.150), #Pho corrected PF charged ISO in EE
    pfNuIsoRhoCorr_EB_cut  = cms.vdouble(9.188,  0.0126, 0.000026), #Rho corrected PF neutral ISO = [0]+[1]*pt+[2]*pt^2
    pfNuIsoRhoCorr_EE_cut  = cms.vdouble(10.471, 0.0119, 0.000025), #Rho corrected PF neutral ISO = [0]+[1]*pt+[2]*pt^2
    pfGmIsoRhoCorr_EB_cut  = cms.vdouble(2.956, 0.0035), #Rho corrected gamma ISO = [0]+[1]*pt
    pfGmIsoRhoCorr_EE_cut  = cms.vdouble(4.895, 0.0040), #Rho corrected gamma ISO = [0]+[1]*pt
    debug                  = cms.untracked.bool(False)
)