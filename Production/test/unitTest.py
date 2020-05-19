import os, subprocess, re, sys

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
        if log: out.close()
        print "\nTest is done!"
        if clean: self.cleanFiles(clean)

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
    mytests.append(Test("Summer16v3","Summer16v3.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer16v3","Summer16v3.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer16v3sig","Summer16v3.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer16v3sigscan","Summer16v3.SMS-T5qqqqZH-mGluino-1000to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.SMS-T5qqqqZH-mGluino-1000to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer16v3Fast","Summer16v3Fast.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3Fast.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Summer16v3Fastsig","Summer16v3Fast.SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3Fast.SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("2016ReReco17Jul",name,numevents,command,inputFilesConfig="Run2016G-17Jul2018-v1.MET",nstart=0,nfiles=10))
    mytests.append(Test("Fall17","Fall17.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Fall17","Fall17.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Fall17sig","Fall17.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Fall17Fast","Fall17Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Fall17Fastsig","Fall17Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("2017ReReco31Mar",name,numevents,command,inputFilesConfig="Run2017B-31Mar2018-v1.MET",nstart=0,nfiles=10))
    mytests.append(Test("Summer16","Summer16.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0010CF3F-1EB7-E611-A46F-00266CFFA678.root"))
    mytests.append(Test("Summer16","Summer16.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0044D655-9DBE-E611-A9D1-008CFA56D764.root"))
    mytests.append(Test("Summer16","Summer16.QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8_opendata",numevents,command,dataset="/eos/opendata/cms/MonteCarlo2016/RunIISummer16MiniAODv2/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0048131D-3CB3-E611-813A-001E67DFFB31.root",redir="root://eospublic.cern.ch/"))
    mytests.append(Test("Summer16sig","SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0818BABF-64BE-E611-B201-008CFA000280.root"))
    mytests.append(Test("Autumn18","Autumn18.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1",numevents,command,inputFilesConfig="Autumn18.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1",nstart=0,nfiles=10))
    mytests.append(Test("Autumn18Fast","Autumn18Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Autumn18Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("Autumn18Fastsig","Autumn18Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Autumn18Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
    mytests.append(Test("2018B26Sep",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018-v1.JetHT",nstart=0,nfiles=10))
    mytests.append(Test("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEM-v1.JetHT",nstart=0,nfiles=10))
    mytests.append(Test("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEMmitigation-v1.JetHT",nstart=0,nfiles=10))
    mytests.append(Test("2018PromptReco",name,numevents,command,inputFilesConfig="Run2018D-PromptReco-v2.JetHT",nstart=244,nfiles=10))
    mytests.append(Test("2018ReReco17Sep",name,numevents,command,inputFilesConfig="Run2018B-17Sep2018-v1.JetHT",nstart=0,nfiles=10))

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
        sys.exit(-1)

    if test<0 or test>=len(mytests):
        print "Predefined tests:"
        for itest, mytest in enumerate(mytests):
            mytest.printTest(itest,log)
    else:
        mytests[test].printTest(test,log)
        if run:
            if fork:
                mytests[test].forkAndRun(clean)
            else:
                mytests[test].run(log,clean)

if __name__ == '__main__':
    unitTest()

#Example:
#  python unitTest.py numevents=1000 run=True test=0
