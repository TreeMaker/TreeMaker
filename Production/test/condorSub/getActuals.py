from collections import OrderedDict
from utils import get_xrdfs, get_sizetest, pprintOD

def getActuals(dir, fnames, do_overall=False, per_event=False):
    if do_overall and per_event:
        raise RuntimeError("do_overall and per_event options currently not supported together")

    xrdfs, flags = get_xrdfs()
    status, listing = xrdfs.dirlist(dir)
    subdirs = [entry.name for entry in listing]

    output = OrderedDict()
    counts = OrderedDict()
    for fname in list(fnames)+(["overall"] if do_overall else []):
        output[fname] = 0
        counts[fname] = 0
    for subdir in subdirs:
        status, listing = xrdfs.dirlist(dir+"/"+subdir,flags.STAT)
        if listing is None: continue
        for fname in fnames:
            selected = [entry for entry in listing if fname in entry.name]
            output[fname] += sum([entry.statinfo.size for entry in selected])
            if per_event:
                for subsubdir in [entry.name for entry in selected]:
                    path = dir+"/"+subdir+"/"+subsubdir
                    f_status, f_listing = xrdfs.dirlist(path)

                    for file in [entry.name for entry in f_listing]:
                        import ROOT as r
                        rfile = r.TFile.Open(str(xrdfs.url)+path+"/"+file)
                        rtree = rfile.Get("TreeMaker2/PreSelection")
                        counts[fname] += rtree.GetEntries()
                    
        if do_overall: output["overall"] += sum([entry.statinfo.size for entry in listing])

    if per_event:
        for fname in fnames:
            if counts[fname]>0:
                output[fname] = float(output[fname])/float(counts[fname])

    return output

if __name__=="__main__":
    tests = get_sizetest()
    output = getActuals("/store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV20",tests,do_overall=True)
    pprintOD(output,"actuals",True)
