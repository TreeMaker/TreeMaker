from TreeMaker.WeightProducer.namedtuple_with_defaults import namedtuple_with_defaults
import re

class MCSampleHelper():
    """Helps to parse MC sample names and return specific pieces of information.

    The various functions are meant to make it easier to parse the many sample names without the duplication of effort.
    The pieces of information that can be returned are:
        1. The center of mass energy simulated within a given sample
        2. The center of mass energy associated to a given year
        3. The sample name when it's stripped of extraneous information
        4.The year associated to a given MiniAOD production

    Args:
        extra_dicts_energy (:obj:`dict` of :obj:`str`): Extra year-center of mass pairings not specified in the internal dictionary
        extra_dicts_strip (:obj:`dict` of :obj:`list` of :obj:`str`): Extra regular expressions used to strip non-physics process information from the MC sample name

    Example:
        from MCSampleValues import MCSampleHelper
        helper = MCSampleHelper()
        helper.get_cm_energy_by_year("2018")
    """

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
        "generators"    : ["(.pythia)([^_-]*)","(.powheg)([^_-]*)","(.madgraph)([^_-]*)","(.madspin)([^_-]*)","(.amcatnlo)([^_-]*)"],
        "tunes"         : ["(.Tune)([^_]*)"],
        "added_info"    : ["(.PS[W,w]eights)([^_]*)"],
        "other"         : ["(.NLO)([^_-]*)","^\s*(RelVal\s*)?|(\s*_13)?\s*$","step4_MINIAOD_2016_","step4_MINIAOD_","(.mDark)(.*)","(.isr|.fsr)(up|down)","([_|-]v)([0-9]*)","(.mWCutfix)","([_])(ttHtranche3)","SVJ_","_erdON","_ext([0-9])","_hdamp(UP|DOWN)"],
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
    """Stores the cross sections and k-factors associated to a given physics process.

    The lists of years and energies used to identify a given cross section are also stored within this class.
    Given a process name, year, and energy the appropriate cross section will be returned.
    If a cross section is not specified for an energy (i.e. multiple years), then the cross section for a given year will be returned.

    Args:
        extra_dicts (:obj:`dict` of :obj:`dict` of :obj:`namedtuple_with_defaults`): Extra cross sections and k-factors to add to the __values_dict.

    Example:
        from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
        helper = MCSampleValuesHelper()
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","kFactor")
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","BranchingRatio")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","kFactor")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","BranchingRatio")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","kFactor")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","BranchingRatio")
    """

    __years = ['2010','2011','2012','2015','2016','2017','2018']
    __energies = ["7TeV","8TeV","13TeV"]
    __xs_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __key_field_map = {
        "CrossSection"   : ("XS",-1.0),
        "BranchingRatio" : ("BR",1.0),
        "kFactor"        : ("kFactor",1.0),
        "Correction"     : ("Corr",1.0),
    }
    for __val in __years+__energies:
        __xs_field_names.append('XS_'+__val)
        __xs_field_names.append('XSSource_'+__val)
        __br_field_names.append('BR_'+__val)
        __br_field_names.append('BRSource_'+__val)
        __kfactor_field_names.append('kFactor_'+__val)
        __kfactor_field_names.append('kFactorSource_'+__val)
        __corr_field_names.append('Corr_'+__val)
        __corr_field_names.append('CorrSource_'+__val)
    XSValues = namedtuple_with_defaults('XSValues', __xs_field_names, [__key_field_map["CrossSection"][1],""]*len(__years+__energies))
    BRValues = namedtuple_with_defaults('BRValues', __br_field_names, [__key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults('kFactorValues', __kfactor_field_names, [__key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues = namedtuple_with_defaults('CorrValues', __corr_field_names, [__key_field_map["Correction"][1],""]*len(__years+__energies))

    __values_dict = {
        "TTJets" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - https://pdg.lbl.gov/2019/reviews/rpp2019-rev-top-quark.pdf",
            ),
        },
        "TTJets_SingleLeptFromT" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.219, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_SingleLeptFromTbar" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.219, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_DiLept" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_SingleLeptFromT_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=32.23, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_SingleLeptFromTbar_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=31.78, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_DiLept_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=22.46, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_SingleLeptFromT_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=5.952, XSSource_2016="XSDB",
                XS_2017=6.196, XSSource_2017="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_SingleLeptFromTbar_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=5.952, XSSource_2016="XSDB",
                XS_2017=6.179, XSSource_2017="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_DiLept_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=3.638, XSSource_2016="XSDB",
                XS_2017=3.655, XSSource_2017="XSDB",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_HT-600to800" : {
            "CrossSection" : XSValues(
                XS_2016=1.65, XSSource_2016="XSDB",
                XS_2017=1.821, XSSource_2017="XSDB",
                XS_2018=1.808, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-800to1200" : {
            "CrossSection" : XSValues(
                XS_2016=0.6736, XSSource_2016="XSDB",
                XS_2017=0.7532, XSSource_2017="XSDB",
                XS_2018=0.7490, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XS_2016=0.1194, XSSource_2016="XSDB",
                XS_2017=0.1313, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.1315, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.001445, XSSource_2016="XSDB",
                XS_2017=0.001410, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.001420, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - https://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop166p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=811.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop169p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=746.2, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop171p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=706.1, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop173p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=668.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop175p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=633.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTTo2L2Nu_mtop178p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=584.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - https://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop166p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=811.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop169p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=746.2, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop171p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=706.1, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop173p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=668.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop175p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=633.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToHadronic_mtop178p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=584.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.457, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - https://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop166p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=811.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop169p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=746.2, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop171p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=706.1, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop173p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=668.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop175p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=633.4, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTToSemiLeptonic_mtop178p5" : {
           "CrossSection" : XSValues(
                 XS_13TeV=584.6, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.438, BRSource_13TeV="http://pdg.lbl.gov/2021/reviews/rpp2020-rev-top-quark.pdf",
            ),
        },
        "TTGamma_SingleLept" : {
            "CrossSection" : XSValues(
                XS_13TeV=5.085, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "TTGamma_Hadronic" : {
            "CrossSection" : XSValues(
                XS_13TeV=4.178, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "TTGamma_Dilept" : {
            "CrossSection" : XSValues(
                XS_13TeV=1.502, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "WJetsToLNu" : {
           "CrossSection" : XSValues(
                 XS_13TeV=61526.7, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#W_jets (NNLO)",
            ),
        },
        "WJetsToLNu_HT-70To100" : {
            "CrossSection" : XSValues(
                XS_13TeV=1264.0, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_13TeV=1256.0, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_13TeV=335.5, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_13TeV=45.25, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-600To800" : {
            "CrossSection" : XSValues(
                XS_13TeV=10.97, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-800To1200" : {
            "CrossSection" : XSValues(
                XS_13TeV=4.933, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-1200To2500" : {
            "CrossSection" : XSValues(
                XS_13TeV=1.16, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToLNu_HT-2500ToInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.02627, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.139, kFactorSource_13TeV="XSDB NNLO/LO=61526.7/54000",
            ),
        },
        "WJetsToQQ_HT-200to400" : {
            "CrossSection" : XSValues(
                XS_13TeV=2549.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "WJetsToQQ_HT-400to600" : {
            "CrossSection" : XSValues(
                XS_13TeV=276.5, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "WJetsToQQ_HT-600to800" : {
            "CrossSection" : XSValues(
                XS_13TeV=59.25, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "WJetsToQQ_HT-800toInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=28.75, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_HT50to100" : {
           "CrossSection" : XSValues(
                 XS_13TeV=186100000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_HT100to200" : {
            "CrossSection" : XSValues(
                XS_13TeV=23630000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_HT200to300" : {
            "CrossSection" : XSValues(
                XS_13TeV=1554000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_HT300to500" : {
            "CrossSection" : XSValues(
                XS_13TeV=325000.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_HT500to700" : {
            "CrossSection" : XSValues(
                XS_13TeV=30350.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_HT700to1000" : {
            "CrossSection" : XSValues(
                XS_13TeV=6403.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues(
                XS_13TeV=1117.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues(
                XS_13TeV=108.4, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=21.93, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_15to30" : {
           "CrossSection" : XSValues(
                 XS_13TeV=1244000000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_30to50" : {
           "CrossSection" : XSValues(
                 XS_13TeV=106500000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_50to80" : {
            "CrossSection" : XSValues(
                XS_13TeV=15700000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_80to120" : {
            "CrossSection" : XSValues(
                XS_13TeV=2346000.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_120to170" : {
            "CrossSection" : XSValues(
                XS_13TeV=407700.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_170to300" : {
            "CrossSection" : XSValues(
                XS_13TeV=103700.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_300to470" : {
            "CrossSection" : XSValues(
                XS_13TeV=6832.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt_470to600" : {
            "CrossSection" : XSValues(
                XS_13TeV=551.2, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_600to800" : {
            "CrossSection" : XSValues(
                XS_13TeV=156.7, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_800to1000" : {
            "CrossSection" : XSValues(
                XS_13TeV=26.25, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_1000to1400" : {
            "CrossSection" : XSValues(
                XS_13TeV=7.465, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_1400to1800" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.6487, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_1800to2400" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.08734, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_2400to3200" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.005237, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "QCD_Pt_3200toInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.0001352, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "DYJetsToLL_M-50_HT-70to100" : {
            "CrossSection" : XSValues(
                XS_13TeV=139.9, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues(
                XS_13TeV=140.3, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues(
                XS_13TeV=38.37, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues(
                XS_13TeV=5.212, XSSource_13TeV="GenXSecAnalzyer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues(
                XS_13TeV=1.267, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.5678, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1332, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.002988, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "DYJetsToLL_M-50" : {
            "CrossSection" : XSValues(
                XS_13TeV=6077.22, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z (NNLO)",
            ),
        },
        "ZJetsToNuNu_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_13TeV=267.0, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_13TeV=73.08, XSSource_13TeV="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_13TeV=9.921, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-600To800" : {
            "CrossSection" : XSValues(
                XS_13TeV=2.409, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-800To1200" : {
            "CrossSection" : XSValues(
                XS_13TeV=1.078, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-1200To2500" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2514, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_HT-2500ToInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.005614, XSSource_13TeV="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_Zpt-100to200" : {
            "CrossSection" : XSValues(
                XS_2016=35.99, XSSource_2016="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "ZJetsToNuNu_Zpt-200toInf" : {
            "CrossSection" : XSValues(
                XS_2016=4.201, XSSource_2016="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_13TeV=1.1347, kFactorSource_13TeV="XSDB NNLO/LO=6077.22/5356",
            ),
        },
        "GJets_HT-40To100" : {
           "CrossSection" : XSValues(
                 XS_13TeV=18540.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "GJets_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_13TeV=8644.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "GJets_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_13TeV=2183.0, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "GJets_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_13TeV=260.2, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "GJets_HT-600ToInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=86.29, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "GJets_DR-0p4_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_13TeV=5030.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_13TeV=1128.0, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_13TeV=126.7, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-600ToInf" : {
            "CrossSection" : XSValues(
                XS_13TeV=41.39, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "ST_s-channel_4f_hadronicDecays" : {
            "CrossSection" : XSValues(
                XS_2017=11.24, XSSource_2017="GenXSecAnalyzer",
                XS_2018=11.24, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=3.36, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Single_top (NLO)",
            ),
        },
        "ST_s-channel_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=10.32, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_s_channel_cross_secti (NLO)",
            ),
        },
        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=136.02, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_t_channel_cross_secti (NLO)",
            ),
        },
        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=80.95, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_t_channel_cross_secti (NLO)",
            ),
        },
        "ST_t-channel_antitop_5f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=71.74, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "ST_t-channel_top_5f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=119.7, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "ST_tW_top_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=32.45, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-(1-3*0.105)**2), BRSource_13TeV="http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
        },
        "ST_tW_antitop_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=32.51, XSSource_13TeV="XSDB (NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-(1-3*0.105)**2), BRSource_13TeV="http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
        },
        "ST_tW_top_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=32.45, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "ST_tW_antitop_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=32.51, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "tZq_ll_4f_ckm" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.07561, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "tZq_W_lept_Z_hadron_4f_ckm" : {
            "CrossSection" : XSValues(
                XS_2016=0.1573, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "tZq_Zhad_Wlept_4f_ckm" : {
            "CrossSection" : XSValues(
                XS_2017=0.1518, XSSource_2017="XSDB (unknown)",
            ),
        },
        "WW" : {
            "CrossSection" : XSValues(
                XS_13TeV=118.7, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV (NNLO)",
            ),
        },
        "WZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=47.13, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson (NLO)",
            ),
        },
        "ZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=16.523, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson (NLO)",
            ),
        },
        "WWTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=12.178, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson (NNLO)",
            ),
        },
        "WGJets_MonoPhoton_PtG-40to130" : {
            "CrossSection" : XSValues(
                XS_13TeV=19.77,  XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "WGJets_MonoPhoton_PtG-130" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.8092, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "WWTo1L1Nu2Q" : {
            "CrossSection" : XSValues(
                XS_2016=45.68, XSSource_2016="XSDB (LO)",
                XS_2017=80.74, XSSource_2017="XSDB (LO)",
                XS_2018=81.46, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WZTo1L1Nu2Q" : {
            "CrossSection" : XSValues(
                XS_2016=10.73, XSSource_2016="XSDB (LO)",
                XS_2017=11.66, XSSource_2017="XSDB (LO)",
                XS_2018=11.76, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WZTo1L3Nu" : {
            "CrossSection" : XSValues(
                XS_2016=3.054, XSSource_2016="XSDB (LO)",
                XS_2017=3.294, XSSource_2017="GenXSecAnalyzer",
                XS_2018=3.322, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WZTo3LNu" : {
            "CrossSection" : XSValues(
                XS_13TeV=5.213, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "WZTo2Q2Nu" : {
           "CrossSection" : XSValues(
                 XS_13TeV=6.901, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "WWTo4Q_4f" : {
           "CrossSection" : XSValues(
                 XS_13TeV=51.07, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "ZGTo2NuG" : {
            "CrossSection" : XSValues(
                XS_2016=28.04, XSSource_2016="XSDB (unknown)",
            ),
        },
        "ZZTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.9738, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "ZZTo2L2Q" : {
            "CrossSection" : XSValues(
                XS_2016=3.222, XSSource_2016="XSDB (unknown)",
                XS_2017=3.688, XSSource_2017="XSDB (unknown)",
                XS_2018=3.709, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ZZTo2Q2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=4.493, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "TTZToLLNuNu_M-10" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2439, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "TTZToQQ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.5113, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "TTZToQQ_Dilept" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.0568, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "TTZToNuNu" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1476, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "TTWJetsToLNu" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.6008, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 160, NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1.-0.6741), BRSource_13TeV="https://pdg.lbl.gov/2021/tables/rpp2021-sum-gauge-higgs-bosons.pdf (p. 1)",
            ),
        },
        "TTWJetsToQQ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.6008, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 160, NLO)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.6741, BRSource_13TeV="https://pdg.lbl.gov/2021/tables/rpp2021-sum-gauge-higgs-bosons.pdf (p. 1)",
            ),
        },
        "TTGJets" : {
            "CrossSection" : XSValues(
                XS_13TeV=3.757, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "ttHJetToNonbb_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.509, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 146, NLO+NLL)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-0.577), BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHJetTobb_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.509, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 146, NLO+NLL)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.577, BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHToNonbb_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.509, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 146, NLO+NLL)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-0.577), BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHTobb_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.509, XSSource_13TeV="http://cds.cern.ch/record/2227475/files/CERN-2017-002-M.pdf?version=1 (p. 146, NLO+NLL)",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.577, BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "TTTT" : {
            "CrossSection" : XSValues(
                XS_2016=0.009103, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X, NLO",
                XS_2017=0.008213, XSSource_2017="XSDB (unknown)",
                XS_2018=0.008213, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTHH" : {
            "CrossSection" : XSValues(
                XS_2016=0.0007367, XSSource_2016="XSDB (LO)",
                XS_2017=0.0006655, XSSource_2017="XSDB (LO)",
                XS_2018=0.0006651, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTTW" : {
            "CrossSection" : XSValues(
                XS_2016=0.0008612, XSSource_2016="XSDB (LO)",
                XS_2017=0.0007314, XSSource_2017="XSDB (LO)",
                XS_2018=0.0007317, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWH" : {
            "CrossSection" : XSValues(
                XS_2016=0.001344, XSSource_2016="XSDB (LO)",
                XS_2017=0.001141, XSSource_2017="XSDB (LO)",
                XS_2018=0.001140, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWW" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.007003, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "TTWZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.002453, XSSource_13TeV="XSDB (LO)",
            ),
        },
        "TTZH" : {
            "CrossSection" : XSValues(
                XS_2016=0.001244, XSSource_2016="XSDB (LO)",
                XS_2017=0.00113,  XSSource_2017="XSDB (LO)",
                XS_2018=0.001131, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.001389, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "TTTJ" : {
            "CrossSection" : XSValues(
                XS_2016=0.0004812, XSSource_2016="XSDB (LO)",
                XS_2017=0.0003974, XSSource_2017="XSDB (LO)",
                XS_2018=0.0003972, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WWW_4F" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2158, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "WWZ_4F" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1707, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "WWZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1651, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "WWG" : {
           "CrossSection" : XSValues(
                 XS_13TeV=0.3369, XSSource_13TeV="GenXSecAnalyzer",
            ),
        },
        "WZG" : {
           "CrossSection" : XSValues(
                 XS_13TeV=0.07876, XSSource_2017="GenXSecAnalyzer",
            ),
        },
        "WZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.05709, XSSource_13TeV="XSDB (NLO)",
            ),
        },
        "ZZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.01476, XSSource_13TeV="XSDB (NLO)",
            ),
        },

        # Gluino-gluino xsecs
        # from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVgluglu
        "SMS-T1bbbb_mGluino-1000_mLSP-900" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T1bbbb_mGluino-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGluino-1200_mLSP-800" : {
            "CrossSection" : XSValues(XS_13TeV=0.985E-01),
        },
        "SMS-T1tttt_mGluino-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGl-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGluino-2000_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.101E-02),
        },
        "SMS-T1qqqq_mGluino-1000_mLSP-800" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T1qqqq_mGluino-1400_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.284E-01),
        },
        "SMS-T1qqqq_mGluino-1800_mLSP-200_ctau-1" : {
            "CrossSection" : XSValues(XS_13TeV=0.293E-02),
        },

        # stop-antistop xsecs
        # from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "SMS-T2tt_mStop-150_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.304E+03),
        },
        "SMS-T2tt_mStop-200_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.755E+02),
        },
        "SMS-T2tt_mStop-225_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.420E+02),
        },
        "SMS-T2tt_mStop-250_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_mStop-250_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_mStop-300_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.100E+02),
        },
        "SMS-T2tt_mStop-325_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.657E+01),
        },
        "SMS-T2tt_mStop-350_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.443E+01),
        },
        "SMS-T2tt_mStop-425_mLSP-325" : {
            "CrossSection" : XSValues(XS_13TeV=0.154E+01),
        },
        "SMS-T2tt_mStop-500_mLSP-325" : {
            "CrossSection" : XSValues(XS_13TeV=0.609E+00),
        },
        "SMS-T2tt_mStop-650_mLSP-350" : {
            "CrossSection" : XSValues(XS_13TeV=0.125E+00),
        },
        "SMS-T2tt_mStop-850_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.216E-01),
        },
        "SMS-T2tt_mStop-1200_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.170E-02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1" : {
            "CrossSection" : XSValues(XS_13TeV=0.146E+03),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-700_mLSP-525" : {
            "CrossSection" : XSValues(XS_13TeV=0.783E-01),
        },
        "SMS-T5qqqqWW_mGluino-1900_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.171E-02),
        },
        "SMS-T5qqqqZH-mGluino750" : {
            "CrossSection" : XSValues(XS_13TeV=0.277E+01),
        },
        "SMS-T5qqqqZH-mGluino1000" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T5qqqqZH-mGluino1100" : {
            "CrossSection" : XSValues(XS_13TeV=0.191E+00),
        },
        "SMS-T5qqqqZH-mGluino1200" : {
            "CrossSection" : XSValues(XS_13TeV=0.985E-01),
        },
        "SMS-T5qqqqZH-mGluino1300" : {
            "CrossSection" : XSValues(XS_13TeV=0.522E-01),
        },
        "SMS-T5qqqqZH-mGluino1400" : {
            "CrossSection" : XSValues(XS_13TeV=0.284E-01),
        },
        "SMS-T5qqqqZH-mGluino1500" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T5qqqqZH-mGluino1600" : {
            "CrossSection" : XSValues(XS_13TeV=0.887E-02),
        },
        "SMS-T5qqqqZH-mGluino1700" : {
            "CrossSection" : XSValues(XS_13TeV=0.507E-02),
        },
        "SMS-T5qqqqZH-mGluino1800" : {
            "CrossSection" : XSValues(XS_13TeV=0.293E-02),
        },
        "SMS-T5qqqqZH-mGluino1900" : {
            "CrossSection" : XSValues(XS_13TeV=0.171E-02),
        },
        "SMS-T5qqqqZH-mGluino2000" : {
            "CrossSection" : XSValues(XS_13TeV=0.101E-02),
        },
        "SMS-T5qqqqZH-mGluino2100" : {
            "CrossSection" : XSValues(XS_13TeV=0.598E-03),
        },
        "SMS-T5qqqqZH-mGluino2200" : {
            "CrossSection" : XSValues(XS_13TeV=0.321E-03),
        },
        "SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1" : {
            "CrossSection" : XSValues(XS_13TeV=0.002548),
        },
        "SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230" : {
            "CrossSection" : XSValues(XS_13TeV=0.6204),
        },
        "SMS-TChiWZ_ZToLL_mZMin-0p1" : {
            "CrossSection" : XSValues(XS_13TeV=0.6204),
        },
        "stealth_stop_350_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "stealth_stop_450_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "stealth_stop_550_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "stealth_stop_650_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "stealth_stop_750_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "stealth_stop_850_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "stealth_stop_350_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "stealth_stop_450_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "stealth_stop_550_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "stealth_stop_650_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "stealth_stop_750_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "stealth_stop_850_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        # Stealth taken From https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "StealthSYY_2t6j_mStop-300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSYY_2t6j_mStop-300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSYY_2t6j_mStop-350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSYY_2t6j_mStop-350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSYY_2t6j_mStop-400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSYY_2t6j_mStop-400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSYY_2t6j_mStop-450_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSYY_2t6j_mStop-450_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSYY_2t6j_mStop-500_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSYY_2t6j_mStop-500_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSYY_2t6j_mStop-550_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSYY_2t6j_mStop-550_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSYY_2t6j_mStop-600_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSYY_2t6j_mStop-600_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSYY_2t6j_mStop-650_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSYY_2t6j_mStop-650_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSYY_2t6j_mStop-700_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSYY_2t6j_mStop-700_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSYY_2t6j_mStop-750_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSYY_2t6j_mStop-750_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSYY_2t6j_mStop-800_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSYY_2t6j_mStop-800_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSYY_2t6j_mStop-850_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSYY_2t6j_mStop-850_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSYY_2t6j_mStop-900_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSYY_2t6j_mStop-900_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSYY_2t6j_mStop-950_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSYY_2t6j_mStop-950_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSYY_2t6j_mStop-1000_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSYY_2t6j_mStop-1000_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSYY_2t6j_mStop-1050_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSYY_2t6j_mStop-1050_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSYY_2t6j_mStop-1100_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSYY_2t6j_mStop-1100_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSYY_2t6j_mStop-1150_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSYY_2t6j_mStop-1150_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSYY_2t6j_mStop-1200_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSYY_2t6j_mStop-1200_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSYY_2t6j_mStop-1250_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSYY_2t6j_mStop-1250_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSYY_2t6j_mStop-1300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSYY_2t6j_mStop-1300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSYY_2t6j_mStop-1350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSYY_2t6j_mStop-1350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSYY_2t6j_mStop-1400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "StealthSYY_2t6j_mStop-1400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "StealthSHH_2t4b_mStop-300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSHH_2t4b_mStop-350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSHH_2t4b_mStop-400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSHH_2t4b_mStop-450_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSHH_2t4b_mStop-500_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSHH_2t4b_mStop-550_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSHH_2t4b_mStop-600_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSHH_2t4b_mStop-650_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSHH_2t4b_mStop-700_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSHH_2t4b_mStop-750_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSHH_2t4b_mStop-800_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSHH_2t4b_mStop-850_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSHH_2t4b_mStop-900_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSHH_2t4b_mStop-950_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSHH_2t4b_mStop-1000_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSHH_2t4b_mStop-1050_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSHH_2t4b_mStop-1100_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSHH_2t4b_mStop-1150_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSHH_2t4b_mStop-1200_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSHH_2t4b_mStop-1250_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSHH_2t4b_mStop-1300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSHH_2t4b_mStop-1350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSHH_2t4b_mStop-1400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "rpv_stop_350_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "rpv_stop_450_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "rpv_stop_550_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "rpv_stop_650_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "rpv_stop_750_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "rpv_stop_850_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        # RPV taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "RPV_2t6j_mStop-300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "RPV_2t6j_mStop-350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "RPV_2t6j_mStop-400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "RPV_2t6j_mStop-450_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "RPV_2t6j_mStop-500_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "RPV_2t6j_mStop-550_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "RPV_2t6j_mStop-600_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "RPV_2t6j_mStop-650_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "RPV_2t6j_mStop-700_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "RPV_2t6j_mStop-750_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "RPV_2t6j_mStop-800_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "RPV_2t6j_mStop-850_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "RPV_2t6j_mStop-900_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "RPV_2t6j_mStop-950_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "RPV_2t6j_mStop-1000_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "RPV_2t6j_mStop-1050_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "RPV_2t6j_mStop-1100_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "RPV_2t6j_mStop-1150_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "RPV_2t6j_mStop-1200_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "RPV_2t6j_mStop-1250_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "RPV_2t6j_mStop-1300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "RPV_2t6j_mStop-1350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "RPV_2t6j_mStop-1400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
    }

    __alternate_names_dict = {
        "TTJets" : ["TT","TTbar"],
        "ST_t-channel_top_4f_InclusiveDecays" : ["ST_t-channel_top_4f_inclusiveDecays"],
        "ST_t-channel_antitop_4f_InclusiveDecays" : ["ST_t-channel_antitop_4f_inclusiveDecays"],
    }

    def __init__(self, extra_dicts=None):
        if self.__alternate_names_dict is not None and len(self.__alternate_names_dict)!=0:
            for key,alt_key_list in self.__alternate_names_dict.items():
                if key in self.__values_dict:
                    for newkey in alt_key_list:
                        self.__values_dict[newkey] = self.__values_dict[key]
                else:
                    raise KeyError('The __values_dict does not contain the key \'' + key + '\'')

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

    def get_value(self, name, energy, year, key, strict=False):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the __key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self.__key_field_map[key][0]+"_"+energy,self.__key_field_map[key][0]+"_"+year]
        if not name in self.__values_dict:
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print self.__values_dict[name]
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self.__key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print self.__values_dict[name][key]
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self.__key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self.__key_field_map[key][1]:
            return self.__values_dict[name][key].__getattribute__(fields[0])
        else:
            return self.__values_dict[name][key].__getattribute__(fields[1])

    def get_xs(self, name, energy, year):
        return self.get_value(name, energy, year, "CrossSection", True)

    def get_br(self, name, energy, year):
        return self.get_value(name, energy, year, "BranchingRatio", False)

    def get_kfactor(self, name, energy, year):
        return self.get_value(name, energy, year, "kFactor", False)

    def get_corr(self, name, energy, year):
        return self.get_value(name, energy, year, "Correction", False)
