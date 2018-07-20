class Scenario:
    def __init__(self,sname):
        if sname == "Spring16Fastsig":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_miniAODv2",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                signal=True,
                jecfile="data/jec/Spring16_25nsFastSimMC_V1",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Spring16Pmssm":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_miniAODv2",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                signal=True,
                pmssm=True,
                jecfile="data/jec/Spring16_25nsFastSimMC_V1",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_TrancheIV_v6",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Summer16_23Sep2016V3_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16sig":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_TrancheIV_v6",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Summer16_23Sep2016V3_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "2016H":
            self.set_vars(
                globaltag="80X_dataRun2_Prompt_v14",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt",
                jecfile="data/jec/Summer16_23Sep2016AllV3_DATA",
                residual=True,
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "2016ReReco23Sep":
            self.set_vars(
                globaltag="80X_dataRun2_2016SeptRepro_v3",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
                jecfile="data/jec/Summer16_23Sep2016AllV3_DATA",
                residual=True,
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "2016ReMiniAOD03Feb":
            self.set_vars(
                globaltag="80X_dataRun2_2016SeptRepro_v7",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile="data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
                jecfile="data/jec/Summer16_23Sep2016AllV3_DATA",
                residual=True,
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16LegacyReMiniAOD":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_TrancheIV_v6",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16LegacyReMiniAODsig":
            self.set_vars(
                globaltag="80X_mcRun2_asymptotic_2016_TrancheIV_v6",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "2016LegacyReMiniAOD":
            self.set_vars(
                globaltag="80X_dataRun2_2016SeptRepro_v7",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile="data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
                jecfile="data/jec/Summer16_07Aug2017All_V10_DATA",
                residual=True,
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Fall17":
            self.set_vars(
                globaltag="94X_mc2017_realistic_v13",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Fall17_17Nov2017_V6_MC",
                jerfile="data/jer/Fall17_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "Fall17sig":
            self.set_vars(
                globaltag="94X_mc2017_realistic_v13",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Fall17_17Nov2017_V6_MC",
                jerfile="data/jer/Fall17_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "2017ReReco31Mar":
            self.set_vars(
                globaltag="94X_dataRun2_v6",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile="data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt",
                jecfile="data/jec/Fall17_17Nov2017BCDEF_V6_DATA",
                residual=True,
                era="Run2_2017",
                localera="TM2017",
            )
        else: # if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

    def set_vars(self, globaltag, era, localera, tagname, hlttagname="", geninfo=False, fastsim=False, signal=False, pmssm=False, jsonfile="", jecfile="", residual=False, jerfile="", pufile=""):
        self.globaltag  = globaltag
        self.tagname    = tagname
        self.hlttagname = hlttagname
        self.geninfo    = geninfo
        self.fastsim    = fastsim
        self.signal     = signal
        self.pmssm      = pmssm
        self.jsonfile   = jsonfile
        self.jecfile    = jecfile
        self.residual   = residual
        self.jerfile    = jerfile
        self.pufile     = pufile
        self.era        = era
        self.localera   = localera
