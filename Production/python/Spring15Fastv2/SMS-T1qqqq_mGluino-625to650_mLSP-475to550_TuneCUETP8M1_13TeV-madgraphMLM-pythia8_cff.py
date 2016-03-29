import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/04794A5F-FA7E-E511-B567-D4AE526A0D2E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/10FA2F14-FB7E-E511-A170-02163E01698B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/14C4E66C-FA7E-E511-BE55-842B2B766849.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1CB8E47C-FA7E-E511-B074-02163E00C760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/26F29087-FA7E-E511-B035-02163E00F53E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/344C349F-FA7E-E511-A008-D4AE526A0D22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/36B73BCB-FA7E-E511-AA13-02163E015CB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/481A1378-FC7E-E511-9ABC-02163E01146B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4A1DAB5F-FA7E-E511-AB94-842B2B76653D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/4E41EEB2-FA7E-E511-BF4A-02163E016A1E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5233DB8E-FA7E-E511-9137-F45214C748B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5437810F-FB7E-E511-AD60-02163E01692A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/580FDBB6-FA7E-E511-9A44-5065F3818261.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5C0EB5A2-FA7E-E511-B08A-02163E013BBB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/66F95B7F-FA7E-E511-A254-0CC47A009352.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/68761A8D-FA7E-E511-8243-1CC1DE18D026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/70030E91-FA7E-E511-9183-02163E012E48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/70946DD2-FA7E-E511-89DF-02163E016739.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7284C88A-FA7E-E511-94FE-02163E013A8C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/74804A74-FA7E-E511-A362-02163E015C8E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/766420BD-FA7E-E511-9748-02163E016760.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7AED636F-FA7E-E511-92EE-0025903D0B8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8438D468-FA7E-E511-9E78-1CC1DE18CD26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8A46DD4F-FB7E-E511-8C41-02163E011542.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8AAAA67D-FA7E-E511-BB27-02163E0139F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8AB62561-FA7E-E511-935C-0CC47A009E26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8E2AB7A2-FA7E-E511-BFBE-02163E016950.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9013256D-FA7E-E511-AE52-02163E013795.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9013D4BD-FA7E-E511-9C77-02163E010BEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/907166B9-FA7E-E511-A329-02163E015026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9E0EBDA8-FA7E-E511-B649-02163E01511F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A803044A-FA7E-E511-BA90-D4AE526A0C7A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AE1E5405-FB7E-E511-AC82-F45214C748B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BABC6404-FB7E-E511-8689-02163E015D95.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BC39C156-FA7E-E511-8A3D-FA163ED66504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/BCE7CEF9-FA7E-E511-8DEB-02163E0147C5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C05F075F-FA7E-E511-B880-782BCB161FC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CECD1872-FA7E-E511-B6D3-1CC1DE18D052.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D03468BE-FA7E-E511-95E7-02163E013E73.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D0E9C461-FA7E-E511-B41B-1CC1DE18CE9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D2E1B661-FA7E-E511-90D2-02163E0167E3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D4467F5F-FA7E-E511-83F4-842B2B76653D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DED64275-FA7E-E511-BE13-0CC47A0091C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E43467BA-FA7E-E511-A7C3-02163E016BEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/EEAD3267-FA7E-E511-96D8-02163E013A86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F0613F72-FA7E-E511-BC85-02163E01673C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/FA4D339C-FA7E-E511-816D-02163E0161A7.root' ] );


secFiles.extend( [
               ] )

