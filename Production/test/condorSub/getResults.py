import os, sys, shutil, difflib
from optparse import OptionParser
from TreeMaker.Production.tm_common import printGetPyDictHeader

parser = OptionParser()
parser.add_option("-d", "--debug", dest="debug", default=False, action="store_true", help="print additional debugging information (default = %default)")
parser.add_option("-g", "--gen_dict", dest="gen_dict", default=False, action="store_true", help="flag to turn on the updating of the get_py.py dictionary (default = %default)")
parser.add_option("-i", "--in_dict", dest="in_dict", default="dict.py", help="input dictionary to update with neff values (default = %default)")
parser.add_option("-l", "--clean", dest="clean", default=False, action="store_true", help="clean up failed log files (default = %default)")
parser.add_option("-o", "--out_dict", dest="out_dict", default="dictNeff.py", help="the name of the output dictionary with updated neff values (default = %default)")
(options, args) = parser.parse_args()

# sanity check the options
if options.gen_dict and (len(options.in_dict)==0 or len(options.out_dict)==0):
    print "Must specify the input and output dictionaries if using the option --gen_dict (-d)"
    exit(-1)

if options.clean:
    fdir = "failures"
    if not os.path.isdir(fdir):
        os.mkdir(fdir)

def getList(cmd):
    return filter(None,os.popen(cmd).read().split('\n'))
    
failures = getList('grep -l "Exception" *.stdout')

results = getList('grep "NeffFinder: " *.stdout')

rdict = {}

for result in results:
    rsplit = result.split(' ')
    
    # check file
    rfile = rsplit[0].split(':')[0]
    if rfile in failures:
        print "failed: "+rfile
        if options.clean: shutil.move(rfile,fdir+"/"+rfile)
        continue
    
    # structure of output:
    # file:NeffFinder: name : #eff (pos = #pos, neg = #neg, tot = #tot)
    rname = rsplit[1]
    rtmp = {
        "eff": int(rsplit[3]),
        "pos": int(rsplit[6].replace(",","")),
        "neg": int(rsplit[9].replace(",","")),
        "tot": int(rsplit[12].replace(")",""))
    }
    
    # check for job that finished but didn't do anything
    if rtmp["tot"]==0:
        print "failed: "+rfile
        continue
    
    # initialize
    if rname not in rdict.keys():
        rdict[rname] = {"eff":0,"pos":0,"neg":0,"tot":0}
    
    # sum up
    for num in rtmp.keys():
        rdict[rname][num] += rtmp[num]

# print results
for rname,rvals in sorted(rdict.iteritems()):
    # reassemble structure
    print rname+" : "+str(rvals["eff"])+" (pos = "+str(rvals["pos"])+", neg = "+str(rvals["neg"])+", tot = "+str(rvals["tot"])+")"

# generate a new dictionary if in_dict and out_dict are set
if options.gen_dict:
    outf = open(options.out_dict,'w')
    printGetPyDictHeader(outf)

    sys.path.append(os.path.abspath(os.path.dirname(options.in_dict)))
    dictname = os.path.basename(options.in_dict.replace(".py",""))
    flist = __import__(dictname).flist

    for fitem in flist:
        if fitem[0]==0: continue #skip the data samples
        ff = fitem[1]
        x = fitem[2]
        nevents_all = []
        line = "    [" + str(fitem[0]) + ", " + str(ff) + ", ["
        for idataset, dataset in enumerate(ff):
            sample = dataset.split("/")[1]
            close_matches = difflib.get_close_matches(sample, rdict, n=10)
            selected_indices = [i for i, s in enumerate(close_matches) if sample in s]
            if len(selected_indices)>1:
                print "WARNING: Double check values with extensions or close names"
            if options.debug:
                print sample + ": " + str(close_matches)
                print "\tSelected indices: " + str(selected_indices)
                print "\tSelected match: " + str(selected_indices[idataset])
            rval = rdict[close_matches[selected_indices[idataset]]]
            line += str(rval["eff"])
            if idataset<len(ff)-1: line += ", "
        line += "]],\n"
        outf.write(line)
  
    outf.write("]\n")
    outf.close()
