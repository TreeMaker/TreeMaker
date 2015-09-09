import sys,os,subprocess,re

# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
dictfile = parameters.value("dict","")
dict = __import__(dictfile.replace(".py",""))
makepy = parameters.value("py",True)
makewp = parameters.value("wp",True)

#format for ordered dict entries:
#                             data: ('sample' , [])
#                               MC: ('sample' , [xsec])
#MC w/ negative weights (amcatnlo): ('sample' , [xsec, neff])

wfile = open("weights.txt",'w')

for f,x in dict.flist.iteritems():
    if makepy:
        #get sample name
        oname = f.split('/')[1]
        
        #check for extended sample
        extcheck = re.search("ext[0-9]",f.split('/')[2])
        if not extcheck==None and len(extcheck.group(0))>0: oname = oname+"_"+extcheck.group(0)
        
        #get python config with list of files
        cmd = "wget --no-check-certificate --output-document="+oname+"_cff.py \"https://cmsweb.cern.ch/das/makepy?dataset="+f+"&instance=prod/global\""
        print cmd
        os.system(cmd)
    
    #only do weightproducer stuff for MC (w/ xsec provided)
    if makewp and len(x)>0:
        xsec = x[0]
        neff = 0
        if len(x)>1: neff = x[1]
    
        #get nevents
        cmd = "das_client.py --query=\"dataset="+f+" | grep dataset.nevents\" --limit=0"
        print cmd
        #nevents = subprocess.check_output(cmd)
        nevents = os.popen(cmd).read()

        #make line for weightproducer
        line = "        MCSample(\""+f.split('/')[1]+"\", \""+"-".join(f.split('/')[2].split('-')[1:3])+"\", \""+f.split('/')[2].split('-')[0]+"\", \"Constant\", "+str(x[0])+", ";
        if neff>0: line = line+str(neff)+"), # straight total = "+nevents.rstrip()+"\n"
        else: line = line+nevents.rstrip()+"),\n"
        wfile.write(line)
