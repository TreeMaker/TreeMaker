import os,glob,re,json
from optparse import OptionParser

def runBril(output,category,pd,section,file,normtag):
    # setup output
    key = section+"_"+category
    if not key in output:
        output[key] = {}
    
    # run bril
    cmd = "./brilcalc lumi -b \"STABLE BEAMS\" " + ("--normtag "+normtag+" " if len(normtag)>0 else "") + "-u /pb -i "+file
    #print cmd
    brilout = os.popen(cmd).read()
    brilsplit = brilout.split('\n')
    lumival = brilsplit[brilsplit.index("#Summary: ")+4].split()[-2]
    
    # store output
    output[key][pd] = lumival

# runs in: /afs/cern.ch/work/p/pedrok/private/SUSY2015/brilcalc

parser = OptionParser()
parser.add_option("-i", "--indir", dest="indir", default="json", help="input directory for JSON files (default = %default)")
parser.add_option("-t", "--normtag", dest="normtag", default="", help="normtag for lumi calculation (default = %default)")
parser.add_option("-l", "--lastUnblindRun", dest="lastUnblindRun", default=258750, help="last unblind run number (-1 = all unblind) (default = %default)")
(options, args) = parser.parse_args()

lastUnblindRun = int(options.lastUnblindRun)
if lastUnblindRun != -1 and not os.path.isdir(options.indir+"/split"):
    os.mkdir(options.indir+"/split")

output = {}

jsonfiles = glob.glob(options.indir+"/lumiSummary_*.json")
for f in jsonfiles:
    print f
    fbase = os.path.basename(f)
    fsplit = re.split('_|\.',fbase)
    # e.g. lumiSummary_DoubleMuon_2015D.json
    pd = fsplit[1]
    section = fsplit[2]

    # split into blind and unblind if desired
    if lastUnblindRun!=-1:
        with open(f,'r') as jsonfile:
            lumidict = json.load(jsonfile)
            lumidictSplit = {
                "unblind": {},
                "blinded": {}
            }
            for k in lumidict:
                if int(k)<=lastUnblindRun:
                    lumidictSplit["unblind"][k] = lumidict[k]
                else:
                    lumidictSplit["blinded"][k] = lumidict[k]
                    
            # output into files and run bril
            for k in lumidictSplit:
                if len(lumidictSplit[k])>0:
                    fname = options.indir+"/split/lumiSummary_"+k+"_"+pd+"_"+section+".json"
                    with open(fname,'w') as fout:
                        json.dump(lumidictSplit[k], fout, sort_keys=True)
                    runBril(output,k,pd,section,fname,options.normtag)
    else:
        # just run bril
        runBril(output,"all",pd,section,f,options.normtag)

#organized print
for key,val in sorted(output.iteritems()):
    print key+"-"*10
    for pd,lumi in sorted(val.iteritems()):
        print pd+": "+lumi
