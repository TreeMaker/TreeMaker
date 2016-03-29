import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/00B437EF-DD96-E511-B1F5-0025907B4E18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/065C5CEA-DD96-E511-9B9D-0090FAA58434.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0C24756C-DE96-E511-A164-0090FAA58084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0E86A8E9-DD96-E511-9A1B-002590D0AFB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0E9C47F8-DD96-E511-BE7B-20CF305B04DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1625A7EE-DD96-E511-9C42-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1A72DCEA-DD96-E511-B1DE-0090FAA1ACF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/308ED4ED-DD96-E511-B3F8-002590D0AFF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/361A5A8E-5D96-E511-A975-20CF3027A62C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3A0F6CEE-DD96-E511-9FEB-20CF3027A578.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3A8BBFE7-DD96-E511-8659-002590D0B052.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4434ABE9-DD96-E511-A389-002590D0AFB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/44F682EB-DD96-E511-81FA-00259073E4D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/527E2AEA-DD96-E511-92D0-0090FAA58434.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/623C0064-DE96-E511-830A-0CC47A4DEEEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7019CE69-DE96-E511-ACB7-02163E013083.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7071A107-DE96-E511-9F06-0002C94CD02C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/70E90166-DE96-E511-BE85-20CF3027A629.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7C3F296E-DE96-E511-A143-0025907B4EEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7CD992ED-DD96-E511-AE90-20CF305B0524.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7CFEDAE9-DD96-E511-9D67-0090FAA57C10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/7E73D662-DE96-E511-BB0A-002590D0B074.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/86AEAE65-DE96-E511-B772-20CF305B0524.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A08D4944-DF96-E511-AD45-02163E00CE2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A81D3DEC-DD96-E511-9DB7-00259073E524.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AADCD0E6-DE96-E511-9C8F-02163E014B2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B0A13C65-DE96-E511-8CA2-20CF305B0524.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B26139ED-DD96-E511-8A62-00259073E500.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B409EBEB-DD96-E511-9F93-0CC47A4DEDB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B46882EB-DD96-E511-940A-20CF3027A626.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B4C61FEB-DD96-E511-B353-0090FAA58204.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BC1FFC61-DE96-E511-B4AF-002590D0AFB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C07AE3E9-DD96-E511-94C3-20CF30561711.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/CC35F3EA-DD96-E511-B1C0-002590D0AFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/CE109A61-DE96-E511-99A2-20CF3027A62C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D0004C63-DE96-E511-B0A7-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D02B11F1-DD96-E511-9586-00259073E50A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D2870FEA-DD96-E511-8B5C-002590D0B096.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D613D3FA-DD96-E511-AF31-0025907750A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E2EE71ED-DD96-E511-A888-00259073E4B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E6C8C8EF-DD96-E511-9E78-00259073E388.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F43DCC68-DE96-E511-850E-00259074AE82.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F89E8365-DE96-E511-97F6-002590D0AFEA.root' ] );


secFiles.extend( [
               ] )

