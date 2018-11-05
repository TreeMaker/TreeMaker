import os, shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--clean", dest="clean", default=False, action="store_true", help="clean up failed log files (default = %default)")
(options, args) = parser.parse_args()

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
