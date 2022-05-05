#!/bin/env python3

import os
import re

def beginList(output_file):
    output_file.write("dataSamples = [\n")

def endList(output_file):
    output_file.write("]\n")

def beginSection(output_file, era, period):
    output_file.write(f"    # {era} datasets: {period}\n")

def writeDir(output_file, basepath, dir, era, period):
    files = os.listdir(basepath + dir)
    files = [file for file in files if "_cff.py" in file and os.path.splitext(file)[1] == ".py"]

    match = re.search("[a-zA-Z]20[0-9]{2}(.*)", period)
    special_period = ""
    if match is not None:
        special_period = match.group(1)

    for file in files:
        match = re.search("(.*?(?=_cff.py))",file)
        pd = match.group(1)
        dataset = f"\"{pd}_{era}{special_period}\","
        path = f"\"{dir}.{pd}_*\""
        output_file.write(f"    [ {dataset : <30}{path}],\n")

def makeDataSampleFiles():
    cmssw_base = os.environ["CMSSW_BASE"]
    basepath = f"{cmssw_base}/src/TreeMaker/Production/python/"
    directories = os.listdir(basepath)
    directories = [dir for dir in directories if os.path.isdir(basepath + dir) and "Run20" in dir]
    directories_dict = {}
    for dir in directories:
        match = re.search("Run(20[0-9]{2})[A-Z]",dir)
        year = match.group(1)
        match = re.search("Run(20[0-9]{2}[A-Z])",dir)
        era = match.group(1)
        if year not in directories_dict:
            directories_dict[year] = {era : [dir]}
        elif era not in directories_dict[year]:
            directories_dict[year][era] = [dir]
        else:
            directories_dict[year][era].append(dir)

    for year, eras in directories_dict.items():
        output_filename = f"dataSamples_Run{year}_UL{year}.py"
        with open(output_filename, "w") as output_file:
            beginList(output_file)
            for era, dirs in eras.items():
                last_period = False
                for dir in dirs:
                    match = re.search("(UL20[0-9]{2}.*?(?=-))",dir)
                    period = match.group(1)
                    if period != last_period:
                        beginSection(output_file, era, period)
                        last_period = period
                    writeDir(output_file, basepath, dir, era, period)
            endList(output_file)

if __name__ == '__main__':
    makeDataSampleFiles()

