import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/183EF18A-4308-E511-A1ED-90E6BA693DFF.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/24D4E806-3D08-E511-BD45-00A0D1EEFF18.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/30F6CEA1-C408-E511-BCA6-001517E7410C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/3C563AC1-3708-E511-BC09-00266CF9B86C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/588F941B-4208-E511-B3C8-001517E73360.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/5EC7651B-4208-E511-A6AD-485B3919F121.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/6EC97AB6-C508-E511-81C1-848F69FD4CB2.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/9A8484E5-3708-E511-90F2-00266CF25F34.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/B86B5699-4308-E511-9948-001E67A40523.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/D0C5AB0F-4208-E511-942A-0026182FD77A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/D45DD4EB-3708-E511-9256-00A0D1EE8B3C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/E08E975F-4108-E511-8E0C-00A0D1EE965C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/EC789BCE-3708-E511-A5A5-00266CF271E8.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/F072F35F-4108-E511-95A3-00266CF9BF5C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/50000/F672590C-3D08-E511-B82C-7845C4FC361A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/0097FEE2-0509-E511-9131-001D09FDD7C5.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/00EBE252-B709-E511-8BC0-00074305CD97.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/04C8E84A-F208-E511-A04A-F04DA275101A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/123EDC5A-D309-E511-88BF-00259073E37A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/1ACDBA65-FE08-E511-B236-3417EBE6443E.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/1E30C2DF-0609-E511-BA5E-F04DA275C328.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/223EA6A4-1909-E511-B18F-00266CFAE144.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/2ABE35A1-1909-E511-AA8C-848F69FD28E3.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/30B17C26-0909-E511-A011-0002C94CD120.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/4248BFFD-2C09-E511-B721-7845C4FC370D.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/4E89C663-0409-E511-B4F9-3417EBE2F4B1.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/56A81CC7-1909-E511-9FC7-848F69FD2520.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/5C7EBBE7-0A09-E511-913F-7845C4FC3A94.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/604B2F9E-1909-E511-904A-180373FF8456.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/60FCE875-5409-E511-9D9E-00266CF25C88.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/62DF8837-F008-E511-8874-848F69FD4E41.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/680B1724-EE08-E511-8620-7845C4FC3C6B.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/70CC10B3-1909-E511-BC3D-7845C4FC3641.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/84D7E34A-EF08-E511-A9F8-7845C4FC3B6F.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/88CAFF7F-D309-E511-9D45-848F69FD289B.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/8E60F369-0509-E511-B8F4-7845C4FC3C7D.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/960E00D9-0509-E511-997D-F04DA275C2CE.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/9C79174B-F208-E511-BB04-848F69FD28AD.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/A836A9E1-0509-E511-BD80-3417EBE34C81.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/AC406108-EC08-E511-BD36-00A0D1EEF5B4.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/B4D3C9F8-FC08-E511-906F-7845C4F9321B.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/B845988C-0B09-E511-8755-3417EBE644B3.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/BA53FC68-D309-E511-83AB-A0369F3102F6.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/C8A67222-EE08-E511-AB5F-848F69FD3EC9.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/C8F3162F-F008-E511-9ACE-7845C4FC3A52.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/CA3EB516-0909-E511-BBF2-7845C4FC3C7D.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/CC7350F1-0609-E511-BAE7-7845C4FC359F.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/D2ED5A49-F208-E511-8AE5-7845C4FC361A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/D4FE6E21-EE08-E511-922A-7845C4FC3C6B.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/DEE9FB21-EE08-E511-899F-7845C4FC374C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/E0FF3D6F-2D09-E511-B565-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/E2996619-EC08-E511-B401-848F69FD4E41.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/E456A92C-F008-E511-87B6-3417EBE2F334.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/E4F36328-0B09-E511-8AD5-848F69FD457A.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/F603E24E-EF08-E511-B3BD-7845C4F92E7F.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v1/70000/F8BDC6AC-0409-E511-8DFB-7845C4F92E7F.root' ] );


secFiles.extend( [
               ] )

