import os, subprocess

def makeTest(scenario, name, numevents, command, dataset="", inputFilesConfig="", nstart=0, nfiles=0):
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
#mytests.append(makeTest("Summer16MiniAODv3",name,numevents,command,inputFilesConfig="",nstart=0,nfiles=1))
#mytests.append(makeTest("Summer16MiniAODv3",name,numevents,command,inputFilesConfig="",nstart=0,nfiles=1))
#mytests.append(makeTest("Summer16MiniAODv3sig",name,numevents,command,inputFilesConfig="",nstart=0,nfiles=1))
mytests.append(makeTest("2016MiniAODv3",name,numevents,command,inputFilesConfig="Run2016G-17Jul2018-v1.MET",nstart=0,nfiles=10))
mytests.append(makeTest("Fall17","Fall17.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8" if len(name)==0 else name,numevents,command,dataset="/store/mc/RunIIFall17MiniAODv2/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/CEB1CF27-F670-E811-BB3F-FA163E528207.root"))
mytests.append(makeTest("2017ReReco31Mar",name,numevents,command,inputFilesConfig="Run2017B-31Mar2018-v1.MET",nstart=0,nfiles=10))
mytests.append(makeTest("Summer16","GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0010CF3F-1EB7-E611-A46F-00266CFFA678.root"))
mytests.append(makeTest("Summer16","TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0044D655-9DBE-E611-A9D1-008CFA56D764.root"))
mytests.append(makeTest("Summer16sig","SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISummer16MiniAODv2/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0818BABF-64BE-E611-B201-008CFA000280.root"))
mytests.append(makeTest("Spring16Fastsig","SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",numevents,command,dataset="/store/mc/RunIISpring16MiniAODv2/SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/00000/004A27F0-5132-E611-A936-02163E016171.root"))
mytests.append(makeTest("Spring16Pmssm","pMSSM_MCMC1_mH-120to130_batch1_TuneCUETP8M1_13TeV-pythia8",numevents,command,dataset="/store/mc/RunIISpring16MiniAODv2/pMSSM_MCMC1_mH-120to130_batch1_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/pLHE_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/60000/008EDC58-EDA2-E611-9608-FA163E1F94C5.root"))
mytests.append(makeTest("2018B26Sep",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018-v1.JetHT",nstart=0,nfiles=10))
mytests.append(makeTest("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEM-v1.JetHT",nstart=0,nfiles=10))
mytests.append(makeTest("2018B26SepHEM",name,numevents,command,inputFilesConfig="Run2018B-26Sep2018_HEMmitigation-v1.JetHT",nstart=0,nfiles=10))


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
