import os, subprocess

def makeTest(scenario, name, numevents, command, dataset="", inputFilesConfig="", nstart=0, nfiles=0, redir=""):
    # handle names
    if len(name)==0 and len(inputFilesConfig)>0: name = inputFilesConfig

    mytest = []
    mytest.append("cmsRun")
    mytest.append("runMakeTreeFromMiniAOD_cfg.py")
    mytest.append("scenario="+scenario+"")
    # different methods for input files
    if len(dataset)>0:
        mytest.append("dataset="+dataset)
    else:
        mytest.append("inputFilesConfig="+inputFilesConfig)
        mytest.append("nstart="+str(nstart))
        mytest.append("nfiles="+str(nfiles))
    # different shell commands
    mytest.append("outfile="+name)
    mytest.append("numevents="+str(numevents))
    if len(command)>0: mytest.append(command)
    if len(redir)>0: mytest.append("redir="+redir)
    mytest.append(name+".log")

    return mytest

def printTest(mytest, itest):
    logname = mytest[-1]
    tmp = str(itest)+":\n  "+" \\\n  ".join(mytest[0:-1])+" \\\n "+" >& "+logname+" &"
    print tmp
    
# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
test=parameters.value("test",-1)
name=parameters.value("name","")
run=parameters.value("run",False)
numevents=parameters.value("numevents",100)
command=parameters.value("command","")

# only set name for a specific test
if test==-1: name = ""

# list of tests
mytests = []
# activate these when the requisite MC exists
mytests.append(makeTest("Summer16v3","Summer16v3.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Summer16v3","Summer16v3.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Summer16v3sig","Summer16v3.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Summer16v3sigscan","Summer16v3.SMS-T5qqqqZH-mGluino-1000to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3.SMS-T5qqqqZH-mGluino-1000to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Summer16v3Fast","Summer16v3Fast.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3Fast.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Summer16v3Fastsig","Summer16v3Fast.SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Summer16v3Fast.SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("2016ReReco17Jul",name,numevents,command,inputFilesConfig="Run2016G-17Jul2018-v1.MET",nstart=0,nfiles=10))
mytests.append(makeTest("Fall17","Fall17.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Fall17","Fall17.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Fall17sig","Fall17.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Fall17Fast","Fall17Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Fall17Fastsig","Fall17Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Fall17Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("2017ReReco31Mar",name,numevents,command,inputFilesConfig="Run2017B-31Mar2018-v1.MET",nstart=0,nfiles=10))
mytests.append(makeTest("Summer16","Summer16.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0010CF3F-1EB7-E611-A46F-00266CFFA678.root"))
mytests.append(makeTest("Summer16","Summer16.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0044D655-9DBE-E611-A9D1-008CFA56D764.root"))
mytests.append(makeTest("Summer16","Summer16.QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8_opendata",numevents,command,dataset="/eos/opendata/cms/MonteCarlo2016/RunIISummer16MiniAODv2/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0048131D-3CB3-E611-813A-001E67DFFB31.root",redir="root://eospublic.cern.ch/"))
mytests.append(makeTest("Summer16sig","SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0818BABF-64BE-E611-B201-008CFA000280.root"))
mytests.append(makeTest("Autumn18","Autumn18.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1",numevents,command,inputFilesConfig="Autumn18.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1",nstart=0,nfiles=10))
mytests.append(makeTest("Autumn18Fast","Autumn18Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Autumn18Fast.TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("Autumn18Fastsig","Autumn18Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",numevents,command,inputFilesConfig="Autumn18Fast.SMS-T1tttt_TuneCP2_13TeV-madgraphMLM-pythia8",nstart=0,nfiles=1))
mytests.append(makeTest("2018B26Sep",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018-v1.JetHT",nstart=0,nfiles=10))
mytests.append(makeTest("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEM-v1.JetHT",nstart=0,nfiles=10))
mytests.append(makeTest("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEMmitigation-v1.JetHT",nstart=0,nfiles=10))
mytests.append(makeTest("2018PromptReco",name,numevents,command,inputFilesConfig="Run2018D-PromptReco-v2.JetHT",nstart=244,nfiles=10))
mytests.append(makeTest("2018ReReco17Sep",name,numevents,command,inputFilesConfig="Run2018B-17Sep2018-v1.JetHT",nstart=0,nfiles=10))


if test<0 or test>len(mytests):
    print "Predefined tests:"
    for itest, mytest in enumerate(mytests):
        printTest(mytest,itest)
else:
    printTest(mytests[test],test)
    if run:
        # fork the cmsRun process and exit
        fork_pid = os.fork()
        if fork_pid == 0:
            with open(mytests[test][-1],'w') as out:
                p = subprocess.Popen(mytests[test][0:-1], stdin=None, stdout=out, stderr=out, close_fds=True)
                print "\nRunning test... ["+str(p.pid)+"]"
                sts = os.waitpid(p.pid, 0)[1]
                print "\nTest is done! ["+str(p.pid)+"]"


#Example:
#  python unitTest.py numevents=1000 run=True test=0
