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
    pt_cut                 = cms.double(30),
    high_pt_cut            = cms.double(100),
    effArEtaLow            = cms.vdouble(0.,     1.000,  1.479,  2.0,    2.2,    2.3,     2.4), #lower boundaries of |eta| in effective area(EA) calculation
    effArEtaHigh           = cms.vdouble(1.,     1.479,  2.000,  2.2,    2.3,    2.4,     99.), #upper boundaries of |eta| in effective area(EA) calculation
    effArChHad             = cms.vdouble(0.0112, 0.0108, 0.0106, 0.01002,0.0098, 0.0089,  0.0087),#EA for charged hadrons in diiferent |eta| ranges
    effArNuHad             = cms.vdouble(0.0668, 0.1054, 0.0786, 0.0233, 0.0078, 0.0028,  0.0137),#EA for neutral hadrons in diiferent |eta| ranges
    effArGamma             = cms.vdouble(0.1113, 0.0953, 0.0619, 0.0837, 0.1070, 0.1212,  0.1466),#EA for photons(gamma) in diiferent |eta| ranges
    hadTowOverEm_EB_cut    = cms.double(0.04596), #H/E cut in EB
    hadTowOverEm_EE_cut    = cms.double(0.0590), #H/E cut in EE
    sieie_EB_cut           = cms.double(0.0106), #Sigma ieta_ieta cut in EB
    sieie_EE_cut           = cms.double(0.0272), #Sigma ieta_ieta cut in EE
    pfChIsoRhoCorr_EB_cut  = cms.double(1.694), #Pho corrected PF charged ISO in EB
    pfChIsoRhoCorr_EE_cut  = cms.double(2.089), #Pho corrected PF charged ISO in EE
    pfNuIsoRhoCorr_EB_cut  = cms.vdouble(24.032, 0.01512, 0.00002259), #Rho corrected PF neutral ISO = [0]+[1]*pt+[2]*pt^2
    pfNuIsoRhoCorr_EE_cut  = cms.vdouble(19.722, 0.0117, 0.000023), #Rho corrected PF neutral ISO = [0]+[1]*pt+[2]*pt^2
    pfGmIsoRhoCorr_EB_cut  = cms.vdouble(2.876, 0.004017), #Rho corrected gamma ISO = [0]+[1]*pt
    pfGmIsoRhoCorr_EE_cut  = cms.vdouble(4.162, 0.0037), #Rho corrected gamma ISO = [0]+[1]*pt
    debug                  = cms.untracked.bool(False)
)
