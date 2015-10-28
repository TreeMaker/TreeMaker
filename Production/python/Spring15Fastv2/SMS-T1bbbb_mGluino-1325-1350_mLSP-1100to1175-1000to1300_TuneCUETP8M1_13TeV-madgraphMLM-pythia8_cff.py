import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/105B1A94-797B-E511-A354-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/125D3020-797B-E511-9C22-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/126002CC-7A7B-E511-8A6F-24BE05C6E7C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/147D76F4-787B-E511-8E56-0002C94D54EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1845F9D0-7A7B-E511-A516-0002C92DB4CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/18A8B0F4-787B-E511-8962-0002C94CD1E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30E4B0FA-787B-E511-A3E3-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/32A68E11-7A7B-E511-A19B-24BE05C6E7C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/385CA29C-797B-E511-83B4-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4EEACD95-797B-E511-99E7-24BE05C44B91.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5EE5D5F6-787B-E511-82A3-0002C94CDAE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/64FFC634-7A7B-E511-9E3A-0002C94CDAE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C15CDE9-787B-E511-B052-0002C92DB44E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EF8B41B-7A7B-E511-8E8E-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/76A3E244-7A7B-E511-8EB2-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/821392ED-787B-E511-82CC-5065F3812291.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8231DA9A-797B-E511-9997-F45214C748C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84FBCDFE-787B-E511-A9E3-24BE05C48801.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/904ED1EC-787B-E511-B692-5065F381E251.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/90527BA7-797B-E511-8EFF-24BE05C48801.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/948009F7-787B-E511-87C9-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9496480F-7A7B-E511-9594-F45214C748CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A2874018-7A7B-E511-B029-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B494B8FE-797B-E511-A196-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B698579B-797B-E511-9228-0002C94CD120.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BAB16F25-797B-E511-9201-F45214C748D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C8D843F4-787B-E511-A9C9-0002C94D564A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D496854B-7A7B-E511-8C28-F45214C748C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA02349A-797B-E511-823D-0002C94D550A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0C827F4-787B-E511-A41A-0002C94D564A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EA08FFF0-787B-E511-BD32-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6685141-797B-E511-B182-24BE05C6E7C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6AD43EC-787B-E511-B5C0-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8BE2295-797B-E511-BEE8-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC121919-7A7B-E511-8C07-0002C90F8094.root' ] );


secFiles.extend( [
               ] )

