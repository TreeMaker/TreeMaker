import re,sys,getopt,urllib2,json,os
# check os
slc = os.environ['SCRAM_ARCH'].split('_')[0]
extra_paths = [
    "/cvmfs/cms.cern.ch/share/cms/crab-prod/3.3.2005-bcolbf/lib/",
]
sys.path = extra_paths + sys.path
from dbs.apis.dbsClient import DbsApi
from optparse import OptionParser
from collections import defaultdict
from TreeMaker.WeightProducer.MCSample import MCSample

def main(args):
    # Read parameters
    parser = OptionParser()
    parser.add_option("-d", "--dict", dest="dict", default="", help="check for samples listed in this dict (default = %default)")
    parser.add_option("-p", "--py", dest="py", default=False, action="store_true", help="generate python w/ list of files (default = %default)")
    parser.add_option("-w", "--wp", dest="wp", default=False, action="store_true", help="generate WeightProducer lines (default = %default)")
    parser.add_option("-s", "--se", dest="se", default=False, action="store_true", help="make list of sites with 100% hosting (default = %default)")
    parser.add_option("-u", "--use-full-name", dest="fn", default=False, action="store_true", help="use the full name of the dataset rather than just the first part (default = %default)")
    parser.add_option("-o", "--output-folder", dest="of", default="./", help="put the output files in the specified folder (default = %default)")
    (options, args) = parser.parse_args(args)
    
    dictname = options.dict.replace(".py","");
    flist = __import__(dictname).flist
    ofolder = options.of
    if ofolder[-1] != "/": ofolder += "/"
    if not os.path.isdir(ofolder):
        os.mkdir(ofolder)
    makepy = options.py
    makewp = options.wp
    makese = options.se
    makefn = options.fn
    if not makepy and not makewp and not makese:
        parser.error("No operations selected!")
    
    # interface with DBS
    dbs3api = DbsApi("https://cmsweb.cern.ch/dbs/prod/global/DBSReader")
    
    # format for dict entries:
    #                                                data: [True,  ['sample'] , []]
    #                                                  MC: [False, ['sample'] , []]
    #                               MC w/ extended sample: [False, ['sample','sample_ext'] , []]
    #                   MC w/ negative weights (amcatnlo): [False, ['sample'] , [neff]]
    # MC w/ negative weights (amcatnlo) + extended sample: [False, ['sample','sample_ext'] , [neff, neff_ext]]
    
    if makewp:
        wname = "weights_"+dictname+".txt"
        wfile = open(ofolder+wname,'w')
    
    if makese:
        sname = "sites_"+dictname+".txt"
        sfile = open(ofolder+sname,'w')
        
    for fitem in flist:
        is_data = fitem[0]==0
        wrong_pu = fitem[0]==2
        ff = fitem[1]
        x = fitem[2]
        nevents_all = []
        for f in ff: # in case of extended samples
            print f
    
            # get sample name
            if makepy:
                if makefn:
                    oname = f.replace('/','_')[1:]
                else:
                    oname = f.split('/')[1]
                    # check for extended sample
                    extcheck = re.search("ext[0-9]",f.split('/')[2])
                    if not extcheck==None and len(extcheck.group(0))>0: oname = oname+"_"+extcheck.group(0)
                
                # make python file with preamble
                pfile = open(ofolder+oname+"_cff.py",'w')
                pfile.write("import FWCore.ParameterSet.Config as cms\n\n")
                pfile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
                pfile.write("readFiles = cms.untracked.vstring()\n")
                pfile.write("secFiles = cms.untracked.vstring()\n")
                pfile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n")
                
            # get list of hosted files using PhEDEx API
            filelist = set()
            sitelist = defaultdict(int)
            url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?dataset=' + f
            jstr = urllib2.urlopen(url).read()
            jstr = jstr.replace("\n", " ")
            result = json.loads(jstr)
            for block in result['phedex']['block']:
                for item in block['file']:
                    filelist.add(item['name'])
                    if makese:
                        for replica in item['replica']:
                            site = replica['node']
                            addr = replica['se']
                            # safety checks
                            if site is None: continue
                            if addr is None: addr = ""
                            ## if (site,addr) not in sitelist.keys(): sitelist[(site,addr)] = 0
                            sitelist[(site,addr)] += 1
    
            # get dataset info - detail only needed in makewp case
            nevents = 0
            if makewp:
                fileArrays = dbs3api.listFileArray(dataset=f,detail=makewp)
                for fileArray in fileArrays:
                    if fileArray["logical_file_name"] in filelist:
                        nevents += fileArray["event_count"]
                nevents_all.append(nevents)
            
            # check for sites with 100% dataset presence (based on PhEDEx)
            # refs:
            # https://github.com/dmwm/DAS/blob/master/src/python/DAS/services/combined/combined_service.py
            # https://github.com/gutsche/scripts/blob/master/PhEDEx/checkLocation.py
            if makese:
                # get total number of expected files
                nfiles_tot = len(filelist)
                # calculate dataset fraction (presence) in % and check for completion
                highest_percent = 0
                for site,addr in sitelist:
                    this_percent = float(sitelist[(site,addr)])/float(nfiles_tot)*100
                    sitelist[(site,addr)] = this_percent
                    if this_percent > highest_percent: highest_percent = this_percent
            
                sfile.write(f+"\n")
                if highest_percent < 100:
                    sfile.write("  !!! No site has complete dataset !!! ( Highest: "+str(highest_percent)+"% )\n")
                for site,addr in sorted(sitelist):
                    this_percent = sitelist[(site,addr)]
                    if this_percent==highest_percent:
                        sfile.write("  "+site+" ("+addr+")\n")
    
            if makepy:
                #sort list of files for consistency
                filesort = sorted(filelist)
                counter = 0
                #split into chunks of 255
                for lfn in filesort:
                    if counter==0: pfile.write("readFiles.extend( [\n")
                    pfile.write("       '"+lfn+"',\n")
                    if counter==254 or lfn==filesort[-1]:
                        pfile.write("] )\n")
                        counter = 0
                    else:
                        counter += 1
    
        #only do weightproducer stuff for MC
        if makewp and is_data==False:
            nevents = nevents_all[0]
            neff = 0
            if len(x)>0: neff = x[0]
            
            #handle combining extended samples
            if len(ff)>1:
                neff = sum(x[0:])
                nevents = sum(nevents_all)
            
            for i,f in enumerate(ff):
                #make line for weightproducer
                line = (" "*8)+repr(MCSample(f.split('/')[1],"-".join(f.split('/')[2].split('-')[1:3]),f.split('/')[2].split('-')[0],"Constant",nevents,wrong_pu,neff if neff>0 else None))+","
                if neff>0:
                    if len(ff)>1: line = line+" # subtotal = "+str(x[i])+", straight subtotal = "+str(nevents_all[i])+"\n"
                    else: line = line+"\n"
                else:
                    if len(ff)>1: line = line+" # subtotal = "+str(nevents_all[i])+"\n"
                    else: line = line+"\n"
                wfile.write(line)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
