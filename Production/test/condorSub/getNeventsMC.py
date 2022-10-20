from glob import glob
from collections import OrderedDict

from TreeMaker.WeightProducer.MCSamples_Summer20UL16APV import Summer20UL16APVsamples
from TreeMaker.WeightProducer.MCSamples_Summer20UL16 import Summer20UL16samples
from TreeMaker.WeightProducer.MCSamples_Summer20UL17 import Summer20UL17samples
from TreeMaker.WeightProducer.MCSamples_Summer20UL18 import Summer20UL18samples

from utils import get_sizetest, pprintOD

tests = get_sizetest()

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
                    if not found: print "WARNING: no entry found for {}".format(f)
        output[fname][fullyear] = outsum

pprintOD(output,"neventsMC",True)
