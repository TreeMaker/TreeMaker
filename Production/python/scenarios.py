class Scenario:
    def __init__(self,sname):
        self.known = True
        ### CURRENT
        if sname == "Spring16":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,False,"","data/jec/Spring16_25nsV1_MC",False,"data/jer/Fall15_25nsV2_MC","Run2_25ns")
        elif sname == "Spring16sig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,True,"","data/jec/Spring16_25nsV1_MC",False,"data/jer/Fall15_25nsV2_MC","Run2_25ns")
        elif sname == "2016B":
            self.set_vars("80X_dataRun2_Prompt_v8","RECO",False,False,False,"data/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt","",False,"","Run2_25ns") # no JECs yet
        elif sname == "Spring15v2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,False,"","data/jec/Summer15_25nsV6_MC",False,"","Run2_25ns")
        elif sname == "Spring15v2sig":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,True,"","data/jec/Summer15_25nsV6_MC",False,"","Run2_25ns")
        elif sname == "Spring15Fastv2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,True,False,"","data/jec/MCRUN2_74_V9",False,"","Run2_25ns")
        elif sname == "Spring15Fastv2sig":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,True,True,"","data/jec/MCRUN2_74_V9",False,"","Run2_25ns")
        elif sname == "re2015C":
            self.set_vars("74X_dataRun2_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","Run2_25ns")
        elif sname == "re2015D":
            self.set_vars("74X_dataRun2_reMiniAOD_v0","PAT",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","Run2_25ns")
        elif sname == "2015Db":
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt","data/jec/Summer15_25nsV6_DATA",True,"","Run2_25ns")
        else: #if no recognized scenario, set defaults
            self.known = False
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"","",False,"","Run2_25ns")

    def set_vars(self, globaltag, tagname, geninfo, fastsim, signal, jsonfile, jecfile, residual, jerfile, era):
        self.globaltag  = globaltag
        self.tagname    = tagname
        self.geninfo    = geninfo
        self.fastsim    = fastsim
        self.signal     = signal
        self.jsonfile   = jsonfile
        self.jecfile    = jecfile
        self.residual   = residual
        self.jerfile    = jerfile
        self.era        = era
