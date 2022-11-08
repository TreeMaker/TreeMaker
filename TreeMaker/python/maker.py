import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.pfnInPath import pfnInPath
import os
import subprocess

# import functions to be assigned as class methods
from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD, transformJetSeq
from TreeMaker.TreeMaker.JetDepot import JetVariations
from TreeMaker.TreeMaker.makeJetVars import makeJetVars, makeGoodJets, makeJetVarsAK8, makeMHTVars
from TreeMaker.TreeMaker.doHadTauBkg import doHadTauBkg, makeJetVarsHadTau
from TreeMaker.TreeMaker.doPhotons import doPhotonVars
from TreeMaker.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg, reclusterZinv

class maker:
    def __init__(self,parameters):
        self.parameters = parameters

        # auto configuration for different scenarios
        self.scenarioName=self.parameters.value("scenario","")
        from TreeMaker.Production.scenarios import Scenario
        self.scenario = Scenario(self.scenarioName)

        self.getParamDefault("verbose",True,bool)
        self.getParamDefault("inputFilesConfig","")
        self.getParamDefault("dataset",[])
        self.getParamDefault("nstart",0)
        self.getParamDefault("nfiles",-1)
        self.getParamDefault("local","")
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
        self.getParamDefault("lostlepton", True, bool)
        self.getParamDefault("hadtau", False, bool)
        self.getParamDefault("hadtaurecluster", 0)
        self.getParamDefault("doZinv", False, bool)

        # special signal stuff
        self.getParamDefault("systematics",True, bool);
        self.getParamDefault("semivisible",True, bool);
        self.getParamDefault("boostedsemivisible",False, bool);
        self.getParamDefault("emerging",False, bool);
        self.getParamDefault("doPhotons",True, bool);
        self.getParamDefault("tchannel",False, bool);
        self.getParamDefault("deepAK8",True, bool);
        self.getParamDefault("deepDoubleB",True, bool);
        self.getParamDefault("doQG",True);
        self.getParamDefault("addPileupId",True, bool);

        # compute the PDF weights
        self.getParamDefault("doPDFs", True, bool);

        # other options off by default
        self.getParamDefault("debugtracks", False, bool)
        self.getParamDefault("debugtap", False, bool)
        self.getParamDefault("debugsubjets", False, bool)
        self.getParamDefault("applybaseline", False, bool)
        self.getParamDefault("saveMinimalGenParticles", True, bool)
        self.getParamDefault("saveGenTops", False, bool)
        self.getParamDefault("doMT2",False, bool)
        self.getParamDefault("nestedVectors", False, bool)
        self.getParamDefault("storeOffsets", False, bool)
        self.getParamDefault("splitLevel", 99)
        self.getParamDefault("saveFloat", True, bool)
        self.getParamDefault("jetsconstituents", 0)
        self.JetsTags = []
        self.JetsNames = []

        # branch control options
        self.getParamDefault("includeBranches", "")
        self.getParamDefault("excludeBranches", "")
        self.getParamDefault("exactBranches", False, bool)
        if len(self.includeBranches)>0 and len(self.excludeBranches)>0:
            raise ValueError("includeBranches and excludeBranches are exclusive options; pick one!")
        for branchListName in ["includeBranches","excludeBranches"]:
            branches = getattr(self,branchListName)
            if not isinstance(branches,list) and branches.endswith(".txt"):
                # get full path ala FileInPath
                branchesFilePath = os.path.realpath(pfnInPath(branches).split(':')[-1])
                with open(branchesFilePath,'r') as bfile:
                    branches = [line.rstrip() for line in bfile.readlines()]
                    setattr(self,branchListName,branches)

        # take command line input (w/ defaults from scenario if specified)
        self.getParamDefault("globaltag",self.scenario.globaltag)
        self.getParamDefault("tagname",self.scenario.tagname)
        self.getParamDefault("hlttagname",self.scenario.hlttagname)
        self.getParamDefault("geninfo",self.scenario.geninfo)
        self.getParamDefault("fastsim",self.scenario.fastsim)
        self.getParamDefault("signal",self.scenario.signal)
        self.getParamDefault("scan",self.scenario.scan)
        self.getParamDefault("jsonfile",self.scenario.jsonfile)
        self.getParamDefault("jecfile",self.scenario.jecfile)
        self.getParamDefault("residual",self.scenario.residual)
        self.getParamDefault("jerfile",self.scenario.jerfile)
        self.getParamDefault("pufile",self.scenario.pufile)
        self.getParamDefault("era",self.scenario.era)
        self.getParamDefault("localera",self.scenario.localera)

        # temporary redirector fix
        self.getParamDefault("redir", "root://cmsxrootd.fnal.gov/")
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


        if len(self.local)>0:
            for iFile,readFile in enumerate(self.readFiles):
                if readFile.startswith("/"):
                    readFileLocal = readFile.replace('/','_')[1:]
                    xrdcp_command = "{} {}{} {}".format(self.local, self.redir, readFile, readFileLocal)
                    proc = subprocess.Popen(xrdcp_command.split()) #, shell = False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    outs, errs = proc.communicate()
                    self.readFiles[iFile] = "file:{}".format(readFileLocal)

        self.readFiles = [(self.redir if val.startswith("/") else "")+val for val in self.readFiles]

        # https://htcondor.readthedocs.io/en/latest/man-pages/condor_chirp.html?highlight=set_job_attr_delayed#chirp-commands
        # https://github.com/cms-sw/cmssw/blob/master/FWCore/Services/plugins/CondorStatusUpdater.cc#L377-L410
        chirp_env = "_CONDOR_CHIRP_CONFIG"
        if chirp_env in os.environ and os.environ[chirp_env]:
            key = "ChirpTreeMakerReadFiles"
            value = "\"" + ",".join(self.readFiles) + "\""
            try:
                chirp_command = "condor_chirp set_job_attr_delayed " + key + " " + value
                if self.verbose:
                    print chirp_command
                proc = subprocess.Popen(chirp_command.split(), shell = False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                outs, errs = proc.communicate()
            except Exception as e:
                proc.kill()
                print "An exception occurred when adding classad {}: {}".format(key,e)
            finally:
                if proc.returncode:
                    # TODO: Right now this is fairly permissive. We may want to make this an exception in the future.
                    print "WARNING::condor_chirp failed to set the attribute \'" + key + "\'" 
                else:
                    if self.verbose:
                        print "HTCondor classad \'" + key + "\' set to " + value

        # branches for treemaker
        self.TitleMap = cms.vstring()
        self.branchLists = [
            'VarsXYZVector','VarsXYZPoint','VarsDouble','VarsInt','VarsBool',
            'VectorRecoCand','VectorLorentzVector','VectorXYZVector','VectorXYZPoint','VectorFloat','VectorDouble','VectorString','VectorInt','VectorBool',
            'VectorVectorBool','VectorVectorInt','VectorVectorDouble','VectorVectorString','VectorVectorLorentzVector','VectorVectorXYZVector','VectorVectorXYZPoint',
            'AssocVectorVectorBool','AssocVectorVectorInt','AssocVectorVectorDouble','AssocVectorVectorString','AssocVectorVectorLorentzVector','AssocVectorVectorXYZVector','AssocVectorVectorXYZPoint',
        ]
        for branchList in self.branchLists:
            setattr(self,branchList,cms.vstring())

    def getParamDefault(self,param,default,ptype=None):
        tmp = self.parameters.value(param,default)
        if ptype is not None: tmp = ptype(tmp)
        setattr(self,param,tmp)

    def printSetup(self):
        print " readFiles: "+str(self.readFiles)
        print " outfile: "+self.outfile
        print " treename: "+self.treename
        print " "
        print " storing lostlepton variables: "+str(self.lostlepton)
        print " storing hadtau variables: "+str(self.hadtau)+" w/ reclustering "+str(self.hadtaurecluster)
        print " storing Zinv variables: "+str(self.doZinv)
        print " storing semi-visible jet variables: "+str(self.semivisible)
        print " storing also boostedsemivisible variables: "+str(self.boostedsemivisible)
        print " storing emerging jet variables: "+str(self.emerging)
        print " storing photon variables: "+str(self.doPhotons)
        print " storing t-channel semi-visible jet variables: "+str(self.tchannel)
        print " storing deepAK8 variables: "+str(self.deepAK8)
        print " storing deepDoubleB variables: "+str(self.deepDoubleB)
        print " storing quark/gluon variables: "+str(self.doQG)
        print " adding PileupJetId for AK4 : "+str(self.addPileupId)
        print " "
        print " storing JEC/JER systematics: "+str(self.systematics)
        print " storing PDF weights: "+str(self.doPDFs)
        print " "
        print " storing track debugging variables: "+str(self.debugtracks)
        print " storing TAP collection debugging variables: "+str(self.debugtap)
        print " storing subjet debugging variables: "+str(self.debugsubjets)
        print " Applying baseline selection filter: "+str(self.applybaseline)
        print " Storing a minimal set of GenParticles: "+str(self.saveMinimalGenParticles)
        print " Storing the GenTops: "+str(self.saveGenTops)
        print " Saving the MT2 variable: "+str(self.doMT2)
        print " Saving jets' constituents: "+str(self.jetsconstituents)
        if self.nestedVectors:
            print " Saving nested vectors as vector<vector<T>>"
            if self.storeOffsets:
                print " Saving counts (not offsets) for nested vectors"
        else: print " Saving nested vectors as vector<T> + vector<int>"
        print " TTree split level: "+str(self.splitLevel)
        if self.saveFloat: print " Converting doubles to floats in output"
        print " "
        print " scenario: "+self.scenarioName
        print " global tag: "+self.globaltag
        print " Instance name of tag information: "+self.tagname
        print " Instance name of HLT tag information: "+self.hlttagname
        print " Including gen-level information: "+str(self.geninfo)
        print " Using fastsim settings: "+str(self.fastsim)
        print " Using scan settings: "+str(self.scan)
        print " Running signal uncertainties: "+str(self.signal)
        if len(self.includeBranches)>0: print " Including branches: "+','.join(self.includeBranches)
        if len(self.excludeBranches)>0: print " Excluding branches: "+','.join(self.excludeBranches)
        if self.exactBranches: print "  Using exact branches (no regex)"
        if len(self.jsonfile)>0: print " JSON file applied: "+self.jsonfile
        if len(self.jecfile)>0: print " JECs applied: "+self.jecfile+(" (residuals)" if self.residual else "")
        if len(self.jerfile)>0: print " JERs applied: "+self.jerfile
        if len(self.pufile)>0: print " PU weights stored: "+self.pufile
        print " era of this dataset: "+self.era
        print " local era of this dataset: "+self.localera

    # assign class methods from functions
    makeTreeFromMiniAOD = makeTreeFromMiniAOD
    transformJetSeq = transformJetSeq
    JetVariations = JetVariations
    makeGoodJets = makeGoodJets
    makeJetVars = makeJetVars
    makeJetVarsAK8 = makeJetVarsAK8
    makeMHTVars = makeMHTVars
    doHadTauBkg = doHadTauBkg
    makeJetVarsHadTau = makeJetVarsHadTau
    doLostLeptonBkg = doLostLeptonBkg
    doZinvBkg = doZinvBkg
    doPhotonVars = doPhotonVars
    reclusterZinv = reclusterZinv
