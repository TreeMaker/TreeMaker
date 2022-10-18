# TreeMaker

<!-- MarkdownTOC levels="2,3" autolink="true" -->

- [Instructions](#instructions)
- [Unit Tests \(Interactive Runs\)](#unit-tests-interactive-runs)
- [Submit Production to Condor](#submit-production-to-condor)
- [Calculate Integrated Luminosity](#calculate-integrated-luminosity)
- [Calculate Pileup Corrections](#calculate-pileup-corrections)
- [Info for New Samples](#info-for-new-samples)
    - [Samples with Negative Weight Events](#samples-with-negative-weight-events)
- [Options](#options)
- [Notes for Contributors](#notes-for-contributors)
    - [Docker](#docker)

<!-- /MarkdownTOC -->

## Instructions

The following installation instructions assume the user wants to process Run 2 ultra-legacy (UL) miniAOD.

```
wget https://raw.githubusercontent.com/TreeMaker/TreeMaker/Run2_UL/setup.sh
chmod +x setup.sh
./setup.sh
cd CMSSW_10_6_29_patch1/src/
cmsenv
cd TreeMaker/Production/test
```

The script [setup.sh](./setup.sh) has options to allow installing a different fork or branch of TreeMaker
(though some branches may have different setup scripts, so check carefully which one you download):
* `-f [fork]`: which fork to download (`git@github.com:fork/TreeMaker.git`, default = TreeMaker)
* `-b [branch]`: which branch to download (`-b branch`, default = Run2_UL)
* `-B`: configure some settings for checkout within batch setups
* `-c [version]`: which CMSSW version to use (default = CMSSW_10_6_29_patch1)
* `-a [protocol]`: which protocol to use for `git clone` (default = ssh, alternative = https)
* `-j [cores]`: run CMSSW compilation on # cores (default = 8)
* `-n [name]`: name of the CMSSW directory if not CMSSW_X_Y_Z (default = CMSSW_10_6_29_patch1)
* `-d [dir]`: project installation area for the CMSSW directory (default = ${PWD})
* `-D`: print additional debug statements (default = false)
* `-h`: display help message and exit

Several predefined scenarios are available for ease of production.
These scenarios define various sample-dependent parameters, including:  
global tag, collection tag name, generator info, fastsim, signal, JSON file, JEC file, residual JECs, era.  
The available scenarios are:  
1.  `Summer16`: for Summer16 miniAOD MC (80X)
2.  `Summer16sig`: for Summer16 miniAOD MC (80X) (signal)
3.  `Summer16v3`: for Summer16 miniAODv3 MC
4.  `Summer16v3sig`: for Summer16 miniAODv3 MC (signal)
5.  `Summer16v3sigscan`: for Summer16 miniAODv3 MC with multiple mass points(signal)
6.  `Summer16v3Fast`: for Summer16 miniAODv3 FastSim MC (background)  
7.  `Summer16v3Fastsig`: for Summer16 miniAODv3 FastSim MC (signal)  
8.  `2016ReReco17Jul`: for 2016 miniAODv3 data (17Jul2018), periods B-H  
9.  `Fall17`: for Fall17 miniAOD MC
10. `Fall17sig`: for Fall17 miniAOD MC (signal)
11. `Fall17sigscan`: for Fall17 miniAOD MC with multiple mass points (signal)
12. `Fall17Fast`: for Fall17 miniAOD FastSim MC (background)
13. `Fall17Fastsig`: for Fall17 miniAOD FastSim MC (signal)
14. `2017ReReco31Mar`: for 2017 ReReco data (31Mar), periods B-F
15. `Autumn18`: for Autumn18 miniAOD MC (102X)
16. `Autumn18sig`: for Autumn18 miniAOD MC (102X) (signal)
17. `Autumn18sigscan`: for Autumn18 miniAOD MC with multiple mass points (102X) (signal)
18. `Autumn18Fast`: for Autumn18 miniAOD FastSim MC (background)
19. `Autumn18Fastsig`: for Autumn18 miniAOD FastSim MC (signal)
20. `2018B26Sep`: for 2018 prompt data, partial period B
21. `2018B26SepHEM`: for 2018 prompt data, partial period B, with the HEM 15/16 issue
22. `2018PromptReco`: for 2018 prompt data (or 22Jan2019, produced w/ prompt conditions), run period D
23. `2018ReReco17Sep`: for 17Sep2018 rereco data, periods A, B, and C

## Unit Tests (Interactive Runs)

Several predefined run commands (at least one for each scenario) are defined in a script called [unitTest.py](./Production/test/unitTest.py). It has several parameters:
* `test`: number of the test to run (default=-1, displays all tests)
* `name`: name of the output ROOT and log files for the test (default="", each test has its own default name)
* `run`: run the selected test (default=False)
* `numevents`: how many events to run (default=100)

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

## Submit Production to Condor

Condor submission is supported for the LPC batch system or for the global pool via [CMS Connect](https://connect.uscms.org/).
Job submission and management is based on the [CondorProduction](https://github.com/kpedro88/CondorProduction) package.
Refer to the package documentation for basic details.

The [test/condorSub](./Production/test/condorSub/) directory contains all of the relevant scripts.
If you make a copy of this directory and run the [submitJobs.py](./Production/test/condorSub/submitJobs.py) script, it will submit one job per file to Condor for all of the relevant samples. Example:
```
./lnbatch.sh myProduction
cd myProduction
python submitJobs.py -p -o root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction -s
```
[submitJobs.py](./Production/test/condorSub/submitJobs.py) can also:
* count the expected number of jobs to submit (for planning purposes),
* check for jobs which were completely removed from the queue and make a resubmission list.

The class [jobSubmitterTM.py](./Production/test/condorSub/jobSubmitterTM.py) extends the class `jobSubmitter` from [CondorProduction](https://github.com/kpedro88/CondorProduction). It adds a few extra arguments:

Python:
* `-d, --dicts [list]`: comma-separated list of input dicts; each prefixed by dict_ and contains scenario + list of samples (default taken from [.prodconfig](./Production/test/condorSub/.prodconfig))
* `-o, --output [dir]`: path to output directory in which root files will be stored (required)
* `-J, --json [jsonfile]`: manually specified json file to check data (override scenario)
* `-N, --nFiles [num]`: number of files to process per job
* `-A, --args [list]`: additional common args to use for all jobs (passed to [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py))
* `-v, --verbose`: enable verbose output (default = False)
* `-x, --redir`: input file redirector
* `-f, --use-folders`: store the output in folders based on era and dataset (default = False)
* `-i, --ignore-args`: ignore args specified in the input dict (default = False)
* `--offset [num]`: offset for arg file naming in chain jobs (default = 0)
* `--maxJobs [num]`: max number of jobs to run (default = -1 -> not applied)

Shell (in [step2.sh](./Production/test/condorSub/step2.sh)):
* `-o [dir]`: output directory
* `-j [jobname]`: job name
* `-p [process]`: process number
* `-x [redir]`: xrootd redirector

When the python file list for a given sample (usually data) is updated, it may be desirable to submit jobs only for the new files.
The input dictionary format for [jobSubmitterTM.py](./Production/test/condorSub/jobSubmitterTM.py) optionally allows a (non-zero) starting number to be placed after the sample name.
To get the number of the first new job, just use `len(readFiles)` from the python file list *before* updating it.

When submitting jobs for prompt data, each data file will be checked to see if the run it contains is certified in the corresponding JSON file. The JSON file is taken by default from the scenario; an alternative can be specified with the `--json` option, e.g. if the JSON is updated and you want to submit jobs only for the newly certified runs. (Use [compareJSON.py](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/FWCore/PythonUtilities/scripts/compareJSON.py) to subtract one JSON list from another, following [this twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGoodLumiSectionsJSONFile#How_to_compare_Good_Luminosity_f).)

## Calculate Integrated Luminosity

Scripts are available to calculate the integrated luminosity from data ntuples (produced with TreeMaker):
```
python lumiSummary.py
python calcLumi.py
```

The script [lumiSummary.py](./Production/test/lumiSummary.py) loops over a list of data samples (by default, a list of Run2015C and Run2015D samples) and creates a JSON
file for each sample consisting of the lumisections which were actually processed. Run `python lumiSummary.py --help` to see the available options.
(This script is based on the CRAB3 client job report scripts.)

The resulting JSON file can be run through [brilcalc](http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html) using [calcLumi.py](./Production/test/calcLumi.py)
to determine the integrated luminosity for the dataset. Run `python calcLumi.py --help` to see the available options. (NB: this only works on lxplus with brilcalc installed.)

## Calculate Pileup Corrections

A script is available to calculate the pileup corrections for MC:
```
python pileupCorr.py
```

A ROOT file containing the data, MC, and data/MC histograms (with uncertainty variations) is produced. Run `python pileupCorr.py --help` to see the available options.

## Info for New Samples

The script [get_mcm.py](./Production/python/get_mcm.py) can search the McM database for given samples (with wildcard support) to discern the status of the sample (whether it has finished running), the generator cross section, and the full dataset path for the sample ("/X/Y/Z" format).
Command line options exist to specify campaign names and other information, which can be viewed with the `--help` option.
An example dictionary of samples and extensions to check can be found at [dict_mcm.py](./Production/test/dict_mcm.py).
This script requires [cern-get-sso-cookie](http://linux.web.cern.ch/linux/docs/cernssocookie.shtml) to access the McM database, which is installed on lxplus and cmslpc.
Kerberos-based access is used by default, but certificate-based access is also available.
Kerberos access requires a ticket for CERN.CH, and currently only works on lxplus. To configure your certificate for access, see the "User certificates" section of the [cern-get-sso-cookie](http://linux.web.cern.ch/linux/docs/cernssocookie.shtml) documentation.
The same arguments `--cert` and `--key` can be used with the `get_mcm.py` script.

The script [get_py.py](./Production/python/get_py.py) will automatically create the "_cff.py" python file containing the list of ROOT files for samples specified in a Python ordered dictionary, e.g. [dict.py](./Production/test/dict.py) (enabled with `-p`).
For MC samples, it can also automatically generate the appropriate configuration line to add the sample to [getWeightProducer_cff.py](./WeightProducer/python/getWeightProducer_cff.py). This is enabled with the `-w` option and is used for MC samples only.
The script can also check to see which sites (if any) have 100% dataset presence for the sample (enabled with `-s`).
(You may also need `export SSL_CERT_DIR='/etc/pki/tls/certs:/etc/grid-security/certificates'` (bash) or `setenv SSL_CERT_DIR '/etc/pki/tls/certs:/etc/grid-security/certificates'` (tcsh) to avoid the error `SSL: CERTIFICATE_VERIFY_FAILED` from `urllib2`.)

To run the script:
```
python get_py.py -d dict.py [options]
```

To check for new samples, use the above script [get_mcm.py](./Production/test/get_mcm.py) or query DAS, e.g.:
```
dasgoclient -query="dataset=/*/RunIISpring16MiniAOD*/MINIAODSIM"
```

A convenient config to compute cross sections using the official GenXSecAnalyzer tool is provided, and can be used as follows:
```
cmsRun xsecfinder_cfg.py name=Autumn18.TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8_ext1 numevents=1e7
```

For samples generated with MadGraph, the LHE header can be dumped, including the PDF weight definitions:
```
cmsRun pdffinder_cfg.py name=Autumn18.TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8_ext1
```

In both configs, an alternate xrootd redirector can be specified with the `redir` argument (default value: `root://cmsxrootd.fnal.gov/`).
A site name (such as T1_US_FNAL) can also be provided, in which case the config will attempt to read the files
from only the specified site using the [SAM access test](https://twiki.cern.ch/twiki/bin/view/Main/XrootdMonitoring#Access_test) method.

### Samples with Negative Weight Events

Samples produced at NLO by amcatnlo have events with negative weights, which must be handled correctly. To get the effective number of events used to weight the sample, there is a multi-step process. This process also produces a histogram of `TrueNumInteractions` for pileup reweighting.

Step 1: Get the "_cff.py" files, without generating WeightProducer lines (assuming samples are listed in `dictNLO.py`).
```
python get_py.py dict=dictNLO.py wp=False
```

Step 2: Run NeffFinder, a simple analyzer which calculates the effective number of events for a sample.
The output is a histogram with four bins, containing: 1. neff (pos-neg), 2. pos, 3. neg, 4. tot (pos+neg).
The analyzer should be submitted as a Condor batch job for each sample (assuming samples are listed in [dict_neff.py](./Production/test/condorSub/dict_neff.py)), because the xrootd I/O bottleneck is prohibitive when running interactively.
The last step, using the `-g` mode, gets and prints the Neff results for each sample from the output histogram.
```
./lnbatch.sh myNeff
cd myNeff
python submitJobsNeff.py -p -d neff -N 50 -o root://cmseos.fnal.gov//store/user/YOURUSERNAME/myNeff
(after jobs are finished)
./haddEOS.sh -d /store/user/YOURUSERNAME/myNeff -g _part -r
python submitJobsNeff.py -g -d neff -N 50 -o root://cmseos.fnal.gov//store/user/YOURUSERNAME/myNeff
```

Step 3: Update `dictNLO.py` with the newly-obtained Neff values and generate WeightProducer lines. Combine all pileup distributions into a single file.
```
cd $CMSSW_BASE/src/TreeMaker/Production/test/myNeff
./haddWrongPU.sh -L /store/user/YOURUSERNAME/myNeff
cd $CMSSW_BASE/src/TreeMaker/Production/python
python get_py.py dict=dictNLO.py py=False
```

## Options

Brief explanation of the options in [maker.py](./TreeMaker/python/maker.py)
* `scenario`: the scenario name, in case of special requirements (default="")
* `inputFilesConfig`: name of the python file with a list of ROOT files for a sample, used for Condor production (automatically appended with "_cff") (default="")
* `nstart`: first file to use in above file list (default=0)
* `nfiles`: number of files to use in above file list, -1 includes all files (default=-1)
* `dataset`: direct list of input files (alternative to above 3 parameters) (default=[])
* `numevents`: number of input events to process, -1 processes all events (default=-1)
* `outfile`: name of the ROOT output file that will be created by the TFileService (appended with `outfilesuff` below) (default="test_run")
* `outfilesuff`: suffix to append to `outfile` above (default="_RA2AnalysisTree")
* `treename`: name of output ROOT TTree (default="PreSelection")
* `lostlepton`: switch to enable the lost lepton background estimation processes (default=True)
* `hadtau`: switch to enable the hadronic tau background estimation processes (storing soft jets and reclustering) (default=False)
* `hadtaurecluster`: switch to enable the hadronic tau reclustering to include jets with pT < 10 GeV, options: 0 = never, 1 = only TTJets/WJets MC, 2 = all MC, 3 = always (default=0)
* `doZinv`: switch to enable the Z->invisible background estimation processes (default=False)
* `doPhotons`: switch to ensure photon variables are stored, implied with `doZinv` (default=True)
* `systematics`: switch to enable JEC- and JER-related systematics (default=True)
* `semivisible`: switch to enable variables for semi-visible jets (default=True)
* `boostedsemivisible`: switch to enable variables for boosted semi-visible jets, i.e. AK15 jets (default=False)
* `emerging`: switch to enable variables for emerging jets (default=False)
* `tchannel`: switch to enable additional variables for t-channel semi-visible jets (default=False)
* `deepAK8`: switch to enable variables from the DeepAK8 tagger (default=True)
* `deepDoubleB`: switch to enable variables from the DeepDoubleB tagger (default=True)
* `doQG`: switch to enable quark/gluon tagging variables for AK4 jets, AK8 jets, AK8 subjets (default=True)  
* `addPileupId`: include pileupJetId discriminator for AK4 jets (default=True)
* `doPDFs`: switch to enable the storage of PDF weights and scale variation weights from LHEEventInfo (default=True)  
  The scale variations stored are: [mur=1, muf=1], [mur=1, muf=2], [mur=1, muf=0.5], [mur=2, muf=1], [mur=2, muf=2], [mur=2, muf=0.5], [mur=0.5, muf=1], [mur=0.5, muf=2], [mur=0.5, muf=0.5]
* `debugtracks`: store information for all PF candidates in every event (default=False) (use with caution, increases run time and output size by ~10x)
* `debugtap`: store extra information for the TAP collections (default=False)
* `debugsubjets`: store some additional information for the AK8 subjets (default=False)
* `applybaseline`: switch to apply the baseline HT selection (default=False)
* `saveMinimalGenParticles`: save only the hard scatter gen particles coming from top decays, boson decays, semi-visible jets, or SUSY particles (default=True)
* `saveGenTops`: save the 4-vectors of the generated tops and the TTbar reweighting scale factor (default=False)
* `doMT2`: switch to enable the storage of the MT2 variable (default=False)
* `jetsconstituents`: store all constituents from all (AK8 and AK15 by default) jet collections; each jet collection gets an index branch into the single vector of all constituents; options: 0 = don't store, 1 = store 4-vector and PDG ID, 2 = also store other properties, 3 = also store for AK4 collection (default=0)
* `nestedVectors`: switch to change from saving `vector<vector<T>>` to saving `vector<T>` values and `vector<int>` counts (default=False)
* `storeOffsets`: if set to True, stores offsets rather than counts when using `nestedVectors=False` (default=False)
* `splitLevel`: split level for output TBranches (default=99)
* `saveFloat`: convert doubles to floats in output (default=True)
* `includeBranches`: write out only the specified list of branches, which can be provided as a comma-separated list or a text file (filename ending in `.txt`). This option uses regular expressions by default (see below). To match a branch name exactly when regex is enabled, surround it in `^$`, e.g. `^Jets$`.
* `excludeBranches`: write out only branches that do not match the specified list. This option is exclusive with the option `includeBranches` (only one can be used). See above for details.
* `exactBranches`: disables regex for above branch control commands

The following parameters take their default values from the specified scenario:
* `globaltag`: global tag for CMSSW database conditions (ref. [FrontierConditions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions))
* `tagname`: tag name for collections that can have different tags for data or MC
* `geninfo`: switch to enable use of generator information, should only be used for MC
* `fastsim`: switch to enable special settings for SUSY signal scans produced with FastSim
* `scan`: switch to enable special settings for scans produced with FullSim
* `signal`: switch to enable assessment of signal systematics (currently unused)
* `jsonfile`: name of JSON file to apply to data
* `jecfile`: name of a database file from which to get JECs
* `jerfile`: name of a database file from which to get JERs
* `residual`: switch to enable residual JECs for data
* `pufile`: name of a ROOT file from which to get pileup weights
* `wrongpufile`: name of a ROOT file from which to get per-sample pileup distributions (for Fall17 samples produced w/ wrong PU)
* `era`: CMS detector era for the dataset
* `redir`: xrootd redirector, storage element address, or site name (default="root://cmsxrootd.fnal.gov/") (`fastsim` default="root://cmseos.fnal.gov/")
* `verbose`: print messages from modules in the `TreeMaker` category (and from JetToolbox) (default=True)

Extra options in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py):
* `reportfreq`: frequency of CMSSW log output (default=1000)
* `dump`: equivalent to `edmConfigDump`, but accounts for all command-line settings; exits without running (default=False)
* `mp`: enable igprof hooks for memory profiling (default=False)
* `threads`: run in multithreaded mode w/ specified number of threads (default=1)
* `streams`: run w/ specified number of streams (default=0 -> streams=threads)
* `tmi`: enable [TimeMemoryInfo](https://github.com/cms-sw/cmssw/blob/master/Validation/Performance/python/TimeMemoryInfo.py) for simple profiling (default=False)
* `trace`: enable the tracer for debugging (default=False)
* `debugjets`: print out user floats and discriminators for each jet collection (default=False)

## Notes for Contributors

### Docker

Two Docker images containing the TreeMaker software will be created upon push or pull request to the default TreeMaker branch. For more information about these images see the [TreeMaker wiki](https://github.com/TreeMaker/TreeMaker/wiki/Docker%20Integration%20Test).

In order to cancel or limit these builds one can add the following strings to their commit message:
* `[skip build]`: neither image will be created
* `[skip test]`: the no-cache image will be created, but the image containing the CVMFS cache will be skipped
