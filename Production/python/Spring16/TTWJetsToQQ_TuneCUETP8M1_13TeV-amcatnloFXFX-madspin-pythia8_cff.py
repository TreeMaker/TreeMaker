import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/024C37A3-9EFB-E511-AA73-D48564597C70.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/08A4DC9F-9EFB-E511-8578-44A84225C911.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1A0C48C4-9EFB-E511-AA34-0025907B4F04.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1AD737E0-90FB-E511-9C78-B083FED07198.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3026E9DD-90FB-E511-B554-44A84225C629.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8AF656AB-9EFB-E511-A225-002590743042.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/925E28F5-A9FB-E511-9ED3-002590D8C7E2.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/ACA66BAB-9EFB-E511-8E8F-00259074AE52.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/BEF5BB0D-B3FB-E511-958B-44A842240F8D.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D2CB7880-D5FB-E511-9E75-44A84225C3D0.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D6A88E5C-D5FB-E511-BDC6-0090FAA57910.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E076BD6C-AAFB-E511-A880-B083FED04276.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E28EF1B6-9EFB-E511-B983-44A84225C4EB.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/140948D7-A8FB-E511-B5F0-0025907B4F04.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/2C8E7285-8DFB-E511-A412-00259073E520.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/46FE81E1-DDFB-E511-B57C-00259073E52A.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/507D30E0-A2FB-E511-97A3-B083FED13803.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/60F0ED5F-DDFB-E511-BADE-0090FAA58134.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/80867CC3-A8FB-E511-A727-002590D6013C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/9E97DAC8-C0FB-E511-AE52-B083FED16468.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/E8879086-AEFB-E511-87D2-44A84225C851.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/40000/F440B194-8DFB-E511-9881-001E4F1BC1D4.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/80000/546E8969-E9FB-E511-83B5-B083FECFD4F0.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/80000/72A81F58-E9FB-E511-97D0-0090FA9DFD8A.root',
       '/store/mc/RunIISpring16MiniAODv1/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/80000/84C7F76C-E9FB-E511-81E1-44A84225CDFE.root',
] )
