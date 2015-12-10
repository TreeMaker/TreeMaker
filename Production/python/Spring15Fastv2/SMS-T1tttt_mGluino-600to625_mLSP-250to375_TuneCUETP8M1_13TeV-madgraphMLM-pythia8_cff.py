import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/045871CE-059F-E511-9E4D-1CC1DE18D052.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/06A04A00-069F-E511-B3C0-842B2B5C2299.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/06CC0F0E-079F-E511-954E-0025907B503A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0A7691F3-059F-E511-A8D0-001EC9AF2073.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/16E0C417-069F-E511-A903-782BCB161F1B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C93E7C8-059F-E511-977F-02163E013F9D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E3A0309-069F-E511-B571-001EC9AF1FD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E79E6FA-059F-E511-910B-02163E0114CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/203EB523-069F-E511-96C5-02163E00F3BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/209B08F6-059F-E511-B127-D4AE526A0A60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/227F5E05-069F-E511-8B25-D4AE526A0A9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/22A6B4CD-069F-E511-8CE7-0CC47A4DEDC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/264611F1-059F-E511-92E3-782BCB161FC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2E438EFB-059F-E511-AE7D-1CC1DE192802.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/32F39AE0-059F-E511-B647-001EC9B21754.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3CE651C8-059F-E511-8E8B-001EC9AF22D5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/40312B04-069F-E511-B552-02163E00F2B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4EDC36E4-069F-E511-AB89-0CC47A4DEE0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/56556EFA-059F-E511-9BF3-0090FAA57C00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5E29D10B-069F-E511-B56D-D4AE5269F919.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/64D6F2FA-059F-E511-AE77-842B2B5C2299.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76ABE714-069F-E511-AC50-842B2B71EDBE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7897FEFB-059F-E511-A82E-001EC9B21439.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7CCE8CF1-059F-E511-A60F-1CC1DE1931B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/801CF0FF-059F-E511-B8B7-D4AE526A048B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9886F2CA-069F-E511-85D0-0CC47A4D99B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9AA64A0B-069F-E511-A291-842B2B7669E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A4ED800B-069F-E511-AC37-D4AE526A0DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B08ABC62-069F-E511-BC3E-02163E01674F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B240C4CA-069F-E511-A0D5-0CC47A4DED6A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BE2C35FE-059F-E511-838B-D4AE526A0A4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C8C24DD7-059F-E511-B3F4-00221965B5AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CA5D04D8-069F-E511-A371-0CC47A1E0C10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D20778D5-069F-E511-84AB-0CC47A4D9980.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D26D7ECD-069F-E511-87E7-0CC47A4DEDC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D27FF300-069F-E511-92EE-0CC47A1DF7FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D4AF3B18-069F-E511-AC74-001E675057D5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D6EA16D2-069F-E511-9B36-0CC47A4DEE68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D8853C06-069F-E511-B1D6-0CC47A1E0C10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DE507218-069F-E511-A9DB-842B2B758AD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E0D49703-069F-E511-B433-842B2B76832A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F660131D-069F-E511-BCA0-D4AE526A0AB5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F6C76328-079F-E511-8135-00259073E502.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F82005E7-059F-E511-98A0-D4AE526A0A4B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F88484CB-069F-E511-8C77-0025907B4F28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FC83831F-069F-E511-B888-02163E00E7CD.root' ] );


secFiles.extend( [
               ] )

