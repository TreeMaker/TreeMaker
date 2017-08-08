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
mytests.append(makeTest("2017BC","MET17Prompt" if len(name)==0 else name,numevents,command,dataset="/store/data/Run2017B/MET/MINIAOD/PromptReco-v2/000/299/178/00000/96D1BD40-E56B-E711-BF3A-02163E0135FC.root"))
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
