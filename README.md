# TreeMaker

## Instructions

The following installation instructions assume the user wants to process Run2015B prompt-reco data or Spring15 MC.

```
cmsrel CMSSW_7_4_6_patch6
cd CMSSW_7_4_6_patch6/src/
cmsenv
git cms-merge-topic -u cms-met:METCorUnc74X
git clone git@github.com:TreeMaker/TreeMaker.git -b Run2
scram b -j 8
cd TreeMaker/Production/test
```

If instead `CMSSW_7_5_1` is used, a different MET branch should be merged: `cms-met:METCorTool75X-071515`.

Several predefined scenarios are available for ease of production.
These scenarios define various sample-dependent parameters, including:  
global tag, collection tag name, generator info, JSON file, JEC file, residual JECs, era.  
The available scenarios are:  
1. `Spring15`: for Spring15 25ns MC  
2. `Spring15Fast`: for Spring15 25ns FastSim MC (signal scans)
3. `2015B`: for 2015B PromptReco 50ns data  
4. `re2015B`: for 2015B re-miniAOD 50ns data  
5. `2015C`: for 2015C PromptReco 25ns data  
6. `2015D`: for 2015D PromptReco 25ns data  
7. `Phys14`: for Phys14 25ns MC (deprecated)  

## Interactive Runs

To run interactively:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py \
scenario=2015B \
dataset="/store/data/Run2015B/..." \
outfile="test"
```

Note that all of the background estimation processes are turned *ON* by default in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py).

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
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction
```

The jobs open the files over xrootd, so [looper.sh](./Production/test/condorSub/looper.sh) will check that you have a valid grid proxy. 
It will also make a tarball of the current CMSSW working directory to send to the worker node. 
If you want to reuse an existing CMSSW tarball (no important changes have been made since the last time you submitted jobs), there is an extra argument:
```
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction keep
```

Because of the large number of events in the Spring15 MC, there are now a number of looper_*.sh scripts for signal, data, and various background categories.

Sometimes, a few jobs might fail, e.g. due to xrootd connectivity problems. The script [resubCondor.sh](./Production/test/condorSub/resubCondor.sh) can identify the failed jobs and prepare them for resubmission by checking the Condor logs.
```
./resubCondor.sh "YYYY-MM-DD HH:MM" myResub.sh
./myResub.sh
```
The first parameter, if used, tells the script to look at only the jobs which finished after the specified starting date/time (default=beginning of time, "1970-01-01 00:00"). The second parameter, if used, specifies the name of the output resubmission script (default="resub.sh"). The existing JDL files are resubmitted by the resubmission script. If the script finds a failed job, it automatically checks to see if any newer instances of that job were successful (to account for multiple rounds of job submission from the same production folder).

## Calculate Integrated Luminosity

Scripts are available to calculate the integrated luminosity from data ntuples (produced with TreeMaker):
```
python lumiSummary.py
```

The script [lumiSummary.py](./Production/test/lumiSummary.py) loops over a list of data samples (by default, a list of Run2015B PromptReco samples) and creates a JSON
file for each sample consisting of the lumisections which were actually processed. (This script is based on
the CRAB3 client job report scripts.) The resulting JSON file can be run through [brilcalc](http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html)
to determine the integrated luminosity for the dataset.

## Info for New Samples

The script [get_py.py](./Production/test/get_py.py) will automatically download the "_cff.py" python file containing the list of ROOT files for samples specified in a Python ordered dictionary, e.g. [dict.py](./Production/test/dict.py) (disabled with `py=False`).
For MC samples, it can also automatically generate the appropriate configuration line to add the sample to [getWeightProducer_cff.py](./WeightProducer/python/getWeightProducer_cff.py), if the cross section is specified (disabled with `wp=False`).
```
python get_py.py dict=dict.py
```

To check for new samples, consult [production monitoring](https://dmytro.web.cern.ch/dmytro/cmsprodmon/requests.php?campaign=RunIISpring15DR74) or query DAS (in this case, for Spring15 MC):
```
das_client.py --query="dataset=/*/RunIISpring15DR74-Asympt25ns*/MINIAODSIM" --limit=0 | & less
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
* `QCD`: switch to enable the QCD LowDeltaPhi background estimation processes (default=False)
* `doPDFs`: switch to enable the production of PDF weights for NNPDF3.0, CT10, MMHT2014, n.b. you need to do `scram setup lhapdf` before running (default=False)
* `tagandprobe`: switch to enable the tag and probe processes, disables MT cut on isolated tracks (default=False)
* `debugtracks`: store information for all PF candidates in every event (default=False) (use with caution, increases run time and output size by ~10x)
* `applybaseline`: switch to apply the baseline HT selection (default=False)
* `gridcontrol`: switch to apply special settings for CRAB submission (default=False)
* `globaltag`: global tag for CMSSW database conditions (ref. [FrontierConditions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions))
* `tagname`: tag name for collections that can have different tags for data or MC (default="PAT")
* `geninfo`: switch to enable use of generator information, should only be used for MC (default=True)
* `fastsim`: switch to enable special settings for SUSY signal scans produced wit FastSim (default=False)
* `jsonfile`: name of JSON file to apply to data
* `jecfile`: name of a database file from which to get JECs (default="")
* `residual`: switch to enable residual JECs for data (default=False)

Extra options in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py):
* `inputFilesConfig`: name of the python file with a list of ROOT files for a sample, used for Condor production (default="", automatically appended with "_cff.py")
* `scenarioName`: name of the scenario for the sample, as described above (default="")
* `era`: CMS detector era for the dataset (default=Run2_50ns)

