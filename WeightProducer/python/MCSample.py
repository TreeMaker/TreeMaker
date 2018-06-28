from collections import namedtuple
import re

XSValues = namedtuple('XSValue', ['CME_7TeV', 'CME_8TeV', 'CME_13TeV', 'CME_14TeV'], verbose=False)

class MCSample():

    '''
    Example use:
    from MCSample import XSValues, MCSample
    m = MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10139950)
    '''

    __xs_dict = {
        "TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                                      : XSValues(-1.0, -1.0, 831.76,      -1.0),
        "TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                      : XSValues(-1.0, -1.0, 182.72,      -1.0),
        "TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                   : XSValues(-1.0, -1.0, 182.72,      -1.0),
        "TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                               : XSValues(-1.0, -1.0, 88.34,       -1.0),
        "TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"           : XSValues(-1.0, -1.0, 5.979,       -1.0),
        "TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"        : XSValues(-1.0, -1.0, 5.936,       -1.0),
        "TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 3.666,       -1.0),
        "TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                          : XSValues(-1.0, -1.0, 2.7343862,   -1.0),
        "TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                         : XSValues(-1.0, -1.0, 1.12075054,  -1.0),
        "TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                        : XSValues(-1.0, -1.0, 0.1979159,   -1.0),
        "TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                         : XSValues(-1.0, -1.0, 0.002368366, -1.0),
        "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8"                                             : XSValues(-1.0, -1.0, 831.76,      -1.0),
        "WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                      : XSValues(-1.0, -1.0, 1627.45,     -1.0),
        "WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                      : XSValues(-1.0, -1.0, 435.24,      -1.0),
        "WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                      : XSValues(-1.0, -1.0, 59.18,       -1.0),
        "WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                      : XSValues(-1.0, -1.0, 14.58,       -1.0),
        "WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                     : XSValues(-1.0, -1.0, 6.66,        -1.0),
        "WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 1.608,       -1.0),
        "WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                     : XSValues(-1.0, -1.0, 0.03891,     -1.0),
        "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                                  : XSValues(-1.0, -1.0, 61334.9,     -1.0),
        "QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                              : XSValues(-1.0, -1.0, 1717000,     -1.0),
        "QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                              : XSValues(-1.0, -1.0, 351300,      -1.0),
        "QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                              : XSValues(-1.0, -1.0, 31630,       -1.0),
        "QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                             : XSValues(-1.0, -1.0, 6802,        -1.0),
        "QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                            : XSValues(-1.0, -1.0, 1206,        -1.0),
        "QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                            : XSValues(-1.0, -1.0, 120.4,       -1.0),
        "QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                             : XSValues(-1.0, -1.0, 25.24,       -1.0),
        "QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8"                                           : XSValues(-1.0, -1.0, 19204300,    -1.0),
        "QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8"                                          : XSValues(-1.0, -1.0, 2762530,     -1.0),
        "QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8"                                         : XSValues(-1.0, -1.0, 471100,      -1.0),
        "QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8"                                         : XSValues(-1.0, -1.0, 117276,      -1.0),
        "QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8"                                         : XSValues(-1.0, -1.0, 7823,        -1.0),
        "QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8"                                         : XSValues(-1.0, -1.0, 648.2,       -1.0),
        "QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8"                                         : XSValues(-1.0, -1.0, 186.9,       -1.0),
        "QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8"                                        : XSValues(-1.0, -1.0, 32.293,      -1.0),
        "QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8"                                       : XSValues(-1.0, -1.0, 9.4183,      -1.0),
        "QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8"                                       : XSValues(-1.0, -1.0, 0.84265,     -1.0),
        "QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8"                                       : XSValues(-1.0, -1.0, 0.114943,    -1.0),
        "QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8"                                       : XSValues(-1.0, -1.0, 0.00682981,  -1.0),
        "QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8"                                        : XSValues(-1.0, -1.0, 0.000165445, -1.0),
        "DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 181.302,     -1.0),
        "DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 50.4177,     -1.0),
        "DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 6.98394,     -1.0),
        "DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 1.68141,     -1.0),
        "DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                : XSValues(-1.0, -1.0, 0.775392,    -1.0),
        "DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"               : XSValues(-1.0, -1.0, 0.186222,    -1.0),
        "DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                : XSValues(-1.0, -1.0, 0.00438495,  -1.0),
        "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                             : XSValues(-1.0, -1.0, 6025.2,      -1.0),
        "ZJetsToNuNu_HT-100To200_13TeV-madgraph"                                             : XSValues(-1.0, -1.0, 344.8305,    -1.0),
        "ZJetsToNuNu_HT-200To400_13TeV-madgraph"                                             : XSValues(-1.0, -1.0, 95.5341,     -1.0),
        "ZJetsToNuNu_HT-400To600_13TeV-madgraph"                                             : XSValues(-1.0, -1.0, 13.1979,     -1.0),
        "ZJetsToNuNu_HT-600To800_13TeV-madgraph"                                             : XSValues(-1.0, -1.0, 3.14757,     -1.0),
        "ZJetsToNuNu_HT-800To1200_13TeV-madgraph"                                            : XSValues(-1.0, -1.0, 1.450908,    -1.0),
        "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph"                                           : XSValues(-1.0, -1.0, 0.3546459,   -1.0),
        "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph"                                            : XSValues(-1.0, -1.0, 0.00854235,  -1.0),
        "GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                           : XSValues(-1.0, -1.0, 9226,        -1.0),
        "GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                           : XSValues(-1.0, -1.0, 2300,        -1.0),
        "GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                           : XSValues(-1.0, -1.0, 277.4,       -1.0),
        "GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                           : XSValues(-1.0, -1.0, 93.38,       -1.0),
        "GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 5000,        -1.0),
        "GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 1079,        -1.0),
        "GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 125.9,       -1.0),
        "GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 43.36,       -1.0),
        "ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 43.5543,     -1.0),
        "ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 5.28654,     -1.0),
        "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1"                   : XSValues(-1.0, -1.0, 3.34,        -1.0),
        "ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8"                             : XSValues(-1.0, -1.0, 10.32,       -1.0),
        "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1"    : XSValues(-1.0, -1.0, 136.02,      -1.0),
        "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1": XSValues(-1.0, -1.0, 80.95,       -1.0),
        "ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1"                   : XSValues(-1.0, -1.0, 19.4674,     -1.0),
        "ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1"                       : XSValues(-1.0, -1.0, 19.4674,     -1.0),
        "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1"                 : XSValues(-1.0, -1.0, 35.6,        -1.0),
        "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1"                     : XSValues(-1.0, -1.0, 35.6,        -1.0),
        "tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8"                              : XSValues(-1.0, -1.0, 0.0758,      -1.0),
        "WW_TuneCUETP8M1_13TeV-pythia8"                                                      : XSValues(-1.0, -1.0, 51.723,      -1.0),
        "WZ_TuneCUETP8M1_13TeV-pythia8"                                                      : XSValues(-1.0, -1.0, 47.13,       -1.0),
        "ZZ_TuneCUETP8M1_13TeV-pythia8"                                                      : XSValues(-1.0, -1.0, 16.523,      -1.0),
        "WWTo2L2Nu_13TeV-powheg"                                                             : XSValues(-1.0, -1.0, 12.178,      -1.0),
        "WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph"                          : XSValues(-1.0, -1.0, 12.7,        -1.0),
        "WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph"                              : XSValues(-1.0, -1.0, 0.834,       -1.0),
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8"                                     : XSValues(-1.0, -1.0, 49.997,      -1.0),
        "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8"                                     : XSValues(-1.0, -1.0, 10.71,       -1.0),
        "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8"                                       : XSValues(-1.0, -1.0, 3.058,       -1.0),
        "ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"                                   : XSValues(-1.0, -1.0, 32.3,        -1.0),
        "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8"                                        : XSValues(-1.0, -1.0, 3.22,        -1.0),
        "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8"                                       : XSValues(-1.0, -1.0, 4.04,        -1.0),
        "TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8"                               : XSValues(-1.0, -1.0, 0.2529,      -1.0),
        "TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8"                                        : XSValues(-1.0, -1.0, 0.5297,      -1.0),
        "TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"                       : XSValues(-1.0, -1.0, 0.2043,      -1.0),
        "TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"                       : XSValues(-1.0, -1.0, 0.2043,      -1.0),
        "TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"                        : XSValues(-1.0, -1.0, 0.4026,      -1.0),
        "TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"                            : XSValues(-1.0, -1.0, 3.697,       -1.0),
        "TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"                            : XSValues(-1.0, -1.0, 3.697,       -1.0),
        "ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix"                     : XSValues(-1.0, -1.0, 0.2118,      -1.0),
        "ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8"                                 : XSValues(-1.0, -1.0, 0.2953,      -1.0),
        "TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8"                                         : XSValues(-1.0, -1.0, 0.009103,    -1.0),
        "TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.000741,    -1.0),
        "TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.000861,    -1.0),
        "TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.00136,     -1.0),
        "TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.007834,    -1.0),
        "TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.00297,     -1.0),
        "TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.00125,     -1.0),
        "TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8"                                         : XSValues(-1.0, -1.0, 0.00157,     -1.0),
        "WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8"                                            : XSValues(-1.0, -1.0, 0.1651,      -1.0),
        "WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8"                                            : XSValues(-1.0, -1.0, 0.05565,     -1.0),
        "ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8"                                            : XSValues(-1.0, -1.0, 0.01398,     -1.0),
        "SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.325388,    -1.0),
        "SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.0141903,   -1.0),
        "SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.0856418,   -1.0),
        "SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.0141903,   -1.0),
        "SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.000981077, -1.0),
        "SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.325388,    -1.0),
        "SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"            : XSValues(-1.0, -1.0, 0.0252977,   -1.0),
        "SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 1.31169,     -1.0),
        "SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 0.51848,     -1.0),
        "SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 0.0189612,   -1.0),
        "SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                  : XSValues(-1.0, -1.0, 36.3818,     -1.0),
        "SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 21.5949,     -1.0),
        "SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                  : XSValues(-1.0, -1.0, 21.5949,     -1.0),
        "SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 249.409,     -1.0),
        "SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 249.409,     -1.0),
        "SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                 : XSValues(-1.0, -1.0, 0.107045,    -1.0),
        "SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"          : XSValues(-1.0, -1.0, 0.00163547,  -1.0),
        "SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                     : XSValues(-1.0, -1.0, 2.26585,     -1.0),
        "SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.325388,    -1.0), 
        "SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.163491,    -1.0),
        "SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.0856418,   -1.0),
        "SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.0460525,   -1.0),
        "SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.0252977,   -1.0),
        "SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.0141903,   -1.0),
        "SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.00810078,  -1.0),
        "SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.00470323,  -1.0),
        "SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.00276133,  -1.0),
        "SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.00163547,  -1.0),
        "SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.000981077, -1.0),
        "SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.000591918, -1.0),
        "SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"                    : XSValues(-1.0, -1.0, 0.000359318, -1.0),
        "step4_MINIAOD_mZprime-1000_mDark-20_rinv-0.3_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 4.612,       -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.1_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.5_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-2000_mDark-20_rinv-0.3_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.1849,      -1.0),
        "step4_MINIAOD_mZprime-4000_mDark-20_rinv-0.3_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.001688,    -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-1_rinv-0.3_alpha-0.2_n-1000"                       : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-50_rinv-0.3_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-100_rinv-0.3_alpha-0.2_n-1000"                     : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.1_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.7_alpha-0.2_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.5_n-1000"                      : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-1_n-1000",                       : XSValues(-1.0, -1.0, 0.0155,      -1.0),
        "stealth_stop_350_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 3.78661,     -1.0),
        "stealth_stop_450_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 0.948333,    -1.0),
        "stealth_stop_550_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 0.296128,    -1.0),
        "stealth_stop_650_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 0.107045,    -1.0),
        "stealth_stop_750_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 0.0431418,   -1.0),
        "stealth_stop_850_singlino_SYY"                                                      : XSValues(-1.0, -1.0, 0.0189612,   -1.0),
        "stealth_stop_350_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 3.78661,     -1.0),
        "stealth_stop_450_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 0.948333,    -1.0),
        "stealth_stop_550_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 0.296128,    -1.0),
        "stealth_stop_650_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 0.107045,    -1.0),
        "stealth_stop_750_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 0.0431418,   -1.0),
        "stealth_stop_850_singlino_SHuHd"                                                    : XSValues(-1.0, -1.0, 0.0189612,   -1.0),
        "rpv_stop_350_t3j_uds"                                                               : XSValues(-1.0, -1.0, 3.78661,     -1.0),
        "rpv_stop_450_t3j_uds"                                                               : XSValues(-1.0, -1.0, 0.948333,    -1.0),
        "rpv_stop_550_t3j_uds"                                                               : XSValues(-1.0, -1.0, 0.296128,    -1.0),
        "rpv_stop_650_t3j_uds"                                                               : XSValues(-1.0, -1.0, 0.107045,    -1.0),
        "rpv_stop_750_t3j_uds"                                                               : XSValues(-1.0, -1.0, 0.0431418,   -1.0),
        "rpv_stop_850_t3j_uds"                                                               : XSValues(-1.0, -1.0, 0.0189612,   -1.0),
    }

    __names_to_strip = {
        "generators" : ["(.pythia)([^_-]*)","(.powheg)([^_-]*)","(.madgraph)([^_-]*)","(.madspin)([^_-]*)","(.amcatnlo)([^_-]*)"],
        "tunes"      : ["(.Tune)([^_]*)"],
    }

    def __init__(self, name, production, mcVersion, Method, NumberEvts):
        self.name = name
        self.production = production
        self.mcVersion = mcVersion
        self.Method = Method
        self.XS = self.get_xs(name)
        self.NumberEvts = NumberEvts

    def get_cm_energy(self, name):
        return (re.sub("(_[0-9]*TeV)","",name),re.search("(_[0-9]*TeV)",name).group(0))

    def get_minimal_name(self, name):
        for category, values_to_strip in self.__names_to_strip.iteritems():
            for regex_value in values_to_strip:
                name = re.sub(regex_value,"",name)
        return name

    def get_xs(self, name):
        name_minimal = self.get_minimal_name(name)
        name_minimal, energy = self.get_cm_energy(name_minimal)
        return self.__xs_dict[name_minimal].__getattribute__("CME"+energy)

    def __repr__(self):
        dict_of_members = self.__dict__
        list_of_keys = dict_of_members.keys()
        list_of_values = dict_of_members.values()
        max_len_keys = max(len(str(x)) for x in list_of_keys)
        max_len_values = max(len(str(x)) for x in list_of_values)
        key_format="{:<"+str(max_len_keys)+"}"
        value_format="{:<"+str(max_len_values)+"}"
        rep_format = "MCSample("
        for ikey, key in enumerate(list_of_keys):
            if ikey != len(list_of_keys)-1:
                rep_format += (key_format+": "+value_format)
                rep_format += ("\n{:<9}")
            else:
                rep_format += (key_format+": {:<"+str(len(str(self.NumberEvts)))+"}")
                rep_format += ")"
        return rep_format.format('name',self.name,' ','production',self.production,' ','mcVersion',self.mcVersion,' ','Method',self.Method,' ','XS',self.XS,' ','NumberEvts',self.NumberEvts)

class MCSample_legacy:
    def __init__(self, name, production, mcVersion, Method, XS, NumberEvts):
        self.name = name
        self.production = production
        self.mcVersion = mcVersion
        self.Method = Method
        self.XS = XS
        self.NumberEvts = NumberEvts