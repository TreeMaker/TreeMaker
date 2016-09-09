class Scenario:
    def __init__(self,sname):
        ### CURRENT
        if sname == "Spring16":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,False,"","data/jec/Spring16_25nsV6_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "Spring16sig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,False,True,"","data/jec/Spring16_25nsV6_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "Spring16Fastsig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,True,True,"","data/jec/Spring16_25nsFastSimMC_V1",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "2016B":
            self.set_vars("80X_dataRun2_Prompt_v8","RECO",False,False,False,"data/Cert_271036-279931_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "2016CD":
            self.set_vars("80X_dataRun2_Prompt_v9","RECO",False,False,False,"data/Cert_271036-279931_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "2016EF":
            self.set_vars("80X_dataRun2_Prompt_v10","RECO",False,False,False,"data/Cert_271036-279931_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        elif sname == "2016G":
            self.set_vars("80X_dataRun2_Prompt_v11","RECO",False,False,False,"data/Cert_271036-279931_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt","data/jec/Spring16_25nsV6_DATA",True,"","","Run2_25ns")
        else: #if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

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
