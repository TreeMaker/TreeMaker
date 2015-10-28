#To submit jobs:

Before submitting jobs, run [cache_all.sh](../cache_all.sh) to prevent unnecessary directories from being included in the CMSSW tarball.

Use [generateSubmission.py](./generateSubmission.py) to automatically generate bash scripts and condor configs for submission. To see the available options:
```
python generateSubmission.py --help
```

The `looper*.sh` scripts show how to use [generateSubmission.py](./generateSubmission.py) for different samples and scenarios.

See the main [README](../../../README.md) for more information.

#Useful condor commands:
* `condor_q -submitter <username>`
* `condor_tail <jobID>`
* `condor_userprio`
* `condor_rm <jobID>`

