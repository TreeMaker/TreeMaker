import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/00DFF92B-6F9F-E511-B56D-02163E011531.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0846BC1B-719F-E511-A056-02163E016B45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/10A1CB0A-6F9F-E511-80C0-003048F0E85A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1CC51D1F-6F9F-E511-84E9-44A84225CFF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1CF9A2F7-6E9F-E511-8E5A-02163E013013.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E6F2C00-6F9F-E511-B98E-B083FECFD4F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/26C8C96F-6F9F-E511-B341-001F29656386.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2AC7A22F-6F9F-E511-9623-02163E013F3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2CB3E6F3-6E9F-E511-8DD3-02163E013EEB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2E8C16FD-6E9F-E511-BE35-20CF3027A5CD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/2ED66CCE-709F-E511-B7AB-02163E00EAB9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3A5939F7-6E9F-E511-A52E-02163E014F22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/3C5EA1AF-6F9F-E511-9600-02163E01533F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/429AFEFA-709F-E511-B3FD-02163E013F78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4448AEFC-6E9F-E511-B3AC-02163E014DFF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/44A2FCE5-6E9F-E511-84B4-02163E00BE5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/484745EF-6E9F-E511-BBA1-02163E013B68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4C7593F6-6E9F-E511-91B7-002590D8C724.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4E30D957-6F9F-E511-B05A-02163E00F4C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6AEC1D13-6F9F-E511-9D03-02163E012CE1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6C85B2DE-6E9F-E511-BDE4-02163E0130F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/74020548-6F9F-E511-8FA3-44A84225CDA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76EBB920-6F9F-E511-BBE0-02163E016936.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/784EA6D2-709F-E511-A0CC-02163E0166E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C4C241D-6F9F-E511-8EA0-002590D8C71A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/803236DE-709F-E511-9055-02163E00EB85.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/826B6F16-6F9F-E511-9980-D48564594FB4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/82ED9637-729F-E511-BDDD-02163E00F36D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8869A9E2-6E9F-E511-BEFE-02163E014E73.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8C0B6418-6F9F-E511-95C3-001F29652580.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/922C2EEB-6E9F-E511-9D6D-02163E013E07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9E8F35ED-6E9F-E511-B1A4-02163E013F1F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A2D9481D-6F9F-E511-A209-44A84225CDFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AEB687D1-6F9F-E511-AE22-02163E016821.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B0BD91D1-709F-E511-A067-02163E013BF5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B25272FC-6E9F-E511-969A-02163E012D2B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C0331F06-6F9F-E511-B330-02163E015C6C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CEC7BAF0-6E9F-E511-A6B8-02163E014A56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D601AFE5-709F-E511-A765-02163E012ECD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DAF49CDF-6E9F-E511-B28F-02163E017804.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E29E6ACC-709F-E511-BC90-02163E016A9D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E6382DE6-6E9F-E511-8B3D-02163E013E9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EE4D4416-6F9F-E511-AD98-D48564591B68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F07DDD27-6F9F-E511-B747-002590D60042.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F8918513-6F9F-E511-BCAA-02163E013278.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FC64891F-6F9F-E511-B0E9-02163E00F455.root' ] );


secFiles.extend( [
               ] )

