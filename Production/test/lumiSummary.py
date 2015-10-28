import os
import subprocess
from FWCore.PythonUtilities.LumiList import LumiList
from itertools import izip
import array
from multiprocessing import Pool
from optparse import OptionParser

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

class sampleInfo : 

    def __init__( self , outName, baseDir, fileNames ) :
        self.fileNames = fileNames
        self.outName = outName
        self.fileList = []
        for f in fileNames:
            self.addToList(baseDir+"/"+f)

    def addToList( self, fileName ):
        redirector = "root://cmseos.fnal.gov//"
        proc = subprocess.Popen( [ "ls /eos/uscms/{0}".format( fileName ) ] , stdout = subprocess.PIPE , shell = True )
        ( files , errors ) = proc.communicate()
        for f in files.split("\n") : 
            if len(f)>0 and f.find("No such file or directory") == -1 : 
                f = redirector+f[11:]
            self.fileList.append(f)

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

#stolen unashamedly from:
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/Commands/report.py
#https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/JobType/BasicJobType.py

def makeJSON(optlist):
    outdir = optlist[0]
    basedir = optlist[1]
    lastUnblindRun = optlist[2]
    name = optlist[3]
    files = optlist[4:]
    s = sampleInfo(name,basedir,files)
    
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
            if irun <= lastUnblindRun or lastUnblindRun==-1:
                if not (irun,ils) in mergedLumisUnblind:
                    mergedLumisUnblind.add((irun,ils))                
            else:
                if not (irun,ils) in mergedLumisBlinded:
                    mergedLumisBlinded.add((irun,ils))

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
    if mergedLumiListUnblind:
        outfile = outdir+'/lumiSummary_unblind_'+s.outName+'.json'
        mergedLumiListUnblind.writeJSON(outfile)
        print "wrote "+outfile
    if mergedLumiListBlinded:
        outfile = outdir+'/lumiSummary_blinded_'+s.outName+'.json'
        mergedLumiListBlinded.writeJSON(outfile)
        print "wrote "+outfile

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-o", "--outdir", dest="outdir", default="json", help="output directory for JSON files (default = %default)")
    parser.add_option("-b", "--basedir", dest="basedir", default="/store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV3", help="location of data ntuples (default = %default)")
    parser.add_option("-l", "--lastUnblindRun", dest="lastUnblindRun", default=257599, help="last unblind run number (-1 = all unblind) (default = %default)")
    parser.add_option("-d", "--dict", dest="dictfile", default="dataSamples.py", help="list of data sample names and files (default = %default)")
    parser.add_option("-n", "--npool", dest="npool", default=4, help="number of processes to run (default = %default)")
    (options, args) = parser.parse_args()

    from ROOT import *
    
    #check for output directory
    if not os.path.isdir(options.outdir):
        os.mkdir(options.outdir)

    dict = __import__(options.dictfile.replace(".py",""))

    #common list of options
    optlist = [options.outdir, options.basedir, options.lastUnblindRun]
    
    #prepend common list to dict
    for i,d in enumerate(dict.dataSamples):
        dict.dataSamples[i] = optlist + dict.dataSamples[i]
    
    p = Pool(int(options.npool))
    p.map(makeJSON,dict.dataSamples)

