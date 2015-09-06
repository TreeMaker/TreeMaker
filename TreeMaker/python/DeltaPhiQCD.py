import FWCore.ParameterSet.Config as cms

def DeltaPhiQCD(process):

      from AllHadronicSUSY.Utils.deltaphiqcd_cfi import deltaphiqcd
      process.DeltaPhiQCD = deltaphiqcd.clone(
      JetTagRecoJets  = cms.InputTag('GoodJets'),
      JetTagGenJets   = cms.InputTag('slimmedGenJets'),
      BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
      GenParticleTag = cms.InputTag('prunedGenParticles'),
      GenMETTag = cms.InputTag("slimmedMETs")
      )
      process.Baseline += process.DeltaPhiQCD

      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMET','DeltaPhiQCD:GenMETPhi'])

      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenNuPt1','DeltaPhiQCD:GenNuEta1','DeltaPhiQCD:GenNuPhi1','DeltaPhiQCD:GenNuPt2','DeltaPhiQCD:GenNuEta2','DeltaPhiQCD:GenNuPhi2','DeltaPhiQCD:GenNuPt3','DeltaPhiQCD:GenNuEta3', 'DeltaPhiQCD:GenNuPhi3','DeltaPhiQCD:GenNuPt4','DeltaPhiQCD:GenNuEta4','DeltaPhiQCD:GenNuPhi4'])
      process.TreeMaker2.VarsInt.extend(['DeltaPhiQCD:GenNuPDGId1','DeltaPhiQCD:GenNuMotherPDGId1','DeltaPhiQCD:GenNuPDGId2','DeltaPhiQCD:GenNuMotherPDGId2','DeltaPhiQCD:GenNuPDGId3','DeltaPhiQCD:GenNuMotherPDGId3','DeltaPhiQCD:GenNuPDGId4','DeltaPhiQCD:GenNuMotherPDGId4'])

      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetPt1','DeltaPhiQCD:RJetEta1','DeltaPhiQCD:RJetPhi1','DeltaPhiQCD:RJetPt2','DeltaPhiQCD:RJetEta2','DeltaPhiQCD:RJetPhi2','DeltaPhiQCD:RJetPt3','DeltaPhiQCD:RJetEta3','DeltaPhiQCD:RJetPhi3','DeltaPhiQCD:RJetPt4','DeltaPhiQCD:RJetEta4','DeltaPhiQCD:RJetPhi4','DeltaPhiQCD:RJetPt5','DeltaPhiQCD:RJetEta5','DeltaPhiQCD:RJetPhi5','DeltaPhiQCD:RJetPt6','DeltaPhiQCD:RJetEta6','DeltaPhiQCD:RJetPhi6','DeltaPhiQCD:RJetPt7','DeltaPhiQCD:RJetEta7','DeltaPhiQCD:RJetPhi7','DeltaPhiQCD:RJetPt8','DeltaPhiQCD:RJetEta8','DeltaPhiQCD:RJetPhi8'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:CSV1','DeltaPhiQCD:CSV2','DeltaPhiQCD:CSV3','DeltaPhiQCD:CSV4','DeltaPhiQCD:CSV5','DeltaPhiQCD:CSV6','DeltaPhiQCD:CSV7','DeltaPhiQCD:CSV8'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetDeltaPhi1','DeltaPhiQCD:RJetDeltaPhi2','DeltaPhiQCD:RJetDeltaPhi3','DeltaPhiQCD:RJetDeltaPhi4','DeltaPhiQCD:RJetDeltaPhi5','DeltaPhiQCD:RJetDeltaPhi6','DeltaPhiQCD:RJetDeltaPhi7','DeltaPhiQCD:RJetDeltaPhi8','DeltaPhiQCD:RPartonFlavor1','DeltaPhiQCD:RPartonFlavor2','DeltaPhiQCD:RPartonFlavor3','DeltaPhiQCD:RPartonFlavor4','DeltaPhiQCD:RPartonFlavor5','DeltaPhiQCD:RPartonFlavor6','DeltaPhiQCD:RPartonFlavor7','DeltaPhiQCD:RPartonFlavor8'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenPt1','DeltaPhiQCD:GenEta1','DeltaPhiQCD:GenPhi1','DeltaPhiQCD:GenPt2','DeltaPhiQCD:GenEta2','DeltaPhiQCD:GenPhi2','DeltaPhiQCD:GenPt3','DeltaPhiQCD:GenEta3','DeltaPhiQCD:GenPhi3','DeltaPhiQCD:GenPt4','DeltaPhiQCD:GenEta4','DeltaPhiQCD:GenPhi4','DeltaPhiQCD:GenPt5','DeltaPhiQCD:GenEta5','DeltaPhiQCD:GenPhi5','DeltaPhiQCD:GenPt6','DeltaPhiQCD:GenEta6','DeltaPhiQCD:GenPhi6','DeltaPhiQCD:GenPt7','DeltaPhiQCD:GenEta7','DeltaPhiQCD:GenPhi7','DeltaPhiQCD:GenPt8','DeltaPhiQCD:GenEta8','DeltaPhiQCD:GenPhi8','DeltaPhiQCD:GenMHT','DeltaPhiQCD:GenMHTphi'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetMinDeltaPhiStarEta5','DeltaPhiQCD:RJetMinDeltaPhiStarEta24','DeltaPhiQCD:RJetMinDeltaPhiStarIndexEta5','DeltaPhiQCD:RJetMinDeltaPhiStarIndexEta24'])
      process.TreeMaker2.VarsInt.extend(['DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle5','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle5','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle4','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle4','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle3','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetMinDeltaPhiEta5Njle5','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle5','DeltaPhiQCD:RJetMinDeltaPhiEta5Njle4','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle4','DeltaPhiQCD:RJetMinDeltaPhiEta5Njle3','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMinDeltaPhiStarEta5','DeltaPhiQCD:GenMinDeltaPhiStarEta24','DeltaPhiQCD:GenMinDeltaPhiStarIndexEta5','DeltaPhiQCD:GenMinDeltaPhiStarIndexEta24'])
      process.TreeMaker2.VarsInt.extend(['DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle5','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle5','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle4','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle4','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle3','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMinDeltaPhiEta5Njle5','DeltaPhiQCD:GenMinDeltaPhiEta24Njle5','DeltaPhiQCD:GenMinDeltaPhiEta5Njle4','DeltaPhiQCD:GenMinDeltaPhiEta24Njle4','DeltaPhiQCD:GenMinDeltaPhiEta5Njle3','DeltaPhiQCD:GenMinDeltaPhiEta24Njle3'])

      return process
