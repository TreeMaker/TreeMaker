import sys,os,subprocess

flist = [
]

xsecs = [
]

if xsecs==[]:
    xsecs = [0]*len(flist)
else:
    wfile = open("weights.txt",'w')

for f,x in zip(flist,xsecs):
    #get python config with list of files
    cmd = "wget --no-check-certificate --output-document="+f.split('/')[1]+"_cff.py \"https://cmsweb.cern.ch/das/makepy?dataset="+f+"&instance=prod/global\""
    print cmd
    os.system(cmd)
    
    #only do weightproducer stuff for MC (w/ xsec provided)
    if not x==0:
        #get nevents
        cmd = "das_client.py --query=\"dataset="+f+" | grep dataset.nevents\" --limit=0"
        print cmd
        #nevents = subprocess.check_output(cmd)
        nevents = os.popen(cmd).read()

        #make line for weightproducer
        line = "        MCSample(\""+f.split('/')[1]+"\", \""+"-".join(f.split('/')[2].split('-')[1:3])+"\", \""+f.split('/')[2].split('-')[0]+"\", \"Constant\", "+str(x)+", "+nevents.rstrip()+"),\n"
        wfile.write(line)
