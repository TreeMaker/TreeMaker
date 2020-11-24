#! /usr/bin/env python

import os
import argparse
import json
import sys
from collections import defaultdict

def rm_hlt_version(name):
    version_start = name.rfind("_v")
    if version_start == -1: 
        return name
    else:
        return name[:version_start+2]

def get_pathname_from_ps_tbl(entry):
    hlt_path = entry.split()[0]
    return rm_hlt_version(hlt_path)

def get_hlt_prescales(ps_tbl,path_table,run):
    counter = 0
    for line in ps_tbl:
        # skip first line (header)
        if counter==0:
            counter += 1
            continue
        # skip emergency at beginning, circulating beam & L1 seeds at end
        prescales = [int(ps) for ps in line[3:-2]]
        psval = min(prescales)
        if psval!=0: psval = max(prescales)
        path_table[get_pathname_from_ps_tbl(line[1])][run] = psval

def get_l1_prescales(l1_ps_tbl,path_table):
    counter = 0
    for line in l1_ps_tbl:
        # skip first line (header)
        if counter==0:
            counter += 1
            continue
        prescales = [int(ps) for ps in line[2:]]
        psval = min(prescales)
        if psval!=0: psval = max(prescales)
        path_table[line[1]][run] = psval

def find_period(run,period_info):
    if len(period_info)==0: return ""
    run = int(run)
    for period,pruns in period_info.iteritems():
        if run >= pruns[0] and run <= pruns[1]:
            return period
    return ""
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
splits a given good lumi json into prescaled and unprescaled components

Dependencies:
=============
Make sure to download the run info, L1 prescales, and HLT prescale trigger data from https://twiki.cern.ch/twiki/bin/viewauth/CMS/HLTStandAlonePrescaleInformation.

There are three tarballs, one for each year:
2016: https://twiki.cern.ch/twiki/pub/CMS/HLTStandAlonePrescaleInformation/triggerData2016.tgz
2017: https://twiki.cern.ch/twiki/pub/CMS/HLTStandAlonePrescaleInformation/triggerData2017.tgz
2018: https://twiki.cern.ch/twiki/pub/CMS/HLTStandAlonePrescaleInformation/triggerData2018.tgz

Despite having the extension .tgz, these are plain, non-gzipped tarballs. You can extract them by doing:
$ tar -xf <filename>

Examples:
=========
python getPrescaledStatusOfPaths.py --run_info triggerData2016_runInfo.json --ps_data triggerData2016_hltprescales.json --grl data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt --isHLT --suffix 2016
python getPrescaledStatusOfPaths.py --run_info triggerData2017_runInfo.json --ps_data triggerData2017_hltprescales.json --grl data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt --isHLT --suffix 2017
python getPrescaledStatusOfPaths.py --run_info hltData2018_runInfo.json --ps_data hltData2018_hltprescales.json --grl data/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt --isHLT --suffix 2018

or:

python getPrescaledStatusOfPaths.py --run_info triggerData2016_runInfo.json --period_info data/period_info_2016.json --ps_data triggerData2016_hltprescales.json --grl data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt --isHLT --suffix 2016_periods
python getPrescaledStatusOfPaths.py --run_info triggerData2017_runInfo.json --period_info data/period_info_2017.json --ps_data triggerData2017_hltprescales.json --grl data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt --isHLT --suffix 2017_periods
python getPrescaledStatusOfPaths.py --run_info hltData2018_runInfo.json --period_info data/period_info_2018.json --ps_data hltData2018_hltprescales.json --grl data/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt --isHLT --suffix 2018_periods
    """,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--period_info',required=False,help='period info json')
    parser.add_argument('--run_info',required=True,help='run info json')
    parser.add_argument('--ps_data',required=True,help='prescale data json') 
    parser.add_argument('--grl',required=True,help='good run list to split')
    parser.add_argument('--suffix',required=True,help='suffix for output files')
    parser.add_argument('--filter',required=False,nargs='+',help='a list of paths or keywords to filter on')
    group_trig = parser.add_mutually_exclusive_group(required=True)
    group_trig.add_argument('--isHLT',action='store_true',help="is a HLT path we are investigating")
    group_trig.add_argument('--isL1',action='store_true',help="is a L1 seed we are investigating")
    args = parser.parse_args()

    #first load all the jsons
    good_lumis = {}
    with open(args.grl) as f:
        good_lumis = json.load(f)

    all_runs_info = {}
    with open(args.run_info) as f:
        all_runs_info = json.load(f)
        
    ps_data = {}
    with open(args.ps_data) as f:
        ps_data = json.load(f)
        
    period_info = {}
    if args.period_info is not None and len(args.period_info)>0:
        with open(args.period_info) as f:
            period_info = json.load(f)

    runs = good_lumis.keys()
    runs.sort()
    
    path_table = defaultdict(dict)

    run_lumis_unprescaled = {}
    run_lumis_prescaled = {}
    
    for run in runs:
        run_info = all_runs_info[run]
        ps_tbl_key = ""
        if args.isHLT:
            ps_tbl_key = run_info["hlt_menu"] #HLT key
        else:
            ps_tbl_key = run_info["trig_mode"] #L1 key
        
        ps_tbl = ps_data[ps_tbl_key]
        
        if args.isHLT:
            get_hlt_prescales(ps_tbl,path_table,run)
        else:
            get_l1_prescales(ps_tbl,path_table,run)
            
    # now loop again to fill in missing runs
    for run in runs:
        for path in path_table:
            if not run in path_table[path].keys():
                path_table[path][run] = 0

    # filter the list of paths
    path_table = {key: value for (key, value) in path_table.items() if any(p in key for p in args.filter)}

    # make a summary
    with open('unprescaled_'+args.suffix+'.txt','w') as unprescaled, open('prescaled_'+args.suffix+'.txt','w') as prescaled:
        for path in sorted(path_table.keys()):
            missing_runs = []
            prescaled_runs = []
            unprescaled_runs = []
            missing_periods = set()
            prescaled_periods = set()
            unprescaled_periods = set()
            for run in path_table[path]:
                prescale = path_table[path][run]
                if prescale==0:
                    missing_runs.append(int(run))
                    missing_periods.add(find_period(run,period_info))
                elif prescale!=1:
                    prescaled_runs.append(int(run))
                    prescaled_periods.add(find_period(run,period_info))
                else:
                    unprescaled_runs.append(int(run))
                    unprescaled_periods.add(find_period(run,period_info))
            if len(missing_runs)==0 and len(prescaled_runs)==0:
                unprescaled.write(path+"\n")
            else:
                prescaled.write(path+"\n")
                if len(period_info)>0:
                    # use periods instead of runs
                    missing_runs = list(missing_periods)
                    prescaled_runs = list(prescaled_periods)
                    unprescaled_runs = list(unprescaled_periods)
                s_missing_runs = "all" if len(missing_runs)==len(runs) else ','.join([str(x) for x in sorted(missing_runs)]) if len(missing_runs)>0 else ""
                s_prescaled_runs = "all" if len(prescaled_runs)==len(runs) else ','.join([str(x) for x in sorted(prescaled_runs)]) if len(prescaled_runs)>0 else ""
                s_unprescaled_runs = ','.join([str(x) for x in sorted(unprescaled_runs)]) if len(unprescaled_runs)>0 else ""
                if len(s_missing_runs)>0:     prescaled.write("\t    missing runs: "+s_missing_runs+"\n")
                if len(s_prescaled_runs)>0:   prescaled.write("\t  prescaled runs: "+s_prescaled_runs+"\n")
                if len(s_unprescaled_runs)>0: prescaled.write("\tunprescaled runs: "+s_unprescaled_runs+"\n")

    print "done"
    
