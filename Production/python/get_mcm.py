#!/usr/bin/env python

# forked from: https://github.com/trandbea/mc_macros/blob/master/mcm/bookkeep.py

import sys,os,pycurl,json,cStringIO,subprocess
from optparse import OptionParser
from collections import OrderedDict
from TreeMaker.Production.tm_common import printGetPyDictHeader
from Condor.Production.parseConfig import list_callback

# curl settings
curl = pycurl.Curl()
curl.setopt(pycurl.COOKIEFILE,os.getenv('HOME')+"/private/ssocookie.txt")
curl.setopt(pycurl.SSL_VERIFYPEER, 0) #originally was 1
curl.setopt(pycurl.SSL_VERIFYHOST, 2)
curl.setopt(pycurl.CAPATH, '/etc/pki/tls/certs')
curl.setopt(pycurl.FOLLOWLOCATION, 1)

class col:
    magenta = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    uline = '\033[4m'

class pyline:
    '''
    Example Use:
    from get_mcm import pyline
    gpl = pyline('dname1',True)
    print gpl
    gpl.append('dname2',True)
    print gpl
    gpl.append('dname3',False)
    print gpl
    gpl.append(['dname4','dname5'],[False,False])
    print gpl

    or

    gpl = pyline(['dname1','dname2'], [False,True])
    '''
    def __init__(self, dataset_names, pu_valids):
        if type(dataset_names) in [str,unicode]: dataset_names = [dataset_names]
        if type(pu_valids) == bool: pu_valids = [pu_valids]
        if len(dataset_names) != len(pu_valids):
            raise ValueError('The length of the dataset and pu validity lists must be the same.')
        self.dataset_names = [str(x) for x in dataset_names]
        self.pu_valids = pu_valids

    def append(self, dataset_names, pu_valids):
        if type(dataset_names) in [str,unicode]: dataset_names = [dataset_names]
        if type(pu_valids) == bool: pu_valids = [pu_valids]
        if len(dataset_names) != len(pu_valids):
            raise ValueError('The length of the dataset and pu validity lists must be the same.')

        self.dataset_names.extend([str(x) for x in dataset_names])
        self.pu_valids.extend(pu_valids)

    def get_process(self):
        return self.dataset_names[0].split('/')[1]

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.dataset_names,self.pu_valids)

    def __str__(self):
        return "\t[%r, %r, []]," % (2 if False in self.pu_valids else 1, self.dataset_names)

def getA(query,debug):
    global curl

    url = "https://cms-pdmv.cern.ch/mcm/search/?db_name=requests&page=-1&"+query
    if debug: print url
    # setup output
    output = cStringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, output.write)
    # read from url
    curl.setopt(pycurl.HTTPGET, 1)
    curl.setopt(pycurl.URL, url)
    curl.perform()
    # process output
    jstr = output.getvalue()
    if debug: print jstr
    try:
        result = json.loads(jstr)
        return result['results']
    except:
        print "ERROR"
        print traceback.format_exc()
        print jstr
        return None

#def parser_callback(option, opt, value, parser):
#  setattr(parser.values, option.dest, value.split(','))

def preq(req,gensim,comment='',debug=False):
    tot = req['total_events'] 
    cmpl = req['completed_events']
    pct_done = float(cmpl)/float(tot)*100.
    # make gen query to get cross section
    qry='dataset_name='+req['dataset_name']+'*&extension='+str(req['extension'])+'&member_of_campaign='+gensim
    req_gs = getA(qry,debug)
    xsec = 0.0
    for igs in req_gs:
        # find intersection
        if len(set(igs['member_of_chain']) & set(req['member_of_chain']))>0:
            # reverse generator_parameters list: assume latest submission is best
            igp = next((ig for ig in reversed(igs["generator_parameters"]) if "cross_section" in ig), None)
            if igp:
                xsec = igp["cross_section"]
            # use GS total as denom
            tot = igs['total_events']
            pct_done = float(cmpl)/float(tot)*100.
            break
    type = 'None '
    if ('MiniAOD' in req['member_of_campaign']): type = 'MiniAOD '
    elif ('DRPremix' in req['member_of_campaign']): type = 'DIG-REC '
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

def pu_dataset_validity(req,digireco,condition='',debug=False):
    if condition == '': return True
    qry='dataset_name='+req['dataset_name']+'*&extension='+str(req['extension'])+'&member_of_chain='+str(req['member_of_chain'][0])
    req_chain = getA(qry,debug)
    all_prepids = []
    for chain in req_chain:
        all_prepids.append(chain['prepid'])
    prepids = [x for x in all_prepids if any(substr in x for substr in ["DRPremix","DRStdmix"])]
    if len(prepids)!=1:
        print "ERROR Something went wrong in checking the pileup dataset validity."
        print " There can only be 1 prepid with \"DRPremix\" in the name (" + str(len(prepids)) + ")."
        print " " + str(all_prepids)
        return False
    qry='prepid='+str(prepids[0])
    req_prepid = getA(qry,debug)
    if condition in req_prepid[0]['pileup_dataset_name']: return True
    else: return False

def main(args):
    parser = OptionParser()
    parser.add_option("-d", "--dict", dest="dict", default="dict_mcm", help="check for samples listed in this dict (default = %default)")
    parser.add_option("-f", "--file", dest="file", default=False, action="store_true", help="write to file instead of displaying in terminal, removes colors (default = %default)")
    parser.add_option("-p", "--pu", dest="pu", default="", help="string to check for in pu dataset to determine validity (default = %default)")
    parser.add_option("-m", "--make", dest="make_dict", default="", help="if set, make a get_py.py dictionary out of the finished datasets (default = %default)")
    parser.add_option("-i", "--inclusive", dest="inclusive", default=False, action="store_true", help="if make is set, include the finished_invalid datasets in the dict (default = %default)")
    parser.add_option("-g", "--grep", dest="grep", default="", type="string", action='callback', callback=list_callback, help="comma separated list of patterns in the dataset name to select for (default = %default). Watch for dangling commas!")
    parser.add_option("-v", "--vgrep", dest="vgrep", default="", type="string", action='callback', callback=list_callback, help="comma separated list of patterns in the dataset name to ignore (default = %default). Watch for dangling commas!")
    parser.add_option("--miniaod", dest="miniaod", default="RunIISummer16MiniAODv2", help="miniAOD campaign name (default = %default)")
    parser.add_option("--digireco", dest="digireco", default="RunIISummer16DR80*", help="DIGI-RECO campaign name (default = %default)")
    parser.add_option("--gensim", dest="gensim", default="RunIISummer15*GS*", help="GEN-SIM campaign name (default = %default)")
    parser.add_option("--debug", dest="debug", default=False, action="store_true", help="print debug info (default = %default)")
    parser.add_option("--cert", dest="cert", default="", help="w/ --key, use certificate access for McM database (otherwise kerberos) (default = %default)")
    parser.add_option("--key", dest="key", default="", help="w/ --cert, use certificate access for McM database (otherwise kerberos) (default = %default)")
    parser.add_option("--verbose", dest="verbose", default=False, action="store_true", help="print some extra messages (not quite as verbose as debug (default = %default)")
    (options, args) = parser.parse_args()
    
    # check options
    if len(options.dict)==0:
    	parser.error("Must specify a dict of samples")
    use_krb = True
    cgso_check = int(len(options.cert)>0) + int(len(options.key)>0)
    if cgso_check==2:
        use_krb = False
    elif cgso_check==1:
        parser.error("Need to specify both --cert and --key")
    
    sys.path.append(os.getcwd())
    dictname = options.dict.replace(".py","");
    datasets = __import__(dictname).datasets
    
    # configure McM access
    if use_krb:
        cgso_access = "--krb"
        # check for ticket
        test_krb = subprocess.Popen('klist', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test_krb_msg = test_krb.communicate()
        has_krb = False
        for line in test_krb_msg[0].split('\n'):
            if "Default principal" in line and "CERN.CH" in line:
                has_krb = True
                break
        if not has_krb:
            print "No kerberos ticket found for CERN.CH"
            sys.exit(1)
    else:
        cgso_access = "--cert "+options.cert+" --key "+options.key
    
    # generate cookie
    cgso = subprocess.Popen("cern-get-sso-cookie "+cgso_access+" -r -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/ssocookie.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cgso_msg = cgso.communicate()
    cgso_code = cgso.returncode
    if cgso_code != 0:
        print cgso_msg[0]
        print cgso_msg[1]
        sys.exit(1)
        
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
        invalidfile = open("results_"+dictname+"_finished_invalid.txt",'w')
        invalidfile.write(cols+"\n")
    else:
        print cols

    if len(options.make_dict)>0:
        getpyfile = open(options.make_dict,'w')
        printGetPyDictHeader(getpyfile)
        
    for ds in datasets.keys():
        if options.file: print ds
        # sort output within each ds
        allcols = []
        goodcols = []
        badcols = []
        invalidcols = []
        getpylines = OrderedDict()
        for ext in datasets[ds]:
            # keep track of all found dataset names (wildcard support)
            found_list = set()
            
            # check miniaod, digireco, gensim
            qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.miniaod
            req_mini = getA(qry,options.debug)
            qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.digireco
            req_dr = getA(qry,options.debug)
            qry = 'dataset_name='+ds+'*&extension='+str(ext)+'&member_of_campaign='+options.gensim
            req_gs = getA(query=qry,debug=options.debug)
            
            # miniaod first
            if req_mini:
                for ireq in req_mini:
                    dname = ireq['dataset_name']
                    output_dataset = ireq['output_dataset']
                    if not any(any(pattern in ds for ds in output_dataset) for pattern in options.grep):
                        if options.verbose: print "\tSkipping",dname,"because of grep"
                        continue
                    if any(any(pattern in ds for ds in output_dataset) for pattern in options.vgrep):
                        if options.verbose: print "\tSkipping",dname,"because of vgrep"
                        continue
                    if dname in found_list: continue
                    found_list.add(dname)
                    hlight = col.red
                    pu_valid = pu_dataset_validity(ireq,options.digireco,options.pu,options.debug) if options.pu!="" else True
                    toprint = preq(ireq,options.gensim,'' if pu_valid else 'Invalid Pileup Dataset',options.debug)
                    if not pu_valid and ireq['status']!='new': hlight = col.yellow
                    elif ireq['status']=='done': hlight = col.green
                    elif ireq['status']=='submitted': hlight = ''
                    if options.file:
                        if ireq['status']=='done' and pu_valid: goodcols.append(toprint)
                        elif ireq['status']=='done' and not pu_valid: invalidcols.append(toprint)
                        else: badcols.append(toprint)

                        if ireq['status']=='done' and len(options.make_dict)>0:
                            PD = output_dataset[0].split('/')[1]
                            if len(getpylines)==0 or PD not in getpylines.keys():
                                if pu_valid: getpylines[PD] = pyline(output_dataset,pu_valid)
                                elif options.inclusive and not pu_valid: getpylines[PD] = pyline(output_dataset,pu_valid)
                            else:
                                if pu_valid: getpylines[PD].append(output_dataset,pu_valid)
                                elif options.inclusive and not pu_valid: getpylines[PD].append(output_dataset,pu_valid)

                    else:
                        allcols.append(hlight+toprint+col.endc)
            
            # digireco second
            if req_dr:
                for ireq in req_dr:
                    dname = ireq['dataset_name']
                    if dname in found_list: continue
                    found_list.add(dname)
                    ireq = req_dr[0]
                    toprint = preq(ireq,options.gensim,"No MiniAOD request yet",options.debug)
                    if options.file: badcols.append(toprint)
                    else: allcols.append(col.blue+toprint+col.endc)
            
            # gensim last
            if req_gs:
                for ireq in req_gs:
                    dname = ireq['dataset_name']
                    if dname in found_list: continue
                    if '0T' in ireq['flown_with']: continue
                    found_list.add(dname)
                    toprint = preq(ireq,options.gensim,'Missing MiniAOD and DIGIRECO',options.debug)
                    if options.file: badcols.append(toprint)
                    else: allcols.append(col.red+toprint+col.endc)
    
        # print at end of ds
        if options.file:
            if len(goodcols)>0: goodfile.write('\n'.join(sorted(goodcols))+'\n')
            if len(badcols)>0: badfile.write('\n'.join(sorted(badcols))+'\n')
            if len(invalidcols)>0: invalidfile.write('\n'.join(sorted(invalidcols))+'\n')
        else:
            if len(allcols)>0: print '\n'.join(sorted(allcols))
    
        if len(options.make_dict)>0 and len(getpylines)>0:
            getpyfile.write('\n'.join(sorted([str(item) for key, item in getpylines.iteritems()]))+'\n')

    # print sorted output
    if options.file:
        goodfile.close()
        badfile.close()
        invalidfile.close()

    if len(options.make_dict)>0:
        getpyfile.write("]\n")
        getpyfile.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
