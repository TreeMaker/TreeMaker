import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/00A75959-3D9F-E511-9F80-6C3BE5B5F210.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/04211C3C-4C9F-E511-861D-B499BAABF37A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/0487C9F4-2F9F-E511-87CC-6C3BE5B51238.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/102F47C0-3C9F-E511-B9F9-0090FAA57C00.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/28AC4B4F-379F-E511-A4D6-0CC47A1DF800.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/2A820F1B-2F9F-E511-A9AE-00259073E49A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/3019418A-329F-E511-898C-0CC47A4D9A48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/365748F1-2F9F-E511-9513-6C3BE5B580B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/36D21EBB-3C9F-E511-9F30-002590D0AFAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/3A45C5AA-349F-E511-81EE-00259073E510.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/44043C78-369F-E511-A9FA-B499BAAB427C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/463D41CF-309F-E511-A26A-02163E0178D7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/4645F024-389F-E511-90AB-0090FAA579F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/46754CBC-3C9F-E511-B959-002590D0B0AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/4E6372EE-2F9F-E511-A1AC-6C3BE5B593F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/4ECDA1BB-3C9F-E511-90EB-20CF3027A57B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/5003C376-3C9F-E511-95CC-D48564599CAA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/54633E5C-369F-E511-8E1B-0025907B5002.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/547047BD-3C9F-E511-AD80-002590D0AFA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/5E6D3896-2F9F-E511-B729-0025907277BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6047E845-359F-E511-BD19-00259073E4D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/64DB1590-2F9F-E511-888F-0025907B4EC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6661EB89-329F-E511-8A65-002590D0B090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6EA90C91-329F-E511-9DD8-0025907B4EC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/726ECF17-2F9F-E511-BBDD-0025907B5002.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/7272B8F2-2F9F-E511-AD83-44A842CFC9A5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/7C82F231-389F-E511-8628-002590D0AFF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/809A9C0F-309F-E511-B027-6C3BE5B50170.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9691A419-2F9F-E511-9A38-0025907B503A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9ADA6C51-3C9F-E511-AEF3-001E4F1BC725.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9C7A78D0-3C9F-E511-AB10-0025907B503A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/A497FB48-359F-E511-8EC7-0CC47A412A30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/B06D334C-369F-E511-A899-0CC47A4D9A72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/B08F61E9-2F9F-E511-ADDA-6C3BE5B59060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/B4A9B064-3D9F-E511-8C91-6C3BE5B580C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/BAAB1176-3B9F-E511-B60A-02163E01602F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CA1B8303-3A9F-E511-A398-44A842CF0600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D00C2560-309F-E511-833D-0CC47A1DF7F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D0407E0F-309F-E511-964B-6C3BE5A4D8E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D644550E-379F-E511-AD9E-02163E012EF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/EC2EC44F-369F-E511-B68F-0CC47A4DED9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/F06F390F-309F-E511-BF56-6C3BE5B50210.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/F62B328C-2F9F-E511-AA9D-02163E012DA3.root' ] );


secFiles.extend( [
               ] )

