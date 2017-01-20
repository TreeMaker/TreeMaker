import re,sys,getopt,urllib2,json
from dbs.apis.dbsClient import DbsApi

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dictfile = parameters.value("dict","")
dict = __import__(dictfile.replace(".py",""))
makepy = parameters.value("py",True)
makewp = parameters.value("wp",True)
makese = parameters.value("se",True)

#interface with DBS
dbs3api = DbsApi("https://cmsweb.cern.ch/dbs/prod/global/DBSReader")

#format for dict entries:
#                                               data: [['sample'] , []]
#                                                 MC: [['sample'] , [xsec]]
#                              MC w/ extended sample: [['sample','sample_ext'] , [xsec]]
#                  MC w/ negative weights (amcatnlo): [['sample'] , [xsec, neff]]
#MC w/ negative weights (amcatnlo) + extended sample: [['sample','sample_ext'] , [xsec, neff, neff_ext]]

if makewp:
    wname = "weights_"+dictfile.replace(".py","")+".txt"
    wfile = open(wname,'w')

if makese:
    sname = "sites_"+dictfile.replace(".py","")+".txt"
    sfile = open(sname,'w')
    
for fitem in dict.flist:
    ff = fitem[0]
    x = fitem[1]
    nevents_all = []
    for f in ff: # in case of extended samples
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
        print f
        fileArrays = dbs3api.listFileArray(dataset=f,detail=makewp)
        for fileArray in fileArrays:
            if makepy:
                filelist.append(fileArray["logical_file_name"])
            if makewp:
                nevents += fileArray["event_count"]
        nevents_all.append(nevents)
        
        # check for sites with 100% dataset presence (using PhEDEx API)
        # refs:
        # https://github.com/dmwm/DAS/blob/master/src/python/DAS/services/combined/combined_service.py
        # https://github.com/gutsche/scripts/blob/master/PhEDEx/checkLocation.py
        if makese:
            url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?dataset=' + f
            jstr = urllib2.urlopen(url).read()
            jstr = jstr.replace("\n", " ")
            result = json.loads(jstr)
            
            site_list = {}
            for block in result['phedex']['block']:
                for replica in block['replica']:
                    site = replica['node']
                    addr = replica['se']
                    #safety checks
                    if site is None: continue
                    if addr is None: addr = ""
                    if (site,addr) not in site_list.keys(): site_list[(site,addr)] = 0
                    site_list[(site,addr)] += replica['files']
                
            # get total number of expected files from DBS
            nfiles_tot = len(fileArrays)
            # calculate dataset fraction (presence) in % and check for completion
            highest_percent = 0
            for site,addr in site_list:
                this_percent = float(site_list[(site,addr)])/float(nfiles_tot)*100
                site_list[(site,addr)] = this_percent
                if this_percent > highest_percent: highest_percent = this_percent
        
            sfile.write(f+"\n")
            if highest_percent < 100:
                sfile.write("  !!! No site has complete dataset !!! ( Highest: "+str(highest_percent)+"% )\n")
            for site,addr in site_list:
                this_percent = site_list[(site,addr)]
                if this_percent==highest_percent:
                    sfile.write("  "+site+" ("+addr+")\n")

        if makepy:
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
        nevents = nevents_all[0]
        neff = 0
        if len(x)>1: neff = x[1]
        
        #handle combining extended samples
        if len(ff)>1:
            neff = sum(x[1:])
            nevents = sum(nevents_all)
        
        for i,f in enumerate(ff):
            #make line for weightproducer
            line = "        MCSample(\""+f.split('/')[1]+"\", \""+"-".join(f.split('/')[2].split('-')[1:3])+"\", \""+f.split('/')[2].split('-')[0]+"\", \"Constant\", "+str(x[0])+", ";
            if neff>0:
                line = line+str(neff)+"),"
                if len(ff)>1: line = line+" # subtotal = "+str(x[i+1])+", straight subtotal = "+str(nevents_all[i])+"\n"
                else: line = line+" # straight total = "+str(nevents)+"\n"
            else:
                line = line+str(nevents)+"),"
                if len(ff)>1: line = line+" # subtotal = "+str(nevents_all[i])+"\n"
                else: line = line+"\n"
            wfile.write(line)
