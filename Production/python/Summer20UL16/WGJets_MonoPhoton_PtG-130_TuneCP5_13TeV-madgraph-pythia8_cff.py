import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/02044C28-BB1E-1F46-9819-A6E8F0DAC51F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/03DF2539-6E00-6C4D-9779-4C8EBA4C1BE4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/07EAD6FE-F175-CF4E-8424-44E6FD1EDAD5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/12F68476-7E3F-9945-97B8-135ECD04D3AC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/181DB97E-CA9E-D743-8722-62BFBDA1CFF4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/1B8C2958-24AF-7445-BF1A-C98DD081C4DE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/31974D78-B713-7145-9D87-4C89ECB00700.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/3AA78999-B801-8F4A-99EF-B8BBA3ECBFBF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/404908C7-E585-4045-AB2D-080E0C069F2E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/42765659-747E-F644-9D5D-DE129E6CE1F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/4563A874-7786-CE41-9AEA-EF3343A4295D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/46CE1D4B-FBEA-6D49-87A4-008CF1CB4C71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/479A3361-523E-FC46-8EE7-5007A761EC74.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/4FC81105-49FC-7346-A8AC-8318B7A5CDEF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/5019A26F-49C0-2249-ABED-86B352CAA766.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/5B4CF40C-398B-3044-8BDF-349A6E34A69C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/63FCBECE-24E4-5E4F-8082-3B44B6383ED4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/6B188FF9-31EB-9945-8B1D-90B709A34910.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/6D98E386-662F-6F4E-9454-A6880BC05887.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/75E0A84B-AACC-E144-9A61-B749899ED91A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/7E97F745-C826-4345-A635-A674B4529C63.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/81436787-7783-5B4B-8318-162E036B189D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/87077B96-F695-8A4F-AD22-F47CFEE785A3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/88508AF5-5C13-8B43-B224-2A0BF07900B8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/8AAB82E8-007E-5D49-B10A-1EBE3F9C3386.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/8CF393EE-E953-2F40-AE26-2AB8D39450C8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/9154DC20-BEC1-6F4E-BD80-AEE49BF2106F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/9537C1DE-4902-9C4B-93F0-78476141434B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/97079199-59E5-3D41-B61E-7B89EC170A23.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/9E989E7D-4BDF-E144-B9BC-CA450F63A944.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/A3A50C9F-0D50-F743-B6A5-95264A4BA22F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/A71E363B-8BB1-3E4C-BD4E-1AEA90DD576C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/B83AD3C2-35D5-DD49-AAA1-66FE34B7ABDD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/BC43BBA8-D962-7241-B6DC-33076628A03B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/C1DA3CF6-6A2C-3944-AEE2-17A2C383EEA8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/C40B0D17-0FC2-CB4B-BACF-F3FAF727E7AA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/C54CB164-934A-0843-85B5-FDF05E3E54C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/C5C77F4B-66E3-B444-AAAC-9B9667A49DB1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/D5DDD2AC-B506-9C40-8348-960CF508C334.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/D8A38ECF-2637-F540-9C79-0C809AB1D281.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/DB429CE6-4FCC-D447-9F78-07C2D8210A83.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/DDD306C0-9A92-4645-98C9-B249185C4DBA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/E0D01D6F-A53A-B149-924B-D1F6321D4F00.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/E2D02BEB-16E7-3D43-8DB7-ADCCE0E1FA62.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/E455137C-DD9A-C64A-8974-11240495B923.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/ED591FDB-8202-E94A-9D31-9CBE0F82AD88.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/F4284200-97B4-C343-83DC-DF1F039D9EF3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/F5659534-7DA7-2243-B9FC-22B2FA6DAF69.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/100000/FC1C2B96-AD0B-304E-BA50-AE41AD84CBF9.root',
] )