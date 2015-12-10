import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/00F6C404-6F9E-E511-A880-0025905C426E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/08071BD7-5A9E-E511-BAE2-002590DB9182.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/08996C95-639E-E511-BE83-0025904E2398.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/0ECDA8CA-3F9E-E511-814E-003048C6D558.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/10343D9C-619E-E511-AA17-0025902CFC44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/1282AAB9-639E-E511-BC9C-00259018867E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/14CEBB05-6D9E-E511-AEBF-0025905C426E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/1814F924-629E-E511-9418-002590DB9166.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/188B870B-629E-E511-AE19-FACADE00016D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/2664321C-3D9E-E511-B3B3-003048C5734E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/26946307-699E-E511-B814-0025905C426E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/2811FA3E-629E-E511-A806-0025904B0FB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/28E10ECE-619E-E511-B8D8-FACADE000116.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/2E215CE4-629E-E511-BF84-003048C70FBA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/30F1F8BC-619E-E511-90A5-0025902CFFDA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/324429EF-639E-E511-AF06-0025902D1212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/44A0F1BF-619E-E511-93E9-00259018867E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/546E1E2D-629E-E511-9402-0025904B8ABA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/567E5DBE-619E-E511-8253-002590AC505C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/64222A9D-639E-E511-AA8C-003048C7BA38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/680487C0-619E-E511-A3C1-002590AC5482.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6A6E98DE-709E-E511-8EAA-0025905C426E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/6C4B4DBC-639E-E511-8785-0025902D0140.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/745D7427-629E-E511-8371-E41D2D08DF60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/7611F30D-6F9E-E511-8017-0025905AC878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/7829D7BD-619E-E511-B778-047D7BD6DE24.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/802FA991-629E-E511-AC96-047D7BD6DE24.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9007412B-629E-E511-94BE-002590DB91E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/92DFA3AD-619E-E511-A80F-0025907FD280.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/9CCD21BA-619E-E511-AC80-002590AC4FDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/B24346A3-639E-E511-BDAB-0025904B8ABA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/B6B92B4B-619E-E511-8A74-003048C70FBA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/BEBFB687-639E-E511-A6ED-0025902D10E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/C8C02409-649E-E511-9641-0025902D11A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CC343B21-4A9E-E511-A098-FACADE00015D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CCF86BC4-619E-E511-A4E5-0025907DC9BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/CE47643A-6B9E-E511-A0C1-0025905C426E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D246C30D-639E-E511-9E94-0025902CFC44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/D29F7E17-6D9E-E511-BC50-0025905AC878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/E8D5B684-629E-E511-AF11-0025902D1212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/EC02150E-639E-E511-A7DD-0025902CFFDA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/ECA27215-459E-E511-B634-003048C6B51A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/F05BEB2B-629E-E511-960B-0025904CEBE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/40000/F468B8C4-639E-E511-9F03-0025904CEBE2.root' ] );


secFiles.extend( [
               ] )

