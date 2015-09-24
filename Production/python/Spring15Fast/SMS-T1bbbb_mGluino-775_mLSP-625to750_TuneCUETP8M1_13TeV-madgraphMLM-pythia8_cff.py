import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/02CF074E-3B5C-E511-AA2D-003048344A90.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/06E2A39A-3B5C-E511-B1D5-0002C90B73DA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/2653A3AA-3B5C-E511-8F22-0002C90C5AC4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/26D65994-3B5C-E511-815B-0002C94CDA06.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/3E629C8A-3B5C-E511-8E42-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/445FF3A8-3B5C-E511-A68F-0002C94CD0BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/48C4069B-3B5C-E511-AFC6-0002C90F7F8A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/4A00303E-3B5C-E511-913D-6CC2173BC990.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5CD40695-3B5C-E511-BCAC-0002C94CD092.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/5CDC10AB-3B5C-E511-ACB7-0002C90B7F2E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/649C67C3-3B5C-E511-81B3-0002C90B7F94.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/6C0F0795-3B5C-E511-AFC3-0002C94CD092.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/74783C9E-3B5C-E511-B89E-0002C94D54DA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/940CC9A3-3B5C-E511-9541-0002C952E75A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/B4C487AD-3B5C-E511-8CAE-0002C94FE9BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/C6EEA2C9-3B5C-E511-81B4-0002C94CD11A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/D6EDA2C9-3B5C-E511-8BD3-0002C94CD11A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E8B91C95-3B5C-E511-95D2-0002C94CD0C2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/EC1BAF88-3B5C-E511-9978-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/F2699990-3B5C-E511-9F36-1CC1DE046F78.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/FC462889-3B5C-E511-ABB1-00238BCE4650.root' ] );


secFiles.extend( [
               ] )

