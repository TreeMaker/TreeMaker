#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
patterns = ('TTJets','TT_Tune')
files_grabbed = []
ostring = ""
for pattern in patterns:
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
        ['RunIIFall17MiniAODv2.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8'],
        ['RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8_ext1'],
    ]
}
