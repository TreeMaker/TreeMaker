from TreeMaker.WeightProducer.namedtuple_with_defaults import namedtuple_with_defaults
import re

class MCSampleHelper():

	__energy_dict = {
		"2010" : "7TeV",
		"2011" : "7TeV",
		"2012" : "8TeV",
		"2015" : "13TeV",
		"2016" : "13TeV",
		"2017" : "13TeV",
		"2018" : "13TeV",
	}

	__names_to_strip = {
		"generators"	: ["(.pythia)([^_-]*)","(.powheg)([^_-]*)","(.madgraph)([^_-]*)","(.madspin)([^_-]*)","(.amcatnlo)([^_-]*)"],
		"tunes"			: ["(.Tune)([^_]*)"],
		"added_info"	: ["(.PSweights)([^_]*)"],
		"other"			: ["(.NLO)([^_-]*)","^\s*(RelVal\s*)?|(\s*_13)?\s*$","step4_MINIAOD_2016_","step4_MINIAOD_","(.mDark)(.*)","(.isr|.fsr)(up|down)","([_|-]v)([0-9]*)","(.mWCutfix)","([_])(ttHtranche3)"],
	}

	def __init__(self, extra_dicts_energy=None, extra_dicts_strip=None):
		if extra_dicts_energy is not None:
			for extra in extra_dicts_energy:
				self.__energy_dict.update(extra)
		if extra_dicts_strip is not None:
			for extra in extra_dicts_strip:
				self.__names_to_strip.update(extra)

	def get_cm_energy(self, name):
		energy_result = re.search("(_[0-9]*TeV)",name)
		# allow a default value
		energy = "_13TeV" if energy_result is None else energy_result.group(0)
		return (re.sub("(_[0-9]*TeV)","",name),energy)

	def get_cm_energy_by_year(self, year):
		return self.__energy_dict[year]

	def get_minimal_name(self, name):
		for category, values_to_strip in self.__names_to_strip.iteritems():
			for regex_value in values_to_strip:
				name = re.sub(regex_value,"",name)
		name, energy = self.get_cm_energy(name)
		return name

	def get_year(self, mcVersion):
		year_result = re.search("[0-9]*MiniAOD",mcVersion)
		year = "2016" if year_result is None else "20"+year_result.group(0).split("MiniAOD")[0]
		return year

class MCSampleValuesHelper():
	
	__years = ['2010','2011','2012','2015','2016','2017','2018']
	__energies = ["7TeV","8TeV","13TeV"]
	__xs_field_names = []
	__kfactor_field_names = []
	for year in __years+__energies:
		__xs_field_names.append('XS_'+year)
		__xs_field_names.append('XSSource_'+year)
		__kfactor_field_names.append('kFactor_'+year)
		__kfactor_field_names.append('kFactorSource_'+year)
	XSValues = namedtuple_with_defaults('XSValues', __xs_field_names, [-1.0,""]*len(__years+__energies))
	kFactorValues = namedtuple_with_defaults('kFactorValues', __kfactor_field_names, [1.0,""]*len(__years+__energies))


	__values_dict = {
		"TT"												: {
			"CrossSection" : XSValues(XS_13TeV=831.76), 
		},
		"TTJets"											: {
			"CrossSection" : XSValues(XS_13TeV=831.76),
		},
		"TTbar"												: {
			"CrossSection" : XSValues(XS_13TeV=831.76),
		},
		# ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
		"TTJets_SingleLeptFromT"							: {
			"CrossSection" : XSValues(XS_13TeV=182.72),
		},
		"TTJets_SingleLeptFromTbar"							: {
			"CrossSection" : XSValues(XS_13TeV=182.72),
		},
		"TTJets_DiLept"										: {
			"CrossSection" : XSValues(XS_13TeV=88.34),
		},
		# MET binned: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs LO), 831.76/511.3 = 1.627
		"TTJets_SingleLeptFromT_genMET-150"					: {
			"CrossSection" : XSValues(XS_2016=9.683904),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTJets_SingleLeptFromTbar_genMET-150"				: {
			"CrossSection" : XSValues(XS_2016=9.657872),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTJets_DiLept_genMET-150"							: {
			"CrossSection" : XSValues(XS_2016=5.919026),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		# HT binned: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs LO), 831.76/511.3 = 1.627
		"TTJets_HT-600to800"								: {
			"CrossSection" : XSValues(XS_2016=2.68455),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTJets_HT-800to1200"								: {
			"CrossSection" : XSValues(XS_2016=1.0959472),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTJets_HT-1200to2500"								: {
			"CrossSection" : XSValues(XS_2016=0.1942638),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTJets_HT-2500toInf"								: {
			"CrossSection" : XSValues(XS_2016=0.002351015),
			"kFactor" : kFactorValues(kFactor_2016=1.627),
		},
		"TTTo2L2Nu"											: {
			"CrossSection" : XSValues(XS_2016=88.29),
		},
		"TTToHadronic"										: {
			"CrossSection" : XSValues(XS_2016=377.96),
		},
		"TTToSemiLeptonic"									: {
			"CrossSection" : XSValues(XS_2016=365.34),
		},
		"TTGamma_SingleLeptFromT"							: {
			"CrossSection" : XSValues(XS_2016=0.704),
		},
		"TTGamma_SingleLeptFromTbar"						: {
			"CrossSection" : XSValues(XS_2016=0.704),
		},
		"TTGamma_Dilept"									: {
			"CrossSection" : XSValues(XS_2016=0.5804),
		},
		# WJets: k-factor of 1.21 applied
		"WJetsToLNu_HT-70To100"								: {
			"CrossSection" : XSValues(XS_2016=1637.13), #From XSDB and not summary page
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-100To200"							: {
			"CrossSection" : XSValues(XS_2016=1627.45),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-200To400"							: {
			"CrossSection" : XSValues(XS_2016=435.24),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-400To600"							: {
			"CrossSection" : XSValues(XS_2016=59.18),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-600To800"							: {
			"CrossSection" : XSValues(XS_2016=14.58),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-800To1200"							: {
			"CrossSection" : XSValues(XS_2016=6.66),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-1200To2500"							: {
			"CrossSection" : XSValues(XS_2016=1.608),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu_HT-2500ToInf"							: {
			"CrossSection" : XSValues(XS_2016=0.03891),
			"kFactor" : kFactorValues(kFactor_2016=1.21),
		},
		"WJetsToLNu"										: {
			"CrossSection" : XSValues(XS_2016=61334.9),
		},
		"QCD_FlatPt_15_3000HS"								: {
			"CrossSection" : XSValues(XS_2016=1356000000.0),
		},
		"QCD_HT200to300"									: {
			"CrossSection" : XSValues(XS_2016=1717000),
		},
		"QCD_HT300to500"									: {
			"CrossSection" : XSValues(XS_2016=351300),
		},
		"QCD_HT500to700"									: {
			"CrossSection" : XSValues(XS_2016=31630),
		},
		"QCD_HT700to1000"									: {
			"CrossSection" : XSValues(XS_2016=6802),
		},
		"QCD_HT1000to1500"									: {
			"CrossSection" : XSValues(XS_2016=1206),
		},
		"QCD_HT1500to2000"									: {
			"CrossSection" : XSValues(XS_2016=120.4),
		},
		"QCD_HT2000toInf"									: {
			"CrossSection" : XSValues(XS_2016=25.24),
		},
		# QCD pT-hat binned MuEnrichedPt5: No k-factor applied (2017 TuneCP5 XSDB values)
		"QCD_Pt-15to20_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=2799000.0),
		},
		"QCD_Pt-20to30_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=2526000.0),
		},
		"QCD_Pt-30to50_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=1362000.0),
		},
		"QCD_Pt-50to80_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=376600.0),
		},
		"QCD_Pt-80to120_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=88930.0),
		},
		"QCD_Pt-120to170_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=21230.0),
		},
		"QCD_Pt-170to300_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=7055.0),
		},
		"QCD_Pt-300to470_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=797.35),
		},
		"QCD_Pt-470to600_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=59.24),
		},
		"QCD_Pt-600to800_MuEnrichedPt5"						: {
			"CrossSection" : XSValues(XS_2016=25.25), #2016 TuneCUETP8M1 XSDB value
		},
		"QCD_Pt-800to1000_MuEnrichedPt5"					: {
			"CrossSection" : XSValues(XS_2016=4.723), #2016 TuneCUETP8M1 XSDB value
		},
		"QCD_Pt-1000toInf_MuEnrichedPt5"					: {
			"CrossSection" : XSValues(XS_2016=1.613), #2016 TuneCUETP8M1 XSDB value
		},
		# QCD pT-hat binned: cross sections from AN2017_013_v17
		"QCD_Pt-15to7000"									: {
			"CrossSection" : XSValues(XS_2016=1372000000.0), #2018 TuneCP5 GenXsecAnalyzer value
		},
		"QCD_Pt_50to80"										: {
			"CrossSection" : XSValues(XS_2016=19204300.0),
		},
		"QCD_Pt_80to120"									: {
			"CrossSection" : XSValues(XS_2016=2762530.0),
		},
		"QCD_Pt_80_120"										: {
			"CrossSection" : XSValues(XS_2016=2762530.0),
		},
		"QCD_Pt_120to170"									: {
			"CrossSection" : XSValues(XS_2016=471100.0),
		},
		"QCD_Pt_170to300"									: {
			"CrossSection" : XSValues(XS_2016=117276.0),
		},
		"QCD_Pt_300to470"									: {
			"CrossSection" : XSValues(XS_2016=7823.0),
		},
		"QCD_Pt_470to600"									: {
			"CrossSection" : XSValues(XS_2016=648.2),
		},
		"QCD_Pt_600to800"									: {
			"CrossSection" : XSValues(XS_2016=186.9),
		},
		"QCD_Pt_600_800"									: {
			"CrossSection" : XSValues(XS_2016=186.9),
		},
		"QCD_Pt_800to1000"									: {
			"CrossSection" : XSValues(XS_2016=32.293),
		},
		"QCD_Pt_1000to1400"									: {
			"CrossSection" : XSValues(XS_2016=9.4183),
		},
		"QCD_Pt_1400to1800"									: {
			"CrossSection" : XSValues(XS_2016=0.84265),
		},
		"QCD_Pt_1800to2400"									: {
			"CrossSection" : XSValues(XS_2016=0.114943),
		},
		"QCD_Pt_2400to3200"									: {
			"CrossSection" : XSValues(XS_2016=0.00682981),
		},
		"QCD_Pt_3200toInf"									: {
			"CrossSection" : XSValues(XS_2016=0.000165445),
		},
		# DY/Z: k-factor of 1.23 applied
		"DYJetsToLL_M-50_HT-100to200"						: {
			"CrossSection" : XSValues(XS_2016=181.302),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-200to400"						: {
			"CrossSection" : XSValues(XS_2016=50.4177),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-400to600"						: {
			"CrossSection" : XSValues(XS_2016=6.98394),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-600to800"						: {
			"CrossSection" : XSValues(XS_2016=1.68141),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-800to1200"						: {
			"CrossSection" : XSValues(XS_2016=0.775392),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-1200to2500"						: {
			"CrossSection" : XSValues(XS_2016=0.186222),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50_HT-2500toInf"						: {
			"CrossSection" : XSValues(XS_2016=0.00438495),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"DYJetsToLL_M-50"									: {
			"CrossSection" : XSValues(XS_2016=6025.2),
		},
		"ZJetsToNuNu_HT-100To200"							: {
			"CrossSection" : XSValues(XS_2016=344.8305),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-200To400"							: {
			"CrossSection" : XSValues(XS_2016=95.5341),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-400To600"							: {
			"CrossSection" : XSValues(XS_2016=13.1979),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-600To800"							: {
			"CrossSection" : XSValues(XS_2016=3.14757),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-800To1200"							: {
			"CrossSection" : XSValues(XS_2016=1.450908),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-1200To2500"							: {
			"CrossSection" : XSValues(XS_2016=0.3546459),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"ZJetsToNuNu_HT-2500ToInf"							: {
			"CrossSection" : XSValues(XS_2016=0.00854235),
			"kFactor" : kFactorValues(kFactor_2016=1.23),
		},
		"GJets_HT-100To200"									: {
			"CrossSection" : XSValues(XS_2016=9226.0),
		},
		"GJets_HT-200To400"									: {
			"CrossSection" : XSValues(XS_2016=2300.0),
		},
		"GJets_HT-400To600"									: {
			"CrossSection" : XSValues(XS_2016=277.4),
		},
		"GJets_HT-600ToInf"									: {
			"CrossSection" : XSValues(XS_2016=93.38),
		},
		"GJets_DR-0p4_HT-100To200"							: {
			"CrossSection" : XSValues(XS_2016=5000.0),
		},
		"GJets_DR-0p4_HT-200To400"							: {
			"CrossSection" : XSValues(XS_2016=1079.0),
		},
		"GJets_DR-0p4_HT-400To600"							: {
			"CrossSection" : XSValues(XS_2016=125.9),
		},
		"GJets_DR-0p4_HT-600ToInf"							: {
			"CrossSection" : XSValues(XS_2016=43.36),
		},
		"ZJetsToNuNu_Zpt-100to200"							: {
			"CrossSection" : XSValues(XS_2016=43.5543),
		},
		"ZJetsToNuNu_Zpt-200toInf"							: {
			"CrossSection" : XSValues(XS_2016=5.28654),
		},
		# single top: NoFullyHadronicDecays xsec scaled by BF for non-fully-hadronic (1-(1-3*0.108)^2)
		"ST_s-channel_4f_leptonDecays"						: {
			"CrossSection" : XSValues(XS_13TeV=3.34),
		},
		"ST_s-channel_4f_InclusiveDecays"					: {
			"CrossSection" : XSValues(XS_13TeV=10.32),
		},
		"ST_t-channel_top_4f_inclusiveDecays"				: {
			"CrossSection" : XSValues(XS_13TeV=136.02),
		},
		"ST_t-channel_antitop_4f_inclusiveDecays"			: {
			"CrossSection" : XSValues(XS_13TeV=80.95),
		},
		"ST_tW_antitop_5f_NoFullyHadronicDecays"			: {
			"CrossSection" : XSValues(XS_13TeV=19.4674),
		},
		"ST_tW_top_5f_NoFullyHadronicDecays"				: {
			"CrossSection" : XSValues(XS_13TeV=19.4674),
		},
		"ST_tW_antitop_5f_inclusiveDecays"					: {
			"CrossSection" : XSValues(XS_13TeV=35.6),
		},
		"ST_tW_top_5f_inclusiveDecays"						: {
			"CrossSection" : XSValues(XS_13TeV=35.6),
		},
		"tZq_W_lept_Z_hadron_4f_ckm"						: {
			"CrossSection" : XSValues(XS_2016=0.0758),
		},
		"WW"												: {
			"CrossSection" : XSValues(XS_2016=51.723),
		},
		"WZ"												: {
			"CrossSection" : XSValues(XS_2016=47.13),
		},
		"ZZ"												: {
			"CrossSection" : XSValues(XS_2016=16.523),
		},
		"WWTo2L2Nu"											: {
			"CrossSection" : XSValues(XS_2016=12.178),
		},
		"WGJets_MonoPhoton_PtG-40to130"						: {
			"CrossSection" : XSValues(XS_2016=12.7),
		},
		"WGJets_MonoPhoton_PtG-130"							: {
			"CrossSection" : XSValues(XS_2016=0.834),
		},
		"WWTo1L1Nu2Q"										: {
			"CrossSection" : XSValues(XS_2016=49.997),
		},
		"WZTo1L1Nu2Q"										: {
			"CrossSection" : XSValues(XS_2016=10.71),
		},
		"WZTo1L3Nu"											: {
			"CrossSection" : XSValues(XS_2016=3.058),
		},
		"ZGTo2NuG"											: {
			"CrossSection" : XSValues(XS_2016=32.3),
		},
		"ZZTo2L2Q"											: {
			"CrossSection" : XSValues(XS_2016=3.22),
		},
		"ZZTo2Q2Nu"											: {
			"CrossSection" : XSValues(XS_2016=4.04),
		},
		"TTZToLLNuNu_M-10"									: {
			"CrossSection" : XSValues(XS_2016=0.2529),
		},
		"TTZToQQ"											: {
			"CrossSection" : XSValues(XS_2016=0.5297),
		},
		"TTWJetsToLNu"										: {
			"CrossSection" : XSValues(XS_2016=0.2043),
		},
		"TTWJetsToLNu"										: {
			"CrossSection" : XSValues(XS_2016=0.2043),
		},
		"TTWJetsToQQ"										: {
			"CrossSection" : XSValues(XS_2016=0.4026),
		},
		"TTGJets"											: {
			"CrossSection" : XSValues(XS_2016=3.697),
		},
		"TTGJets"											: {
			"CrossSection" : XSValues(XS_2016=3.697),
		},
		"ttHJetToNonbb_M125"								: {
			"CrossSection" : XSValues(XS_2016=0.2118),
		},
		"ttHJetTobb_M125"									: {
			"CrossSection" : XSValues(XS_2016=0.2953),
		},
		"TTTT"												: {
			"CrossSection" : XSValues(XS_2016=0.009103),
		},
		"TTHH"												: {
			"CrossSection" : XSValues(XS_2016=0.000741),
		},
		"TTTW"												: {
			"CrossSection" : XSValues(XS_2016=0.000861),
		},
		"TTWH"												: {
			"CrossSection" : XSValues(XS_2016=0.00136),
		},
		"TTWW"												: {
			"CrossSection" : XSValues(XS_2016=0.006979),
		},
		"TTWZ"												: {
			"CrossSection" : XSValues(XS_2016=0.00297),
		},
		"TTZH"												: {
			"CrossSection" : XSValues(XS_2016=0.00125),
		},
		"TTZZ"												: {
			"CrossSection" : XSValues(XS_2016=0.00157),
		},
		"TTTJ"												: {
			"CrossSection" : XSValues(XS_2016=0.0004812),
		},
		"WWW_4F"											: {
			"CrossSection" : XSValues(XS_2016=0.2086),
		},
		"WWZ_4F"											: {
			"CrossSection" : XSValues(XS_2016=0.1651),
		},
		"WWZ"												: {
			"CrossSection" : XSValues(XS_2016=0.1651),
		},
		"WZZ"												: {
			"CrossSection" : XSValues(XS_2016=0.05565),
		},
		"ZZZ"												: {
			"CrossSection" : XSValues(XS_2016=0.01398),
		},
		"SMS-T1bbbb_mGluino-1000_mLSP-900"					: {
			"CrossSection" : XSValues(XS_13TeV=0.385E+00),
		},
		"SMS-T1bbbb_mGluino-1500_mLSP-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.157E-01),
		},
		"SMS-T1tttt_mGluino-1200_mLSP-800"					: {
			"CrossSection" : XSValues(XS_13TeV=0.985E-01),
		},
		"SMS-T1tttt_mGluino-1500_mLSP-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.157E-01),
		},
		"SMS-T1tttt_mGl-1500_mLSP-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.157E-01),
		},
		"SMS-T1tttt_mGluino-2000_mLSP-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.101E-02),
		},
		"SMS-T1qqqq_mGluino-1000_mLSP-800"					: {
			"CrossSection" : XSValues(XS_13TeV=0.385E+00),
		},
		"SMS-T1qqqq_mGluino-1400_mLSP-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.284E-01),
		},
		"SMS-T1qqqq_mGluino-1800_mLSP-200_ctau-1"			: {
			"CrossSection" : XSValues(XS_13TeV=0.293E-02),
		},
		"SMS-T2tt_mStop-150_mLSP-50"						: {
			"CrossSection" : XSValues(XS_13TeV=0.304E+03),
		},
		"SMS-T2tt_mStop-200_mLSP-50"						: {
			"CrossSection" : XSValues(XS_13TeV=0.755E+02),
		},
		"SMS-T2tt_mStop-225_mLSP-50"						: {
			"CrossSection" : XSValues(XS_13TeV=0.420E+02),
		},
		"SMS-T2tt_mStop-250_mLSP-150"						: {
			"CrossSection" : XSValues(XS_13TeV=0.248E+02),
		},
		"SMS-T2tt_mStop-250_mLSP-50"						: {
			"CrossSection" : XSValues(XS_13TeV=0.248E+02),
		},
		"SMS-T2tt_mStop-300_mLSP-150"						: {
			"CrossSection" : XSValues(XS_13TeV=0.100E+02),
		},
		"SMS-T2tt_mStop-325_mLSP-150"						: {
			"CrossSection" : XSValues(XS_13TeV=0.657E+01),
		},
		"SMS-T2tt_mStop-350_mLSP-150"						: {
			"CrossSection" : XSValues(XS_13TeV=0.443E+01),
		},
		"SMS-T2tt_mStop-425_mLSP-325"						: {
			"CrossSection" : XSValues(XS_13TeV=0.154E+01),
		},
		"SMS-T2tt_mStop-500_mLSP-325"						: {
			"CrossSection" : XSValues(XS_13TeV=0.609E+00),
		},
		"SMS-T2tt_mStop-650_mLSP-350"						: {
			"CrossSection" : XSValues(XS_13TeV=0.125E+00),
		},
		"SMS-T2tt_mStop-850_mLSP-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.216E-01),
		},
		"SMS-T2tt_mStop-1200_mLSP-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.170E-02),
		},
		"SMS-T5qqqqWW_mGluino-1900_mLSP-100"				: {
			"CrossSection" : XSValues(XS_13TeV=0.171E-02),
		},
		"SMS-T5qqqqZH-mGluino750"							: {
			"CrossSection" : XSValues(XS_13TeV=0.277E+01),
		},
		"SMS-T5qqqqZH-mGluino1000"							: {
			"CrossSection" : XSValues(XS_13TeV=0.385E+00),
		},
		"SMS-T5qqqqZH-mGluino1100"							: {
			"CrossSection" : XSValues(XS_13TeV=0.191E+00),
		},
		"SMS-T5qqqqZH-mGluino1200"							: {
			"CrossSection" : XSValues(XS_13TeV=0.985E-01),
		},
		"SMS-T5qqqqZH-mGluino1300"							: {
			"CrossSection" : XSValues(XS_13TeV=0.522E-01),
		},
		"SMS-T5qqqqZH-mGluino1400"							: {
			"CrossSection" : XSValues(XS_13TeV=0.284E-01),
		},
		"SMS-T5qqqqZH-mGluino1500"							: {
			"CrossSection" : XSValues(XS_13TeV=0.157E-01),
		},
		"SMS-T5qqqqZH-mGluino1600"							: {
			"CrossSection" : XSValues(XS_13TeV=0.887E-02),
		},
		"SMS-T5qqqqZH-mGluino1700"							: {
			"CrossSection" : XSValues(XS_13TeV=0.507E-02),
		},
		"SMS-T5qqqqZH-mGluino1800"							: {
			"CrossSection" : XSValues(XS_13TeV=0.293E-02),
		},
		"SMS-T5qqqqZH-mGluino1900"							: {
			"CrossSection" : XSValues(XS_13TeV=0.171E-02),
		},
		"SMS-T5qqqqZH-mGluino2000"							: {
			"CrossSection" : XSValues(XS_13TeV=0.101E-02),
		},
		"SMS-T5qqqqZH-mGluino2100"							: {
			"CrossSection" : XSValues(XS_13TeV=0.598E-03),
		},
		"SMS-T5qqqqZH-mGluino2200"							: {
			"CrossSection" : XSValues(XS_13TeV=0.321E-03),
		},
		"SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1"		: {
			"CrossSection" : XSValues(XS_13TeV=0.002548),
		},
		"SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230"	: {
			"CrossSection" : XSValues(XS_13TeV=0.6204),
		},
		"SMS-TChiWZ_ZToLL_mZMin-0p1"						: {
			"CrossSection" : XSValues(XS_13TeV=0.6204),
		},
		"stealth_stop_350_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"stealth_stop_450_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"stealth_stop_550_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"stealth_stop_650_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"stealth_stop_750_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"stealth_stop_850_singlino_SYY"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		"stealth_stop_350_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"stealth_stop_450_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"stealth_stop_550_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"stealth_stop_650_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"stealth_stop_750_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"stealth_stop_850_singlino_SHuHd"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		# Stealth taken From https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
		"StealthSYY_2t6j_mStop-300_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=8.51615),
		},
		"StealthSYY_2t6j_mStop-300_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=8.51615),
		},
		"StealthSYY_2t6j_mStop-350_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"StealthSYY_2t6j_mStop-350_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"StealthSYY_2t6j_mStop-400_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=1.83537),
		},
		"StealthSYY_2t6j_mStop-400_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=1.83537),
		},
		"StealthSYY_2t6j_mStop-450_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"StealthSYY_2t6j_mStop-450_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"StealthSYY_2t6j_mStop-500_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.51848),
		},
		"StealthSYY_2t6j_mStop-500_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.51848),
		},
		"StealthSYY_2t6j_mStop-550_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"StealthSYY_2t6j_mStop-550_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"StealthSYY_2t6j_mStop-600_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.174599),
		},
		"StealthSYY_2t6j_mStop-600_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.174599),
		},
		"StealthSYY_2t6j_mStop-650_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"StealthSYY_2t6j_mStop-650_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"StealthSYY_2t6j_mStop-700_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0670476),
		},
		"StealthSYY_2t6j_mStop-700_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0670476),
		},
		"StealthSYY_2t6j_mStop-750_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"StealthSYY_2t6j_mStop-750_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"StealthSYY_2t6j_mStop-800_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0283338),
		},
		"StealthSYY_2t6j_mStop-800_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0283338),
		},
		"StealthSYY_2t6j_mStop-850_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		"StealthSYY_2t6j_mStop-850_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		"StealthSYY_2t6j_mStop-900_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0128895),
		},
		"StealthSYY_2t6j_mStop-900_mN1-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0128895),
		},
		"StealthSHH_2t4b_mStop-300_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=8.51615),
		},
		"StealthSHH_2t4b_mStop-350_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"StealthSHH_2t4b_mStop-400_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=1.83537),
		},
		"StealthSHH_2t4b_mStop-450_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"StealthSHH_2t4b_mStop-500_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.51848),
		},
		"StealthSHH_2t4b_mStop-550_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"StealthSHH_2t4b_mStop-600_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.174599),
		},
		"StealthSHH_2t4b_mStop-650_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"StealthSHH_2t4b_mStop-700_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0670476),
		},
		"StealthSHH_2t4b_mStop-750_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"StealthSHH_2t4b_mStop-800_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0283338),
		},
		"StealthSHH_2t4b_mStop-850_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		"StealthSHH_2t4b_mStop-900_mSo-100"					: {
			"CrossSection" : XSValues(XS_13TeV=0.0128895),
		},
		"rpv_stop_350_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"rpv_stop_450_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"rpv_stop_550_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"rpv_stop_650_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"rpv_stop_750_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"rpv_stop_850_t3j_uds"								: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		# RPV taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
		"RPV_2t6j_mStop-300_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=8.51615),
		},
		"RPV_2t6j_mStop-350_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=3.78661),
		},
		"RPV_2t6j_mStop-400_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=1.83537),
		},
		"RPV_2t6j_mStop-450_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.948333),
		},
		"RPV_2t6j_mStop-500_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.51848),
		},
		"RPV_2t6j_mStop-550_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.296128),
		},
		"RPV_2t6j_mStop-600_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.174599),
		},
		"RPV_2t6j_mStop-650_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.107045),
		},
		"RPV_2t6j_mStop-700_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0670476),
		},
		"RPV_2t6j_mStop-750_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0431418),
		},
		"RPV_2t6j_mStop-800_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0283338),
		},
		"RPV_2t6j_mStop-850_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0189612),
		},
		"RPV_2t6j_mStop-900_mN1-100"						: {
			"CrossSection" : XSValues(XS_13TeV=0.0128895),
		},
	}

	def __init__(self, extra_dicts=None):
		if extra_dicts is not None:
			self.__values_dict.update(extra_dicts)

	def get_kfactor(self, name, year):
		# Default is to return 1.0 if the process does not contain a kFactorValues tuple or if that tuple doesn't contain a field for a given year

		field = "kFactor_"+year
		if not name in self.__values_dict:
			raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + name + "\"")
		if not "kFactor" in self.__values_dict[name] or not field in self.__values_dict[name]["kFactor"]._fields:
			return 1.0
		return self.__values_dict[name]["kFactor"].__getattribute__(field)

	def get_xs(self, name, year, energy):
		fields = ["XS_"+energy, "XS_"+year]
		if not name in self.__values_dict:
			raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + name + "\"")
		if not "CrossSection" in self.__values_dict[name]:
			print self.__values_dict[name]
			raise KeyError("ERROR MCSampleValuesHelper::The process \"" + name + "\" does not contain a cross section tuple")
		if not any(f in self.__values_dict[name]["CrossSection"]._fields for f in fields):
			print self.__values_dict[name]["CrossSection"]
			raise KeyError("ERROR MCSampleValuesHelper::The CrossSectionValues tuple for process \"" + name + "\" does contain the key(s) \"" + fields + "\"")

		if self.__values_dict[name]["CrossSection"].__getattribute__(fields[0]) >= 0:
			return self.__values_dict[name]["CrossSection"].__getattribute__(fields[0])
		else:
			return self.__values_dict[name]["CrossSection"].__getattribute__(fields[1])