import FWCore.ParameterSet.Config as cms

def doZinvBkg(process,is74X,METTag):
    ##### add branches for photon studies
    process.TreeMaker2.VectorDouble.append("goodPhotons:isEB(photon_isEB)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:genMatched(photon_genMatched)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hadTowOverEM(photon_hadTowOverEM)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hasPixelSeed(photon_hasPixelSeed)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:passElectronVeto(photon_passElectronVeto)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIso(photon_pfChargedIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(photon_pfChargedIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIso(photon_pfGammaIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(photon_pfGammaIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIso(photon_pfNeutralIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(photon_pfNeutralIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:sigmaIetaIeta(photon_sigmaIetaIeta)")

    process.TreeMaker2.VectorRecoCand.append("slimmedPhotons(photonCands)")
    
    process.ZinvClean = cms.Sequence()

    from TreeMaker.Utils.zproducer_cfi import ZProducer
    process.maketheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon')
    )
    process.ZinvClean += process.maketheZs
    process.TreeMaker2.VarsInt.extend(['maketheZs:ZNum'])
    process.TreeMaker2.VectorTLorentzVector.append("maketheZs:Zp4")
    
    from TreeMaker.Utils.jetcleaner_cfi import JetCleaner
    process.cleanTheJets = JetCleaner.clone(
       JetTag      = cms.InputTag('GoodJets'),
       ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
       ElectronR   = cms.double(0.4),
       MuonTag     = cms.InputTag('LeptonsNew:IdIsoMuon'),
       MuonR       = cms.double(0.4),
       PhotonTag   = cms.InputTag('goodPhotons', 'bestPhoton'),
       PhotonR     = cms.double(0.4)
    )
    process.ZinvClean += process.cleanTheJets

    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    process.HTJetsclean = SubJetSelection.clone(
       JetTag = cms.InputTag('cleanTheJets', 'GoodJetsclean'),
       MinPt  = cms.double(30),
       MaxEta = cms.double(2.4),
    )
    process.ZinvClean += process.HTJetsclean

    from TreeMaker.Utils.htdouble_cfi import htdouble
    process.HTclean = htdouble.clone(
       JetTag = cms.InputTag('HTJetsclean'),
    )
    process.ZinvClean += process.HTclean
    process.TreeMaker2.VarsDouble.extend(['HTclean'])

    from TreeMaker.Utils.njetint_cfi import njetint
    process.NJetsclean = njetint.clone(
       JetTag = cms.InputTag('HTJetsclean'),
    )
    process.ZinvClean += process.NJetsclean
    process.TreeMaker2.VarsInt.extend(['NJetsclean'])

    from TreeMaker.Utils.btagint_cfi import btagint
    process.BTagsclean = btagint.clone(
       JetTag       = cms.InputTag('HTJetsclean'),
       BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
       BTagCutValue = cms.double(0.814)
    )
    if is74X:
        process.BTagsclean.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')
        process.BTagsclean.BTagCutValue = cms.double(0.890)

    process.ZinvClean += process.BTagsclean
    process.TreeMaker2.VarsInt.extend(['BTagsclean'])

    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    process.MHTJetsclean = SubJetSelection.clone(
       JetTag = cms.InputTag('cleanTheJets', 'GoodJetsclean'),
       MinPt = cms.double(30),
       MaxEta = cms.double(5.0),
    )
    process.ZinvClean += process.MHTJetsclean

    from TreeMaker.Utils.deltaphidouble_cfi import deltaphidouble
    process.DeltaPhiClean = deltaphidouble.clone(
        DeltaPhiJets  = cms.InputTag('HTJetsclean'),
        MHTJets  = cms.InputTag("MHTJetsclean"),
        )
    process.ZinvClean += process.DeltaPhiClean
    process.TreeMaker2.VarsDouble.extend(['DeltaPhiClean:DeltaPhi1(DeltaPhi1clean)','DeltaPhiClean:DeltaPhi2(DeltaPhi2clean)','DeltaPhiClean:DeltaPhi3(DeltaPhi3clean)','DeltaPhiClean:DeltaPhi4(DeltaPhi4clean)'])
    
    from TreeMaker.Utils.subJetSelection_cfi import SubJetSelection
    from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
    process.MHTclean = mhtdouble.clone(
       JetTag = cms.InputTag('MHTJetsclean'),
    )
    process.ZinvClean += process.MHTclean
    process.TreeMaker2.VarsDouble.extend(['MHTclean:Pt(MHTclean)'])

    from TreeMaker.Utils.metdouble_cfi import metdouble
    process.METclean = metdouble.clone(
       METTag = METTag,
       JetTag = cms.InputTag('HTJetsclean'),
       cleanTag = cms.untracked.VInputTag(cms.InputTag('LeptonsNew:IdIsoElectron'), cms.InputTag('LeptonsNew:IdIsoMuon'), cms.InputTag('goodPhotons', 'bestPhoton'))
    )
    process.ZinvClean += process.METclean
    process.TreeMaker2.VarsDouble.extend(['METclean:minDeltaPhiN(minDeltaPhiNclean)', 'METclean:Pt(METPtclean)'])

    process.AdditionalSequence += process.ZinvClean
    
    return process
