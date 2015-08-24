import FWCore.ParameterSet.Config as cms

def doTagAndProbe(process,geninfo,METTag):
    from TreeMaker.Utils.activityProducer_cfi import activityProducer
    process.MuonIsoTag = activityProducer.clone(
        objectSource               = cms.InputTag('LeptonsNew:IdMuon'), # probe source
        objectMatchSource          = cms.InputTag('LeptonsNew:IdIsoMuon'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(1),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoMuon'),
    )

    process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("LeptonsNewTag:IdIsoMuon@+ LeptonsNew:IdMuon@-"), # charge conjugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.muonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairs"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("MuonIsoTag","Activity"),
            Passing       = cms.InputTag("MuonIsoTag","Passing"),
            Pt            = cms.InputTag("MuonIsoTag","Pt"),
            Eta           = cms.InputTag("MuonIsoTag","Eta"),
            MTW           = cms.InputTag("MuonIsoTag","MTW"),
            MTWClean      = cms.InputTag("MuonIsoTag","MTWClean"),
            RecomputedMET = cms.InputTag("MuonIsoTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("MuonIsoTag","TagObjectsNum"),
            Weight        = cms.InputTag("MuonIsoTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC                    = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # mu reco
    process.MuonRecoTag = activityProducer.clone(
        #objectSource              = cms.InputTag('SelectedPFCandidatesProbeCands10'), # probe source
        objectSource               = cms.InputTag('SelectedPFMuCandidates'), # probe source
        objectMatchSource          = cms.InputTag('LeptonsNew:IdMuon'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(11),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoMuon'),
    )

    process.tpPairsMuReco = cms.EDProducer("CandViewShallowCloneCombiner",
        #decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFCandidatesProbeCands10@-"), # charge conjugate states are implied
        decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFMuCandidates@-"), # charge conjugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.muonRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsMuReco"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("MuonRecoTag","Activity"),
            Passing       = cms.InputTag("MuonRecoTag","Passing"),
            Pt            = cms.InputTag("MuonRecoTag","Pt"),
            Eta           = cms.InputTag("MuonRecoTag","Eta"),
            MTW           = cms.InputTag("MuonRecoTag","MTW"),
            MTWClean      = cms.InputTag("MuonRecoTag","MTWClean"),
            RecomputedMET = cms.InputTag("MuonRecoTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("MuonRecoTag","TagObjectsNum"),
            Weight        = cms.InputTag("MuonRecoTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC                    = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # elec iso
    from TreeMaker.Utils.activityProducer_cfi import activityProducer

    process.ElectronIsoTag = activityProducer.clone(
        objectSource               = cms.InputTag('LeptonsNew:IdElectron'), # probe source
        objectMatchSource          = cms.InputTag('LeptonsNew:IdIsoElectron'), # to be matched to collection (IDIsoMuons)
        objectTyp                  = cms.int32(2), ## change here for different lepton isotrack type
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoElectron'),
    )

    process.tpPairsElecIso = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("LeptonsNewTag:IdIsoElectron@+ LeptonsNew:IdElectron@-"), # charge conjugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.elecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsElecIso"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
        ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("ElectronIsoTag","Activity"),
            Passing       = cms.InputTag("ElectronIsoTag","Passing"),
            Pt            = cms.InputTag("ElectronIsoTag","Pt"),
            Eta           = cms.InputTag("ElectronIsoTag","Eta"),
            MTW           = cms.InputTag("ElectronIsoTag","MTW"),
            MTWClean      = cms.InputTag("ElectronIsoTag","MTWClean"),
            RecomputedMET = cms.InputTag("ElectronIsoTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("ElectronIsoTag","TagObjectsNum"),
            Weight        = cms.InputTag("ElectronIsoTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #   passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # elec reco
    process.ElectronRecoTag = activityProducer.clone(
        objectSource               = cms.InputTag('slimmedPhotons'), # probe source
        objectMatchSource          = cms.InputTag('LeptonsNew:IdElectron'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(22),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoElectron'),
    )

    process.tpPairsElecReco = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("LeptonsNewTag:IdIsoElectron@+ slimmedPhotons"), # charge coniugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.elecRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsElecReco"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("ElectronRecoTag","Activity"),
            Passing       = cms.InputTag("ElectronRecoTag","Passing"),
            Pt            = cms.InputTag("ElectronRecoTag","Pt"),
            Eta           = cms.InputTag("ElectronRecoTag","Eta"),
            MTW           = cms.InputTag("ElectronRecoTag","MTW"),
            MTWClean      = cms.InputTag("ElectronRecoTag","MTWClean"),
            RecomputedMET = cms.InputTag("ElectronRecoTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("ElectronRecoTag","TagObjectsNum"),
            Weight        = cms.InputTag("ElectronRecoTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #   passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # isolated track muons
    process.IsoTrackMuonTag = activityProducer.clone(
        #objectSource              = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
        objectSource               = cms.InputTag('SelectedPFMuCandidates'), # probe source
        objectMatchSource          = cms.InputTag('IsolatedMuonTracksVeto'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(3),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNewTag:IdIsoMuon'),
        METTag                     = METTag, 
    )

    process.tpPairsIsoTrackMu = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFMuCandidates@-"), # charge coniugate states are implied
        #decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.IsoTrackMuonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsIsoTrackMu"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("IsoTrackMuonTag","Activity"),
            Passing       = cms.InputTag("IsoTrackMuonTag","Passing"),
            Pt            = cms.InputTag("IsoTrackMuonTag","Pt"),
            Eta           = cms.InputTag("IsoTrackMuonTag","Eta"),
            MTW           = cms.InputTag("IsoTrackMuonTag","MTW"),
            MTWClean      = cms.InputTag("IsoTrackMuonTag","MTWClean"),
            RecomputedMET = cms.InputTag("IsoTrackMuonTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("IsoTrackMuonTag","TagObjectsNum"),
            Weight        = cms.InputTag("IsoTrackMuonTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #   passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC                    = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # isolated track electrons
    process.IsoTrackElecTag = activityProducer.clone(
        objectSource               = cms.InputTag('SelectedPFElecCandidates'), # probe source
        #objectSource              = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
        objectMatchSource          = cms.InputTag('IsolatedElectronTracksVeto'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(4),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('LeptonsNewTag:IdIsoElectron'),
        METTag                     = METTag, 
    )

    process.tpPairsIsoTrackElec = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFElecCandidates@-"), # charge coniugate states are implied
        #decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.IsoTrackElecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsIsoTrackElec"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("IsoTrackElecTag","Activity"),
            Passing       = cms.InputTag("IsoTrackElecTag","Passing"),
            Pt            = cms.InputTag("IsoTrackElecTag","Pt"),
            Eta           = cms.InputTag("IsoTrackElecTag","Eta"),
            MTW           = cms.InputTag("IsoTrackElecTag","MTW"),
            MTWClean      = cms.InputTag("IsoTrackElecTag","MTWClean"),
            RecomputedMET = cms.InputTag("IsoTrackElecTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("IsoTrackElecTag","TagObjectsNum"),
            Weight        = cms.InputTag("IsoTrackElecTag","Weight"),
            ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #   passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC                    = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    # isolated track pion
    process.IsoTrackPionTag = activityProducer.clone(
        objectSource               = cms.InputTag('SelectedPFPionCandidates'), # probe source
        #objectSource              = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
        objectMatchSource          = cms.InputTag('IsolatedPionTracksVeto'), # to be matched to collection  (IDIsoMuons)
        objectTyp                  = cms.int32(5),
        activityTyp                = cms.int32(0),
        maxDeltaR                  = cms.double(1.0),
        jetSrc                     = cms.InputTag('HTJets'),
        TagObjectForMTWComputation = cms.InputTag('IsolatedPionTracksVeto'),
        METTag                     = METTag, 
    )

    process.tpPairsIsoTrackPion = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("IsolatedPionTracksVeto@+ SelectedPFPionCandidates@-"), # charge coniugate states are implied
        #decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
        cut   = cms.string("60.0 < mass < 130.0"),
    )

    process.IsoTrackPionIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
        # pairs
        tagProbePairs      = cms.InputTag("tpPairsIsoTrackPion"),
        #arbitration       = cms.string("OneProbe"),
        arbitration        = cms.string("None"),
        massForArbitration = cms.double(91),
        # variables to use
        variables = cms.PSet(
            ## methods of reco::Candidate
            eta           = cms.string("eta"),
            pt            = cms.string("pt"),
            #muonsMiniIso = cms.string("muonsMiniIso"),
            #miniIso      = cms.string("miniIso"),
            ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
            #nsegm        = cms.string("numberOfMatches"), 
            ## this one is an external variable
            #drj          = cms.InputTag("drToNearestJet"),
            #nGV          = cms.InputTag("goodVertices.size()"),
            #miniIso      = cms.InputTag("probeMuons","muonsMiniIso"),
            #miniIso      = cms.InputTag("probeMuons","miniIso"),
            activity      = cms.InputTag("IsoTrackPionTag","Activity"),
            Passing       = cms.InputTag("IsoTrackPionTag","Passing"),
            Pt            = cms.InputTag("IsoTrackPionTag","Pt"),
            Eta           = cms.InputTag("IsoTrackPionTag","Eta"),
            MTW           = cms.InputTag("IsoTrackPionTag","MTW"),
            RecomputedMET = cms.InputTag("IsoTrackPionTag","RecomputedMET"),
            TagObjectsNum = cms.InputTag("IsoTrackPionTag","TagObjectsNum"),
            Weight        = cms.InputTag("IsoTrackPionTag","Weight"),
        ),
        # choice of what defines a 'passing' probe
        flags = cms.PSet(
            ## one defined by an external collection of passing probes
            #passingCal = cms.InputTag("probesPassingCal"), 
            ## two defined by simple string cuts
            #   passingGlb = cms.string("isGlobalMuon"),
            passingIso = cms.InputTag("LeptonsNew:IdMuon"),
            #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
            #passingGlb = cms.string("Passing<0.5"),
            #passingIso = cms.InputTag("MuonIsoTag","Passing"),
            #passingIso = cms.InputTag("probePassingIso"),
        ),
        # mc-truth info
        isMC                    = cms.bool(False),
        motherPdgId             = cms.vint32(22,23),
        #makeMCUnbiasTree       = cms.bool(True),
        #checkMotherInUnbiasEff = cms.bool(True),
        #tagMatches             = cms.InputTag("muMcMatch"),
        #probeMatches           = cms.InputTag("muMcMatch"),
        #allProbes              = cms.InputTag("probeMuons"),
    )

    process.Baseline += process.SelectedPFCandidatesProbeCands5
    process.Baseline += process.SelectedPFCandidatesProbeCands10
    process.Baseline += process.SelectedPFElecCandidates
    process.Baseline += process.SelectedPFMuCandidates
    process.Baseline += process.SelectedPFPionCandidates
    if geninfo : 
        process.Baseline += process.GenLeptons
    process.Baseline += process.JetsProperties
    process.Baseline += process.SelectedPFCandidates
    process.Baseline += process.MuonIsoTag
    process.Baseline += process.tpPairs
    process.Baseline += process.muonIsoEffs
    process.Baseline += process.MuonRecoTag
    process.Baseline += process.tpPairsMuReco
    process.Baseline += process.muonRecoEffs
    process.Baseline += process.ElectronIsoTag
    process.Baseline += process.tpPairsElecIso
    process.Baseline += process.elecIsoEffs
    process.Baseline += process.ElectronRecoTag
    process.Baseline += process.tpPairsElecReco
    process.Baseline += process.elecRecoEffs
    process.Baseline += process.IsoTrackMuonTag
    process.Baseline += process.tpPairsIsoTrackMu
    process.Baseline += process.IsoTrackMuonIsoEffs
    process.Baseline += process.IsoTrackElecTag
    process.Baseline += process.tpPairsIsoTrackElec
    process.Baseline += process.IsoTrackElecIsoEffs
    process.Baseline += process.IsoTrackPionTag
    process.Baseline += process.tpPairsIsoTrackPion
    process.Baseline += process.IsoTrackPionIsoEffs
    process.TreeMaker2.VectorRecoCand.extend(['slimmedPhotons'])

    return process