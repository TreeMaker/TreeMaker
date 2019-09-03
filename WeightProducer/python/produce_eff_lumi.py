import os, glob, importlib, argparse
from Condor.Production.parseConfig import list_callback
from TreeMaker.WeightProducer.MCSample import MCSample

meta_dict = {
    "diboson"   :   ('WGJets','WW','WZ','ZG','ZZ'),
    "dyjets"    :   ('DYJetsToLL_M-50_HT',), #unused: DYJetsToLL
    "gjets"     :   ('GJets',),
    "qcd"       :   ('QCD_HT',),
    "qcd_pt"    :   ('QCD_Pt',),
    "signal"    :   ('SMS','RPV','StealthSYY','StealthSHH'),
    "singlet"   :   ('ST_s-channel','ST_t-channel','ST_tW','tZq'),
    "ttbar"     :   ('TTJets',), #unused: 'TT_Tune','TTTo2L2Nu','TTToSemiLeptonic','TTToHadronic'
    "tth"       :   ('TTZTo','TTWJets','TTGJets','TTGamma','TTHH','TTTT','TTTW','TTWH','TTWW','TTWZ','TTZH','TTZZ','ttHJet'),
    "wjets"     :   ('WJetsToLNu_HT',), #unused: WJetsTolNu
    "zjets"     :   ('ZJetsToNuNu',),
    "diboson-an":   ('TZToLLNuNu_M-10','TTZToQQ','TTWJetsToLNu','TTWJetsToQQ','TTGJets','WWTo1L1Nu2Q','WWTo2L2Nu','WZTo1L1Nu2Q','WZTo1L3Nu','ZZTo2Q2Nu','ZZTo2L2Q','TTTT','WWZ','WZZ','ZZZ',),
}

era_year_dict = {
    "Summer16"      : "2016",
    "Fall17"        : "2017",
    "Summer16v3"    : "2016",
    "Autumn18"      : "2018",
    "SVJ"           : "unknown",
}

def main(args):

    # Read parameters
    parser = argparse.ArgumentParser(description='Create lists of samples with their cross sections and effective luminosities.',
                                     epilog='Example usage:\n\tpython produce_eff_lumi.py -t',
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-c",   "--categories",     dest="categories",  default=[], nargs="+",  choices=meta_dict.keys(),                           help="List of categories to make dicts for rather than making all of the files (default = %(default)s)")
    parser.add_argument("-e",   "--eras",           dest="eras",        default=["Summer16","Fall17","Summer16v3","Autumn18","SVJ"],    nargs="+",  help="List of eras for which to produce a table (default = %(default)s)")
    parser.add_argument("-f",   "--filename",       dest="filename",    default="eff_lumi",                                                         help="The output filename without the extension (default = %(default)s)")
    parser.add_argument("-F",   "--filter",         dest="filter",      action="store_true",                                                        help="Filter out the duplicate entries based on sample name (default = %(default)s)")
    parser.add_argument("-o",   "--output_folder",  dest="ofolder",     default="./",                                                               help="Put the output files in the specified folder (default = %(default)s)")
    parser.add_argument("-t",   "--tex",            dest="tex",         action="store_true",                                                        help="Output in latex format (default = %(default)s)")
    args = parser.parse_args()

    # dict of modules
    era_list_dict = {}
    for era in args.eras:
        module_name = "SVJsamples" if era=="SVJ" else "MCSamples_"+era
        var = era+"samples"
        mod = importlib.import_module(module_name)
        era_list_dict[era] = getattr(mod, var)

    for era in args.eras:
        samples = era_list_dict[era]
        ofile = open(args.ofolder+"/"+args.filename+"_"+era+".txt",'w')
        for category in meta_dict:
            sample_selected = []
            sample_names = []
            sample_xs = []
            sample_lumi = []

            if len(args.categories)>0 and category not in args.categories: continue
            patterns = meta_dict[category]
            for pattern in patterns:
                samples_in_category = [sample for sample in samples if pattern in sample.name]
                for sample in samples_in_category:
                    if args.filter and sample.name in sample_selected: continue
                    sample_selected.append(sample.name)
                    sample_names.append(sample.name.replace("_","\_") if args.tex else ("/"+sample.name+"/"+sample.mcVersion+"_"+sample.production+"/MINIAODSIM"))
                    sample_xs.append(("%0.3f" % sample.XS if sample.XS < 10 else "%0.2f" % sample.XS) if args.tex else "")
                    sample_lumi.append("%.2f" %(sample.get_effective_lumi()/1000.0) if args.tex else "%.2f" % (sample.get_effective_lumi()/1000.0))

            # Don't write anything if there are no samples in this category
            if len(sample_names)==0: continue

            year_col = "\\multirow{"+str(len(sample_names))+"}{*}{"+str(era_year_dict[era])+"}"
            max_len_name = len(max(sample_names, key=len))
            max_len_xs = len(max(sample_xs, key=len))
            max_len_lumi = len(max(sample_lumi, key=len))
            for isample,sample_name in enumerate(sample_names):
                line = ""
                if args.tex:
                    if isample==0:
                        line += year_col
                    else:
                        line += (" "*len(year_col))
                    line += " & " + '{:{width}}'.format(sample_name,width=max_len_name) + " & " + '{:{width}}'.format(sample_xs[isample],width=max_len_xs) + " & " + '{:{width}}'.format(sample_lumi[isample],width=max_len_lumi) + " \\\\\n"
                else:
                    line = sample_name + " : " + sample_lumi[isample]+ "\n"
                ofile.write(line)

        ofile.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])