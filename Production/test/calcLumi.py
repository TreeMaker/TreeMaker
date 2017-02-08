import os,glob,re,json
from optparse import OptionParser

def runBril(output,category,pd,section,file,normtag):
    # setup output
    key = section+"_"+category

    # run bril
    cmd = "./brilcalc lumi -b \"STABLE BEAMS\" " + ("--normtag "+normtag+" " if len(normtag)>0 else "") + "-u /pb -i "+file
    #print cmd
    brilout = os.popen(cmd).read()
    brilsplit = brilout.split('\n')
    lumival = brilsplit[brilsplit.index("#Summary: ")+4].split()[-2]
    
    # store output
    output[pd][key] = float(lumival)
    return key

# runs in: /afs/cern.ch/work/p/pedrok/private/SUSY2015/brilcalc

parser = OptionParser()
parser.add_option("-i", "--indir", dest="indir", default="json", help="input directory for JSON files (default = %default)")
parser.add_option("-t", "--normtag", dest="normtag", default="", help="normtag for lumi calculation (default = %default)")
parser.add_option("-l", "--lastUnblindRun", dest="lastUnblindRun", default=258750, help="last unblind run number (-1 = all unblind) (default = %default)")
parser.add_option("-f", "--firstUnblindRun", dest="firstUnblindRun", default=0, help="first unblind run number (-1 = all unblind) (default = %default)")
(options, args) = parser.parse_args()

lastUnblindRun = int(options.lastUnblindRun)
firstUnblindRun = int(options.firstUnblindRun)
if (firstUnblindRun != -1 or lastUnblindRun != -1) and not os.path.isdir(options.indir+"/split"):
    os.mkdir(options.indir+"/split")

output = {}
# global lists
sections = []
keys = []

jsonfiles = glob.glob(options.indir+"/lumiSummary_*.json")
for f in jsonfiles:
    print f
    fbase = os.path.basename(f)
    fsplit = re.split('_|\.',fbase)
    # e.g. lumiSummary_DoubleMuon_2015D.json
    pd = fsplit[1]
    section = fsplit[2]
    if not pd in output:
        output[pd] = {}
    if not section in sections:
        sections.append(section)

    # split into blind and unblind if desired
    if firstUnblindRun != -1 or lastUnblindRun != -1:
        with open(f,'r') as jsonfile:
            lumidict = json.load(jsonfile)
            lumidictSplit = {
                "unblind": {},
                "blinded": {}
            }
            for k in lumidict:
                if (firstUnblindRun==-1 or int(k)>=firstUnblindRun) and (lastUnblindRun==-1 or int(k)<=lastUnblindRun):
                    lumidictSplit["unblind"][k] = lumidict[k]
                else:
                    lumidictSplit["blinded"][k] = lumidict[k]
                    
            # output into files and run bril
            for k in lumidictSplit:
                if len(lumidictSplit[k])>0:
                    fname = options.indir+"/split/lumiSummary_"+k+"_"+pd+"_"+section+".json"
                    with open(fname,'w') as fout:
                        json.dump(lumidictSplit[k], fout, sort_keys=True)
                    key = runBril(output,k,pd,section,fname,options.normtag)
                    if not key in keys:
                        keys.append(key)
    else:
        # just run bril
        key = runBril(output,"all",pd,section,f,options.normtag)
        if not key in keys:
            keys.append(key)

# organized print

# header
col0 = "Primary Dataset"
header = "| "+col0+" | "
keysToUse = []
columnLengths = [len(col0)]
for section in sorted(sections):
    cats = ["_all","_unblind","_blinded"]
    pcats = [""," (unblind)"," (blinded)"]
    for ic,cat in enumerate(cats):
        key = section+cat
        if key in keys:
            pkey = key.replace(cat,pcats[ic])
            header += pkey+" | "
            keysToUse.append(key)
            columnLengths.append(len(pkey))
colN = "Total"+' '*10
columnLengths.append(len(colN))
header += colN+" |"
print header

for pd,val in sorted(output.iteritems()):
    row = "| "+"{0:<{1}} | ".format(pd,columnLengths[0])
    total = 0
    for ik,key in enumerate(keysToUse):
        lumi = val[key] if key in val else 0
        total += lumi
        row += "{0:>{1}.3f} | ".format(lumi,columnLengths[ik+1])
    row += "{0:>{1}.3f} |".format(total,columnLengths[-1])
    print row
