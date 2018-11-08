from collections import namedtuple
import re

class MCSampleHelper():
    
    XSValues = namedtuple('XSValue', ['CME_7TeV', 'CME_8TeV', 'CME_13TeV', 'CME_14TeV'], verbose=False)

    __xs_dict = {
        "TT"                                                             : XSValues(-1.0, -1.0, 831.76,       -1.0),
        "TTJets"                                                         : XSValues(-1.0, -1.0, 831.76,       -1.0),
        "TTbar"                                                          : XSValues(-1.0, -1.0, 831.76,       -1.0),
        "TTJets_SingleLeptFromT"                                         : XSValues(-1.0, -1.0, 182.72,       -1.0),
        "TTJets_SingleLeptFromTbar"                                      : XSValues(-1.0, -1.0, 182.72,       -1.0),
        "TTJets_DiLept"                                                  : XSValues(-1.0, -1.0, 88.34,        -1.0),
        "TTJets_SingleLeptFromT_genMET-150"                              : XSValues(-1.0, -1.0, 5.979,        -1.0),
        "TTJets_SingleLeptFromTbar_genMET-150"                           : XSValues(-1.0, -1.0, 5.936,        -1.0),
        "TTJets_DiLept_genMET-150"                                       : XSValues(-1.0, -1.0, 3.666,        -1.0),
        "TTJets_HT-600to800"                                             : XSValues(-1.0, -1.0, 2.7343862,    -1.0),
        "TTJets_HT-800to1200"                                            : XSValues(-1.0, -1.0, 1.12075054,   -1.0),
        "TTJets_HT-1200to2500"                                           : XSValues(-1.0, -1.0, 0.1979159,    -1.0),
        "TTJets_HT-2500toInf"                                            : XSValues(-1.0, -1.0, 0.002368366,  -1.0),
        "TTGamma_SingleLeptFromT"                                        : XSValues(-1.0, -1.0, 0.704,        -1.0),
        "TTGamma_SingleLeptFromTbar"                                     : XSValues(-1.0, -1.0, 0.704,        -1.0),
        "TTGamma_Dilept"                                                 : XSValues(-1.0, -1.0, 0.5804,       -1.0),
        "WJetsToLNu_HT-100To200"                                         : XSValues(-1.0, -1.0, 1627.45,      -1.0),
        "WJetsToLNu_HT-200To400"                                         : XSValues(-1.0, -1.0, 435.24,       -1.0),
        "WJetsToLNu_HT-400To600"                                         : XSValues(-1.0, -1.0, 59.18,        -1.0),
        "WJetsToLNu_HT-600To800"                                         : XSValues(-1.0, -1.0, 14.58,        -1.0),
        "WJetsToLNu_HT-800To1200"                                        : XSValues(-1.0, -1.0, 6.66,         -1.0),
        "WJetsToLNu_HT-1200To2500"                                       : XSValues(-1.0, -1.0, 1.608,        -1.0),
        "WJetsToLNu_HT-2500ToInf"                                        : XSValues(-1.0, -1.0, 0.03891,      -1.0),
        "WJetsToLNu"                                                     : XSValues(-1.0, -1.0, 61334.9,      -1.0),
        "QCD_FlatPt_15_3000HS"                                           : XSValues(-1.0, -1.0, 1356000000.0, -1.0),
        "QCD_HT200to300"                                                 : XSValues(-1.0, -1.0, 1717000,      -1.0),
        "QCD_HT300to500"                                                 : XSValues(-1.0, -1.0, 351300,       -1.0),
        "QCD_HT500to700"                                                 : XSValues(-1.0, -1.0, 31630,        -1.0),
        "QCD_HT700to1000"                                                : XSValues(-1.0, -1.0, 6802,         -1.0),
        "QCD_HT1000to1500"                                               : XSValues(-1.0, -1.0, 1206,         -1.0),
        "QCD_HT1500to2000"                                               : XSValues(-1.0, -1.0, 120.4,        -1.0),
        "QCD_HT2000toInf"                                                : XSValues(-1.0, -1.0, 25.24,        -1.0),
        "QCD_Pt_50to80"                                                  : XSValues(-1.0, -1.0, 19204300,     -1.0),
        "QCD_Pt_80to120"                                                 : XSValues(-1.0, -1.0, 2762530,      -1.0),
        "QCD_Pt_80_120"                                                  : XSValues(-1.0, -1.0, 2762530,      -1.0),
        "QCD_Pt_120to170"                                                : XSValues(-1.0, -1.0, 471100,       -1.0),
        "QCD_Pt_170to300"                                                : XSValues(-1.0, -1.0, 117276,       -1.0),
        "QCD_Pt_300to470"                                                : XSValues(-1.0, -1.0, 7823,         -1.0),
        "QCD_Pt_470to600"                                                : XSValues(-1.0, -1.0, 648.2,        -1.0),
        "QCD_Pt_600to800"                                                : XSValues(-1.0, -1.0, 186.9,        -1.0),
        "QCD_Pt_600_800"                                                 : XSValues(-1.0, -1.0, 186.9,        -1.0),
        "QCD_Pt_800to1000"                                               : XSValues(-1.0, -1.0, 32.293,       -1.0),
        "QCD_Pt_1000to1400"                                              : XSValues(-1.0, -1.0, 9.4183,       -1.0),
        "QCD_Pt_1400to1800"                                              : XSValues(-1.0, -1.0, 0.84265,      -1.0),
        "QCD_Pt_1800to2400"                                              : XSValues(-1.0, -1.0, 0.114943,     -1.0),
        "QCD_Pt_2400to3200"                                              : XSValues(-1.0, -1.0, 0.00682981,   -1.0),
        "QCD_Pt_3200toInf"                                               : XSValues(-1.0, -1.0, 0.000165445,  -1.0),
        "DYJetsToLL_M-50_HT-100to200"                                    : XSValues(-1.0, -1.0, 181.302,      -1.0),
        "DYJetsToLL_M-50_HT-200to400"                                    : XSValues(-1.0, -1.0, 50.4177,      -1.0),
        "DYJetsToLL_M-50_HT-400to600"                                    : XSValues(-1.0, -1.0, 6.98394,      -1.0),
        "DYJetsToLL_M-50_HT-600to800"                                    : XSValues(-1.0, -1.0, 1.68141,      -1.0),
        "DYJetsToLL_M-50_HT-800to1200"                                   : XSValues(-1.0, -1.0, 0.775392,     -1.0),
        "DYJetsToLL_M-50_HT-1200to2500"                                  : XSValues(-1.0, -1.0, 0.186222,     -1.0),
        "DYJetsToLL_M-50_HT-2500toInf"                                   : XSValues(-1.0, -1.0, 0.00438495,   -1.0),
        "DYJetsToLL_M-50"                                                : XSValues(-1.0, -1.0, 6025.2,       -1.0),
        "ZJetsToNuNu_HT-100To200"                                        : XSValues(-1.0, -1.0, 344.8305,     -1.0),
        "ZJetsToNuNu_HT-200To400"                                        : XSValues(-1.0, -1.0, 95.5341,      -1.0),
        "ZJetsToNuNu_HT-400To600"                                        : XSValues(-1.0, -1.0, 13.1979,      -1.0),
        "ZJetsToNuNu_HT-600To800"                                        : XSValues(-1.0, -1.0, 3.14757,      -1.0),
        "ZJetsToNuNu_HT-800To1200"                                       : XSValues(-1.0, -1.0, 1.450908,     -1.0),
        "ZJetsToNuNu_HT-1200To2500"                                      : XSValues(-1.0, -1.0, 0.3546459,    -1.0),
        "ZJetsToNuNu_HT-2500ToInf"                                       : XSValues(-1.0, -1.0, 0.00854235,   -1.0),
        "GJets_HT-100To200"                                              : XSValues(-1.0, -1.0, 9226,         -1.0),
        "GJets_HT-200To400"                                              : XSValues(-1.0, -1.0, 2300,         -1.0),
        "GJets_HT-400To600"                                              : XSValues(-1.0, -1.0, 277.4,        -1.0),
        "GJets_HT-600ToInf"                                              : XSValues(-1.0, -1.0, 93.38,        -1.0),
        "GJets_DR-0p4_HT-100To200"                                       : XSValues(-1.0, -1.0, 5000,         -1.0),
        "GJets_DR-0p4_HT-200To400"                                       : XSValues(-1.0, -1.0, 1079,         -1.0),
        "GJets_DR-0p4_HT-400To600"                                       : XSValues(-1.0, -1.0, 125.9,        -1.0),
        "GJets_DR-0p4_HT-600ToInf"                                       : XSValues(-1.0, -1.0, 43.36,        -1.0),
        "ZJetsToNuNu_Zpt-100to200"                                       : XSValues(-1.0, -1.0, 43.5543,      -1.0),
        "ZJetsToNuNu_Zpt-200toInf"                                       : XSValues(-1.0, -1.0, 5.28654,      -1.0),
        "ST_s-channel_4f_leptonDecays"                                   : XSValues(-1.0, -1.0, 3.34,         -1.0),
        "ST_s-channel_4f_InclusiveDecays"                                : XSValues(-1.0, -1.0, 10.32,        -1.0),
        "ST_t-channel_top_4f_inclusiveDecays"                            : XSValues(-1.0, -1.0, 136.02,       -1.0),
        "ST_t-channel_antitop_4f_inclusiveDecays"                        : XSValues(-1.0, -1.0, 80.95,        -1.0),
        "ST_tW_antitop_5f_NoFullyHadronicDecays"                         : XSValues(-1.0, -1.0, 19.4674,      -1.0),
        "ST_tW_top_5f_NoFullyHadronicDecays"                             : XSValues(-1.0, -1.0, 19.4674,      -1.0),
        "ST_tW_antitop_5f_inclusiveDecays"                               : XSValues(-1.0, -1.0, 35.6,         -1.0),
        "ST_tW_top_5f_inclusiveDecays"                                   : XSValues(-1.0, -1.0, 35.6,         -1.0),
        "tZq_W_lept_Z_hadron_4f_ckm"                                     : XSValues(-1.0, -1.0, 0.0758,       -1.0),
        "WW"                                                             : XSValues(-1.0, -1.0, 51.723,       -1.0),
        "WZ"                                                             : XSValues(-1.0, -1.0, 47.13,        -1.0),
        "ZZ"                                                             : XSValues(-1.0, -1.0, 16.523,       -1.0),
        "WWTo2L2Nu"                                                      : XSValues(-1.0, -1.0, 12.178,       -1.0),
        "WGJets_MonoPhoton_PtG-40to130"                                  : XSValues(-1.0, -1.0, 12.7,         -1.0),
        "WGJets_MonoPhoton_PtG-130"                                      : XSValues(-1.0, -1.0, 0.834,        -1.0),
        "WWTo1L1Nu2Q"                                                    : XSValues(-1.0, -1.0, 49.997,       -1.0),
        "WZTo1L1Nu2Q"                                                    : XSValues(-1.0, -1.0, 10.71,        -1.0),
        "WZTo1L3Nu"                                                      : XSValues(-1.0, -1.0, 3.058,        -1.0),
        "ZGTo2NuG"                                                       : XSValues(-1.0, -1.0, 32.3,         -1.0),
        "ZZTo2L2Q"                                                       : XSValues(-1.0, -1.0, 3.22,         -1.0),
        "ZZTo2Q2Nu"                                                      : XSValues(-1.0, -1.0, 4.04,         -1.0),
        "TTZToLLNuNu_M-10"                                               : XSValues(-1.0, -1.0, 0.2529,       -1.0),
        "TTZToQQ"                                                        : XSValues(-1.0, -1.0, 0.5297,       -1.0),
        "TTWJetsToLNu"                                                   : XSValues(-1.0, -1.0, 0.2043,       -1.0),
        "TTWJetsToLNu"                                                   : XSValues(-1.0, -1.0, 0.2043,       -1.0),
        "TTWJetsToQQ"                                                    : XSValues(-1.0, -1.0, 0.4026,       -1.0),
        "TTGJets"                                                        : XSValues(-1.0, -1.0, 3.697,        -1.0),
        "TTGJets"                                                        : XSValues(-1.0, -1.0, 3.697,        -1.0),
        "ttHJetToNonbb_M125"                                             : XSValues(-1.0, -1.0, 0.2118,       -1.0),
        "ttHJetTobb_M125"                                                : XSValues(-1.0, -1.0, 0.2953,       -1.0),
        "TTTT"                                                           : XSValues(-1.0, -1.0, 0.009103,     -1.0),
        "TTHH"                                                           : XSValues(-1.0, -1.0, 0.000741,     -1.0),
        "TTTW"                                                           : XSValues(-1.0, -1.0, 0.000861,     -1.0),
        "TTWH"                                                           : XSValues(-1.0, -1.0, 0.00136,      -1.0),
        "TTWW"                                                           : XSValues(-1.0, -1.0, 0.007834,     -1.0),
        "TTWZ"                                                           : XSValues(-1.0, -1.0, 0.00297,      -1.0),
        "TTZH"                                                           : XSValues(-1.0, -1.0, 0.00125,      -1.0),
        "TTZZ"                                                           : XSValues(-1.0, -1.0, 0.00157,      -1.0),
        "WWZ"                                                            : XSValues(-1.0, -1.0, 0.1651,       -1.0),
        "WZZ"                                                            : XSValues(-1.0, -1.0, 0.05565,      -1.0),
        "ZZZ"                                                            : XSValues(-1.0, -1.0, 0.01398,      -1.0),
        "SMS-T1bbbb_mGluino-1000_mLSP-900"                               : XSValues(-1.0, -1.0, 0.325388,     -1.0),
        "SMS-T1bbbb_mGluino-1500_mLSP-100"                               : XSValues(-1.0, -1.0, 0.0141903,    -1.0),
        "SMS-T1tttt_mGluino-1200_mLSP-800"                               : XSValues(-1.0, -1.0, 0.0856418,    -1.0),
        "SMS-T1tttt_mGluino-1500_mLSP-100"                               : XSValues(-1.0, -1.0, 0.0141903,    -1.0),
        "SMS-T1tttt_mGl-1500_mLSP-100"                                   : XSValues(-1.0, -1.0, 0.0141903,    -1.0),
        "SMS-T1tttt_mGluino-2000_mLSP-100"                               : XSValues(-1.0, -1.0, 0.000981077,  -1.0),
        "SMS-T1qqqq_mGluino-1000_mLSP-800"                               : XSValues(-1.0, -1.0, 0.325388,     -1.0),
        "SMS-T1qqqq_mGluino-1400_mLSP-100"                               : XSValues(-1.0, -1.0, 0.0252977,    -1.0),
        "SMS-T2tt_mStop-225_mLSP-50"                                     : XSValues(-1.0, -1.0, 36.3818,      -1.0),
        "SMS-T2tt_mStop-250_mLSP-150"                                    : XSValues(-1.0, -1.0, 21.5949,      -1.0),
        "SMS-T2tt_mStop-250_mLSP-50"                                     : XSValues(-1.0, -1.0, 21.5949,      -1.0),
        "SMS-T2tt_mStop-300_mLSP-150"                                    : XSValues(-1.0, -1.0, 249.409,      -1.0),
        "SMS-T2tt_mStop-325_mLSP-150"                                    : XSValues(-1.0, -1.0, 249.409,      -1.0),
        "SMS-T2tt_mStop-425_mLSP-325"                                    : XSValues(-1.0, -1.0, 1.31169,      -1.0),
        "SMS-T2tt_mStop-500_mLSP-325"                                    : XSValues(-1.0, -1.0, 0.51848,      -1.0),
        "SMS-T2tt_mStop-650_mLSP-350"                                    : XSValues(-1.0, -1.0, 0.107045,     -1.0),
        "SMS-T2tt_mStop-850_mLSP-100"                                    : XSValues(-1.0, -1.0, 0.0189612,    -1.0),
        "SMS-T2tt_mStop-1200_mLSP-100"                                   : XSValues(-1.0, -1.0, 0.00159844,   -1.0),
        "SMS-T5qqqqWW_mGluino-1900_mLSP-100"                             : XSValues(-1.0, -1.0, 0.00163547,   -1.0),
        "SMS-T5qqqqZH-mGluino750"                                        : XSValues(-1.0, -1.0, 2.26585,      -1.0),
        "SMS-T5qqqqZH-mGluino1000"                                       : XSValues(-1.0, -1.0, 0.325388,     -1.0),
        "SMS-T5qqqqZH-mGluino1100"                                       : XSValues(-1.0, -1.0, 0.163491,     -1.0),
        "SMS-T5qqqqZH-mGluino1200"                                       : XSValues(-1.0, -1.0, 0.0856418,    -1.0),
        "SMS-T5qqqqZH-mGluino1300"                                       : XSValues(-1.0, -1.0, 0.0460525,    -1.0),
        "SMS-T5qqqqZH-mGluino1400"                                       : XSValues(-1.0, -1.0, 0.0252977,    -1.0),
        "SMS-T5qqqqZH-mGluino1500"                                       : XSValues(-1.0, -1.0, 0.0141903,    -1.0),
        "SMS-T5qqqqZH-mGluino1600"                                       : XSValues(-1.0, -1.0, 0.00810078,   -1.0),
        "SMS-T5qqqqZH-mGluino1700"                                       : XSValues(-1.0, -1.0, 0.00470323,   -1.0),
        "SMS-T5qqqqZH-mGluino1800"                                       : XSValues(-1.0, -1.0, 0.00276133,   -1.0),
        "SMS-T5qqqqZH-mGluino1900"                                       : XSValues(-1.0, -1.0, 0.00163547,   -1.0),
        "SMS-T5qqqqZH-mGluino2000"                                       : XSValues(-1.0, -1.0, 0.000981077,  -1.0),
        "SMS-T5qqqqZH-mGluino2100"                                       : XSValues(-1.0, -1.0, 0.000591918,  -1.0),
        "SMS-T5qqqqZH-mGluino2200"                                       : XSValues(-1.0, -1.0, 0.000359318,  -1.0),
        "SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1"                     : XSValues(-1.0, -1.0, 0.002548,     -1.0),
        "SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230"                : XSValues(-1.0, -1.0, 0.6204,       -1.0),
        "mZprime-1000"                                                   : XSValues(-1.0, -1.0, 4.612,        -1.0),
        "mZprime-2000"                                                   : XSValues(-1.0, -1.0, 0.1849,       -1.0),
        "mZprime-3000"                                                   : XSValues(-1.0, -1.0, 0.0155,       -1.0),
        "mZprime-4000"                                                   : XSValues(-1.0, -1.0, 0.001688,     -1.0),
        "stealth_stop_350_singlino_SYY"                                  : XSValues(-1.0, -1.0, 3.78661,      -1.0),
        "stealth_stop_450_singlino_SYY"                                  : XSValues(-1.0, -1.0, 0.948333,     -1.0),
        "stealth_stop_550_singlino_SYY"                                  : XSValues(-1.0, -1.0, 0.296128,     -1.0),
        "stealth_stop_650_singlino_SYY"                                  : XSValues(-1.0, -1.0, 0.107045,     -1.0),
        "stealth_stop_750_singlino_SYY"                                  : XSValues(-1.0, -1.0, 0.0431418,    -1.0),
        "stealth_stop_850_singlino_SYY"                                  : XSValues(-1.0, -1.0, 0.0189612,    -1.0),
        "stealth_stop_350_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 3.78661,      -1.0),
        "stealth_stop_450_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 0.948333,     -1.0),
        "stealth_stop_550_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 0.296128,     -1.0),
        "stealth_stop_650_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 0.107045,     -1.0),
        "stealth_stop_750_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 0.0431418,    -1.0),
        "stealth_stop_850_singlino_SHuHd"                                : XSValues(-1.0, -1.0, 0.0189612,    -1.0),
        # Stealth taken From https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "StealthSYY_2t6j_mStop-300_mSo-100"                              : XSValues(-1.0, -1.0, 8.51615,      -1.0),
        "StealthSYY_2t6j_mStop-500_mSo-100"                              : XSValues(-1.0, -1.0, 0.51848,      -1.0),
        "StealthSHH_2t4b_mStop-350_mSo-100"                              : XSValues(-1.0, -1.0, 3.78661,      -1.0),
        "StealthSHH_2t4b_mStop-500_mSo-100"                              : XSValues(-1.0, -1.0, 0.51848,      -1.0),
        "rpv_stop_350_t3j_uds"                                           : XSValues(-1.0, -1.0, 3.78661,      -1.0),
        "rpv_stop_450_t3j_uds"                                           : XSValues(-1.0, -1.0, 0.948333,     -1.0),
        "rpv_stop_550_t3j_uds"                                           : XSValues(-1.0, -1.0, 0.296128,     -1.0),
        "rpv_stop_650_t3j_uds"                                           : XSValues(-1.0, -1.0, 0.107045,     -1.0),
        "rpv_stop_750_t3j_uds"                                           : XSValues(-1.0, -1.0, 0.0431418,    -1.0),
        "rpv_stop_850_t3j_uds"                                           : XSValues(-1.0, -1.0, 0.0189612,    -1.0),
        # RPV taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "RPV_2t6j_mStop-350_mN1-100"                                     : XSValues(-1.0, -1.0, 3.78661,      -1.0),
        "RPV_2t6j_mStop-500_mN1-100"                                     : XSValues(-1.0, -1.0, 0.51848,      -1.0),
    }

    __names_to_strip = {
        "generators" : ["(.pythia)([^_-]*)","(.powheg)([^_-]*)","(.madgraph)([^_-]*)","(.madspin)([^_-]*)","(.amcatnlo)([^_-]*)"],
        "tunes"      : ["(.Tune)([^_]*)"],
        "added_info" : ["(.PSweights)([^_]*)"],
        "other"      : ["(.NLO)([^_-]*)","^\s*(RelVal\s*)?|(\s*_13)?\s*$","step4_MINIAOD_2016_","step4_MINIAOD_","(.mDark)(.*)","(.isr|.fsr)(up|down)","([_|-]v)([0-9]*)"],
    }

    def get_cm_energy(self, name):
        energy_result = re.search("(_[0-9]*TeV)",name)
        # allow a default value
        energy = "_13TeV" if energy_result is None else energy_result.group(0)
        return (re.sub("(_[0-9]*TeV)","",name),energy)

    def get_minimal_name(self, name):
        for category, values_to_strip in self.__names_to_strip.iteritems():
            for regex_value in values_to_strip:
                name = re.sub(regex_value,"",name)
        return name

    def get_xs(self, name):
        name_minimal = self.get_minimal_name(name)
        name_minimal, energy = self.get_cm_energy(name_minimal)
        return self.__xs_dict[name_minimal].__getattribute__("CME"+energy)

class MCSample():

    '''
    Example use:
    from TreeMaker.WeightProducer.MCSample import MCSample
    m = MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10139950, 0)
    '''

    __helper = MCSampleHelper()

    def __init__(self, name, production, mcVersion, Method, NumberEvtsTotal, WrongPU = False, NumberEvtsDiff = None):
        self.name = name
        self.production = production
        self.mcVersion = mcVersion
        self.Method = Method
        self.XS = self.get_xs(name)
        self.NumberEvtsTotal = NumberEvtsTotal
        self.WrongPU = WrongPU
        self.NumberEvtsDiff = NumberEvtsTotal if NumberEvtsDiff==None else NumberEvtsDiff

    def get_effective_lumi(self):
        #NumberEvtsTotal = NumberEvtsPos + NumberEvtsNeg
        #NumberEvtsDiff = NumberEvtsPos - NumberEvtsNeg
        #NumberEvtsTotal - NumberEvtsDiff = 2 * NumberEvtsNeg
        #==>NumberEvtsNeg = (NumberEvtsTotal - NumberEvtsDiff) / 2
        #lumi_eff = N_all/xs * (1-2*(N_neg/N_all))^2
        NumberEvtsNeg = (self.NumberEvtsTotal - self.NumberEvtsDiff)/2.0
        return (self.NumberEvtsTotal/self.XS)*((1.0-(2.0*(NumberEvtsNeg/self.NumberEvtsTotal))) ** 2)

    def get_xs(self, name):
        return self.__helper.get_xs(name)

    def __repr__(self):
        return "%s(%r, %r, %r, %r, %i, %r)" % (self.__class__.__name__, self.name,self.production,self.mcVersion,self.Method,self.NumberEvtsTotal,self.WrongPU) if self.NumberEvtsTotal==self.NumberEvtsDiff else "%s(%r, %r, %r, %r, %i, %r, %i)" % (self.__class__.__name__, self.name,self.production,self.mcVersion,self.Method,self.NumberEvtsTotal,self.WrongPU,self.NumberEvtsDiff)

    def __str__(self):
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
                rep_format += (key_format+": {:<"+str(len(str(self.NumberEvtsDiff)))+"}")
                rep_format += ")"
        return rep_format.format('name',self.name,' ','production',self.production,' ','mcVersion',self.mcVersion,' ','Method',self.Method,' ','XS',self.XS,' ','NumberEvtsTotal',self.NumberEvtsTotal,' ','WrongPU',self.WrongPU,' ','NumberEvtsDiff',self.NumberEvtsDiff)
