from collections import OrderedDict
import json

def get_sizetest(name="sizetest.py"):
    tests = __import__(name.replace(".py","")).tests
    tests = OrderedDict(tests)

    for fname,test in tests.iteritems():
        if "dname" not in test:
            tests[fname]["dname"] = fname.lower()

    return tests

def pprintOD(obj,name,complete=False):
    is_dict = isinstance(obj,dict)
    if complete and is_dict:
        print "from collections import OrderedDict\n"
    prefix = "OrderedDict([" if is_dict else "["
    suffix = "])" if is_dict else "]"
    # a not-very-extensible hack for stable pretty-print of ordered dict
    print "{} = {}".format(name,prefix)
    for key,val in obj.iteritems() if is_dict else obj:
        print '    ("{}", {}),'.format(key, json.dumps(val, sort_keys=True))
    print suffix

def get_xrdfs():
    from XRootD import client
    from XRootD.client.flags import DirListFlags

    redirector = "root://cmseos.fnal.gov//"
    xrdfs = client.FileSystem(redirector)

    return xrdfs, DirListFlags
