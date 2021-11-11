import os

class Scenario:
    reldatapath = "TreeMaker/Production/test/data/"
    absdatapath = os.environ['CMSSW_BASE']+"/src/TreeMaker/Production/test/data/"

    def __init__(self,sname):
        if sname == "Summer20UL16":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_v17",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016",
            )
        elif sname == "Summer20UL16APV":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_preVFP_v11",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16APV_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16APV_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016APV_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016APV",
            )
        elif sname == "Summer20UL16sig":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_v17",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016",
            )
        elif sname == "Summer20UL16Fast":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_v17",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016",
            )
        elif sname == "Summer20UL16Fastsig":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_v17",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016",
            )
        elif sname == "Summer20UL16APVsig":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_preVFP_v11",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16APV_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16APV_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016APV_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016APV",
            )
        elif sname == "Summer20UL16APVFast":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_preVFP_v11",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16APV_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16APV_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016APV_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016APV",
            )
        elif sname == "Summer20UL16APVFastsig":
            self.set_vars(
                globaltag="106X_mcRun2_asymptotic_preVFP_v11",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL16APV_V7_MC",
                jerfile=self.absdatapath+"/jer/Summer20UL16APV_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2016APV_69mb_pm5.root",
                era="Run2_2016",
                localera="TMUL2016APV",
            )
        elif sname == "Summer20UL16_DATA":
            self.set_vars(
                globaltag="106X_dataRun2_v33",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile=self.absdatapath+"/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                jecfile=self.absdatapath+"/jec/Summer19UL16_RunBCDEFGH_Combined_V7_DATA",
                residual=True,
                era="Run2_2016",
                localera="TMUL2016",
            )
        elif sname == "Summer20UL17":
            self.set_vars(
                globaltag="106X_mc2017_realistic_v8",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile=self.absdatapath+"/jec/Summer19UL17_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL17_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2017_69mb_pm5.root",
                era="Run2_2017",
                localera="TMUL2017",
            )
        elif sname == "Summer20UL17sig":
            self.set_vars(
                globaltag="106X_mc2017_realistic_v8",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile=self.absdatapath+"/jec/Summer19UL17_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL17_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2017_69mb_pm5.root",
                era="Run2_2017",
                localera="TMUL2017",
            )
        elif sname == "Summer20UL17Fast":
            self.set_vars(
                globaltag="106X_mc2017_realistic_v8",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL17_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL17_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2017_69mb_pm5.root",
                era="Run2_2017",
                localera="TMUL2017",
            )
        elif sname == "Summer20UL17Fastsig":
            self.set_vars(
                globaltag="106X_mc2017_realistic_v8",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL17_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL17_JRV3_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2017_69mb_pm5.root",
                era="Run2_2017",
                localera="TMUL2017",
            )
        elif sname == "Summer20UL17_DATA":
            self.set_vars(
                globaltag="106X_dataRun2_v33",
                tagname="PAT",
                hlttagname="HLT",
                jsonfile=self.absdatapath+"/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                jecfile=self.absdatapath+"/jec/Summer19UL17_RunBCDEF_V5_DATA",
                residual=True,
                era="Run2_2017",
                localera="TMUL2017",
            )
        elif sname == "Summer20UL18":
            self.set_vars(
                globaltag="106X_upgrade2018_realistic_v15_L1v1",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                jecfile=self.absdatapath+"/jec/Summer19UL18_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL18_JRV2_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2018_69mb_pm5.root",
                era="Run2_2018",
                localera="TMUL2018",
            )
        elif sname == "Summer20UL18sig":
            self.set_vars(
                globaltag="106X_upgrade2018_realistic_v15_L1v1",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                jecfile=self.absdatapath+"/jec/Summer19UL18_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL18_JRV2_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2018_69mb_pm5.root",
                era="Run2_2018",
                localera="TMUL2018",
            )
        elif sname == "Summer20UL18Fast":
            self.set_vars(
                globaltag="106X_upgrade2018_realistic_v15_L1v1",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL18_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL18_JRV2_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2018_69mb_pm5.root",
                era="Run2_2018",
                localera="TMUL2018",
            )
        elif sname == "Summer20UL18Fastsig":
            self.set_vars(
                globaltag="106X_upgrade2018_realistic_v15_L1v1",
                tagname="PAT",
                hlttagname="HLT",
                geninfo=True,
                signal=True,
                fastsim=True,
                jecfile=self.absdatapath+"/jec/Summer19UL18_V5_MC",
                jerfile=self.absdatapath+"/jer/Summer19UL18_JRV2_MC",
                pufile=self.reldatapath+"/PileupHistograms_UL2018_69mb_pm5.root",
                era="Run2_2018",
                localera="TMUL2018",
            )
        elif sname == "Summer20UL18_DATA":
            self.set_vars(
                globaltag="106X_dataRun2_v33",
                tagname="RECO",
                hlttagname="HLT",
                jsonfile=self.absdatapath+"/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                jecfile=self.absdatapath+"/jec/Summer19UL18_V5_DATA", 
                residual=True,
                era="Run2_2018",
                localera="TMUL2018",
            )
        else: # if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

    def set_vars(self, globaltag, era, localera, tagname, hlttagname="", geninfo=False, fastsim=False, signal=False, pmssm=False, scan=False, jsonfile="", jecfile="", residual=False, jerfile="", pufile=""):
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
        self.era        = era
        self.localera   = localera
