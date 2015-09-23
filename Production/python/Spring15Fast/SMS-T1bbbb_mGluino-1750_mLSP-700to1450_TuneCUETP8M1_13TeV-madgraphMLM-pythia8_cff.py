import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/264ED739-D15D-E511-953E-002590A3C984.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/2A9B5943-D15D-E511-B5CA-00304865C2C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/30F38149-D15D-E511-9D4B-0025904A8EC4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/384AED47-D15D-E511-931D-0025901D08DE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/3AFFFC6A-D35D-E511-8250-002590A3C984.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/48BD2E93-D05D-E511-B860-002590E39F2E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4AC85A45-D15D-E511-84D1-0CC47A13D16E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/54D3A53B-D05D-E511-AD8E-0025B3E063AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/7002475D-D15D-E511-9197-0025901D0C4E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/88C9B45C-D05D-E511-9DB8-90B11C2AB44B.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/8CB6CA4A-D15D-E511-9617-002590A3C97E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/8E631146-D15D-E511-B75D-0025901D08BE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/92E2C446-D15D-E511-9B40-0025900EAB2A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/943D6242-D15D-E511-AA4F-003048344A90.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9601B33F-D15D-E511-8F19-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/A426C55E-D15D-E511-B5FB-002590E3A2D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/BA44F946-D15D-E511-AAFD-00259048BF92.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/C2BF033C-D15D-E511-B5BD-002590A887AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/C2E97243-D15D-E511-8952-0CC47A13CB62.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/CC4DD739-D15D-E511-B735-002590A3C984.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/F0ABDB4E-D15D-E511-8BF8-0025901D08D6.root' ] );


secFiles.extend( [
               ] )

