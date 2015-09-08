import FWCore.ParameterSet.Config as cms

def DeltaPhiQCD(process, METTag):
      from TreeMaker.Utils.deltaphiqcd_cfi import deltaphiqcd
      process.DeltaPhiQCD = deltaphiqcd.clone(
      JetTagRecoJets      = cms.InputTag('GoodJets'),
      JetTagGenJets       = cms.InputTag('slimmedGenJets'),
      BTagInputTag        = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
      GenParticleTag      = cms.InputTag('prunedGenParticles'),
      GenMETTag           = METTag
      )
      process.Baseline += process.DeltaPhiQCD


      process.TreeMaker2.VectorTLorentzVector.extend(['DeltaPhiQCD:RJetLorentzVector'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:RJetCSV'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:RJetPartonFlavor'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:RJetDeltaPhi'])

      process.TreeMaker2.VectorTLorentzVector.extend(['DeltaPhiQCD:RJetLorentzVector'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:GenJetCSV'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:GenJetPartonFlavor'])
      process.TreeMaker2.VectorDouble.extend(['DeltaPhiQCD:GenJetDeltaPhi'])

      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMET','DeltaPhiQCD:GenMETphi','DeltaPhiQCD:GenMHT','DeltaPhiQCD:GenMHTphi'])

      process.TreeMaker2.VectorTLorentzVector.extend(['DeltaPhiQCD:NeutrinoLorentzVector'])
      process.TreeMaker2.VectorInt.extend(['DeltaPhiQCD:NeutrinoPdg'])
      process.TreeMaker2.VectorInt.extend(['DeltaPhiQCD:NeutrinoMotherPdg'])

      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetMinDeltaPhiStarEta5','DeltaPhiQCD:RJetMinDeltaPhiStarEta24','DeltaPhiQCD:RJetMinDeltaPhiStarIndexEta5','DeltaPhiQCD:RJetMinDeltaPhiStarIndexEta24'])
      process.TreeMaker2.VarsInt.extend(['DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle5','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle5','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle4','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle4','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta5Njle3','DeltaPhiQCD:RJetMinDeltaPhiJetIndexEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:RJetMinDeltaPhiEta5Njle5','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle5','DeltaPhiQCD:RJetMinDeltaPhiEta5Njle4','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle4','DeltaPhiQCD:RJetMinDeltaPhiEta5Njle3','DeltaPhiQCD:RJetMinDeltaPhiEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMinDeltaPhiStarEta5','DeltaPhiQCD:GenMinDeltaPhiStarEta24','DeltaPhiQCD:GenMinDeltaPhiStarIndexEta5','DeltaPhiQCD:GenMinDeltaPhiStarIndexEta24'])
      process.TreeMaker2.VarsInt.extend(['DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle5','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle5','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle4','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle4','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta5Njle3','DeltaPhiQCD:GenMinDeltaPhiJetIndexEta24Njle3'])
      process.TreeMaker2.VarsDouble.extend(['DeltaPhiQCD:GenMinDeltaPhiEta5Njle5','DeltaPhiQCD:GenMinDeltaPhiEta24Njle5','DeltaPhiQCD:GenMinDeltaPhiEta5Njle4','DeltaPhiQCD:GenMinDeltaPhiEta24Njle4','DeltaPhiQCD:GenMinDeltaPhiEta5Njle3','DeltaPhiQCD:GenMinDeltaPhiEta24Njle3'])


      return process
