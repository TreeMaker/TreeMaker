import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0A4E0BF5-7B7B-E511-8ED0-00238B8A3CEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1268A9D5-7B7B-E511-BB41-0CC47A6C186C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C9E4A0D-7C7B-E511-A58E-0025902345B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20C53ABB-7B7B-E511-B236-002590488694.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/380CBD2E-7C7B-E511-AECC-001E682F1FA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3C7715F4-7B7B-E511-921D-0CC47A6C138A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/404587E2-7B7B-E511-A92C-0CC47A6C1810.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4AC779F0-7B7B-E511-8784-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4AFDDC2E-7C7B-E511-BF5F-003048344A98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E9F8BF3-7B7B-E511-93B5-002A6ADFC6FF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6050EDDD-7B7B-E511-9234-A4BADB38EC0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60E48F83-7C7B-E511-B9EB-90B11C2801E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/689329CA-7B7B-E511-A16A-90B11C2ACF20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E2B50BA-7B7B-E511-A10A-90B11C26815F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/725B194B-7A7B-E511-9F21-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E22D51E-7C7B-E511-8522-00304865C244.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/80E6F8F3-7B7B-E511-BE2A-00259023466C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88297E4D-7A7B-E511-81EF-0025905B85B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8A20B7B5-7B7B-E511-A258-00304865C45E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A52985E-7D7B-E511-A07E-0025904AC2C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9EDBB732-7A7B-E511-A9BE-00238BBD7564.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A2ABCCBC-7A7B-E511-B458-0CC47A6C186E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A2FD3ECF-7B7B-E511-B76D-0025902D944E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A4B14B2C-7A7B-E511-B33B-00304865C49C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A4FD09BC-7B7B-E511-A2B3-1C6A7A26BDCF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAA87490-7C7B-E511-A74C-90E2BA726FA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE73034D-7B7B-E511-99F6-0CC47A6C0758.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AE732BB6-7B7B-E511-B5EB-0CC47A6C0682.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA97040C-7C7B-E511-8CB7-003048F5ADEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC3553EB-7B7B-E511-AF75-0CC47A6C1864.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE71AE5F-7D7B-E511-B351-00238BDFD122.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE4ABAD4-7B7B-E511-AEE0-00238BDFD032.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F441C61F-7C7B-E511-A1E3-90B11C2C93C9.root' ] );


secFiles.extend( [
               ] )

