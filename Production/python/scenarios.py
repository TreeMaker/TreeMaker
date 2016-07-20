class Scenario:
    def __init__(self,sname):
        self.known = True
        ### CURRENT
        if sname == "Spring16":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,False,"","data/jec/Spring16_25nsV6_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0704.root","Run2_25ns")
        elif sname == "Spring16sig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,True,"","data/jec/Spring16_25nsV6_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0704.root","Run2_25ns")
        elif sname == "Spring16Fastsig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,True,True,"","data/jec/Spring16_25nsFastSimMC_V1",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0704.root","Run2_25ns")
        elif sname == "2016B":
            self.set_vars("80X_dataRun2_Prompt_v8","RECO",False,False,False,"data/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "2016CD":
            self.set_vars("80X_dataRun2_Prompt_v9","RECO",False,False,False,"data/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "Spring15v2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,False,"","data/jec/Summer15_25nsV6_MC",False,"","TreeMaker/Production/test/data/PileupHistograms_1117.root","Run2_25ns")
        elif sname == "Spring15v2sig":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,True,"","data/jec/Summer15_25nsV6_MC",False,"","TreeMaker/Production/test/data/PileupHistograms_1117.root","Run2_25ns")
        elif sname == "Spring15Fastv2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,True,False,"","data/jec/MCRUN2_74_V9",False,"","TreeMaker/Production/test/data/PileupHistograms_1117.root","Run2_25ns")
        elif sname == "Spring15Fastv2sig":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,True,True,"","data/jec/MCRUN2_74_V9",False,"","TreeMaker/Production/test/data/PileupHistograms_1117.root","Run2_25ns")
        elif sname == "re2015C":
            self.set_vars("74X_dataRun2_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "re2015D":
            self.set_vars("74X_dataRun2_reMiniAOD_v0","PAT",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "2015Db":
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","","Run2_25ns")
        else: #if no recognized scenario, set defaults
            self.known = False
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"","",False,"","","Run2_25ns")

    def set_vars(self, globaltag, tagname, geninfo, fastsim, signal, jsonfile, jecfile, residual, jerfile, pufile, era):
        self.globaltag  = globaltag
        self.tagname    = tagname
        self.geninfo    = geninfo
        self.fastsim    = fastsim
        self.signal     = signal
        self.jsonfile   = jsonfile
        self.jecfile    = jecfile
        self.residual   = residual
        self.jerfile    = jerfile
        self.pufile     = pufile
        self.era        = era
