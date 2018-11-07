#Made in python using:
'''
import glob
location = 'RunIIFall17MiniAODv2/'
patterns = ('SMS','RPV','StealthSYY','StealthSHH')
files_grabbed = []
ostring = ""
for pattern in patterns:
    files_grabbed.extend(glob.glob(location+pattern+'*'))

ostring = "flist = {\n" + (4 * ' ') + "\"scenario\": \"Fall17sig\",\n" + (4 * ' ') + "\"samples\": [\n"
for f in files_grabbed:
     ostring = ostring + (8 * ' ') + "[\'"+f.replace("_cff.py","").replace("/",".")+"\'],\n"

ostring = ostring + (4 * ' ') + "]\n}\n"
print ostring
'''

flist = {
    "scenario": "Fall17sig",
    "samples": [
        ['RunIIFall17MiniAODv2.SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
        ['RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8'],
    ]
}
