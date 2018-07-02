#!/usr/bin/env python
import argparse
import TreeMaker.Production.get_py as get_py

'''
Example of how to run:
python run_get_py.py -d dict_Run2017B-31Mar2018-v1.py dict_Run2017C-31Mar2018-v1.py dict_Run2017D-31Mar2018-v1.py dict_Run2017E-31Mar2018-v1.py dict_Run2017F-31Mar2018-v1.py \
 -o ../python/Run2017B-31Mar2018-v1/ ../python/Run2017C-31Mar2018-v1/ ../python/Run2017D-31Mar2018-v1/ ../python/Run2017E-31Mar2018-v1/ ../python/Run2017F-31Mar2018-v1/ -p -s
'''

# Read parameters
parser = argparse.ArgumentParser(description='Run get_py.py for multiple input dictionaries and output folders. You can also place any arguments you want passed to get_py.py here.')
parser.add_argument("-d",   "--dicts",          nargs='+',                default="[]",   help="check for samples listed in these dicts (default = %default)")
parser.add_argument("-o",   "--output-folders", nargs='+',                default="[./]", help="put the output files in the specified folders (default = %default)")
args, unknown = parser.parse_known_args()

dicts   = args.dicts
folders = args.output_folders

if len(dicts)!=len(folders):
	if len(folders)==1:
		print "Warning: There was only one output folder specified, but multiple input dictionaries. All output will go to the same folder, but some files may be overwritten by multiple runs of get_py.py\n"
		folders = [folders[0] for i in range(0,len(dicts))]
	else:
		parser.error("There is a mismatch in the number of dictionaries and output folders! You either need equal numbers or multiple dictionaries and one output folder.")

for idict, dict in enumerate(args.dicts):
	tmpargs = ["-d",dict,"-o",folders[idict]]
	tmpargs += unknown
	get_py.main(tmpargs)
