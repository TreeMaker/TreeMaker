# TreeMaker

## Instructions

The following installation instructions assume the user wants to process Run2015 data or Spring15 MC (miniAOD v2 format).

```
cmsrel CMSSW_7_4_15
cd CMSSW_7_4_15/src/
cmsenv
git cms-merge-topic -u kpedro88:METfix7415
git clone git@github.com:TreeMaker/TreeMaker.git -b Run2
scram b -j 8
cd TreeMaker/Production/test
```

Several predefined scenarios are available for ease of production.
These scenarios define various sample-dependent parameters, including:  
global tag, collection tag name, generator info, fastsim, signal, JSON file, JEC file, residual JECs, era.  
The available scenarios are:  
1. `Spring15v2`: for Spring15 re-miniAOD (v2) 25ns MC  
2. `Spring15v2sig`: for Spring15 re-miniAOD (v2) 25ns MC (signal)  
3. `Spring15Fastv2`: for Spring15 re-miniAOD (v2) 25ns FastSim MC
4. `Spring15Fastv2sig`: for Spring15 re-miniAOD (v2) 25ns FastSim MC (signal scans)  
5. `re2015C`: for 2015C re-reco 25ns data  
6. `re2015D`: for 2015D re-miniAOD (v2) 2015D 25ns data (part 1)  
7. `2015Db`: for 2015D PromptReco 25ns data (part 2)  

## Unit Tests (Interactive Runs)

Several predefined run commands (at least one for each scenario) are defined in a script called [unitTest.py](./Production/test/unitTest.py). It has several parameters:
* `test`: number of the test to run (default=-1, displays all tests)
* `name`: name of the output ROOT and log files for the test (default="", each test has its own default name)
* `run`: run the selected test (default=False)
* `numevents`: how many events to run (default=100)
* `shell`: how to format the command (default="tcsh", also knows "bash")

A few examples of how to run the script:  
1) To see all tests:
```
python unitTest.py
```
2) To run test 2:
```
python unitTest.py test=2 run=True
```

Note that all of the background estimation processes (and some processes necessary to estimate systematic uncertainties) are turned *ON* by default in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py).

## Submit Production to Condor (@ LPC)

To reduce the size of the CMSSW tarball sent to the Condor worker node, there are a few standard directories that can be marked as cached using the script [cache_all.sh](./Production/test/cache_all.sh):
```
./cache_all.sh
```

The [test/condorSub](./Production/test/condorSub/) directory contains all of the relevant scripts.
If you copy this to another directory and run the [looper.sh](./Production/test/condorSub/looper.sh) script, it will submit one job per file to condor for all of the relevant samples. Example:
```
cp -r condorSub myProduction
cd myProduction
./looper.sh -d root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction
```

The jobs open the files over xrootd, so [looper.sh](./Production/test/condorSub/looper.sh) will check that you have a valid grid proxy. 
It will also make a tarball of the current CMSSW working directory to send to the worker node. 
If you want to reuse an existing CMSSW tarball (no important changes have been made since the last time you submitted jobs), add the argument `-k`.

When the python file list for a given sample is updated, it may be desirable to submit jobs only for the new files. [looper_data_update.sh](./Production/test/condorSub/looper_data_update.sh) shows an example of how to do this.
To get the number of the first new job, just use `len(readFiles)` from the python file list *before* updating it.

If the `-d` flag is used with [generateSubmission.py](./Production/test/condorSub/generateSubmission.py) when submitting jobs, each data file will be checked to see if the run it contains is certified in the corresponding JSON file. The JSON file is taken by default from the scenario; an alternative can be specified with the `--json` option, e.g. if the JSON is updated and you want to submit jobs only for the newly certified runs. (Use [compareJSON.py](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/FWCore/PythonUtilities/scripts/compareJSON.py) to subtract one JSON list from another, following [this twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGoodLumiSectionsJSONFile#How_to_compare_Good_Luminosity_f).)

Because of the large number of events in the Spring15 MC, there are now a number of looper_*.sh scripts for signal, data, and various background categories.

Sometimes, a few jobs might fail, e.g. due to xrootd connectivity problems. The script [resubCondor.sh](./Production/test/condorSub/resubCondor.sh) can identify the failed jobs and prepare them for resubmission by checking the Condor logs.
The existing JDL files are listed for resubmission in the output script. If the script finds a failed job, it automatically checks to see if any newer instances of that job were successful (to account for multiple rounds of job submission from the same production folder).
```
./resubCondor.sh -t "YYYY-MM-DD HH:MM" -o myResub.sh
./myResub.sh
```

These are the parameters for the script:
* `-o` : output script name, default = "resub.sh"
* `-t` : search for logs modified after this time (in specified format)
* `-f` : search for logs modified after this file
* if neither `-t` nor `-f` is given, all logs will be searched

## Calculate Integrated Luminosity

Scripts are available to calculate the integrated luminosity from data ntuples (produced with TreeMaker):
```
python lumiSummary.py
python calcLumi.py
```

The script [lumiSummary.py](./Production/test/lumiSummary.py) loops over a list of data samples (by default, a list of Run2015C and Run2015D samples) and creates a JSON
file for each sample consisting of the lumisections which were actually processed. Run `python lumiSummaryTest.py --help` to see the available options.
(This script is based on the CRAB3 client job report scripts.)

The resulting JSON file can be run through [brilcalc](http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html) using [calcLumi.py](./Production/test/calcLumi.py)
to determine the integrated luminosity for the dataset. (NB: this only works on lxplus with brilcalc installed.)

## Info for New Samples

The script [get_py.py](./Production/test/get_py.py) will automatically create the "_cff.py" python file containing the list of ROOT files for samples specified in a Python ordered dictionary, e.g. [dict.py](./Production/test/dict.py) (disabled with `py=False`).
For MC samples, it can also automatically generate the appropriate configuration line to add the sample to [getWeightProducer_cff.py](./WeightProducer/python/getWeightProducer_cff.py), if the cross section is specified (disabled with `wp=False`).

Before running the script for the first time, some environment settings are necessary:
```
source /cvmfs/cms.cern.ch/crab3/crab_gcc493.csh
```

To run the script:
```
python get_py.py dict=dict.py
```

To check for new samples, consult [production monitoring](https://dmytro.web.cern.ch/dmytro/cmsprodmon/requests.php?campaign=RunIISpring15MiniAODv2) or query DAS (in this case, for Spring15 MC):
```
das_client.py --query="dataset=/*/RunIISpring15MiniAODv2*/MINIAODSIM" --limit=0 | & less
```

### Samples with Negative Weight Events

Samples produced at NLO by amcatnlo have events with negative weights, which must be handled correctly. To get the effective number of events used to weight the sample, there is a multi-step process.

Step 1: Get the "_cff.py" files, without generating WeightProducer lines (assuming samples are listed in `dictNLO.py`).
```
python get_py.py dict=dictNLO.py wp=False
```

Step 2: Run NeffFinder, a simple analyzer which calculates the effective number of events for a sample.
The analyzer should be submitted as a Condor batch job for each sample (assuming samples are listed in [looperNeff.sh](./Production/test/condorSubNeff/looperNeff.sh)), because the xrootd I/O bottleneck is prohibitive when running interactively.
Be sure to sanity-check the results, as xrootd failures can cause jobs to terminate early.
```
cp -r condorSubNeff myNeff
cd myNeff
./looperNeff.sh
(after jobs are finished)
./getFailures.sh
./removeFailures.sh
./getResults.sh
```
(The script [./removeFailures.sh](./Production/test/condorSubNeff/removeFailures.sh) renames the output files from the failed jobs so they do not get picked up by [./getResults.sh](./Production/test/condorSubNeff/getResults.sh).)

Step 3: Update `dictNLO.py` with the newly-obtained Neff values and generate WeightProducer lines.
```
python get_py.py dict=dictNLO.py py=False
```

## Options

Brief explanation of the options in [makeTreeFromMiniAOD_cff.py](./TreeMaker/python/makeTreeFromMiniAOD_cff.py)
* `dataset`: name of the miniAOD input file(s)
* `numevents`: number of input events to process, -1 processes all events (default=1000)
* `reportfreq`: frequency of CMSSW log output (default=10)
* `outfile`: name of the ROOT output file that will be created by the TFileService (automatically appended with "_RA2AnalysisTree.root" when passed from [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py))
* `lostlepton`: switch to enable the lost lepton background estimation processes (default=False)
* `hadtau`: switch to enable the hadronic tau background estimation processes (default=False)
* `doZinv`: switch to enable the Z->invisible background estimation processes (default=False)
* `doPDFs`: switch to enable the storage of PDF weights and scale variation weights from LHEEventInfo (default=False)  
  The scale variations stored are: [mur=1, muf=1], [mur=1, muf=2], [mur=1, muf=0.5], [mur=2, muf=1], [mur=2, muf=2], [mur=2, muf=0.5], [mur=0.5, muf=1], [mur=0.5, muf=2], [mur=0.5, muf=0.5]
* `tagandprobe`: switch to enable the tag and probe processes, disables MT cut on isolated tracks (default=False)
* `debugtracks`: store information for all PF candidates in every event (default=False) (use with caution, increases run time and output size by ~10x)
* `applybaseline`: switch to apply the baseline HT selection (default=False)
* `gridcontrol`: switch to apply special settings for CRAB submission (default=False)
* `globaltag`: global tag for CMSSW database conditions (ref. [FrontierConditions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions))
* `tagname`: tag name for collections that can have different tags for data or MC (default="PAT")
* `geninfo`: switch to enable use of generator information, should only be used for MC (default=True)
* `fastsim`: switch to enable special settings for SUSY signal scans produced with FastSim (default=False)
* `signal`: switch to enable assessment of signal systematics (default=False) (currently unused)
* `jsonfile`: name of JSON file to apply to data
* `jecfile`: name of a database file from which to get JECs (default="")
* `residual`: switch to enable residual JECs for data (default=False)

Extra options in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py):
* `inputFilesConfig`: name of the python file with a list of ROOT files for a sample, used for Condor production (default="", automatically appended with "_cff.py")
* `scenarioName`: name of the scenario for the sample, as described above (default="")
* `era`: CMS detector era for the dataset (default=Run2_50ns)

