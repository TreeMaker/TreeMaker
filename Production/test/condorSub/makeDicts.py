import os, glob, fnmatch
from optparse import OptionParser
from Condor.Production.parseConfig import list_callback

meta_dict = {
    "diboson" : ('WGJets','WW','WZ','ZG','ZZ'),
    "dyjets"  : ('DYJetsToLL',),
    "gjets"   : ('GJets',),
    "qcd"     : ('QCD_HT',),
    "qcd_pt"  : ('QCD_Pt',),
    "signal"  : ('SMS','RPV','StealthSYY','StealthSHH'),
    "singlet" : ('ST_s-channel','ST_t-channel','ST_tW','tZq'),
    "ttbar"   : ('TTJets','TT_Tune','TTTo2L2Nu','TTToSemiLeptonic','TTToHadronic'),
    "tth"     : ('TTZTo','TTWJets','TTGJets','TTGamma','TTHH','TTTT','TTTW','TTWH','TTWW','TTWZ','TTZH','TTZZ','ttHJet'),
    "wjets"   : ('WJetsToLNu',),
    "zjets"   : ('ZJetsToNuNu',),
}

def main(args):
    '''
    Example usage:
    python makeDicts.py -o tmp/
    '''

    # Read parameters
    parser = OptionParser()
    parser.add_option("-b", "--base",          dest="base",     default=os.environ["CMSSW_BASE"]+"/src/TreeMaker/Production/python/",   help="Base path to the python folder containing the file lists (default = %default)")
    parser.add_option("-c", "--categories",    dest="categories", default="", type="string", action='callback', callback=list_callback, help="Comma separated list of categories to make dicts for rather than making all of the files (default = %default)")
    parser.add_option("-d", "--debug",         dest="debug",    default=False, action="store_true",                                     help="Print extra debugging information (default = %default)")
    parser.add_option("-e", "--era",           dest="era",      default='RunIIFall17MiniAODv2',                                         help="The era used in the naming of the ouput dictionaries (default = %default)")
    parser.add_option("-l", "--location",      dest="location", default='RunIIFall17MiniAODv2/',                                        help="Location of the file lists which will be added to the dictionary (default = %default)")
    parser.add_option("-o", "--output_folder", dest="ofolder",  default="./",                                                           help="Put the output files in the specified folder (default = %default)")
    parser.add_option("-s", "--sig_scenario",  dest="sigsen",   default='Fall17sig',                                                    help="The scenario used for the signal samples (default = %default)")
    parser.add_option("-S", "--bkg_scenario",  dest="bkgsen",   default='Fall17',                                                       help="The scenario used for the background samples (default = %default)")
    (options, args) = parser.parse_args(args)

    written_files = []
    if options.location[-1]!="/": options.location += "/"
    location = options.base+options.location

    for category in meta_dict:
        if len(options.categories)>0 and category not in options.categories: continue
        patterns = meta_dict[category]
        files_grabbed = []
        ofile = open(options.ofolder+"/dict_"+options.era+"_"+category+".py",'w')

        for pattern in patterns:
            files_grabbed.extend(glob.glob(location+pattern+'*_cff.py'))
        files_grabbed = [options.location+os.path.basename(x) for x in files_grabbed]
        #nfiles_total+=len(files_grabbed)

        ofile.write("flist = {\n" + (4 * ' ') + "\"scenario\": \""+(options.sigsen if category=="signal" else options.bkgsen)+"\",\n" + (4 * ' ') + "\"samples\": [\n")
        for f in files_grabbed:
            filename = f.replace("_cff.py","").replace("/",".")
            written_files.append(filename)
            ofile.write((8 * ' ') + "[\'"+filename+"\'],\n")
        
        ofile.write((4 * ' ') + "]\n}\n")
        ofile.close()

    all_files = os.listdir(location)
    all_files = fnmatch.filter(all_files, "*_cff.py")

    endc = '\033[0m'
    if len(written_files) != len(all_files):
        print "\033[91mWARNING Some files might be duplicated across dictionaries or missing."+endc
    if len(written_files) != len(all_files) or options.debug:
        color = '\033[92m' if options.debug else '\033[91m'
        written_files = [x[x.find('.')+1:]+"_cff.py" for x in written_files]
        missing = set(written_files).difference(all_files)
        print color+"\tCounted "+str(len(written_files))+" file lists in the dictionaries"+endc
        print "\t\tValues in the dictionaries that are not found at "+location+":"+endc
        print '\033[93m',"\t\t",list(missing),endc
        print color+"\tFound "+str(len(all_files))+" in the folder "+location+endc
        add = set(all_files).difference(written_files)
        print "\t\tValues at "+location+" not found in the dictionaries:"+endc
        print '\033[93m',"\t\t",add,endc

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
