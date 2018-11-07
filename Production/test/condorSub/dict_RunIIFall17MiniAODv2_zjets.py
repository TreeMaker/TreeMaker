#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
pattern = 'ZJetsToNuNu'
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
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-100To200_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-200To400_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-400To600_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-600To800_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-800To1200_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-1200To2500_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph'],
    ]
}
