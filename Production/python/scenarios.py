class Scenario:
    def __init__(self,sname):
        if sname == "Summer16MiniAODv3":
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
        elif sname == "Summer16MiniAODv3sig":
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
        elif sname == "2016MiniAODv3":
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

    def set_vars(self, globaltag, era, localera, tagname, hlttagname="", geninfo=False, fastsim=False, signal=False, pmssm=False, jsonfile="", jecfile="", residual=False, jerfile="", pufile="", pudir=""):
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
        self.pudir      = pudir
        self.era        = era
        self.localera   = localera
