class Scenario:
    def __init__(self,sname):
        if sname == "Summer16":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016_80X",
            )
        elif sname == "Summer16sig":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016_80X",
            )
        elif sname == "Summer16v3":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16v3sig":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16v3sigscan":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                scan=True,
                jecfile="data/jec/Summer16_07Aug2017_V10_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16v3Fast":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                signal=False,
                jecfile="data/jec/Summer16_FastSimV1_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "Summer16v3Fastsig":
            self.set_vars(
                globaltag="94X_mcRun2_asymptotic_v3",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                signal=True,
                jecfile="data/jec/Summer16_FastSimV1_MC",
                jerfile="data/jer/Summer16_25nsV1_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0121_69p2mb_pm4p6.root",
                era="Run2_2016",
                localera="TM2016",
            )
        elif sname == "2016ReReco17Jul":
            self.set_vars(
                globaltag="94X_dataRun2_v10",
                tagname="DQM",
                hlttagname="HLT",
                jsonfile="data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
                jecfile="data/jec/Summer16_07Aug2017All_V11_DATA",
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
                jecfile="data/jec/Fall17_17Nov2017_V32_102X_MC",
                jerfile="data/jer/Fall17_V3_94X_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                wrongpufile="TreeMaker/Production/test/data/Fall17PU.root",
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
                jecfile="data/jec/Fall17_17Nov2017_V32_102X_MC",
                jerfile="data/jer/Fall17_V3_94X_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                wrongpufile="TreeMaker/Production/test/data/Fall17PU.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "Fall17sigscan":
            self.set_vars(
                globaltag="94X_mc2017_realistic_v13",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                scan=True,
                jecfile="data/jec/Fall17_17Nov2017_V32_102X_MC",
                jerfile="data/jer/Fall17_V3_94X_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                wrongpufile="TreeMaker/Production/test/data/Fall17PU.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "Fall17Fast":
            self.set_vars(
                globaltag="94X_mc2017_realistic_v13",
                tagname="PAT",
                hlttagname="RECO",
                geninfo=True,
                fastsim=True,
                signal=False,
                jecfile="data/jec/Fall17_25nsFastSim_V1_MC",
                jerfile="data/jer/Fall17_V3_94X_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                wrongpufile="TreeMaker/Production/test/data/Fall17PU.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "Fall17Fastsig":
            self.set_vars(
                globaltag="94X_mc2017_realistic_v13",
                tagname="PAT",
                hlttagname="RECO",
                geninfo=True,
                fastsim=True,
                signal=True,
                jecfile="data/jec/Fall17_25nsFastSim_V1_MC",
                jerfile="data/jer/Fall17_V3_94X_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0328_63mb_pm5.root",
                wrongpufile="TreeMaker/Production/test/data/Fall17PU.root",
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "2017ReReco31Mar":
            self.set_vars(
                globaltag="94X_dataRun2_v6",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile="data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt",
                jecfile="data/jec/Fall17_17Nov2017_V32_102X_DATA",
                residual=True,
                era="Run2_2017",
                localera="TM2017",
            )
        elif sname == "Autumn18":
            self.set_vars(
                globaltag="102X_upgrade2018_realistic_v16",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile="data/jec/Autumn18_V8_MC",
                jerfile="data/jer/Autumn18_V7b_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0118_63mb_pm5.root",
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "Autumn18sig":
            self.set_vars(
                globaltag="102X_upgrade2018_realistic_v16",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile="data/jec/Autumn18_V8_MC",
                jerfile="data/jer/Autumn18_V7b_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0118_63mb_pm5.root",
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "Autumn18sigscan":
            self.set_vars(
                globaltag="102X_upgrade2018_realistic_v16",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                scan=True,
                jecfile="data/jec/Autumn18_V8_MC",
                jerfile="data/jer/Autumn18_V7b_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0118_63mb_pm5.root",
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "Autumn18Fast":
            self.set_vars(
                globaltag="102X_upgrade2018_realistic_v16",
                tagname="PAT",
                hlttagname="PAT",
                geninfo=True,
                fastsim=True,
                signal=False,
                jecfile="data/jec/Autumn18_FastSimV1_MC",
                jerfile="data/jer/Autumn18_V7b_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0118_63mb_pm5.root",
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "Autumn18Fastsig":
            self.set_vars(
                globaltag="102X_upgrade2018_realistic_v16",
                tagname="PAT",
                hlttagname="PAT",
                geninfo=True,
                fastsim=True,
                signal=True,
                jecfile="data/jec/Autumn18_FastSimV1_MC",
                jerfile="data/jer/Autumn18_V7b_MC",
                pufile="TreeMaker/Production/test/data/PileupHistograms_0118_63mb_pm5.root",
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "2018B26Sep":
            self.set_vars(
                globaltag="102X_dataRun2_PromptLike_v7",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt",
                jecfile="data/jec/Autumn18_RunABCD_V8_DATA",
                residual=True,
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "2018B26SepHEM":
            self.set_vars(
                globaltag="102X_dataRun2_PromptLike_HEfail_v1",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt",
                jecfile="data/jec/Autumn18_RunABCD_V8_DATA",
                residual=True,
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "2018PromptReco":
            self.set_vars(
                globaltag="102X_dataRun2_Prompt_v11",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
                jecfile="data/jec/Autumn18_RunABCD_V8_DATA",
                residual=True,
                era="Run2_2018",
                localera="TM2018",
            )
        elif sname == "2018ReReco17Sep":
            self.set_vars(
                globaltag="102X_dataRun2_Sep2018Rereco_v1",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile="data/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
                jecfile="data/jec/Autumn18_RunABCD_V8_DATA",
                residual=True,
                era="Run2_2018",
                localera="TM2018",
            )
        else: # if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

    def set_vars(self, globaltag, era, localera, tagname, hlttagname="", geninfo=False, fastsim=False, signal=False, pmssm=False, scan=False, jsonfile="", jecfile="", residual=False, jerfile="", pufile="", wrongpufile=""):
        self.globaltag  = globaltag
        self.tagname    = tagname
        self.hlttagname = hlttagname
        self.geninfo    = geninfo
        self.fastsim    = fastsim
        self.signal     = signal
        self.pmssm      = pmssm
        self.scan       = scan
        self.jsonfile   = jsonfile
        self.jecfile    = jecfile
        self.residual   = residual
        self.jerfile    = jerfile
        self.pufile     = pufile
        self.wrongpufile= wrongpufile
        self.era        = era
        self.localera   = localera
