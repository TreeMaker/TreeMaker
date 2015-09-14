import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/005AF174-DE01-E511-94EC-20CF3027A5E8.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/7499F6AC-DE01-E511-81A7-008CFA052C0C.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/8AD69B78-DE01-E511-9CBA-0025907B4F3A.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/F4506047-DF01-E511-B499-0025905A60E4.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/80FCECFD-4502-E511-9022-0CC47A4DED8A.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A4E6A29E-4502-E511-ADAE-0025905A60B6.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B0EA1E9F-4502-E511-AAEC-C4346BC08440.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B65B6EBA-4502-E511-A762-0CC47A4DEDF2.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CEB64D03-4602-E511-BE43-00259073E3D0.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D65881FD-4502-E511-96B6-485B39800BBA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F828789C-4502-E511-B357-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/02B13991-FD01-E511-AF4C-20CF3019DEED.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/14B62E94-FD01-E511-8E8D-E0CB4E19F983.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/84EF5A5F-FD01-E511-AE71-0CC47A4D99D6.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CA8A6E82-EA01-E511-8768-00266CFFBF80.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CC9DB991-FD01-E511-9F53-20CF305B04DA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D6A6229D-FD01-E511-A52F-E0CB4E29C4FA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E42B2292-FD01-E511-B46B-00259073E478.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/EACE5018-EB01-E511-83FD-003048FFCB8C.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F206E016-EB01-E511-875D-0025905A60A0.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/2A3A9A2D-1802-E511-A45E-0CC47A4DEE12.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/2C7D9EC0-1802-E511-AA5A-002590D0AFCA.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/2E510FBF-3C02-E511-84CC-0025905B855C.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/441E7FE9-3C02-E511-A3C3-6CC2173BC370.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/5E37E5BE-3C02-E511-9EAC-003048FFCB74.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/823E96A3-1702-E511-ACC6-002590D0B062.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/866B1F99-1702-E511-B594-00259073E370.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/B22EB3C4-1802-E511-9CD4-E0CB4E553696.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/CCEE7CE8-3C02-E511-A848-0CC47A4D9A58.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D6B0F799-1702-E511-AD10-0CC47A4DEDB0.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/E87F3D48-1A02-E511-B60A-485B39897214.root',
       '/store/mc/RunIISpring15DR74/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/EE9F36AC-1902-E511-A580-20CF305B04F0.root' ] );


secFiles.extend( [
               ] )

