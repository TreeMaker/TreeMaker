from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import OrderedDict
from utils import get_xrdfs, get_sizetest, pprintOD
from getTotals import getTotals

def convert_bytes(val, current, new):
    expo = {"": 0, "k": 1, "M": 2, "G": 3, "T": 4, "P": 5, "E": 6, "Z": 7, "Y": 8}
    base = 1024
    for prefix in [current,new]:
        if prefix not in expo:
            raise ValueError("Unknown unit {}".format(prefix))
    return float(val)/(base**(expo[new]-expo[current]))

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--sizetest", dest="sizetest", type=str, help="input sizetest .py file", required=True)
parser.add_argument("-d", "--testdirs", dest="testdirs", default=[], type=str, action="append", help="test file directory(s) in priority order", required=True)
# todo: add "refresh" option for nevents & totals
parser.add_argument("-u", "--update", dest="update", default=False, action="store_true", help="update corrections and sizetest .py file")
parser.add_argument("-o", "--output", dest="output", type=str, help="output sizetest .py file name (if updating and different from input)")
parser.add_argument("-t", "--totals", dest="totals", default=False, action="store_true", help="use totals.py")
args = parser.parse_args()

# todo: make everything configurable... and/or merge into one application
from neventsMC import neventsMC
from neventsData import neventsData
from utils import get_sizetest, pprintOD
if args.totals:
    from totals import totals
else:
    totals = None

tests = get_sizetest(args.sizetest)
fnames = [fname for fname in tests]
columns = ["sizeEvt", "nevents", "projection", "correction", "corrected"]
units = ["k", "", "T", "", "T"]
formats = ["{:.2f}", "{:d}", "{:.2f}", "{:.2f}", "{:.2f}"]
if args.totals:
    columns.insert(3, "actual")
    units.insert(3, "T")
    formats.insert(3, "{:.2f}")
results = OrderedDict([(fname,{col: 0 for col in columns}) for fname in fnames+(["other"] if args.totals else [])])

# get sizes from size test
xrdfs, flags = get_xrdfs()
for tdir in args.testdirs:
    # prioritize: remove tests if already filled from previous dir
    temp = getTotals(tdir, [fname for fname in fnames if results[fname]["sizeEvt"]==0], per_event=True)
    for fname, val in temp.iteritems():
        results[fname]["sizeEvt"] = convert_bytes(temp[fname],"","k")

# continue to fill results
for fname in fnames:
    neventsDict = neventsMC if tests[fname]["type"]=="MC" else neventsData
    results[fname]["nevents"] = sum([count for year,count in neventsDict[fname].iteritems()])
    results[fname]["projection"] = convert_bytes(results[fname]["sizeEvt"]*results[fname]["nevents"],"k","T")
    if args.totals: results[fname]["actual"] = convert_bytes(totals[fname],"","T")
    results[fname]["correction"] = tests[fname]["correction"] if not args.update else results[fname]["actual"]/results[fname]["projection"]
    results[fname]["corrected"] = results[fname]["correction"]*results[fname]["projection"]

# compute "other" as the remainder
if args.totals:
    results["other"]["actual"] = convert_bytes(totals["overall"],"","T") - sum(results[fname]["actual"] for fname in fnames)
    results["other"]["correction"] = 1.0
    results["other"]["corrected"] = results["other"]["actual"]

# print table
headers = ["Sample"] + [col+(" [{}B]".format(units[ic]) if len(units[ic])>0 else "") for ic,col in enumerate(columns)]
table_rows = [[fname] + [form.format(result[col]) for col,form in zip(columns,formats)] for fname, result in results.iteritems()]

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
    for test in tests_orig:
        tests_orig[test]["correction"] = results[test]["correction"]
    if len(args.output)==0: args.output = args.sizetest
    with open(args.output,'w') as ofile:
        ofile.write(pprintOD(tests_orig,"tests"))
