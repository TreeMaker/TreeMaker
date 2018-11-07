#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
patterns = ('WGJets','WW','WZ','ZG','ZZ')
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
        ['RunIIFall17MiniAODv2.WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph'],
        ['RunIIFall17MiniAODv2.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8'],
        ['RunIIFall17MiniAODv2.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8'],
        ['RunIIFall17MiniAODv2.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2'],
        ['RunIIFall17MiniAODv2.WZZ_TuneCP5_13TeV-amcatnlo-pythia8'],
        ['RunIIFall17MiniAODv2.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8'],
        ['RunIIFall17MiniAODv2.ZZZ_TuneCP5_13TeV-amcatnlo-pythia8'],
    ]
}
