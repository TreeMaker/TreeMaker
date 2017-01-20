#!/usr/bin/env python

# forked from: https://github.com/trandbea/mc_macros/blob/master/mcm/bookkeep.py

import sys,os,pycurl,json,cStringIO,subprocess
from optparse import OptionParser

class col:
    magenta = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    uline = '\033[4m'

parser = OptionParser()
parser.add_option("-d", "--dict", dest="dict", default="dict_mcm", help="check for samples listed in this dict (default = %default)")
parser.add_option("-f", "--file", dest="file", default=False, action="store_true", help="write to file instead of displaying in terminal, removes colors (default = %default)")
parser.add_option("--miniaod", dest="miniaod", default="RunIISummer16MiniAODv2", help="miniAOD campaign name (default = %default)")
parser.add_option("--digireco", dest="digireco", default="RunIISummer16DR80*", help="DIGI-RECO campaign name (default = %default)")
parser.add_option("--gensim", dest="gensim", default="RunIISummer15*GS*", help="GEN-SIM campaign name (default = %default)")
parser.add_option("--debug", dest="debug", default=False, action="store_true", help="print debug info (default = %default)")
(options, args) = parser.parse_args()

dictname = options.dict.replace(".py","");
datasets = __import__(dictname).datasets

# generate cookie
cgso = subprocess.Popen("cern-get-sso-cookie --krb -r -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/ssocookie.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cgso_msg = cgso.communicate()
cgso_code = cgso.returncode
if cgso_code != 0:
    print cgso_msg[0]
    print cgso_msg[1]
    sys.exit(1)

# curl settings
curl = pycurl.Curl()
curl.setopt(pycurl.COOKIEFILE,os.getenv('HOME')+"/private/ssocookie.txt")
curl.setopt(pycurl.SSL_VERIFYPEER, 1)
curl.setopt(pycurl.SSL_VERIFYHOST, 2)
curl.setopt(pycurl.CAPATH, '/etc/pki/tls/certs')
curl.setopt(pycurl.FOLLOWLOCATION, 1)
    
def getA(query):
    url = "https://cms-pdmv.cern.ch/mcm/search/?db_name=requests&page=-1&"+query
    if options.debug: print url
    # setup output
    output = cStringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, output.write)
    # read from url
    curl.setopt(pycurl.HTTPGET, 1)
    curl.setopt(pycurl.URL, url)
    curl.perform()
    # process output
    jstr = output.getvalue()
    if options.debug: print jstr
    try:
        result = json.loads(jstr)
        return result['results']
    except:
        print "ERROR"
        print traceback.format_exc()
        print jstr
        return None

def preq(req,comment=''):
    tot = req['total_events'] 
    cmpl = req['completed_events']
    pct_done = float(cmpl)/float(tot)*100.
    # make gen query to get cross section
    qry='dataset_name='+req['dataset_name']+'*&extension='+str(req['extension'])+'&member_of_campaign='+options.gensim
    req_gs = getA(qry)
    xsec = 0.0
    for igs in req_gs:
        found_ich = False
        # find intersection
        if len(set(igs['member_of_chain']) & set(req['member_of_chain']))>0:
            # reverse generator_parameters list: assume latest submission is best
            igp = next((ig for ig in reversed(igs["generator_parameters"]) if "cross_section" in ig), None)
            if igp:
                xsec = igp["cross_section"]
            if pct_done<0:
                pct_done = float(cmpl)/float(igs['completed_events'])*100.
                tot = igs['completed_events']
            break
    type = 'None'
    if ('MiniAOD' in req['member_of_campaign']): type = 'MiniAOD '
    elif ('DR80' in req['member_of_campaign']): type = 'DIG-REC '
    elif ('GS' in req['member_of_campaign']): type = 'GEN-SIM '
    cols = '{:<72}'.format(req['dataset_name'][0:68])
    cols += '{:<10}'.format(req['extension'])
    cols += type+'{:<15}'.format(req['status'])
    cols += '{:>13.0f}'.format(pct_done)
    cols += '{:>15,}'.format(tot)
    cols += '{:>15.6E}'.format(xsec)
    cols += ' '+' '.join(req['output_dataset'])
    if len(comment)>0: cols += '    '+comment
    return cols

cols = '{:<72}'.format('Dataset name')
cols += '{:<10}'.format('Extension')
cols += '{:<23}'.format('Latest status')
cols += '{:>13}'.format('Completed [%]')
cols += '{:>15}'.format('# Events')
cols += '{:>15}'.format('Cross Section')
cols += ' Paths'

if options.file:
    goodfile = open("results_"+dictname+"_finished.txt",'w')
    goodfile.write(cols+"\n")
    badfile = open("results_"+dictname+"_unfinished.txt",'w')
    badfile.write(cols+"\n")
else:
    print cols
    
for ds in datasets.keys():
    if options.file: print ds
    # sort output within each ds
    allcols = []
    goodcols = []
    badcols = []
    for ext in datasets[ds]:
        # keep track of all found dataset names (wildcard support)
        found_list = set()
        
        # check miniaod, digireco, gensim
        qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.miniaod
        req_mini = getA(qry)
        qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.digireco
        req_dr = getA(qry)
        qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.gensim
        req_gs = getA(query=qry)
        
        # miniaod first
        if req_mini:
            for ireq in req_mini:
                dname = ireq['dataset_name']
                if dname in found_list: continue
                found_list.add(dname)
                hlight = col.red
                toprint = preq(ireq)
                if ireq['status']=='done': hlight = col.green
                elif ireq['status']=='submitted': hlight = ''
                if options.file:
                    if ireq['status']=='done': goodcols.append(toprint)
                    else: badcols.append(toprint)
                else:
                    allcols.append(hlight+toprint+col.endc)
        
        # digireco second
        if req_dr:
            for ireq in req_dr:
                dname = ireq['dataset_name']
                if dname in found_list: continue
                found_list.add(dname)
                ireq = req_dr[0]
                toprint = preq(ireq,"No MiniAOD request yet")
                if options.file: badcols.append(toprint)
                else: allcols.append(col.blue+toprint+col.endc)
        
        # gensim last
        if req_gs:
            for ireq in req_gs:
                dname = ireq['dataset_name']
                if dname in found_list: continue
                if '0T' in ireq['flown_with']: continue
                found_list.add(dname)
                toprint = preq(ireq,'Missing MiniAOD and DIGIRECO')
                if options.file: badcols.append(toprint)
                else: allcols.append(col.red+toprint+col.endc)

    # print at end of ds
    if options.file:
        if len(goodcols)>0: goodfile.write('\n'.join(sorted(goodcols))+'\n')
        if len(badcols)>0: badfile.write('\n'.join(sorted(badcols))+'\n')
    else:
        if len(allcols)>0: print '\n'.join(sorted(allcols))

# print sorted output
if options.file:
    goodfile.close()
    badfile.close()
