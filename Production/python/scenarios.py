class Scenario:
    def __init__(self,sname):
        ### CURRENT
        if sname == "Spring16Fastsig":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,True,True,False,"","data/jec/Spring16_25nsFastSimMC_V1",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "Spring16Pmssm":
            self.set_vars("80X_mcRun2_asymptotic_2016_miniAODv2","PAT",True,True,True,True,"","data/jec/Spring16_25nsFastSimMC_V1",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")            
        elif sname == "Summer16":
            self.set_vars("80X_mcRun2_asymptotic_2016_TrancheIV_v6","PAT",True,False,False,False,"","data/jec/Summer16_23Sep2016V3_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "Summer16sig":
            self.set_vars("80X_mcRun2_asymptotic_2016_TrancheIV_v6","PAT",True,False,True,False,"","data/jec/Summer16_23Sep2016V3_MC",False,"data/jer/Spring16_25nsV6_MC","TreeMaker/Production/test/data/PileupHistograms_0721_63mb_pm5.root","Run2_25ns")
        elif sname == "2016H":
            self.set_vars("80X_dataRun2_Prompt_v14","RECO",False,False,False,False,"data/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt","data/jec/Summer16_23Sep2016AllV3_DATA",False,"","","Run2_25ns")
        elif sname == "2016ReReco23Sep":
            self.set_vars("80X_dataRun2_2016SeptRepro_v3","RECO",False,False,False,False,"data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt","data/jec/Summer16_23Sep2016AllV3_DATA",False,"","","Run2_25ns")
        else: #if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

    def set_vars(self, globaltag, tagname, geninfo, fastsim, signal, pmssm, jsonfile, jecfile, residual, jerfile, pufile, era):
        self.globaltag  = globaltag
        self.tagname    = tagname
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
