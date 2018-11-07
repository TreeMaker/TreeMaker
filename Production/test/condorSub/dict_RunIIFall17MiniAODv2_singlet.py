#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
patterns = ('ST_s-channel','ST_t-channel','ST_tW','tZq')
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
        ['RunIIFall17MiniAODv2.ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8'],
        ['RunIIFall17MiniAODv2.ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8'],
        ['RunIIFall17MiniAODv2.ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8'],
        ['RunIIFall17MiniAODv2.ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8'],
        ['RunIIFall17MiniAODv2.ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8'],
        ['RunIIFall17MiniAODv2.ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'],
        ['RunIIFall17MiniAODv2.ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'],
    ]
}
