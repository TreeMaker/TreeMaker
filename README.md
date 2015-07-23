# TreeMaker

## Instructions

The following installation instructions assume the user wants to process Run2015B prompt-reco data or Spring15 MC.

```
cmsrel CMSSW_7_4_6_patch6
cd CMSSW_7_4_6_patch6/src/
cmsenv
git clone https://github.com/TreeMaker/TreeMaker.git -b Run2
scram b -j 8
cd TreeMaker/TreeMaker/test/
```

To run on data:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=GR_P_V56::All geninfo=False tagname="RECO" dataset="/store/data/Run2015B/..."
```

To run on data with a JSON file (when running interactively or on Condor), there is an extra argument:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=GR_P_V56::All geninfo=False tagname="RECO" dataset="/store/data/Run2015B/..." jsonfile="runs.json"
```

To run on Spring15 MC:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py globaltag=MCRUN2_74_V9::All geninfo=True tagname="PAT" dataset="/store/mc/..."
```

If the user instead wants to process Phys14 MC, the CMSSW version `CMSSW_7_2_3_patch1` should be used for the installation:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py globaltag=PHYS14_25_V2::All geninfo=True tagname="PAT" dataset="/store/mc/..."
```

## Options

Brief explanation of the options in [makeTreeFromMiniAOD_cff.py](./TreeMaker/python/makeTreeFromMiniAOD_cff.py)
* `outfile`: name of the ROOT output file that will be created by the TFileService.
* `reportfreq`: frequency of CMSSW log output (default=10)
* `dataset`: name of the miniAOD input file(s)
* `globaltag`: global tag for CMSSW database conditions (ref. [FrontierConditions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions))
* `numevents`: number of input events to process, -1 processes all events (default=1000)
* `tagname`: tag name for collections that can have different tags for data or MC (default="PAT")
* `geninfo`: switch to enable use of generator information, should only be used for MC (default=True)
* `jsonfile`: name of JSON file to apply to data
* `applyjec`: switch to apply new JECs from a database file (default=False)
* `debugtracks`: store information for all PF candidates in every event (default=False) (use with caution, increases run time and output size by ~10x)
* `applybaseline`: switch to apply the baseline HT selection (default=False)
* `tagandprobe`: switch to enable the tag and probe processes, disables MT cut on isolated tracks (default=False)
* `lostlepton`: switch to enable the lost lepton background estimation processes (default=False)
* `hadtau`: switch to enable the hadronic tau background estimation processes (default=False)
* `doZinv`: switch to enable the Z->invisible background estimation processes (default=False)
