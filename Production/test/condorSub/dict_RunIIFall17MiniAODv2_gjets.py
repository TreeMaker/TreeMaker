#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
pattern = 'GJets'
files_grabbed = []
ostring = ""
files_grabbed.extend(glob.glob(location+pattern+'*'))

ostring = "flist = {\n" + (4 * ' ') + "\"scenario\": \"Fall17\",\n" + (4 * ' ') + "\"samples\": [\n"
for f in files_grabbed:
     ostring = ostring + (8 * ' ') + "[\'"+f.replace("_cff.py","").replace("/",".")+"\'],\n"

ostring = ostring + (4 * ' ') + "]\n}\n"
print ostring
'''

flist = {
    "scenario": "Fall17",
    "samples": [
        ['RunIIFall17MiniAODv2.GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8'],
    ]
}
