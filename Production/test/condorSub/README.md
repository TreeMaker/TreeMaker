# Production planning

The application `prodPlanner.py` provides several functions to assist with ntuple production planning.

## Size test definition

The file `sizetest.py` categorizes the major samples (MC backgrounds and primary datasets) 
and provides some associated information for each category:
* correction factor (based on comparing a size test to a full production)
* dictionary name (optional, in case the dictionary name does not correspond to the category name)
* sample (to use for [size test jobs](#size-test-jobs))
* type (data or MC)

Alternate versions of this file can be created manually or automatically (see below).

## Size test jobs

As an input to the [size projections](#size-projections), size test jobs should be run.

The following arguments can be supplied to `submitJobs.py`, along with whatever commands are normally used for production:
```
--mask sizetest.py --maxJobs 1 -d $(ls dict*.py | sed 's/dict_//; s/.py//' | tr '\n' ',' | sed 's/,$//')
```

The files for each size test should be output into their own specific directory, rather than the full ntuple production directory.

## Aggregate info

The aggregate information used in the [size projections](#size-projections) includes:
* number of events for each MC background category
* number of events for each primary dataset category
* actual size of existing ntuples (if available)

This info can be refreshed by calling:
```
python prodPlanner.py refresh
```

Options are available to restrict the refresh operation to only some of the above pieces of information  or to specify non-default names for the output files.

This is a separate function because this information does not need to be updated often (only when samples are changed/updated or a new ntuple production is done).

## Size projections

The aggregate and size test info can be combined into a projection table by calling:
```
python prodPlanner.py project -s sizetest.py ...
```

Important arguments:
* `-d, --dir [dir(s)]`: these are the location(s) of size tests, in order of priority. Multiple directories can be specified in case of variations in size tests that only affect a subset of categories.
* `-a, --actualAll` or `-A, --actualOther`: enables the use of the actual size of the full ntuple production, either for a full comparison or just to get the size of the "other" category (whatever small samples are not covered by the major categories in `sizetest.py`).
* `-u, --update`: update the correction factors, either in-place or by making a new file (controlled by `-o, --output [name]`).

Other options are available to specify non-default input names.

The output is a table with these columns:
```
         Sample  sizeEvt [kB]     nevents  projection [TB]  actual [TB]  correction  corrected [TB]
---------------------------------------------------------------------------------------------------
```

If `-a` is not used, the column "actual [TB]" will be omitted.
