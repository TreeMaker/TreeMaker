import re,sys
from dbs.apis.dbsClient import DbsApi

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dictfile = parameters.value("dict","")
dict = __import__(dictfile.replace(".py",""))
makepy = parameters.value("py",True)
makewp = parameters.value("wp",True)

#interface with DBS
dbs3api = DbsApi("https://cmsweb.cern.ch/dbs/prod/global/DBSReader")

#format for ordered dict entries:
#                             data: ('sample' , [])
#                               MC: ('sample' , [xsec])
#MC w/ negative weights (amcatnlo): ('sample' , [xsec, neff])

if makewp:
    wfile = open("weights.txt",'w')

for f,x in dict.flist.iteritems():
    if makepy:
        #get sample name
        oname = f.split('/')[1]
        
        #check for extended sample
        extcheck = re.search("ext[0-9]",f.split('/')[2])
        if not extcheck==None and len(extcheck.group(0))>0: oname = oname+"_"+extcheck.group(0)
        
        #make python file with preamble
        pfile = open(oname+"_cff.py",'w')
        pfile.write("import FWCore.ParameterSet.Config as cms\n\n")
        pfile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
        pfile.write("readFiles = cms.untracked.vstring()\n")
        pfile.write("secFiles = cms.untracked.vstring()\n")
        pfile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n")
        
    #get dataset info - detail only needed in makewp case
    filelist = []
    nevents = 0
    fileArrays = dbs3api.listFileArray(dataset=f,detail=makewp)
    for fileArray in fileArrays:
        if makepy:
            filelist.append(fileArray["logical_file_name"])
        if makewp:
            nevents += fileArray["event_count"]
    
    if makewp:
        #sort list of files for consistency
        filelist.sort()
        counter = 0
        #split into chunks of 255
        for lfn in filelist:
            if counter==0: pfile.write("readFiles.extend( [\n")
            pfile.write("       '"+lfn+"',\n")
            if counter==254 or lfn==filelist[-1]:
                pfile.write("] )\n")
                counter = 0
            else:
                counter += 1

    #only do weightproducer stuff for MC (w/ xsec provided)
    if makewp and len(x)>0:
        xsec = x[0]
        neff = 0
        if len(x)>1: neff = x[1]
        
        #make line for weightproducer
        line = "        MCSample(\""+f.split('/')[1]+"\", \""+"-".join(f.split('/')[2].split('-')[1:3])+"\", \""+f.split('/')[2].split('-')[0]+"\", \"Constant\", "+str(x[0])+", ";
        if neff>0: line = line+str(neff)+"), # straight total = "+str(nevents)+"\n"
        else: line = line+str(nevents)+"),\n"
        wfile.write(line)
