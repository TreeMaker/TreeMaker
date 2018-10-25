import FWCore.ParameterSet.Config as cms

# import functions to be assigned as class methods
from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
from TreeMaker.TreeMaker.JetDepot import JetVariations
from TreeMaker.TreeMaker.makeJetVars import makeJetVars, makeGoodJets, makeJetVarsAK8
from TreeMaker.TreeMaker.doHadTauBkg import doHadTauBkg, makeJetVarsHadTau
from TreeMaker.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg, reclusterZinv

class maker:
    def __init__(self,parameters):
        self.parameters = parameters
    
        # auto configuration for different scenarios
        self.scenarioName=self.parameters.value("scenario","")
        from TreeMaker.Production.scenarios import Scenario
        self.scenario = Scenario(self.scenarioName)

        # to keep track of MET fix, currently applied to all 2017 data and MC
        self.doMETfix = ("Fall17" in self.scenarioName or "2017" in self.scenarioName)
        
        self.getParamDefault("verbose",True)
        self.getParamDefault("inputFilesConfig","")
        self.getParamDefault("dataset",[])
        self.getParamDefault("nstart",0)
        self.getParamDefault("nfiles",-1)
        self.getParamDefault("numevents",-1)
        self.getParamDefault("outfile","test_run")
        # get base sample name, assuming format is name or name_#
        outfilesplit = self.outfile.split('_')
        if outfilesplit[-1].isdigit(): outfilesplit = outfilesplit[:-1]
        self.sample = '_'.join(outfilesplit)
        outfilesuff=self.parameters.value("outfilesuff","_RA2AnalysisTree")
        self.outfile += outfilesuff
        self.getParamDefault("treename","PreSelection")
        
        # background estimations on by default
        self.getParamDefault("lostlepton", True)
        self.getParamDefault("hadtau", False)
        self.getParamDefault("hadtaurecluster", 0)
        self.getParamDefault("doZinv", True)

        # special signal stuff
        self.getParamDefault("systematics",True);
        self.getParamDefault("semivisible",True);
        self.getParamDefault("deepAK8",True);
        
        # compute the PDF weights
        self.getParamDefault("doPDFs", True);
        
        # other options off by default
        self.getParamDefault("debugtracks", False)
        self.getParamDefault("applybaseline", False)
        
        # take command line input (w/ defaults from scenario if specified)
        self.getParamDefault("globaltag",self.scenario.globaltag)
        self.getParamDefault("tagname",self.scenario.tagname)
        self.getParamDefault("hlttagname",self.scenario.hlttagname)
        self.getParamDefault("geninfo",self.scenario.geninfo)
        self.getParamDefault("pmssm",self.scenario.pmssm)
        self.getParamDefault("fastsim",self.scenario.fastsim)
        self.getParamDefault("signal",self.scenario.signal)
        self.getParamDefault("jsonfile",self.scenario.jsonfile)
        self.getParamDefault("jecfile",self.scenario.jecfile)
        self.getParamDefault("residual",self.scenario.residual)
        self.getParamDefault("jerfile",self.scenario.jerfile)
        self.getParamDefault("pufile",self.scenario.pufile)
        self.getParamDefault("wrongpufile",self.scenario.wrongpufile)
        self.getParamDefault("era",self.scenario.era)
        self.getParamDefault("localera",self.scenario.localera)
        
        # temporary redirector fix
        # fastsim signal is phedexed to LPC Tier3
        self.getParamDefault("redir", "root://cmseos.fnal.gov/" if self.fastsim and self.signal else "root://cmsxrootd.fnal.gov/")
        # handle site name usage
        if self.redir[0]=="T":
            self.redir = "root://cmsxrootd.fnal.gov//store/test/xrootd/"+self.redir
        
        # Load input files
        self.readFiles = cms.untracked.vstring()

        if self.inputFilesConfig!="" :
            readFilesImport = getattr(__import__("TreeMaker.Production."+self.inputFilesConfig+"_cff",fromlist=["readFiles"]),"readFiles")
            if self.nfiles==-1:
                self.readFiles.extend( readFilesImport )
            else:
                self.readFiles.extend( readFilesImport[self.nstart:(self.nstart+self.nfiles)] )

        if self.dataset!=[] :    
            self.readFiles.extend( [self.dataset] )

        self.readFiles = [(self.redir if val[0:6]=="/store" else "")+val for val in self.readFiles]
        
        # branches for treemaker
        self.VectorRecoCand             = cms.vstring()
        self.VarsDouble                 = cms.vstring()
        self.VarsInt                    = cms.vstring()
        self.VarsBool                   = cms.vstring()
        self.VectorTLorentzVector       = cms.vstring()
        self.VectorDouble               = cms.vstring()
        self.VectorString               = cms.vstring()
        self.VectorInt                  = cms.vstring()
        self.VectorBool                 = cms.vstring()
        self.VectorVectorBool           = cms.vstring()
        self.VectorVectorInt            = cms.vstring()
        self.VectorVectorDouble         = cms.vstring()
        self.VectorVectorString         = cms.vstring()
        self.VectorVectorTLorentzVector = cms.vstring()

    def getParamDefault(self,param,default):
        setattr(self,param,self.parameters.value(param,default))
        
    def printSetup(self):
        print " readFiles: "+str(self.readFiles)
        print " outfile: "+self.outfile
        print " treename: "+self.treename
        print " "
        print " storing lostlepton variables: "+str(self.lostlepton)
        print " storing hadtau variables: "+str(self.hadtau)+" w/ reclustering "+str(self.hadtaurecluster)
        print " storing Zinv variables: "+str(self.doZinv)
        print " storing semi-visible jet variables: "+str(self.semivisible)
        print " storing deepAK8 variables: "+str(self.deepAK8)
        print " "
        print " storing JEC/JER systematics: "+str(self.systematics)
        print " storing PDF weights: "+str(self.doPDFs)
        print " "
        print " storing track debugging variables: "+str(self.debugtracks)
        print " Applying baseline selection filter: "+str(self.applybaseline)
        print " "
        print " scenario: "+self.scenarioName
        print " global tag: "+self.globaltag
        print " Instance name of tag information: "+self.tagname
        print " Instance name of HLT tag information: "+self.hlttagname
        print " Including gen-level information: "+str(self.geninfo)
        print " Including pMSSM-related information: "+str(self.pmssm)
        print " Using fastsim settings: "+str(self.fastsim)
        print " Running signal uncertainties: "+str(self.signal)
        if len(self.jsonfile)>0: print " JSON file applied: "+self.jsonfile
        if len(self.jecfile)>0: print " JECs applied: "+self.jecfile+(" (residuals)" if self.residual else "")
        if len(self.jerfile)>0: print " JERs applied: "+self.jerfile
        if len(self.pufile)>0: print " PU weights stored: "+self.pufile
        print " era of this dataset: "+self.era
        print " local era of this dataset: "+self.localera

    # assign class methods from functions
    makeTreeFromMiniAOD = makeTreeFromMiniAOD
    JetVariations = JetVariations
    makeGoodJets = makeGoodJets
    makeJetVars = makeJetVars
    makeJetVarsAK8 = makeJetVarsAK8
    doHadTauBkg = doHadTauBkg
    makeJetVarsHadTau = makeJetVarsHadTau
    doLostLeptonBkg = doLostLeptonBkg
    doZinvBkg = doZinvBkg
    reclusterZinv = reclusterZinv
