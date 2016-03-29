import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/12DCEE99-C56D-E511-AA75-08606E15EABA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/249EA2A1-C76D-E511-BBC6-3085A9262DA0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/2ABAF8BC-C56D-E511-86C0-08606E17C77E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/3037C502-C76D-E511-88A9-7824AFAE696F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/34C62EC0-C66D-E511-9DDB-08606E15EABA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/4A29A1F2-C66D-E511-BA65-08606E15EABA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5AA8E358-C66D-E511-B0CF-F46D042E833B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5C09A7A4-C76D-E511-BF37-08606E15E9AE.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5C43A46A-C56D-E511-A68A-F46D042E833B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/780FDDC7-C46D-E511-A152-D8D385FF18C4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/84BA46E6-C66D-E511-89FE-002618943BF9.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/886062C3-C46D-E511-9D57-34E6D7E387A8.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/8AE4F60B-C66D-E511-9AC6-3085A9262DA0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/947A13FA-C56D-E511-A9A5-F46D043B3D41.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9C3CB4F9-C46D-E511-AB13-F46D043B3D41.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/9CFD6044-C66D-E511-86CD-08606E15E9AE.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/A2BED061-C76D-E511-9AFE-E03F49D6226B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/AE542E18-C66D-E511-BAAF-F46D043B3D41.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/B270BDC9-C46D-E511-95E1-B499BAABCF0E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C4FF999A-C66D-E511-90F4-BCEE7B2FE01D.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C8FAEB9D-C76D-E511-8AF1-BCEE7B2FE01D.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/D2A16942-C76D-E511-BAFB-F46D042E833B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/D65E0A4F-C76D-E511-A3E6-08606E17C77E.root' ] );


secFiles.extend( [
               ] )

