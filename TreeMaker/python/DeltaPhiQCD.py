import FWCore.ParameterSet.Config as cms

def DeltaPhiQCD(process, geninfo):
    process.DeltaPhiQCDSeq = cms.Sequence()

    if geninfo:
        #make genjet subcollections
        from TreeMaker.Utils.subJetSelection_cfi import SubGenJetSelection
        
        process.GenHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        process.DeltaPhiQCDSeq += process.GenHTJets
        
        process.GenMHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(5.0),
        )
        process.DeltaPhiQCDSeq += process.GenMHTJets
        process.TreeMaker2.VectorRecoCand.extend ( [ 'GenMHTJets(GenJets)' ] )
        
        #make gen MHT
        from TreeMaker.Utils.mhtdouble_cfi import mhtdouble
        process.GenMHT = mhtdouble.clone(
            JetTag  = cms.InputTag('GenMHTJets'),
        )
        process.DeltaPhiQCDSeq += process.GenMHT
        process.TreeMaker2.VarsDouble.extend(['GenMHT:Pt(GenMHT)','GenMHT:Phi(GenMHT_Phi)'])

    from TreeMaker.Utils.deltaphiqcd_cfi import deltaphiqcd
    process.DeltaPhiQCD = deltaphiqcd.clone (
        JetTagRecoJets      = cms.VInputTag ( 'MHTJets','HTJets' ) ,
        JetTagGenJets       = cms.VInputTag ( 'GenMHTJets', 'GenHTJets' ) ,
        BTagInputTag        = cms.string   ( 'pfCombinedInclusiveSecondaryVertexV2BJetTags' ) ,
        GenParticleTag      = cms.InputTag ( 'prunedGenParticles' ) ,
    )
    process.DeltaPhiQCDSeq += process.DeltaPhiQCD

    from TreeMaker.Utils.genjetproperties_cfi import genjetproperties
    process.GenJetProperties = genjetproperties.clone(
        GenJetTag  = cms.InputTag('GenMHTJets')
    )
    process.DeltaPhiQCDSeq += process.GenJetProperties
 
    process.AdditionalSequence += process.DeltaPhiQCDSeq

    process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:RJetDeltaPhi' ] )

    process.TreeMaker2.VectorDouble.extend ( [ 'DeltaPhiQCD:GenDeltaPhi' ] )
    process.TreeMaker2.VectorDouble.extend ( [ 'GenJetProperties:invisibleEnergy(GenJets_invisibleEnergy)' ] )

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
