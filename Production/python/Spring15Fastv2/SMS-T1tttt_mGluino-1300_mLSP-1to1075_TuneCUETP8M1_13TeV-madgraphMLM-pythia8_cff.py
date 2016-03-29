import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/02E9CD2D-8183-E511-A639-782BCB4086A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/04B7FDAD-478D-E511-98F2-02163E0114E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18BE9493-4287-E511-B340-02163E010F93.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C3EBC6E-FA84-E511-B4CF-0025904C68DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C4D3EEF-8A83-E511-A67C-D067E5FB79AB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C8D9311-4C8D-E511-893B-02163E01157E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2679C9F1-8A83-E511-8823-000F5327375C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/28E178DB-D283-E511-A9DE-02163E016BE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2A19BEF3-F988-E511-A49A-0025905C2CD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2E0A8C70-FA84-E511-B951-0025905C2CB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3054A173-FA84-E511-9705-0025905C4300.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/32F28A3A-FA84-E511-BD8E-0025905C43EA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/36D803D9-8E8A-E511-9547-0025905C95FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/48E1A0E3-D283-E511-84FA-02163E01502D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4CA8962E-8183-E511-ABBB-008CFAF06942.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4EB964C3-FA84-E511-901C-0025905C96A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/58542F0E-D383-E511-AE61-02163E013F88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5875F175-E783-E511-A8DD-008CFA197900.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A0D20D5-FA84-E511-83A6-0025905BA736.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A18B3B6-A28A-E511-AE04-0025904C6214.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5ED3B2E8-F988-E511-A9AB-0025904C637C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62260C93-A28A-E511-87F8-0025905C2C86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6468086F-FA84-E511-AEFF-0025905C3D98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6E14A7ED-D283-E511-937A-02163E0135B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/703A341A-6F8D-E511-B5A3-001E675792D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/78C4CDF4-F988-E511-AA4F-0025904C66F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7A229529-D583-E511-93AE-02163E01156A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/94153173-FA84-E511-A53B-0025905C2CA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/94D84DB8-A28A-E511-BB20-0025904C4F50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9C790F10-D383-E511-B2EC-02163E016BC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9C87E28E-4287-E511-BA6F-02163E0167CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AA4539F7-FA84-E511-9CD0-0025905C3DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AAF8FD85-4287-E511-9658-02163E00F4FF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B2DCE3D0-FA84-E511-A34A-0025905C4264.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B6272516-9583-E511-8E1B-842B2B296063.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BE53CD85-FD88-E511-8FE9-0025905C2CD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C298EEF7-9483-E511-BAC9-B083FED7477A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CA245946-FB84-E511-859D-0025905C3D96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CEA470FC-D283-E511-9D7C-02163E012D97.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D6C840C0-9A83-E511-B324-008CFAF07044.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DCBFCEFA-FC88-E511-A18B-0025905C2C84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E21369FA-F988-E511-A039-0025905C431C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E4BBC16E-FA84-E511-A82C-0025905C2CE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E4C982F9-FA84-E511-AA14-0025905C42A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA01BC73-FA84-E511-9FD4-0025904C637C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE1256B7-A28A-E511-B2A1-0025905C3E66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F4184DCC-D283-E511-8235-02163E01502D.root' ] );


secFiles.extend( [
               ] )

