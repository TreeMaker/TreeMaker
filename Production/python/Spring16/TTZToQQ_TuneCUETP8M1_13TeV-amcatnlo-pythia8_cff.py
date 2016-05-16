import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/020C3A78-B402-E611-8FDA-001E675A622F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1E145555-BB02-E611-9BE7-D4AE526A1654.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/26AE0D62-B302-E611-AB0A-0CC47A0109A6.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/280D7282-9102-E611-AC6A-90B11C08C1BA.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/2EF9A09E-B302-E611-B097-D4AE526A03AD.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3EC8F625-BB02-E611-B4F9-842B2B71EDBE.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/4E9EC9AF-A903-E611-B287-001E67A3EF70.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/5C4B5C1C-9102-E611-8198-842B2B71EDBE.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/7AF65473-B402-E611-AEC6-001E67A3F92F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/7EA892C8-CE03-E611-86C0-D4AE526A1687.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8404EAD8-BA02-E611-A120-001E67A3F92F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/92D5F010-CE03-E611-BB62-90B11C04F778.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/984F636C-B302-E611-9B1C-842B2B7669E2.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/AE2CDC4B-B302-E611-B955-1CC1DE19285A.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CC2B6171-9102-E611-82F5-001E67DFFB31.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CE0C9233-BB02-E611-ACD3-782BCB161FC2.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/DEFCA7A7-B302-E611-A939-D4AE526A0CE0.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E05D336D-9102-E611-AC78-90B11C064B50.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F42466B2-D902-E611-9E30-0CC47A009258.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F429F7A6-B302-E611-B7F4-0CC47A00941C.root',
] )
