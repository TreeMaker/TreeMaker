class Scenario:
    def __init__(self,sname):
        ### CURRENT
        if sname == "2017BC":
            self.set_vars(globaltag="92X_dataRun2_Prompt_v8",
                          tagname="RECO",
                          jsonfile="data/Cert_294927-299649_13TeV_PromptReco_Collisions17_JSON.txt",
                          jecfile="",
                          residual=True,
                          era="Run2_2017")
        else: #if no recognized scenario, cannot go forward
            raise ValueError('Unknown scenario name: '+sname)

    def set_vars(self, globaltag, era, tagname, filtname="", geninfo=False, fastsim=False, signal=False, pmssm=False, jsonfile="", jecfile="", residual=False, jerfile="", pufile=""):
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
