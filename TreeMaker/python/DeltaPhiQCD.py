import FWCore.ParameterSet.Config as cms

def DeltaPhiQCD(process, METTag, is74X):
      from TreeMaker.Utils.deltaphiqcd_cfi import deltaphiqcd
      process.DeltaPhiQCD = deltaphiqcd.clone (
      JetTagRecoJets      = cms.InputTag ( 'GoodJets' ) ,
      JetTagGenJets       = cms.InputTag ( 'slimmedGenJets' ) ,
      BTagInputTag        = cms.string   ( 'combinedInclusiveSecondaryVertexV2BJetTags' ) ,
      GenParticleTag      = cms.InputTag ( 'prunedGenParticles' ) ,
      GenMETTag           = METTag
      )

      if is74X:
         process.DeltaPhiQCD.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')

      process.Baseline += process.DeltaPhiQCD


      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:RJetDeltaPhi' ] )

      process.TreeMaker2.VectorTLorentzVector.extend ( [ 'DeltaPhiQCD:GenLorentzVector' ] )
      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:GenDeltaPhi' ] )

      process.TreeMaker2.VarsDouble.extend ( [ 'DeltaPhiQCD:GenMET' , 'DeltaPhiQCD:GenMETphi' , 'DeltaPhiQCD:GenMHT' , 'DeltaPhiQCD:GenMHTphi' ] )

      process.TreeMaker2.VectorTLorentzVector.extend ( [ 'DeltaPhiQCD:NeutrinoLorentzVector' ] )
      process.TreeMaker2.VectorInt.extend ( [ 'DeltaPhiQCD:NeutrinoPdg' ] )
      process.TreeMaker2.VectorInt.extend ( [ 'DeltaPhiQCD:NeutrinoMotherPdg' ] )

      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:RJetMinDeltaPhiEta24'      ] )
      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:RJetMinDeltaPhiEta5'       ] )
      process.TreeMaker2.VectorInt.extend    ( [ 'DeltaPhiQCD:RJetMinDeltaPhiIndexEta24' ] )
      process.TreeMaker2.VectorInt.extend    ( [ 'DeltaPhiQCD:RJetMinDeltaPhiIndexEta5'  ] )

      process.TreeMaker2.VectorString.extend ( [ 'DeltaPhiQCD:minDeltaPhiNames'          ] )

      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:GenMinDeltaPhiEta24'       ] )
      process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:GenMinDeltaPhiEta5'        ] )
      process.TreeMaker2.VectorInt.extend    ( [ 'DeltaPhiQCD:GenMinDeltaPhiIndexEta24'  ] )
      process.TreeMaker2.VectorInt.extend    ( [ 'DeltaPhiQCD:GenMinDeltaPhiIndexEta5'   ] )


      return process
