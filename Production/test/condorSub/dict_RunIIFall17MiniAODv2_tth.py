#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
patterns = ('TTZTo','TTWJets','TTGJets','TTGamma','TTHH','TTTT','TTTW','TTWH','TTWW','TTWZ','TTZH','TTZZ','ttHJet')
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
        ['RunIIFall17MiniAODv2.TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8'],
        ['RunIIFall17MiniAODv2.TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8'],
        ['RunIIFall17MiniAODv2.TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8'],
        ['RunIIFall17MiniAODv2.TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8'],
        ['RunIIFall17MiniAODv2.TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8'],
        ['RunIIFall17MiniAODv2.TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_ext1'],
        ['RunIIFall17MiniAODv2.TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8'],
        ['RunIIFall17MiniAODv2.TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8'],
        ['RunIIFall17MiniAODv2.TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8'],
        ['RunIIFall17MiniAODv2.TTHH_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.TTTT_TuneCP5_13TeV-amcatnlo-pythia8'],
        ['RunIIFall17MiniAODv2.TTTW_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.TTWH_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.TTWZ_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.TTZH_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.TTZZ_TuneCP5_13TeV-madgraph-pythia8'],
        ['RunIIFall17MiniAODv2.ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8'],
        ['RunIIFall17MiniAODv2.ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8'],
    ]
}
