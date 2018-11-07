#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
pattern = 'QCD_Pt'
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
        ['RunIIFall17MiniAODv2.QCD_Pt_80to120_TuneCP5_13TeV_pythia8_ext1'],
        ['RunIIFall17MiniAODv2.QCD_Pt_120to170_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_170to300_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_300to470_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_300to470_TuneCP5_13TeV_pythia8_ext1'],
        ['RunIIFall17MiniAODv2.QCD_Pt_470to600_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_600to800_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_ext1'],
        ['RunIIFall17MiniAODv2.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8_ext1'],
        ['RunIIFall17MiniAODv2.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8'],
        ['RunIIFall17MiniAODv2.QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8'],
    ]
}
