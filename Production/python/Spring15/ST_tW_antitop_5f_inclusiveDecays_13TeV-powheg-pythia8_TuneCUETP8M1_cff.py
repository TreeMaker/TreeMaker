import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/906D9FB3-4906-E511-9C81-0025905A6056.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/EEE9127A-4906-E511-ABE9-F45214C748B6.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/00521409-AE05-E511-8DBE-00259074AE8A.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/02B6373F-5C06-E511-97C5-0025905A6092.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/04BDB74B-B805-E511-B532-00259073E442.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/067182F3-AD05-E511-AB4B-00259073E322.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0A7DF19E-1906-E511-BE74-0026189438CB.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0E94E17C-B805-E511-92EA-00259073E3AE.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1A72E98A-C705-E511-A042-0025907277E8.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/30045136-5C06-E511-A5DB-0026189438C4.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/329C3EE1-AC05-E511-BACB-00259073E42E.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3463F3A4-B506-E511-BF97-0025905B8572.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/363DDBA9-B506-E511-8FB0-003048FFCC2C.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5427793A-5C06-E511-AF5C-0025905A48B2.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5C8D0573-AC05-E511-BA29-00259073E4BC.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/68003405-AE05-E511-AB4A-002590747E1A.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/70AEDFC2-B506-E511-8B59-0002C90F8094.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8060263C-5C06-E511-9885-0025905A60F4.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8C069105-AE05-E511-8B35-00259074AE5C.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8E75C05F-B805-E511-8DDA-00259073E50A.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/960D751C-7E06-E511-B68F-0025905A48D0.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9E2CB305-AE05-E511-B997-00259073E4DA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9E5D6613-B606-E511-9C6E-00259074AE7E.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B254B3E7-AD05-E511-B214-00259073E4E6.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C661FC30-9A06-E511-B025-00259074AE44.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CE367A44-BE05-E511-9773-F45214C748B6.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D4C8BD4B-D105-E511-8F7B-0002C90F8088.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DA9A757A-B805-E511-9CAE-00259073E4EA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DEB77C7F-B805-E511-B903-002590747D92.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F2EDDD40-BF05-E511-91D1-0002C94CD098.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F8C3B17E-B805-E511-9483-00259074AE7E.root',
       '/store/mc/RunIISpring15DR74/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FAE2246B-1906-E511-8052-0025905964C4.root' ] );


secFiles.extend( [
               ] )

