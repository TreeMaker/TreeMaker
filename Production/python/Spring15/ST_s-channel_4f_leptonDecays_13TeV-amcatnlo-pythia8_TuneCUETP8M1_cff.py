import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/0CA0CCA6-CE02-E511-B56D-00266CFF0044.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/32134FB6-9D03-E511-A1E4-B083FECFC6ED.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/3ED412CF-D102-E511-9F97-C4346BC75558.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/4084CBB3-F002-E511-BCF6-0025905B85AE.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/487CCE11-C702-E511-B03D-00266CFF0044.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/4A893053-F102-E511-9354-0025905B85D8.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5672D752-F102-E511-9AB9-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/58D9E1F6-D902-E511-8888-6CC2173BC120.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5E3FA511-C702-E511-8A39-6CC2173BBEE0.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/66A689EF-C702-E511-B9F8-00266CFF0044.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/745AFA94-C702-E511-B24E-C4346BC75558.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/7AD881B2-9D03-E511-ABDA-525400616EC2.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/909661F3-C702-E511-856D-AC162DA87230.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/90A649C0-9D03-E511-9024-0CC47A0AD704.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/90A759A0-9D03-E511-B2B0-6CC2173BBE80.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/98FFCED3-D102-E511-A5E4-00266CFF0044.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A24908B4-F002-E511-88BD-0025905B8592.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A4167E98-C702-E511-86B9-008CFA0518D4.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A6850AD2-D102-E511-9317-008CFA0518D4.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A6ED6744-EA02-E511-800A-00259073E3E6.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A86547B9-E902-E511-A9D1-0CC47A4DECFC.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B2D9D474-D202-E511-B354-00266CFF0044.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/BAEDC8C2-D302-E511-A5FB-20CF3019DEEE.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/CA73E4B9-9D03-E511-95B6-20CF3019DF02.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E24246BF-F002-E511-B8B2-0025905B85D0.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E26D5170-D202-E511-BFE5-C4346BC75558.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E4DAEA40-EA02-E511-B307-E0CB4E55366E.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E4E4D7B0-FB02-E511-B84A-0025901AC3F8.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F09483B5-9D03-E511-9BF3-0025905A606A.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F81F98A6-CE02-E511-8D2F-008CFA0518D4.root',
       '/store/mc/RunIISpring15DR74/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/FC14083B-EF02-E511-8637-002590747DE2.root' ] );


secFiles.extend( [
               ] )

