from collections import OrderedDict
import json

def get_sizetest(name="sizetest.py"):
    tests = __import__(name.replace(".py","")).tests
    tests = OrderedDict(tests)

    for fname,test in tests.iteritems():
        if "dname" not in test:
            tests[fname]["dname"] = fname.lower()

    return tests

def pprintOD(obj,name):
    # a not-very-extensible hack for stable pretty-print of ordered dict
    print "{} = OrderedDict([".format(name)
    for key,val in obj.iteritems() if isinstance(obj,dict) else obj:
        print '    ("{}", {}),'.format(key, json.dumps(val, sort_keys=True))
    print "])"

def get_xrdfs():
    from XRootD import client
    from XRootD.client.flags import DirListFlags

    redirector = "root://cmseos.fnal.gov//"
    xrdfs = client.FileSystem(redirector)

    return xrdfs, DirListFlags
