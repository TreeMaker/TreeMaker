import os, subprocess

def makeTest(scenario, name, numevents, command, dataset="", inputFilesConfig="", nstart=0, nfiles=0):
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

def printTest(mytest, itest, shell):
    tmp = str(itest)+":\n  "+" \\\n  ".join(mytest[0:-1])+" \\\n "
    logname = mytest[-1]
    if shell=="tcsh":
        tmp += " >& "+logname+" &"
    elif shell=="bash" or shell=="sh":
        tmp += " > "+logname+" 2>&1 &"
    
    print tmp
    
# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
test=parameters.value("test",-1)
name=parameters.value("name","")
run=parameters.value("run",False)
numevents=parameters.value("numevents",100)
command=parameters.value("command","")
shell=parameters.value("shell","tcsh")

# only set name for a specific test
if test==-1: name = ""

# list of tests
mytests = []
mytests.append(makeTest("Spring16","gjet16" if len(name)==0 else name,numevents,command,dataset="/store/mc/RunIISpring16MiniAODv1/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/0060A792-DBFC-E511-B178-0CC47A0AD704.root"))
mytests.append(makeTest("Spring16sig","T1tttt16" if len(name)==0 else name,numevents,command,dataset="/store/mc/RunIISpring16MiniAODv1/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/26C76166-0FFE-E511-BA96-0025905D1D60.root"))
mytests.append(makeTest("Spring16Fastsig","T1ttttFast" if len(name)==0 else name,numevents,command,dataset="/store/mc/RunIISpring16MiniAODv2/SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/00000/004A27F0-5132-E611-A936-02163E016171.root"))
mytests.append(makeTest("2016B","MET16B" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016B-PromptReco-v2.MET",nstart=39,nfiles=2))
mytests.append(makeTest("2016CD","MET16C" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016C-PromptReco-v2.MET",nstart=6,nfiles=3))
mytests.append(makeTest("2016CD","MET16D" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016D-PromptReco-v2.MET",nstart=0,nfiles=3))
mytests.append(makeTest("2016EF","MET16E" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016E-PromptReco-v2.MET",nstart=2,nfiles=10))
mytests.append(makeTest("2016EF","MET16F" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016F-PromptReco-v1.MET",nstart=23,nfiles=2))
mytests.append(makeTest("2016G","MET16G" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016G-PromptReco-v1.MET",nstart=21,nfiles=1))
mytests.append(makeTest("2016H","MET16H" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016H-PromptReco-v2.MET",nstart=30,nfiles=2))
mytests.append(makeTest("2016ReReco23Sep","MET16ReReco" if len(name)==0 else name,numevents,command,inputFilesConfig="Run2016C-23Sep2016-v1.MET",nstart=0,nfiles=10))

if test<0 or test>len(mytests):
    print "Predefined tests:"
    for itest, mytest in enumerate(mytests):
        printTest(mytest,itest,shell)
else:
    printTest(mytests[test],test,shell)
    if run:
        # fork the cmsRun process and exit
        fork_pid = os.fork()
        if fork_pid == 0:
            with open(mytests[test][-1],'w') as out:
                p = subprocess.Popen(mytests[test][0:-1], stdin=None, stdout=out, stderr=out, close_fds=True)
                print "\nRunning test... ["+str(p.pid)+"]"
                sts = os.waitpid(p.pid, 0)[1]
                print "\nTest is done! ["+str(p.pid)+"]"
