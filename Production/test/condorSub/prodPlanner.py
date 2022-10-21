import os,sys,json,subprocess,shlex
from glob import glob
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import OrderedDict

# utility functions

def get_sizetest(name):
    tests = __import__(name.replace(".py","")).tests
    tests = OrderedDict(tests)

    for fname,test in tests.iteritems():
        if "dname" not in test:
            tests[fname]["dname"] = fname.lower()

    return tests

def writeOD(obj,name,filename,complete=False):
    file = open(filename,'w')

    lines = []
    is_dict = isinstance(obj,dict)
    if complete and is_dict:
        lines.append("from collections import OrderedDict\n")
    prefix = "OrderedDict([" if is_dict else "["
    suffix = "])" if is_dict else "]"
    # a not-very-extensible hack for stable pretty-print of ordered dict
    lines.append("{} = {}".format(name,prefix))
    for key,val in obj.iteritems() if is_dict else obj:
        lines.append('    ("{}", {}),'.format(key, json.dumps(val, sort_keys=True)))
    lines.append(suffix)

    file.write('\n'.join(lines)+'\n')
    file.close()

def get_xrdfs():
    from XRootD import client
    from XRootD.client.flags import DirListFlags

    redirector = "root://cmseos.fnal.gov//"
    xrdfs = client.FileSystem(redirector)

    return xrdfs, DirListFlags

def convert_bytes(val, current, new, base=1000):
    expo = {"": 0, "k": 1, "M": 2, "G": 3, "T": 4, "P": 5, "E": 6, "Z": 7, "Y": 8}
    for prefix in [current,new]:
        if prefix not in expo:
            raise ValueError("Unknown unit {}".format(prefix))
    return float(val)/(base**(expo[new]-expo[current]))

# functions for refresh

def getNeventsData(sizetest,filename):
    tests = get_sizetest(sizetest)

    years = ['2016', '2017', '2018']

    output = OrderedDict()
    for fname,test in tests.iteritems():
        if test["type"]!="data": continue
        output[fname] = {}
        for year in years:
            outsum = 0
            dicts = glob("dict_*{}*_{}.py".format(year,test["dname"]))
            for d in dicts:
                flist = __import__(d.replace(".py","")).flist
                for ff in flist["samples"]:
                    for f in ff:
                        fsplit = getattr(__import__('TreeMaker.Production.{}_cff'.format(f),fromlist=['readFiles']),'readFiles')[0].split('/')
                        fjoin = fsplit[3]+'-'+fsplit[6]
                        dataset = "/{}/{}/MINIAOD".format(fname, fjoin)
                        cmd = 'dasgoclient -query="file dataset={} | sum(file.nevents)"'.format(dataset)
                        dasout = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
                        try:
                            outsum += int(dasout.split()[-1])
                        except:
                            print "WARNING from getNeventsData: command failed: {}".format(cmd)
            output[fname][year] = outsum

    writeOD(output,"neventsData",filename,True)

def getNeventsMC(sizetest,filename):
    from TreeMaker.WeightProducer.MCSamples_Summer20UL16APV import Summer20UL16APVsamples
    from TreeMaker.WeightProducer.MCSamples_Summer20UL16 import Summer20UL16samples
    from TreeMaker.WeightProducer.MCSamples_Summer20UL17 import Summer20UL17samples
    from TreeMaker.WeightProducer.MCSamples_Summer20UL18 import Summer20UL18samples

    tests = get_sizetest(sizetest)

    output = OrderedDict()
    years = OrderedDict([
        ("16APV", Summer20UL16APVsamples),
        ("16", Summer20UL16samples),
        ("17", Summer20UL17samples),
        ("18", Summer20UL18samples),
    ])
    for fname,test in tests.iteritems():
        if test["type"]!="MC": continue
        output[fname] = {}
        for year, samples in years.iteritems():
            fullyear = "20"+year
            outsum = 0
            dicts = glob("dict_*{}_{}.py".format(year,test["dname"]))
            for d in dicts:
                flist = __import__(d.replace(".py","")).flist
                for ff in flist["samples"]:
                    for f in ff:
                        fmatch = f.split('.')[1]
                        found = False
                        for sample in samples:
                            if sample.name==fmatch:
                                found = True
                                outsum += sample.NumberEvtsTotal
                                break
                        if not found: print "WARNING from getNeventsMC: no entry found for {}".format(f)
            output[fname][fullyear] = outsum

    writeOD(output,"neventsMC",filename,True)

def getActualsImpl(dir, fnames, do_overall=False, per_event=False):
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

def getActuals(sizetest,filename,dir):
    tests = get_sizetest(sizetest)
    output = getActualsImpl(dir,tests,do_overall=True)
    writeOD(output,"actuals",filename,True)

def dnames():
    return OrderedDict([
        ("neventsMC",getNeventsMC),
        ("neventsData",getNeventsData),
        ("actuals",getActuals),
    ])

# external functions

def refresh(args):
    for dname,dfunc in dnames().iteritems():
        if getattr(args,dname):
            print "refreshing {}...".format(dname)
            dargs = [args.sizetest,getattr(args,dname)]
            if dname=="actuals": dargs.append(args.dir)
            dfunc(*dargs)
            print "done"

def project(args):
    neventsMC = __import__(args.neventsMC.replace(".py","")).neventsMC
    neventsData = __import__(args.neventsData.replace(".py","")).neventsData
    if args.actualsAll or args.actualsOther:
        actuals = __import__(args.actuals.replace(".py","")).actuals
    else:
        actuals = None

    tests = get_sizetest(args.sizetest)
    fnames = [fname for fname in tests]
    columns = ["sizeEvt", "nevents", "projection", "correction", "corrected"]
    units = ["k", "", "T", "", "T"]
    formats = ["{:.2f}", "{:d}", "{:.2f}", "{:.2f}", "{:.2f}"]
    if args.actualsAll:
        columns.insert(3, "actual")
        units.insert(3, "T")
        formats.insert(3, "{:.2f}")
    results = OrderedDict([(fname,{col: 0 for col in columns}) for fname in fnames+(["other"] if args.actualsAll or args.actualsOther else [])+["total"]])

    # get sizes from size test
    xrdfs, flags = get_xrdfs()
    for tdir in args.testdirs:
        # prioritize: remove tests if already filled from previous dir
        temp = getActualsImpl(tdir, [fname for fname in fnames if results[fname]["sizeEvt"]==0], per_event=True)
        for fname, val in temp.iteritems():
            results[fname]["sizeEvt"] = convert_bytes(temp[fname],"","k")

    # continue to fill results
    for fname in fnames:
        neventsDict = neventsMC if tests[fname]["type"]=="MC" else neventsData
        results[fname]["nevents"] = sum([count for year,count in neventsDict[fname].iteritems()])
        results[fname]["projection"] = convert_bytes(results[fname]["sizeEvt"]*results[fname]["nevents"],"k","T")
        if args.actualsAll: results[fname]["actual"] = convert_bytes(actuals[fname],"","T")
        results[fname]["correction"] = tests[fname]["correction"] if not args.update else results[fname]["actual"]/results[fname]["projection"]
        results[fname]["corrected"] = results[fname]["correction"]*results[fname]["projection"]

    # compute "other" as the remainder
    if args.actualsAll or args.actualsOther:
        results["other"]["sizeEvt"] = ""
        results["other"]["nevents"] = ""
        other_actual = convert_bytes(actuals["overall"],"","T") - sum(convert_bytes(actuals[fname],"","T") for fname in fnames)
        if args.actualsAll: results["other"]["actual"] = other_actual
        results["other"]["correction"] = 1.0
        results["other"]["corrected"] = other_actual
        results["other"]["projection"] = other_actual

    # compute totals
    for col,unit in zip(columns,units):
        if unit!="T": results["total"][col] = ""
        else: results["total"][col] = sum(results[fname][col] for fname in results if fname!="total" and not isinstance(results[fname][col],str))

    # print table
    headers = ["Sample"] + [col+(" [{}B]".format(units[ic]) if len(units[ic])>0 else "") for ic,col in enumerate(columns)]
    table_rows = [[fname] + [form.format(result[col]) if not isinstance(result[col],str) else result[col] for col,form in zip(columns,formats)] for fname, result in results.iteritems()]

    # transpose to find max length for each column
    column_lengths = [max(len(row[i]) for row in [headers]+table_rows) for i in range(len(columns)+1)]
    for irow,row in enumerate([headers]+table_rows):
        cells = ["{0:>{1}}".format(row[i],column_lengths[i]) for i in range(len(row))]
        line = '  '.join(cells)
        print line
        if irow==0:
            print '-'*len(line)

    # print updated dict
    if args.update:
        # use original rather than derived format
        tests_orig = __import__(args.sizetest.replace(".py","")).tests
        # get new correction factors
        for itest,test in enumerate(tests_orig):
            tests_orig[itest][1]["correction"] = float("{:.2f}".format(results[test[0]]["correction"]))
        if len(args.output)==0: args.output = args.sizetest
        pprintOD(tests_orig,"tests",filename=args.output)

def assign(args):
    production = __import__(args.production.replace(".py",""),fromlist=["dicts","users"])
    indicts = getattr(production,"dicts")
    users = getattr(production,"users")

    # get number of jobs for each dict
    dicts = []
    from jobSubmitterTM import jobSubmitterTM
    # supress jobSubmitter printouts
    orig_stdout = sys.stdout
    if args.verbose<2:
        devnull = open(os.devnull, 'w')
        sys.stdout = devnull
    for dict_ in indicts:
        if args.verbose>=2: print dict_
        js = jobSubmitterTM(argv=shlex.split("-c -o . -d {}".format(dict_)))
        js.run()
        dicts.append((js.njobs,dict_))
    if args.verbose<2:
        sys.stdout = orig_stdout
        devnull.close()
    dicts.sort(key=lambda x: -x[0])

    assignments = {user:[0,[]] for user in users}

    def add_dict(user, dict_):
        assignments[user][0] += dict_[0]
        assignments[user][1].append(dict_[1])

    user_index = 0
    begin_index = 0
    end_index = len(dicts)-1
    while begin_index < end_index:
        user = users[user_index]
        add_dict(user, dicts[begin_index])
        while (assignments[user][0] < args.maxJobs or user_index >= len(users)-1) and end_index > begin_index:
            add_dict(user, dicts[end_index])
            end_index -= 1
        user_index += 1
        begin_index += 1

    if args.verbose>=1:
        print '\n'.join(["{} {} {}".format(user, assignments[user][0], ','.join(assignments[user][1])) for user in users])
        print '\nSanity check: {} {}'.format(sum(x[0] for x in dicts), sum(assignments[user][0] for user in users))

    if not os.path.isdir(args.outdir):
        os.mkdir(args.outdir)
    for user in users:
        with open("{}/{}.prodconfig".format(args.outdir,user),'w') as outfile:
            out = [
                "[manage]",
                "dir = .",
                "[caches]",
                "$CMSSW_BASE/test = 1",
                "[submit]",
                "input = {}".format(','.join(assignments[user][1]))
            ]
            outfile.write('\n'.join(out))

# main function

def prodPlanner(argv=None):
    if argv is None: argv = sys.argv[1:]

    # top-level parser
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    # subparser for each operation
    refresh_desc = "refresh nevents and actuals"
    parser_refresh = subparsers.add_parser("refresh", formatter_class=ArgumentDefaultsHelpFormatter, help=refresh_desc, description=refresh_desc)
    project_desc = "make size projection table"
    parser_project = subparsers.add_parser("project", formatter_class=ArgumentDefaultsHelpFormatter, help=project_desc, description=project_desc)
    assign_desc = "assign job dicts to users"
    parser_assign = subparsers.add_parser("assign", formatter_class=ArgumentDefaultsHelpFormatter, help=assign_desc, description=assign_desc)

    # common options
    for subp in [parser_refresh, parser_project]:
        subp.add_argument("-s", "--sizetest", dest="sizetest", default="sizetest.py", type=str, help="input sizetest .py file")
        for dname in dnames():
            subp.add_argument("--{}".format(dname), dest=dname, default="{}.py".format(dname), type=str, help="name for {} .py file".format(dname)+(" (empty: don't refresh)" if subp==parser_refresh else ""))

    # refresh-specific options
    parser_refresh.add_argument("-d", "--dir", dest="dir", type=str, default="/store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV20", help="ntuple directory")
    parser_refresh.set_defaults(func=refresh)

    # project-specific options
    parser_project.add_argument("-d", "--testdirs", dest="testdirs", type=str, nargs='+', help="test file directory(s) in priority order", required=True)
    parser_project.add_argument("-u", "--update", dest="update", default=False, action="store_true", help="update corrections and sizetest .py file")
    parser_project.add_argument("-o", "--output", dest="output", default="", type=str, help="output sizetest .py file name (if updating and different from input)")
    parser_project.add_argument("-a", "--actualsAll", dest="actualsAll", default=False, action="store_true", help="use actuals")
    parser_project.add_argument("-A", "--actualsOther", dest="actualsOther", default=False, action="store_true", help='use actuals just for "other" category')
    parser_project.set_defaults(func=project)

    # assign-specific options
    parser_assign.add_argument("-p", "--production", dest="production", default="production.py", type=str, help="input production .py file")
    parser_assign.add_argument("-m", "--maxJobs", dest="maxJobs", default=14000, type=int, help="approximate maximum number of jobs per user")
    parser_assign.add_argument("-o", "--outdir", dest="outdir", default="assignments", type=str, help="output directory for .prodconfig files")
    parser_assign.add_argument("-v", "--verbose", dest="verbose", default=0, type=int, help="verbosity level")
    parser_assign.set_defaults(func=assign)

    args = parser.parse_args(args=argv)
    args.func(args)

if __name__=="__main__":
    prodPlanner()
