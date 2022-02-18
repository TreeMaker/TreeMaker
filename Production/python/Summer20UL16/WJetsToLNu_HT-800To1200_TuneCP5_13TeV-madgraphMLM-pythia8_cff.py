import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/24091771-A11E-7343-84D9-026786B404B7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/4F3C7CB4-0C6F-374F-A3CC-9B95A99933B8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/623C0F05-F71E-9C4F-AFE4-3787E4621A8C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/6F23B97A-1F72-F04A-B7CC-309988842EA0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/79C21123-A36B-1F43-823C-2F2897754D77.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/8C7D64F9-3B94-7242-A8B0-5076C3B8141F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/B1A25768-BAB6-F34E-9975-B1F61509C03D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/C9928F98-30B8-C04A-897C-36B86F2D102E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/D75947C2-F89D-3B40-91D8-68CBB851B265.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/DCEEECD6-56C0-BB40-B1C2-90F8B642C046.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F924985D-D6AB-DA4A-BFFE-8585794F7E00.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/079DCBE8-42C5-CA43-8BDD-85F91D357EA7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/1E40B6BC-C26C-E842-A478-B6337F286688.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/2198B388-855A-B04B-8316-34870C14F935.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/22CB91AD-C6DE-3C42-B594-D4D16E99E4A6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/3440999E-2BFF-F54A-9015-00AD74C98B01.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/361B4E70-D32B-9E4C-B547-CAA81D3B3273.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/3816E541-10CB-8E4A-BFD9-1A486833DBCD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/4A198727-9207-1147-8B3F-038A00FDD2D5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/536042AF-8D57-1544-8F3B-E5D9CDA909F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/8D763CE8-A747-EC4F-94E7-37F524FE8FCF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/956D4172-10C3-B446-A1EE-420332CC77FF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/99FF1671-257E-0B43-A94C-296F63B5C751.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/9C35E3E3-B19E-674B-BB38-9026E25A65B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/CDF99018-7966-0E43-BBF8-73BF8C166A86.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/CEB9C4B6-17B1-8C43-AC46-0C2C038476C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/FC5EDB1A-FB1B-694E-AB22-23EF0CB83395.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/1005D5E2-F969-AC40-BA41-359735D75E7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/18905F50-75D0-554E-83E3-A21F63F9D242.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/3602C309-C923-E343-9173-48531947C62B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/4C8FB3D9-3132-4940-879E-587E36ABADDD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7478F3DF-8356-704F-ADF8-CDB189EED55A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/75E6181F-C2F2-8141-BD68-E6CF1C13EA05.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/888F0DA3-BFE7-6F44-8DAE-5FC21D0DDD2C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/8F3ADA1A-07AD-DB4F-AEB5-65DB821D1F5D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/B79218E4-18AF-0F4A-9428-07A6E29903AF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/B892A8DF-75FA-AA48-9B45-68D0944A08A6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/C076EE3F-B479-7144-ABE1-293E8F1D2237.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/C6473CB7-FFF3-AD43-B359-F3B739588478.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/DD6CE6BE-62AB-9746-8E7E-18E480575002.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/EAA17914-4A3A-DC43-BD24-4740978669F3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/FC7D50E3-FAF0-E44F-AA9D-19F96F229F07.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0697708C-EAAA-AE45-9825-C4B0B2CBC670.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/6C058F18-34B9-5A41-B9BE-64731C10D9BB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7924F8CC-F6FB-E74C-BA7D-947C021F95A9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7D5AB69D-9FBE-9645-B9B3-B742B77AD41C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7FEC350B-5D6D-1F49-B353-CC44C39C6C04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/81064402-B567-704C-9A07-E29D59314ACD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/987FBC30-DB2F-0E48-B4E3-2A18EF621E7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/98D730D6-2D5B-5748-8FE2-731D9E4651E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/A77303E4-679D-2246-9D05-F0876D196D8C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/AD12ABBC-C19D-B346-B208-FC315407898B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B9901669-AAA1-2341-B5EF-03FD95DC8E05.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BE2FD0CF-F492-DC4D-8C93-BE8E5349BA3F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C80202A0-08ED-8247-B78F-7AA79AD51AA1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F1ECDEBB-32B9-804F-800E-8C42AEFF316F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F83F262E-9E5C-DE4E-AA08-0FED854B77C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0204AA3B-427D-1145-BDF3-32E22B6E90CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/14B490BF-B813-7E4B-9079-794F1E112991.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/1DED81BF-6C72-FC45-84B1-CCF012A8EDA3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/1E08C245-B07B-6E40-A126-B860A777208B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3637252B-A529-C14A-98CF-7D09EDA9304E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3D7600A7-FCA0-1348-840D-36B81A3B0B7F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4669566D-B97B-4248-96C2-AB770EC14FA7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4B646AB6-0222-B249-A7D8-32AFE3F5C709.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4DABF176-2C1D-7D49-BDC9-89CC9D78F813.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5402D3ED-EA83-F34E-B8C9-AF65FE6828B9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/61862872-D84F-B545-A2E3-B6B251729566.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6D17E7F1-0E11-2A44-808D-7CC83461EE75.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8DADF2F5-AB82-FE4C-9DAB-D3552FCE1ED3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8EA22CE2-EACA-8442-A033-689F3E62BF32.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A2D56F7A-E2B0-6744-B55D-4107CDA286D7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A86DA521-23E2-D64C-9465-20C0987AB7E7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/AC84A393-AD74-4048-A21F-E6CB12EE9466.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B882187E-D618-CF47-BD8D-F4F5B7045361.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C19A7221-D877-1E48-9E14-DE74041513EB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C3BA6B19-70AE-654F-BB8A-9D6B9E7F9F74.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D0969988-35C3-554B-86CB-3129292F22F5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E3715E0C-013B-4046-8933-E68EA873E490.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E4C6A99E-EDAE-CD4E-991E-266C79CB6F41.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F93B514D-B993-CD41-BD76-FE63F3992069.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FFEDFBDD-1707-8644-A283-3F641E71F3AC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/4EF4B9C6-6568-4A47-89D6-856FF48D7446.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/5A0E8B42-BB98-1A42-BB1E-76A6081A4EBA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/613F4B4D-1595-D841-8CD0-4C47F314D1A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/86209619-2DD5-6645-95BF-DEA72455EAF6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/91B993DA-AFA5-BD4F-B03A-8249E7247323.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/B54B1999-76D8-894D-830D-34AEC8FC1354.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/C5F74FA8-38B0-354D-989F-3C0FA4317159.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/E49AAA47-9DC2-DC4F-A844-B429440A4A89.root',
] )