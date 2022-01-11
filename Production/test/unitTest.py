import os
import re
import subprocess
import sys

class Test:
    def __init__(self, scenario, name, numevents, command, dataset="", inputFilesConfig="", nstart=0, nfiles=0, redir=""):
        self.scenario = scenario
        self.dataset = dataset
        self.inputFilesConfig = inputFilesConfig
        self.nstart = nstart
        self.nfiles = nfiles
        self.outfile = name
        self.numevents = numevents
        self.command = command
        self.redir = redir
        self.cmd = "cmsRun"
        self.config = os.environ['CMSSW_BASE']+"/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py"
        self.array = self.getArray()

    def getArray(self):
        mytest = []
        mytest += [self.cmd, self.config, "scenario="+self.scenario]
        # different methods for input files
        if len(self.dataset)>0:
            mytest.append("dataset="+self.dataset)
        else:
            mytest.append("inputFilesConfig="+self.inputFilesConfig)
            mytest.append("nstart="+str(self.nstart))
            mytest.append("nfiles="+str(self.nfiles))
        # different shell commands
        mytest += ["outfile="+self.outfile, "numevents="+str(self.numevents)]
        if len(self.command)>0: 
            # check is you can do some additional formatting to protect against later problems
            pattern = re.compile("((?:\S+)[=]+(?:\S+))")
            commands = pattern.findall(self.command)
            splits = self.command.split(" ")
            if len(commands)>0 and len(commands)==len(splits):
                mytest.extend(commands)
            else:
                mytest.append(self.command)
        if len(self.redir)>0: mytest.append("redir="+self.redir)
        mytest.append(self.getLogName())
        return mytest

    def getLogName(self):
        return self.outfile+".log"

    def getROOTName(self):
        return self.outfile+"_RA2AnalysisTree.root"

    def printTest(self, itest, log):
        logname = self.array[-1]
        tmp = str(itest)+":\n  "+" \\\n  ".join(self.array[0:-1])
        if log:
            tmp +=" \\\n "+" >& "+logname+" &"
        print tmp

    def forkAndRun(self, clean):
        # fork the cmsRun process and exit
        fork_pid = os.fork()
        if fork_pid == 0:
            with open(self.getLogName(),'w') as out:
                p = subprocess.Popen(self.array[0:-1], stdin=None, stdout=out, stderr=out, close_fds=True)
                print "\nRunning test... ["+str(p.pid)+"]"
                sts = os.waitpid(p.pid, 0)[1]
                print "\nTest is done! ["+str(p.pid)+"]"
                if clean: self.cleanFiles(clean)
                exitstatus_pid = "{0:b}".format(sts)
                exitstatus = int(exitstatus_pid[0:8],2)
                if exitstatus != 0:
                    raise RuntimeError("\nERROR::The Test did not complete successfully!")

    def run(self, log, clean):
        out = None
        if log: out = open(self.getLogName(),'w')
        p = subprocess.Popen(self.array[0:-1], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True, bufsize=1)
        print "\nRunning test..."
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                print line,
                if log: out.write(line)
        p.wait()
        print "\nTest is done!"
        if log: out.close()
        if clean: self.cleanFiles(clean)
        if p.returncode != 0:
            raise RuntimeError("\nERROR::The Test did not complete successfully!")

    def cleanFiles(self, clean):
        print "\nCleaning output files..."
        files=[self.getROOTName(),self.getLogName()]
        if clean>0: files=files[0:clean]
        for file in files:
            if os.path.exists(file):
                os.remove(file)
        print "\nDone cleaning files!"

def defineTests(mytests, scenario, name, numevents, command, dataset, inputFilesConfig):
    # User defined test
    # make sure this is the first test defined
    mytests.append(Test(scenario,name,numevents,command,dataset,inputFilesConfig,nstart=0,nfiles=10,redir=""))

    # pre-defined tests
    mytests.append(Test("Summer20UL16","Summer20UL16.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",numevents,command,inputFilesConfig="Summer20UL16.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16APV","Summer20UL16APV.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",numevents,command,inputFilesConfig="Summer20UL16APV.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL17","Summer20UL17.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",numevents,command,inputFilesConfig="Summer20UL17.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL18","Summer20UL18.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",numevents,command,inputFilesConfig="Summer20UL18.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16","Summer20UL16.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer20UL16.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16APV","Summer20UL16APV.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer20UL16APV.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL17","Summer20UL17.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer20UL17.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL18","Summer20UL18.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer20UL18.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16_DATA","Summer20UL16_DATA.Run2016G-UL2016-v2.JetHT",numevents,command,inputFilesConfig="Run2016G-UL2016-v2.JetHT",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16_DATA","Summer20UL16_DATA.Run2016H-UL2016-v2.JetHT",numevents,command,inputFilesConfig="Run2016H-UL2016-v2.JetHT",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16APV_DATA","Summer20UL16APV_DATA.Run2016D-UL2016_HIPM-v2.SingleElectron",numevents,command,inputFilesConfig="Run2016D-UL2016_HIPM-v2.SingleElectron",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL17_DATA","Summer20UL17_DATA.Run2017E-UL2017-v1.SingleMuon",numevents,command,inputFilesConfig="Run2017E-UL2017-v1.SingleMuon",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL18_DATA","Summer20UL18_DATA.Run2018A-UL2018-v2.MET",numevents,command,inputFilesConfig="Run2018A-UL2018-v2.MET",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL18_DATA","Summer20UL18_DATA.Run2018C-UL2018-v1.EGamma",numevents,command,inputFilesConfig="Run2018C-UL2018-v1.EGamma",nstart=0,nfiles=1))
    mytests.append(Test("Summer20UL16sig","PrivateSamples.EMJ_UL16_mMed-1000_mDark-20_kappa-0p25_aligned-down",numevents,"emerging=True doPhotons=True deepAK8=False deepDoubleB=False doZinv=False nestedVectors=False splitLevel=99"+command,inputFilesConfig="PrivateSamples.EMJ_UL16_mMed-1000_mDark-20_kappa-0p25_aligned-down",nstart=0,nfiles=10))
    mytests.append(Test("Summer20UL16sig","PrivateSamples.EMJ_UL16_mMed-1000_mDark-20_ctau-150_unflavored-down",numevents,"emerging=True doPhotons=True deepAK8=False deepDoubleB=False doZinv=False nestedVectors=False splitLevel=99"+command,inputFilesConfig="PrivateSamples.EMJ_UL16_mMed-1000_mDark-20_ctau-150_unflavored-down",nstart=0,nfiles=10))
    mytests.append(Test("Summer20UL17sig","PrivateSamples.EMJ_UL17_mMed-1000_mDark-20_kappa-0p25_aligned-down",numevents,"emerging=True doPhotons=True deepAK8=False deepDoubleB=False doZinv=False nestedVectors=False splitLevel=99"+command,inputFilesConfig="PrivateSamples.EMJ_UL17_mMed-1000_mDark-20_kappa-0p25_aligned-down",nstart=0,nfiles=10))
    mytests.append(Test("Summer20UL17sig","PrivateSamples.EMJ_UL17_mMed-1000_mDark-20_ctau-150_unflavored-down",numevents,"emerging=True doPhotons=True deepAK8=False deepDoubleB=False doZinv=False nestedVectors=False splitLevel=99"+command,inputFilesConfig="PrivateSamples.EMJ_UL17_mMed-1000_mDark-20_ctau-150_unflavored-down",nstart=0,nfiles=10))

def unitTest():
    # Read parameters
    from TreeMaker.Utils.CommandLineParams import CommandLineParams
    parameters = CommandLineParams()
    fork=parameters.value("fork",True)
    log=parameters.value("log",True)
    clean=parameters.value("clean",0)
    test=parameters.value("test",-1)
    name=parameters.value("name","")
    run=parameters.value("run",False)
    numevents=parameters.value("numevents",100)
    command=parameters.value("command","")
    scenario=parameters.value("scenario","")
    dataset=parameters.value("dataset","")
    inputFilesConfig=parameters.value("inputFilesConfig","")

    # only set name for a specific test
    if test==-1: name = ""

    # list of tests
    mytests = []
    defineTests(mytests,scenario,name,numevents,command,dataset,inputFilesConfig)

    # sanity check for defining an on-the-fly test
    if test==0 and dataset=="" and inputFilesConfig=="":
        print "If defining a unitTest on-the-fly, you must either specify a \'dataset\' or an \'inputFilesConfig\'."
        sys.exit(1)

    if test<0 or test>=len(mytests):
        print "Predefined tests:"
        for itest, mytest in enumerate(mytests):
            mytest.printTest(itest,log)
    else:
        mytests[test].printTest(test,log)
        if run:
            try:
                if fork:
                    mytests[test].forkAndRun(clean)
                else:
                    mytests[test].run(log,clean)
            except RuntimeError, e:
                print str(e)
                sys.exit(2)

if __name__ == '__main__':
    unitTest()

#Example:
#  python unitTest.py numevents=1000 run=True test=0
