import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/061BB791-927B-E511-836E-24BE05C3CBE1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0C06733E-937B-E511-A1D9-00304865C254.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/10B3EC09-937B-E511-A928-5065F38142E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1624A1D4-927B-E511-A670-00304865C2D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1C7813B6-947B-E511-A4D0-24BE05C6C741.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2251262F-937B-E511-A74E-001E682F2056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/24CDECFE-927B-E511-8A43-0CC47A6C115C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/28FCF850-937B-E511-9726-5065F37D7121.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2ED309E1-927B-E511-9139-24BE05C6E711.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/2EE7169D-927B-E511-8240-002590E39F4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/38E2B624-937B-E511-AAD6-24BE05C656A1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4627CAFE-937B-E511-847B-24BE05C656A1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/46843696-927B-E511-A9E1-0CC47A6C138A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/487B1FA8-947B-E511-8D08-0025902345C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4A984AAB-927B-E511-BEF8-24BE05C33C61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4C43B0FC-927B-E511-BBF0-0CC47A13D09C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/507DD8DC-927B-E511-833E-002590E2F8B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5E9B51B8-947B-E511-B94F-24BE05C6E591.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/5EC3CABE-927B-E511-B65A-24BE05C6D711.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/62A94AAD-947B-E511-A4AD-0CC47A6C1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6408EBE9-927B-E511-B326-24BE05C38C91.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/687585CF-927B-E511-A486-0CC47A6C063E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6895192A-937B-E511-912B-0CC47A6C115C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/68D2F7B9-927B-E511-9E6C-24BE05C3CBD1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6A80AC30-947B-E511-8CC7-5065F37D7121.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6ADB4FFC-927B-E511-8FF6-5065F3816291.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6E47BF11-947B-E511-BC5D-24BE05C488E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/761DFBD5-927B-E511-9F65-24BE05C44BC1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/769E210F-947B-E511-A2A9-24BE05C44BB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7E834DF7-927B-E511-84A4-5065F3817221.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/829AF51F-937B-E511-9C0C-00304865C478.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/86B569FB-927B-E511-94AE-0CC47A6C186E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9491482D-937B-E511-9596-5065F381A2E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9CB9F419-937B-E511-BDB3-0CC47A6C1864.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/A0A5EADE-927B-E511-BFF0-0025901D08B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/AA94BAC0-927B-E511-85F5-002590E3A224.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/ACA9400F-937B-E511-9114-24BE05C63791.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B0298014-937B-E511-96BC-0025904A91F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B08D3806-947B-E511-B531-5065F3816201.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B20525A6-927B-E511-8F8F-002590725380.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/B6A8F211-947B-E511-BBE6-24BE05C6E571.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/BA9A5C90-927B-E511-A10E-0002C92A1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C2494CA8-927B-E511-952C-24BE05C4D851.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C4735A09-937B-E511-9402-24BE05C63791.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C66C3BAB-927B-E511-AF22-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CAC903D2-927B-E511-A129-0CC47A6C1038.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D4FC9E39-947B-E511-B94A-24BE05C6C7E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E08D3DF9-937B-E511-A19E-0CC47A6C1818.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E2FB04A5-927B-E511-A91D-00259082131A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E6783A1B-937B-E511-9C10-0CC47A13D09C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/ECF30C0D-947B-E511-9956-5065F381A2E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F2DB2C97-927B-E511-856C-0CC47A6C1864.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FCE8DAE5-927B-E511-B2B3-0CC47A6C1038.root' ] );


secFiles.extend( [
               ] )

