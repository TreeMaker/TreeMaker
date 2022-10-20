# format: name, sample, correction factor
tests = [
    ("SingleElectron", {"correction": 1.0, "sample": "Run2017D-UL2017-v2.SingleElectron", "type": "data"}),
    ("SingleMuon", {"correction": 1.0, "sample": "Run2018B-UL2018-v2.SingleMuon", "type": "data"}),
    ("JetHT", {"correction": 1.0, "sample": "Run2018B-UL2018-v1.JetHT", "type": "data"}),
    ("EGamma", {"correction": 1.0, "sample": "Run2018B-UL2018-v1.EGamma", "type": "data"}),
    ("SinglePhoton", {"correction": 1.0, "sample": "Run2017D-UL2017-v1.SinglePhoton", "type": "data"}),
    ("HTMHT", {"correction": 1.0, "sample": "Run2017D-UL2017-v1.HTMHT", "type": "data"}),
    ("MET", {"correction": 1.0, "sample": "Run2018B-UL2018-v2.MET", "type": "data"}),
    ("QCD_HT", {"correction": 1.0, "dname": "qcd", "sample": "Summer20UL18.QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8", "type": "MC"}),
    ("QCD_Pt", {"correction": 1.0, "sample": "Summer20UL18.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8", "type": "MC"}),
    ("GJets_HT", {"correction": 1.0, "dname": "gjets", "sample": "Summer20UL16.GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8", "type": "MC"}),
    ("GJets_DR-0p4_HT", {"correction": 1.0, "dname": "gjets_dr0p4", "sample": "Summer20UL18.GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8", "type": "MC"}),
    ("TTTo", {"correction": 1.0, "dname": "ttbar", "sample": "Summer20UL18.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8", "type": "MC"}),
    ("TTJets_", {"correction": 1.0, "dname": "ttjets", "sample": "Summer20UL18.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8", "type": "MC"}),
    ("WJetsToLNu", {"correction": 1.0, "dname": "wjetslep", "sample": "Summer20UL18.WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8", "type": "MC"}),
    ("ZJetsToNuNu", {"correction": 1.0, "dname": "zjets", "sample": "Summer20UL18.ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8", "type": "MC"}),
]
