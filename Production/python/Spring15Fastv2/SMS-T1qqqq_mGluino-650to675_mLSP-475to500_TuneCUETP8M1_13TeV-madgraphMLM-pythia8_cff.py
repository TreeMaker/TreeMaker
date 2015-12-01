import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0C476DDF-2E95-E511-8187-00259073E466.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1CC34EC1-2F95-E511-914D-001EC9ADDBA5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1EB723E3-2E95-E511-93D5-0CC47A124458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/204A1ADF-2E95-E511-B768-002590C14B38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2276D0E1-2E95-E511-9C93-0025907B4FAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2406DFE0-2F95-E511-AA30-001EC9ADEA9B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2C24DEBB-2F95-E511-920E-0CC47A124224.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/30127EC5-2F95-E511-9C7A-0CC47A124574.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/324A2CBF-2F95-E511-8E05-001EC9ADDB87.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/341DD6BD-2F95-E511-BB3A-0CC47A124224.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/34BD59C2-2F95-E511-BC8D-0025900EB52C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3A6298E8-2E95-E511-ADDE-FA163EA26299.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3A7779BF-2F95-E511-B850-002590C18A26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4207C6EF-2E95-E511-B289-0025900EB504.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/462402DE-2E95-E511-95BC-00259074AE8A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/481500DE-2E95-E511-8646-002590D0B0C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4A356AC9-2F95-E511-B19E-002590E50600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4C66B0DD-2E95-E511-B3AD-0CC47A4DEECE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/582E70EA-2E95-E511-B0FF-0CC47A1244CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/607C90EC-2E95-E511-8AAE-0022195E66A7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/62225FDA-2E95-E511-85F0-0CC47A123FA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/68DAD1E0-2E95-E511-BEFF-00259073E450.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6A0E37DC-2E95-E511-ADD5-002590D0B044.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6E325AE1-2E95-E511-B587-20CF3027A60B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/82BD75E0-2E95-E511-A1F0-002590E50AFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/843DBEDE-2E95-E511-BAAF-0025907B4F78.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/94B41EE3-2E95-E511-8E69-0CC47A124458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9A7DDDDC-2E95-E511-8BB8-001EC9ADE744.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9CE0FFE1-2E95-E511-8086-001EC9ADE177.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A4BE66F4-2E95-E511-9CA9-001EC9ADDBF5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A4D3D7E1-2E95-E511-93A3-00259073E322.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A80975E2-2E95-E511-8C69-001EC9ADCBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A8CB88F8-2E95-E511-84F4-002590C14CD2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B44507E0-2E95-E511-948E-00259073E370.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BE042EC2-2F95-E511-8B0F-001EC9ADC0B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C0A776EE-2E95-E511-AFBB-002590C1946A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C4624CE1-2E95-E511-BD3E-002590747DDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D0EE4BE0-2E95-E511-BF4C-001EC9ADE550.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D225B2CC-2F95-E511-9175-002590E50602.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D8BD90EC-2E95-E511-9FFF-0022195E66A7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D8D3A1C9-2F95-E511-BE05-002590E50600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DC2D73EB-2E95-E511-BD99-002590E50B28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E289A3E0-2E95-E511-8B8D-00259073E34C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E4197969-2F95-E511-AECE-02163E013E3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/EA5EC9DD-2E95-E511-85AB-00259073E3E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/EA6E8CDD-2E95-E511-A8DD-0025907308DE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F2FEAAE0-2E95-E511-B85F-00259073E34C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F48768DE-2E95-E511-B976-002590C192A8.root' ] );


secFiles.extend( [
               ] )

