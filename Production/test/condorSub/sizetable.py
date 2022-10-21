import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import OrderedDict
from utils import get_xrdfs, get_sizetest, pprintOD
from getActuals import getActuals

def convert_bytes(val, current, new, base=1000):
    expo = {"": 0, "k": 1, "M": 2, "G": 3, "T": 4, "P": 5, "E": 6, "Z": 7, "Y": 8}
    for prefix in [current,new]:
        if prefix not in expo:
            raise ValueError("Unknown unit {}".format(prefix))
    return float(val)/(base**(expo[new]-expo[current]))

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--sizetest", dest="sizetest", type=str, help="input sizetest .py file", required=True)
parser.add_argument("-d", "--testdirs", dest="testdirs", type=str, nargs='+', help="test file directory(s) in priority order", required=True)
# todo: add "refresh" option for nevents & actuals
parser.add_argument("-u", "--update", dest="update", default=False, action="store_true", help="update corrections and sizetest .py file")
parser.add_argument("-o", "--output", dest="output", default="", type=str, help="output sizetest .py file name (if updating and different from input)")
parser.add_argument("-a", "--actuals", dest="actuals", default=False, action="store_true", help="use actuals.py")
parser.add_argument("-A", "--actualsOther", dest="actualsOther", default=False, action="store_true", help='use actuals.py just for "other" category')
args = parser.parse_args()

# todo: make everything configurable... and/or merge into one application
from neventsMC import neventsMC
from neventsData import neventsData
from utils import get_sizetest, pprintOD
if args.actuals or args.actualsOther:
    from actuals import actuals
else:
    actuals = None

tests = get_sizetest(args.sizetest)
fnames = [fname for fname in tests]
columns = ["sizeEvt", "nevents", "projection", "correction", "corrected"]
units = ["k", "", "T", "", "T"]
formats = ["{:.2f}", "{:d}", "{:.2f}", "{:.2f}", "{:.2f}"]
if args.actuals:
    columns.insert(3, "actual")
    units.insert(3, "T")
    formats.insert(3, "{:.2f}")
results = OrderedDict([(fname,{col: 0 for col in columns}) for fname in fnames+(["other"] if args.actuals or args.actualsOther else [])+["total"]])

# get sizes from size test
xrdfs, flags = get_xrdfs()
for tdir in args.testdirs:
    # prioritize: remove tests if already filled from previous dir
    temp = getActuals(tdir, [fname for fname in fnames if results[fname]["sizeEvt"]==0], per_event=True)
    for fname, val in temp.iteritems():
        results[fname]["sizeEvt"] = convert_bytes(temp[fname],"","k")

# continue to fill results
for fname in fnames:
    neventsDict = neventsMC if tests[fname]["type"]=="MC" else neventsData
    results[fname]["nevents"] = sum([count for year,count in neventsDict[fname].iteritems()])
    results[fname]["projection"] = convert_bytes(results[fname]["sizeEvt"]*results[fname]["nevents"],"k","T")
    if args.actuals: results[fname]["actual"] = convert_bytes(actuals[fname],"","T")
    results[fname]["correction"] = tests[fname]["correction"] if not args.update else results[fname]["actual"]/results[fname]["projection"]
    results[fname]["corrected"] = results[fname]["correction"]*results[fname]["projection"]

# compute "other" as the remainder
if args.actuals or args.actualsOther:
    results["other"]["sizeEvt"] = ""
    results["other"]["nevents"] = ""
    other_actual = convert_bytes(actuals["overall"],"","T") - sum(convert_bytes(actuals[fname],"","T") for fname in fnames)
    if args.actuals: results["other"]["actual"] = other_actual
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
    with open(args.output,'w') as ofile:
        orig_stdout = sys.stdout
        # redirect print to file
        sys.stdout = ofile
        pprintOD(tests_orig,"tests")
        sys.stdout = orig_stdout
