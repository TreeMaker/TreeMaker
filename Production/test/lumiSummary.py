import os
from ROOT import *
import subprocess
from FWCore.PythonUtilities.LumiList import LumiList
import json
from itertools import izip
import array

redirector = "root://cmseos.fnal.gov//"
baseDir = "/store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV3/"

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

class sampleInfo : 

    def __init__( self , outName, fileNames ) :
        self.fileNames = fileNames
        self.outName = outName
        self.fileList = []
        for f in fileNames:
            self.addToList(f)

    def addToList( self, fileName ):

        proc = subprocess.Popen( [ "ls /eos/uscms/{0}".format( fileName ) ] , stdout = subprocess.PIPE , shell = True )
        ( files , errors ) = proc.communicate()
        for f in files.split("\n") : 
            if len(f)>0 and f.find("No such file or directory") == -1 : 
                f = redirector+f[11:]
            self.fileList.append(f)

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

dataSamples = [
    # 2015C datasets: prompt
    sampleInfo( "DoubleEG_2015C", [baseDir+"/Run2015C-PromptReco-v1.DoubleEG_*"] ),
    sampleInfo( "DoubleMuon_2015C", [baseDir+"/Run2015C-PromptReco-v1.DoubleMuon_*"] ),
    sampleInfo( "HTMHT_2015C", [baseDir+"/Run2015C-PromptReco-v1.HTMHT_*"] ),
    sampleInfo( "JetHT_2015C", [baseDir+"/Run2015C-PromptReco-v1.JetHT_*"] ),
    sampleInfo( "MET_2015C", [baseDir+"/Run2015C-PromptReco-v1.MET_*"] ),
    sampleInfo( "SingleElectron_2015C", [baseDir+"/Run2015C-PromptReco-v1.SingleElectron_*"] ),
    sampleInfo( "SingleMuon_2015C", [baseDir+"/Run2015C-PromptReco-v1.SingleMuon_*"] ),
    sampleInfo( "SinglePhoton_2015C", [baseDir+"/Run2015C-PromptReco-v1.SinglePhoton_*"] ),
    # 2015D datasets: re-miniAOD, prompt v4
    sampleInfo( "DoubleEG_2015D",       [baseDir+"/Run2015D-05Oct2015-v1.DoubleEG_*"      , baseDir+"/Run2015D-PromptReco-v4.DoubleEG_*"      ] ),
    sampleInfo( "DoubleMuon_2015D",     [baseDir+"/Run2015D-05Oct2015-v1.DoubleMuon_*"    , baseDir+"/Run2015D-PromptReco-v4.DoubleMuon_*"    ] ),
    sampleInfo( "HTMHT_2015D",          [baseDir+"/Run2015D-05Oct2015-v1.HTMHT_*"         , baseDir+"/Run2015D-PromptReco-v4.HTMHT_*"         ] ),
    sampleInfo( "JetHT_2015D",          [baseDir+"/Run2015D-05Oct2015-v1.JetHT_*"         , baseDir+"/Run2015D-PromptReco-v4.JetHT_*"         ] ),
    sampleInfo( "MET_2015D",            [baseDir+"/Run2015D-05Oct2015-v1.MET_*"           , baseDir+"/Run2015D-PromptReco-v4.MET_*"           ] ),
    sampleInfo( "SingleElectron_2015D", [baseDir+"/Run2015D-05Oct2015-v1.SingleElectron_*", baseDir+"/Run2015D-PromptReco-v4.SingleElectron_*"] ),
    sampleInfo( "SingleMuon_2015D",     [baseDir+"/Run2015D-05Oct2015-v1.SingleMuon_*"    , baseDir+"/Run2015D-PromptReco-v4.SingleMuon_*"    ] ),
    sampleInfo( "SinglePhoton_2015D",   [baseDir+"/Run2015D-05Oct2015-v1.SinglePhoton_*"  , baseDir+"/Run2015D-PromptReco-v4.SinglePhoton_*"  ] ),
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

    lastUnblindRun = 257599
        
    for s in dataSamples:
        #lumi set for this sample
        mergedLumisUnblind = set()
        mergedLumisBlinded = set()
    
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
                if irun > lastUnblindRun:
                    if not (irun,ils) in mergedLumisBlinded:
                        mergedLumisBlinded.add((irun,ils))
                else:
                    if not (irun,ils) in mergedLumisUnblind:
                        mergedLumisUnblind.add((irun,ils))                
                    
            file.Close()

        ### end loop over files in sample

        #convert the runlumis from list of pairs to dict: [(123,3), (123,4), (123,5), (123,7), (234,6)] => {123 : [3,4,5,7], 234 : [6]}
        mLumisDictUnblind = {}
        mLumisDictBlinded = {}
        for k, v in mergedLumisUnblind:
            mLumisDictUnblind.setdefault(k, []).append(int(v))
        for k, v in mergedLumisBlinded:
            mLumisDictBlinded.setdefault(k, []).append(int(v))

        #make lumi list from dict
        mergedLumiListUnblind = LumiList(runsAndLumis=mLumisDictUnblind)
        mergedLumiListBlinded = LumiList(runsAndLumis=mLumisDictBlinded)
        #get the compact list using CMSSW framework
        analyzedUnblind = mergedLumiListUnblind.getCompactList()
        analyzedBlinded = mergedLumiListBlinded.getCompactList()
        if analyzedUnblind:
            outfile = 'json/lumiSummary_unblind_'+s.outName+'.json'
            with open(outfile, 'w') as jsonFile:
                json.dump(analyzedUnblind, jsonFile)
                jsonFile.write("\n")
                print "wrote "+outfile
        if analyzedBlinded:
            outfile = 'json/lumiSummary_blinded_'+s.outName+'.json'
            with open(outfile, 'w') as jsonFile:
                json.dump(analyzedBlinded, jsonFile)
                jsonFile.write("\n")
                print "wrote "+outfile
