import os, glob, fnmatch
from optparse import OptionParser

def parser_callback(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))

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
    parser.add_option("-b", "--base",          dest="base",     default=os.environ["CMSSW_BASE"]+"/src/TreeMaker/Production/python/", help="Base path to the python folder containing the file lists (default = %default)")
    parser.add_option("-c", "--categories",    dest="categories", default="", type="string", action='callback', callback=parser_callback, help="Comma separated list of categories to make dicts for rather than making all of the files (default = %default)")
    parser.add_option("-d", "--debug",         dest="debug",    default=False, action="store_true",                                   help="Print extra debugging information (default = %default)")
    parser.add_option("-e", "--era",           dest="era",      default='RunIIFall17MiniAODv2',                                       help="The era used in the naming of the ouput dictionaries (default = %default)")
    parser.add_option("-l", "--location",      dest="location", default='RunIIFall17MiniAODv2/',                                      help="Location of the file lists which will be added to the dictionary (default = %default)")
    parser.add_option("-o", "--output_folder", dest="ofolder",  default="./",                                                         help="Put the output files in the specified folder (default = %default)")
    parser.add_option("-s", "--sig_scenario",  dest="sigsen",   default='Fall17sig',                                                  help="The scenario used for the signal samples (default = %default)")
    parser.add_option("-S", "--bkg_scenario",  dest="bkgsen",   default='Fall17',                                                     help="The scenario used for the background samples (default = %default)")
    (options, args) = parser.parse_args(args)

    nfiles_total = 0
    location = options.base+options.location

    for category in meta_dict:
        if len(options.categories)>0 and category not in options.categories: continue
        patterns = meta_dict[category]
        files_grabbed = []
        ofile = open(options.ofolder+"/dict_"+options.era+"_"+category+".py",'w')

        for pattern in patterns:
            files_grabbed.extend(glob.glob(location+pattern+'*'))
        files_grabbed = [options.location+os.path.basename(x) for x in files_grabbed]
        nfiles_total+=len(files_grabbed)

        ofile.write("flist = {\n" + (4 * ' ') + "\"scenario\": \""+(options.sigsen if category=="signal" else options.bkgsen)+"\",\n" + (4 * ' ') + "\"samples\": [\n")
        for f in files_grabbed:
             ofile.write((8 * ' ') + "[\'"+f.replace("_cff.py","").replace("/",".")+"\'],\n")
        
        ofile.write((4 * ' ') + "]\n}\n")
        ofile.close()

    all_files = os.listdir(location)
    all_files = fnmatch.filter(all_files, "*_cff.py")

    if nfiles_total != len(all_files):
        print "WARNING Some files might be duplicated across dictionaries or missing."
    if nfiles_total != len(all_files) or options.debug:
        print "\tFound "+str(len(all_files))+" in the folder "+location
        print "\tCounted "+str(nfiles_total)+" file lists in the dictionaries"

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
