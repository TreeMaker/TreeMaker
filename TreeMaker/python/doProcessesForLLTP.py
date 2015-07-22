import FWCore.ParameterSet.Config as cms

def doProcessesForLLTP(process,is74X,geninfo):
    from TreeMaker.Utils.selectpfcandidates_cfi import SelectPFCandidates
    process.SelectedPFCandidatesProbeCands5 = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(5),
        MaxEta                = cms.double(2.5),
    )
    process.SelectedPFCandidatesProbeCands10 = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(10),
        MaxEta                = cms.double(2.5),
    )
    process.SelectedPFElecCandidates = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(5),
        MaxEta                = cms.double(2.5),
        SelectpdgIDTyp        = cms.int32(11),
    )
    process.SelectedPFMuCandidates = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(5),
        MaxEta                = cms.double(2.4),
        SelectpdgIDTyp        = cms.int32(13), 
    )
    process.SelectedPFPionCandidates = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(10),
        MaxEta                = cms.double(2.4),
        SelectpdgIDTyp        = cms.int32(211), 
    )
    process.SelectedPFCandidates = SelectPFCandidates.clone(
        PackedPFCandidatesTag = cms.InputTag('packedPFCandidates'),
        MinPt                 = cms.double(4),
        MaxEta                = cms.double(5.0),
    )
    
    if geninfo:
        from TreeMaker.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
        process.GenLeptons = genLeptonRecoCand.clone(
            PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
        )

    from TreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsProperties = jetproperties.clone(
        JetTag       = cms.InputTag('HTJets'),
        BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
        METTag       = cms.InputTag("slimmedMETs"),
    )
    if is74X: process.JetsProperties.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')

    return process