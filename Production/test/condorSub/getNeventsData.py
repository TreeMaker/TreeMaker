from glob import glob
from collections import OrderedDict
import subprocess, shlex

from utils import get_sizetest, pprintOD

tests = get_sizetest()

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
                        print "WARNING: command failed: {}".format(cmd)
        output[fname][year] = outsum

pprintOD(output,"neventsData",True)
