from Condor.Production.jobSubmitter import *
import bisect
from FWCore.PythonUtilities.LumiList import LumiList
from TreeMaker.Production.scenarios import Scenario

class jobSubmitterTM(jobSubmitter):
    def initStep1(self):
        # skip this for count mode
        if not self.count:
            super(jobSubmitterTM,self).initStep1()

    def addExtraOptions(self,parser):
        super(jobSubmitterTM,self).addExtraOptions(parser)
        
        parser.add_option("-d", "--dicts", dest="dicts", type="string", action="callback", callback=list_callback, default=parser_dict["submit"]["input"].split(','),
            help="comma-separated list of input dicts; each prefixed by dict_ and contains scenario + list of samples (default = %default)")
        parser.add_option("-o", "--output", dest="output", default="", help="path to output directory in which root files will be stored (required) (default = %default)")
        parser.add_option("-J", "--json", dest="json", default="", help="manually specified json file to check data (override scenario) (default = %default)")
        parser.add_option("-N", "--nFiles", dest="nFiles", default=1, help="number of files to process per job (default = %default)")
        parser.add_option("-A", "--args", dest="args", default="", help="additional common args to use for all jobs (default = %default)")
        parser.add_option("-v", "--verbose", dest="verbose", default=False, action="store_true", help="enable verbose output (default = %default)")
        parser.add_option("-x", "--redir", dest="redir", default="", help="input file redirector (default = %default)")
        parser.add_option("-f", "--use-folders", dest="useFolders", default=False, action="store_true", help="store the output in folders based on era and dataset (default = %default)")
        parser.add_option("-i", "--ignore-args", dest="ignoreArgs", default=False, action="store_true", help="ignore args specified in the input dict (default = %default)")
        parser.add_option("--maxJobs", dest="maxJobs", default=-1, type="int", help="Max number of jobs to run")
        parser.add_option("--offset", dest="offset", default=0, type="int", help="offset for arg file naming in chain jobs (default = %default)")
        parser.add_option("--mask", dest="mask", default="", type="str", help=".py file in sizetest format to select specific samples from larger dicts (default = %default)")

    def checkExtraOptions(self,options,parser):
        super(jobSubmitterTM,self).checkExtraOptions(options,parser)
    
        if options.dicts is None or len(options.dicts)==0:
            parser.error("Required option: --dicts [dict]")
            
        if len(options.output)==0 and (options.prepare or not options.count):
            parser.error("Required option: --output [directory]")
            
    def generateExtra(self,job):
        super(jobSubmitterTM,self).generateExtra(job)
        job.patterns.update([
            ("JOBNAME",job.name+"_$(Process)_$(Cluster)"),
            ("EXTRAINPUTS","input/args_"+job.name+"_$(Process).txt"),
            ("EXTRAARGS","-j "+job.name+" -p $(Process) -o "+self.output+(" -x "+self.redir if len(self.redir)>0 else "")+(" -f " if self.useFolders else "")),
        ])
        if "cmslpc" in os.uname()[1]:
            job.appends.append(
                'ONE_DAY = 86400\n'
                'periodic_hold = (\\\n'
                '    ( JobUniverse == 5 && JobStatus == 2 && CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 1.75 ) || \\\n'
                '    ( JobRunCount > 8 ) || \\\n'
                '    ( JobStatus == 5 && CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 6 ) || \\\n'
                '    ( DiskUsage > 38000000 ) || \\\n'
                '    ( ifthenelse(ResidentSetSize isnt undefined, ResidentSetSize > RequestMemory * 950, false) ) )\n'
                'periodic_hold_reason = strcat("Job held by PERIODIC_HOLD due to ", \\\n'
                '    ifThenElse(( JobUniverse == 5 && JobStatus == 2 && CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 1.75 ), "runtime longer than 1.75 days", \\\n'
                '    ifThenElse(( JobRunCount > 8 ), "JobRunCount greater than 8", \\\n'
                '    ifThenElse(( JobStatus == 5 && CurrentTime - EnteredCurrentStatus > $(ONE_DAY) * 6 ), "hold time longer than 6 days", \\\n'
                '    ifThenElse(( DiskUsage > 38000000 ), "disk usage greater than 38GB", \\\n'
                '                strcat("memory usage ",ResidentSetSize," greater than requested ",RequestMemory*1000))))), ".")'
            )
        
    def generateSubmission(self):
        # check mask
        mask = set()
        if len(self.mask)>0:
            tests = __import__(self.mask.replace(".py","")).tests
            mask = set([test["sample"] for fname,test in tests])

        # loop over dicts
        for input in self.dicts:
            # loop over dict entries
            process = input.replace(".py","")
            flist = __import__("dict_"+process).flist
            # args can be specified like scenario in dict
            # args specified on the command line appended to dict args (so command line overrides dict)
            dictArgs = self.args[:]
            if not self.ignoreArgs and "args" in flist:
                dictArgs = " ".join([x for x in [flist["args"],dictArgs] if len(x)>0])
            scenarioName = flist["scenario"]
            scenario = Scenario(scenarioName)
            data = not scenario.geninfo
            
            if data and self.json=="":
                # get from scenario
                # data directory is next to condor directory
                self.json = scenario.jsonfile
            if data and self.json=="":
                raise Exception, "data was specified, but no json file was found"

            # loop over samples
            for file in flist["samples"]:
                filesConfig = file[0]

                # apply mask if any
                if len(mask)>0:
                    if filesConfig not in mask:
                        continue
                    elif self.verbose:
                        print "passed mask: "+filesConfig+" from "+process

                firstJob = 0
                # extra optional field for updating data
                if len(file)>1: firstJob = file[1]
                
                # fix malformed options
                if filesConfig[-7:]=="_cff.py":
                    filesConfig = filesConfig[:-7]
                elif filesConfig[-4:]=="_cff":
                    filesConfig = filesConfig[:-4]

                # verify specified options
                if self.verbose:
                    print "nFiles: ",self.nFiles
                    print "filesConfig: ",filesConfig
                    print "scenario: ",scenarioName
                    print "submit: ",self.submit
                    print "firstJob: ",firstJob
                    if data: print "json: ",self.json
                    
                # for data, get the (sorted) list of good runs from the json
                runlist = []
                if data:
                    runlist = LumiList(self.json).getRuns()

                # grab full file list from config files
                readFiles = getattr(__import__("TreeMaker.Production."+filesConfig+"_cff",fromlist=["readFiles"]),"readFiles")

                # to keep track of how many data files have been divied up
                fileListLen = len(readFiles)

                if self.verbose: print "There are "+str(fileListLen)+" files in your sample"

                # calculate the number of jobs necessary
                if self.nFiles==-1:
                    nJobs = 1
                else:
                    nJobs = fileListLen / int( self.nFiles )
                    if ( fileListLen % int( self.nFiles ) != 0 ) :
                        nJobs += 1

                if self.maxJobs >= 0:
                    if self.verbose: print "Limiting to max {0} jobs".format(self.maxJobs)
                    nJobs = min([nJobs, self.maxJobs])

                netJobs = nJobs - int(firstJob)
                if self.verbose:
                    print "I will create "+str(netJobs)+" jobs for you!"
                    if firstJob>0: print "(starting from job "+str(firstJob)+")"

                # create protojob
                job = protoJob()
                job.name = filesConfig
                self.generatePerJob(job)
                    
                # start loop over N jobs
                nActualJobs = 0
                discontinuousJobs = (firstJob>0)
                for iJob in range( int(firstJob), nJobs ) :
                    # get starting file number
                    nstart = iJob*int(self.nFiles)

                    # skipping data files with bad runs only works with nFiles==1 right now
                    if data and int(self.nFiles)==1:
                        # check if this file's run is in the list of good runs
                        readFileSplit = readFiles[iJob].split('/')
                        # some filenames don't have the run in them
                        if len(readFileSplit)==12:
                            discontinuousJobs = True
                            readFileRun = readFileSplit[8]+readFileSplit[9]
                            i = bisect.bisect_left(runlist,readFileRun)
                            # skip this file if the run was not found
                            if i==len(runlist) or runlist[i]!=readFileRun:
                                if self.verbose: print "skipping run "+readFileRun
                                continue
                    
                    job.njobs += 1
                    if self.count and not self.prepare:
                        continue

                    job.nums.append(iJob)
                    
                    # just keep list of jobs
                    if self.missing and not self.prepare:
                        continue
                        
                    # write job options to file - will be transferred with job
                    if self.prepare:
                        jname = job.makeName(job.nums[-1]+self.offset)
                        with open("input/args_"+jname+".txt",'w') as argfile:
                            args = "outfile="+jname+" inputFilesConfig="+filesConfig+" nstart="+str(nstart)+" nfiles="+str(self.nFiles)+" scenario="+scenarioName
                            if len(dictArgs)>0: args = args+" "+dictArgs
                            argfile.write(args)

                # append queue comment
                job.queue = "-queue "+str(job.njobs)
                if discontinuousJobs: job.queue = "-queue Process in "+','.join(map(str,job.nums))

                if self.verbose and data: print "("+str(job.njobs)+" actual jobs)"
                
                # store protojob
                self.protoJobs.append(job)

    def findFolderizedJobs(self,job):
        if not hasattr(self,"checkedDirectories"):
            setattr(self,"checkedDirectories",set())

        if hasattr(self,"output"):
            bottomDir = self.output + "/" + job.name.replace('.','/')
            if bottomDir not in self.checkedDirectories:
                finishedFilesPerJob = pyxrdfsls(bottomDir,self.minDate,self.maxDate)
                finishedFilesPerJobSplit = [finished.split('/') for finished in finishedFilesPerJob]
                finishedFilesPerJob = ['.'.join(finished[-3:-1]) + "_" + finished[-1].replace("_RA2AnalysisTree.root","") for finished in finishedFilesPerJobSplit]
                self.filesSet |= set(finishedFilesPerJob)
                self.checkedDirectories.add(bottomDir)

    def doMissing(self,job):
        # add to finished files in case the files are folderized
        if self.useFolders:
            self.findFolderizedJobs(job)

        # now do the rest of missing mode
        super(jobSubmitterTM,self).doMissing(job)

    def doClean(self,job):
        # add to finished files in case the files are folderized
        if self.useFolders:
            self.findFolderizedJobs(job)

        # now do the rest of clean mode
        super(jobSubmitterTM,self).doClean(job)

    def finishedToJobName(self,val):
        return val.split("/")[-1].replace("_RA2AnalysisTree.root","")

