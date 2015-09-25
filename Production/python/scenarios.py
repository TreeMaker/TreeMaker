class Scenario:
    def __init__(self,sname):
        self.known = True
        if sname == "Phys14":
            self.set_vars("PHYS14_25_V2","PAT",True,False,"","",False,"Run2_25ns")
        elif sname == "Spring15":
            self.set_vars("MCRUN2_74_V9","PAT",True,False,"","data/Summer15_25nsV2_MC",False,"Run2_25ns")
        elif sname == "Spring15Fast":
            self.set_vars("MCRUN2_74_V9","PAT",True,True,"","data/Summer15_25nsV2_MC",False,"Run2_25ns")
        elif sname == "2015B":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,"data/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON.txt","data/Summer15_50nsV5_DATA",True,"Run2_50ns")
        elif sname == "re2015B":
            self.set_vars("74X_dataRun2_Prompt_v1","PAT",False,False,"data/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON.txt","data/Summer15_50nsV5_DATA",True,"Run2_50ns")
        elif sname == "2015C":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,"data/Cert_246908-256869_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV2_DATA",True,"Run2_25ns")
        elif sname == "2015D":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,"data/Cert_246908-256869_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV2_DATA",True,"Run2_25ns")
        else: #if no recognized scenario, set defaults
            self.known = False
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,"","",False,"Run2_50ns")

    def set_vars(self, globaltag, tagname, geninfo, fastsim, jsonfile, jecfile, residual, era):
        self.globaltag = globaltag
        self.tagname   = tagname
        self.geninfo   = geninfo
        self.fastsim   = fastsim
        self.jsonfile  = jsonfile
        self.jecfile   = jecfile
        self.residual  = residual
        self.era       = era
