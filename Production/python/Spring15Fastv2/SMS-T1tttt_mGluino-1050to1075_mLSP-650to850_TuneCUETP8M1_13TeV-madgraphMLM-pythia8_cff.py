import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/004B2A16-B69F-E511-9624-003048FFD79C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/00DB4B37-B69F-E511-9F7B-02163E0114DB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/025C480D-B69F-E511-A33C-0CC47A4D76C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1801E8D1-CD9F-E511-96C0-002618FDA28E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1AC3676A-BA9F-E511-A774-002590596468.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1E0B8081-1BA0-E511-8E1D-0025905B85E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/20BB136B-BA9F-E511-BB6F-0CC47A4D75F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/24DD57A7-CD9F-E511-AFA7-0CC47A78A30E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2A90CCDD-CD9F-E511-8423-002618943935.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2ED729D6-CD9F-E511-B71D-0025905A6090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2ED80380-1BA0-E511-95D3-0CC47A4D76C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/34FAEE80-1BA0-E511-BB96-0CC47A78A360.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42986C5C-C19F-E511-AA96-0025905B85EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/440F736B-BA9F-E511-BFC5-0CC47A4D7686.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4A7A3E6B-BA9F-E511-9237-0CC47A4D765E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A8F675C-C19F-E511-A76B-0025905B85EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/60B49216-B69F-E511-87D3-003048FFD796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/669F2218-B69F-E511-BC92-003048FFCB9E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/687F0F17-B69F-E511-B191-0025905A611E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/740405C6-1BA0-E511-B206-0CC47A78A496.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/76564FD5-CD9F-E511-BCC0-0CC47A78A30E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7E04C0C4-1BA0-E511-9161-0CC47A78A496.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/88263786-1BA0-E511-9350-002618943865.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8EB7D411-B69F-E511-8282-002618943960.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/90B9EE6C-BA9F-E511-9CD1-0025905A48F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/9404218A-1BA0-E511-8808-0025905A60E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A213405D-C19F-E511-A89F-0CC47A4D7698.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A8D31085-1BA0-E511-B919-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A8D48AD5-CD9F-E511-AD90-0CC47A4D7604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AAC0156B-BA9F-E511-B32C-0CC47A4D75F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C81D405A-C19F-E511-8297-0CC47A4D7692.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DEB5B680-1BA0-E511-AA58-0026189438C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E2742974-B69F-E511-9D99-0CC47A009352.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E60E3E17-B69F-E511-BFF6-0025905B8568.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EC89E76A-BA9F-E511-953C-0CC47A78A3B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE27C180-1BA0-E511-9FAE-0CC47A78A360.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F24F1687-1BA0-E511-BFD5-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F8F30F89-1BA0-E511-8878-0025905A6066.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FEACFB5B-C19F-E511-9668-0CC47A4C8EC8.root' ] );


secFiles.extend( [
               ] )

