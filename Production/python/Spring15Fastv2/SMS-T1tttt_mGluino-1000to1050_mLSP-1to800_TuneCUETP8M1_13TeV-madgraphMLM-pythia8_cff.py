import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/001D5E23-EA85-E511-9C03-02163E013C3B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/08D326FF-8889-E511-98A2-008CFA166008.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1089D717-8989-E511-8AAE-008CFA1CB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/10E9D91F-378A-E511-A774-00259048AC10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/141B79D3-DA85-E511-84DB-02163E00EA6C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1428C31B-378A-E511-A143-02163E0144A9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/18E27D3A-DB85-E511-B4ED-02163E0169E7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1CEF3E14-DF85-E511-B3C1-02163E0169C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2C821660-378A-E511-B6FC-02163E016886.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/304B5680-378A-E511-B893-02163E00E9F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/307CCC61-F485-E511-AC77-02163E01680C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3696B223-378A-E511-B712-001E675A58D9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3CBD8D5F-B289-E511-B55B-003048CB860C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3EDB178B-EF85-E511-AF69-02163E01306B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/44875045-378A-E511-B6EF-02163E0160FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4A1BD526-378A-E511-A3C2-00259029ED16.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4CB8D56C-B189-E511-9D56-002590FD5A48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4E36713A-EA85-E511-A491-02163E016A06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5C823C6E-F085-E511-BB6D-02163E0147AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5C8D1A2E-B289-E511-8EA7-00304867FD03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6A0F73E9-E985-E511-A305-02163E00E73B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/789C7482-378A-E511-86EE-0CC47A0AD668.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/840B877B-B189-E511-980F-002590D9D880.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8A46FE0E-8989-E511-9869-008CFA1C6414.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/924F0822-378A-E511-AC07-002590791DA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92AA4368-378A-E511-955B-02163E013E73.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/98ED3AD5-DE85-E511-B750-02163E016BAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/98F78590-CE85-E511-9E8C-02163E0169F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A81E0B4E-378A-E511-80CD-02163E013DCB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B0CD7CCA-F085-E511-8208-02163E016BAD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B2A3DE78-EF85-E511-877A-002590494E8C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B2ADFE57-378A-E511-9B65-02163E0151EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B440CA7E-378A-E511-9DA4-02163E014F1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B603C244-378A-E511-96AF-02163E011E9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BAF9CC60-B289-E511-810A-00259075D702.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CCE2CA82-B089-E511-9888-00304867FD03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D21D1370-F285-E511-ACDA-02163E00F51E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D4EBD29B-378A-E511-8774-02163E014AC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D6667252-378A-E511-8155-02163E013C4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E0011875-B189-E511-AB52-002590D9D984.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E23182BE-F285-E511-958E-02163E0169EB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E46A8158-388A-E511-86E1-02163E015119.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E4E15B60-8A89-E511-8984-008CFA1983BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EC93671A-378A-E511-A331-00259029ED1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FA45CD23-E886-E511-AD5C-02163E015352.root' ] );


secFiles.extend( [
               ] )

