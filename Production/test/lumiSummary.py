import os
from ROOT import *
import subprocess
from FWCore.PythonUtilities.LumiList import LumiList
import json
from itertools import izip
import array

redirector = "root://cmseos.fnal.gov//"
baseDir = "/store/user/lpcsusyhad/SusyRA2Analysis2015/FinalProductionDPSv1/"

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

class sampleInfo : 

    def __init__( self , fileName, outName ) :
        self.fileName = fileName
        self.outName = outName
        self.fileList = []
        self.addToList()

    def addToList( self ):

        proc = subprocess.Popen( [ "ls /eos/uscms/{0}".format( self.fileName ) ] , stdout = subprocess.PIPE , shell = True )
        ( files , errors ) = proc.communicate()
        for f in files.split("\n") : 
            if len(f)>0 and f.find("No such file or directory") == -1 : 
                f = redirector+f[11:]
            self.fileList.append(f)

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

dataSamples = [ sampleInfo( baseDir+"/Run2015B-PromptReco-v1.DoubleEG_*", "DoubleEG")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.DoubleMuon_*", "DoubleMuon")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.EGamma_*", "EGamma")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.SinglePhoton_*", "SinglePhoton")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.HTMHT_*", "HTMHT")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.MET_*", "MET")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.SingleElectron_*", "SingleElectron")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.SingleMu_*", "SingleMu")  , 
                sampleInfo( baseDir+"/Run2015B-PromptReco-v1.SingleMuon_*", "SingleMuon")  , 
]

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

#stolen unashamedly from:
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/Commands/report.py
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/JobType/BasicJobType.py

if __name__ == "__main__":
    #check for output directory
    if not os.path.isdir("json"):
        os.mkdir("json")

    for s in dataSamples:
        #lumi set for this sample
        mergedLumis = set()
    
        for f in s.fileList:
            file = TFile.Open(f)
            if file == None: continue
            # only keep necessary branches
            t = file.Get("TreeMaker2/PreSelection")
            if t == None: continue
            t.SetBranchStatus("*",0)
            t.SetBranchStatus("RunNum",1)
            t.SetBranchStatus("LumiBlockNum",1)

            #get tree entries
            nentries = t.GetEntries()
            if nentries==0: continue
            t.SetEstimate(nentries)
            t.Draw("RunNum:LumiBlockNum","","goff")
            v1 = t.GetV1(); v1.SetSize(t.GetSelectedRows()); a1 = array.array('d',v1); v1 = None;
            v2 = t.GetV2(); v2.SetSize(t.GetSelectedRows()); a2 = array.array('d',v2); v2 = None;
            
            #loop over tree entries
            for run,ls in izip(a1,a2):
                irun = int(run)
                ils = int(ls)
                if not (irun,ils) in mergedLumis:
                    mergedLumis.add((irun,ils))
                    
            file.Close()

        ### end loop over files in sample

        #convert the runlumis from list of pairs to dict: [(123,3), (123,4), (123,5), (123,7), (234,6)] => {123 : [3,4,5,7], 234 : [6]}
        mLumisDict = {}
        for k, v in mergedLumis:
            mLumisDict.setdefault(k, []).append(int(v))

        #make lumi list from dict
        mergedLumiList = LumiList(runsAndLumis=mLumisDict)
        #get the compact list using CMSSW framework
        analyzed = mergedLumiList.getCompactList()
        if analyzed:
            outfile = 'json/lumiSummary_'+s.outName+'.json'
            with open(outfile, 'w') as jsonFile:
                json.dump(analyzed, jsonFile)
                jsonFile.write("\n")
                print "wrote "+outfile
