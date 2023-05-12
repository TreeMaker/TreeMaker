from jobSubmitterTM import *
from TreeMaker.Production.tm_common import printGetPyDictHeader
import difflib, pprint

class jobSubmitterNeff(jobSubmitterTM):
    def __init__(self):
        super(jobSubmitterNeff,self).__init__()
        
        self.scripts = ["step1.sh","step2Neff.sh"]
        self.outf = None
        self.flist = []
        self.flist_indices = {}

    def addDefaultOptions(self,parser):
        super(jobSubmitterNeff,self).addDefaultOptions(parser)
        parser.add_option("-g", "--getresults", dest="getresults", default=False, action="store_true", help="get neff results (default = %default)")
        parser.add_option("-U", "--updatedict", dest="updatedict", default="", help="name of the get_py dict to update with the neff results (default = %default)")
        parser.add_option("-S", "--suffix", dest = "suffix", default="_neff", help="the suffix to append to the modified get_py dictionary if updatedict is set (default = %default)")
        self.modes.update({
            "getresults": 1,
        })

    def addExtraOptions(self,parser):
        super(jobSubmitterNeff,self).addExtraOptions(parser)
        
        self.removeOptions(parser,"-d","--dicts","--json","--cpus")
        self.cpus = 1
        
        parser.add_option("-d", "--dict", dest="dict", default="neff", help="input dict, prefixed by dict_ and list of samples (default = %default)")
        
    def checkExtraOptions(self,options,parser):
        jobSubmitter.checkExtraOptions(self,options,parser)

        if options.dict is None or len(options.dict)==0:
            parser.error("Required option: --dict [dict]")

    def initRun(self):
        super(jobSubmitterNeff,self).initRun()

        # generate a new dictionary if updatedict is set
        if self.getresults and self.updatedict!="":
            idict = self.updatedict
            odict = idict[:idict.find(".py")]+self.suffix+idict[idict.find(".py"):]
            self.outf = open(odict,'w')
            printGetPyDictHeader(self.outf)
            sys.path.insert(0,os.path.abspath(os.path.dirname(idict)))
            dictname = os.path.basename(idict.replace(".py",""))
            self.flist = __import__(dictname).flist
            # prefill the dictionary with zeros for the neff values and update them sample-by-sample
            for ifitem, fitem in enumerate(self.flist):
                nsamples = len(fitem[1])
                fitem[2] = [0 for i in range(nsamples)]
                for idataset, dataset in enumerate(fitem[1]):
                    dataset_split = dataset.split('/')
                    dname = dataset_split[1] + "" if "_ext" not in dataset_split[2] else dataset_split[2][dataset_split[2].find("_ext"):].split('-')[0]
                    self.flist_indices[dname] = [ifitem,idataset]

    def runPerJob(self,job):
        super(jobSubmitterNeff,self).runPerJob(job)
        if self.getresults:
            self.doResults(job)

    def finishRun(self):
        super(jobSubmitterNeff,self).finishRun()

        if self.getresults and self.updatedict!="":
            self.outf.write(" "+pprint.pformat(self.flist,indent=4,depth=3,width=max([len(str(f)) for f in self.flist])+6)[1:-1]+",\n]\n")
            self.outf.close()

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

            # to keep track of how many data files have been divvied up
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
                        args = (self.args+" " if len(self.args)>0 else "")+"name="+filesConfig+" nstart="+str(nstart)+" nfiles="+str(self.nFiles)+(" part="+str(job.nums[-1]) if nJobs>1 else "")
                        argfile.write(args)

            # append queue comment
            job.queue = "-queue "+str(job.njobs)
            
            # store protojob
            self.protoJobs.append(job)

    def finishedToJobName(self,val):
        tmp = val.split("/")[-1].replace("NeffInfo_","").replace(".root","")
        # handle case where there is no part number because only one job
        if "_part" in tmp: tmp = tmp.replace("_part","_")
        else: tmp = tmp+"_0"
        return tmp

    def generateJdl(self,job):
        job.jdl = self.jdl.replace(".jdl","Neff_"+job.name+".jdl")

    def doResults(self,job):
        from ROOT import TFile, TH1
        jfile = TFile.Open(self.output+"/NeffInfo_"+job.name+".root")
        jhist = jfile.Get("NeffFinder/NeffInfo_"+job.name)
        print("NeffFinder: "+job.name+" : "+str(int(jhist.GetBinContent(1)))+" (pos = "+str(int(jhist.GetBinContent(2)))+", neg = "+str(int(jhist.GetBinContent(3)))+", tot = "+str(int(jhist.GetBinContent(4)))+")")

        
        # update the neff value for the current sample
        if self.updatedict!="":
            samplename = job.name.split('.')[1]
            if samplename not in self.flist_indices:
                print "WARNING: Unable to update the neff value for",job.name,"as no match was found in the input dictionary"
                return
            else:
                flist_index = self.flist_indices[samplename][0]
                dataset_index = self.flist_indices[samplename][1]
                self.flist[flist_index][2][dataset_index] = int(jhist.GetBinContent(1))