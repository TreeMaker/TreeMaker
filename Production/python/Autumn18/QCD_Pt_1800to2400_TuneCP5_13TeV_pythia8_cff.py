import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/26B4D9D7-31DF-CB4F-9534-28024B4085E0.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/279CBE72-9AE1-3E49-88B2-45C2ADD1D02E.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/2B3487D4-62FE-1B48-8186-2013DF94EC78.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/3376FDD5-22D2-D146-A9D6-55DAF851F84F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/339DF112-9626-0945-872A-6CE3245B655A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/388705A5-4160-BF41-A576-4BB6806E3C27.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/394AD3A2-07AD-5345-B344-25A1B4F46E91.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/480B09D0-3E5A-A24A-815F-EBB159FCEFC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/6419C56C-62B4-B94A-AAFF-D9D127668A5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/641E09CC-072D-6249-B20D-A742C6759232.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/6B327844-66E8-D643-9ADA-A02BF38A3A3A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/6C4EF3C0-4BE9-D04B-B2D8-7B6F03032323.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/6FA0E32E-C553-C541-B433-B636475C4ABB.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/71F5DB96-F0E0-6344-899F-7FEED1752088.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/772F305E-63EE-9749-8871-01D6F816E5E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/77FA6BC7-AAF3-0348-AEF4-A7A4F0353638.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/7DE853B8-1648-9D4A-926F-9CD6D5258809.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/81624B26-5BF0-0E45-A6DC-A274B1293045.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/8533A19D-53F1-0345-8CF3-3E654F17CB00.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/8F839AE9-76C8-0F42-836B-1D23E97E0F32.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/A1CD1388-05F4-F148-9306-EA289ACD5BD1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/A2235E19-0B30-744A-AAD9-77E5553A8BE5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/A9852662-F05D-F547-A5D5-6CD8B46ADB20.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/B2A7FDE0-6A4B-8D45-AB6E-A53038739668.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/BCC714E5-BF70-5E4C-85FB-5345FD2ABF9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/D37C8A2F-D353-7C45-9A59-66826120DF0A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/D74AACBA-4EBB-374D-B422-11104D37E1B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/D9E4282C-AD7C-7B46-AD69-0EB83DB54732.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/DC84B8C4-99DB-074C-9058-A079B916DC61.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/E1749025-409B-BD4D-A1ED-A6789CBB4BF3.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/EB52E4FB-ACE9-FA45-BA9E-1178F364CF37.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/EE3BE86D-254D-8041-B1C2-CDE7F97319A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/FCD1D50F-6AA6-6644-82B5-9EE1C00AC3CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/FEFEF3C3-79E7-D247-8E51-0FB091023B78.root',
] )
