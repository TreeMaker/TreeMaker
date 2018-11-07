#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
pattern = 'DYJetsToLL'
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
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1'],
    ]
}
