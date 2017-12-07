from jobSubmitterTM import *

# todo: integrate getResults functionality into missing mode (and add new "results" mode?)

class jobSubmitterNeff(jobSubmitterTM):
    def __init__(self):
        super(jobSubmitterNeff,self).__init__()
        
        self.scripts = ["step1.sh","step2Neff.sh"]

    def addExtraOptions(self,parser):
        super(jobSubmitterNeff,self).addExtraOptions(parser)
        
        self.removeOptions(parser,"-d","--dicts","-o","--output","--json","--cpus")
        self.cpus = 1
        
        parser.add_option("-d", "--dict", dest="dict", default="neff", help="input dict, prefixed by dict_ and list of samples (default = %default)")
        
    def checkExtraOptions(self,options,parser):
        jobSubmitter.checkExtraOptions(self,options,parser)
    
        if options.dict is None or len(options.dict)==0:
            parser.error("Required option: --dict [dict]")
            
    def generateExtra(self,job):
        super(jobSubmitterNeff,self).generateExtra(job)
        job.patterns["EXTRAINPUTS"] = "input/argsNeff_"+job.name+"_$(Process).txt"
        
    def generateSubmission(self):
        # get entries
        process = self.dict.replace(".py","")
        flist = __import__("dict_"+process).flist

        # loop over entries
        for input in flist:
            filesConfig = input
            
            # fix malformed options
            if filesConfig[-7:]=="_cff.py":
                filesConfig = filesConfig[:-7]
            elif filesConfig[-4:]=="_cff":
                filesConfig = filesConfig[:-4]

            # verify specified options
            if self.verbose:
                print "nFiles: ",self.nFiles
                print "filesConfig: ",filesConfig
                print "submit: ",self.submit

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

            if self.verbose:
                print "I will create "+str(nJobs)+" jobs for you!"

            # create protojob
            job = protoJob()
            job.name = filesConfig
            self.generatePerJob(job)
                
            # start loop over N jobs
            nActualJobs = 0
            for iJob in range( nJobs ) :
                # get starting file number
                nstart = iJob*int(self.nFiles)
                
                job.njobs += 1
                if self.count and not self.prepare:
                    continue

                job.nums.append(iJob)
                
                # just keep list of jobs
                if self.missing and not self.prepare:
                    continue
                    
                # write job options to file - will be transferred with job
                if self.prepare:
                    jname = job.makeName(job.nums[-1])
                    with open("input/argsNeff_"+jname+".txt",'w') as argfile:
                        args = (self.args+" " if len(self.args)>0 else "")+"name="+filesConfig+" nstart="+str(nstart)+" nfiles="+str(self.nFiles)
                        argfile.write(args)

            # append queue comment
            job.queue = "-queue "+str(job.njobs)
            
            # store protojob
            self.protoJobs.append(job)

    def finishedToJobName(self,val):
        pass

    def generateJdl(self,job):
        job.jdl = self.jdl.replace(".jdl","Neff_"+job.name+".jdl")
