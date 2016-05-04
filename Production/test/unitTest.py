import os

def makeTest(scenario, name, numevents, shell, dataset="", inputFilesConfig="", nstart=0, nfiles=0):
    mytest = []
    mytest.append("cmsRun runMakeTreeFromMiniAOD_cfg.py")
    mytest.append("scenario="+scenario+"")
    # different methods for input files
    if len(dataset)>0:
        mytest.append("dataset=\""+dataset+"\"")
    else:
        mytest.append("inputFilesConfig="+inputFilesConfig+"")
        mytest.append("nstart="+str(nstart)+" nfiles="+str(nfiles)+"")
    # different shell commands
    endstr = "outfile=\""+name+"\" numevents="+str(numevents)
    if shell=="tcsh":
        mytest.append(endstr+" >& "+name+".log &")
    elif shell=="bash" or shell=="sh":
        mytest.append(endstr+" > "+name+".log 2>&1 &")
    return mytest

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
test=parameters.value("test",-1)
name=parameters.value("name","")
run=parameters.value("run",False)
numevents=parameters.value("numevents",100)
shell=parameters.value("shell","tcsh")

# list of tests
mytests = []
mytests.append(makeTest("Spring15v2","gjet" if len(name)==0 else name,numevents,shell,dataset="/store/mc/RunIISpring15MiniAODv2/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/10B3B366-4C71-E511-8364-00259074AE3C.root"))
mytests.append(makeTest("Spring15v2","ttbar" if len(name)==0 else name,numevents,shell,dataset="/store/mc/RunIISpring15MiniAODv2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/001F4F14-786E-E511-804F-0025905A60FE.root"))
mytests.append(makeTest("Spring15v2sig","T1tttt" if len(name)==0 else name,numevents,shell,dataset="/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/38C49928-8D72-E511-94A6-001E67579188.root"))
mytests.append(makeTest("Spring15Fastv2","TTbarFast" if len(name)==0 else name,numevents,shell,dataset="/store/mc/RunIISpring15MiniAODv2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/02152095-E27D-E511-B425-00259073E49A.root"))
mytests.append(makeTest("Spring15Fastv2sig","T1bbbbFast" if len(name)==0 else name,numevents,shell,dataset="/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1000-1025_mLSP-1to975-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/00B3085A-7D7B-E511-A75B-003048335516.root"))
mytests.append(makeTest("re2015C","HTMHTreC" if len(name)==0 else name,numevents,shell,inputFilesConfig="Run2015C_25ns-05Oct2015-v1.HTMHT",nstart=0,nfiles=4))
mytests.append(makeTest("re2015D","HTMHTreD" if len(name)==0 else name,numevents,shell,inputFilesConfig="Run2015D-05Oct2015-v1.HTMHT",nstart=102,nfiles=10))
mytests.append(makeTest("2015Db","HTMHTDb" if len(name)==0 else name,numevents,shell,dataset="/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v4/000/258/159/00000/42D9839F-DC6B-E511-82B0-02163E0136EC.root"))

if test<0 or test>len(mytests):
    print "Predefined tests:"
    for itest, mytest in enumerate(mytests):
        print str(itest)+":\n  "+" \\\n  ".join(mytest)
else:
    print str(test)+":\n  "+" \\\n  ".join(mytests[test])
    if run:
        print "Running test..."
        os.system(" ".join(mytests[test]))

