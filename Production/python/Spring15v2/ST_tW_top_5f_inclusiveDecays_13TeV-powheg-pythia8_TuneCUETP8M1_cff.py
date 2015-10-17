import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/123BBFB2-7E71-E511-9EDE-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/1ADF17B3-7E71-E511-9AF8-00261894396D.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/32F080B7-7E71-E511-9B37-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/449FDABF-7E71-E511-B95C-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/4AB7C5B6-7E71-E511-A215-0025905A60E4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/767D215B-7D71-E511-9CD5-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/7A0FFD24-7E71-E511-BF21-0025905A60B6.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/7A909321-7E71-E511-B36D-002590593902.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/80616E57-7D71-E511-9305-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/82336D57-7D71-E511-A4F0-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/8242CBB1-7E71-E511-ADD6-002618FDA28E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/8694801F-7E71-E511-A02A-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/9AFB5359-7D71-E511-B710-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/B2E84760-7D71-E511-AF0E-002618943982.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/B6FF0258-7D71-E511-B303-00261894397B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/BAF818B7-7E71-E511-B5CD-0025905A60B8.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/C6460EB3-7E71-E511-94EA-00261894389D.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/C6B46CB4-7E71-E511-A969-002618943972.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/CA10365F-7D71-E511-B71E-0025905964C0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/DC30F65D-7D71-E511-9C75-00261894387E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/DEB463AF-7E71-E511-9E56-00261894391B.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/E4DF5D58-7D71-E511-80EC-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/50000/EA77B3B3-7E71-E511-94AE-002354EF3BE0.root' ] );


secFiles.extend( [
               ] )

