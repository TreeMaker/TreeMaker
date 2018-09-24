import sys, os
from optparse import OptionParser

# define options
parser = OptionParser()
parser.add_option("-d", "--dir", dest="dir", default="", help="directory to search (LFN)")
parser.add_option("-g", "--grep", dest="grep", default="", help="string to grep in file list")
parser.add_option("-x", "--xrdir", dest="xrdir", default="root://cmseos.fnal.gov/", help="xrootd storage element location (default = %default)")
parser.add_option("-r", "--remove", dest="remove", default="block,part,fast", help="comma-separated list of strings to remove when finding sample names (default = %default)")
(options, args) = parser.parse_args()

if options.xrdir[-1] != '/':
    options.xrdir += '/'
rmlist = options.remove.split(',')

fileArray = filter(None,os.popen("xrdfs "+options.xrdir+" ls "+options.dir+" | grep \""+options.grep+"\"").read().split('\n'))

#basename
fileArray = [ f.split("/")[-1] for f in fileArray]

#find sample names
fileArray = [ "_".join(f.split("_")[:-( sum([r in f for r in rmlist]) )]) for f in fileArray ]

#find unique samples
fileSet = set(fileArray)

print("\n".join(sorted(fileSet)))
