import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/36234526-BC47-E511-813B-008CFA198314.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/52633985-694A-E511-BC90-00266CFE6404.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8EA74C5F-8A48-E511-B4B3-B083FECFF6AB.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/C0D10049-8648-E511-B593-008CFA0A59C0.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/D6E01861-B947-E511-A50D-A4BADB1E67BA.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E8232A16-6E4A-E511-9A32-00266CFFBDAC.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/02BB766B-DC47-E511-BADD-00221982B698.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/04110371-454A-E511-996C-00266CFF0608.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/18E3B08B-E546-E511-A4D1-6CC2173BC120.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/18FE5B72-0548-E511-9AEE-B083FED179D6.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/228A93E7-E047-E511-8921-0025905C94D0.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/28C95C7C-E446-E511-AEBE-00266CF3DF00.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2A5A2874-C447-E511-9F26-008CFA1C64A0.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2AFBCDEB-C848-E511-BD0F-008CFA152144.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/36480F8A-F146-E511-8F3C-842B2B61B189.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/367AA0CD-EF46-E511-9EB0-008CFA0646A4.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3AE4AE4D-EE46-E511-8B44-842B2B61B189.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3E9B3618-DA48-E511-9238-0025905C95FA.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4EB061D8-B048-E511-ADCA-0025901286F0.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/54F6241E-4B4A-E511-A3D4-001517F807D4.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/68C2F0A2-3B47-E511-84F2-B083FED43141.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6C126E39-E846-E511-ACE8-008CFA14FA8C.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7073CFE0-F746-E511-8C89-00266CFCC304.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/727CAE04-4B4A-E511-B779-AC162DACE1B8.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/74D2D7A6-FD46-E511-B495-008CFA064700.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/764E084F-0147-E511-8D45-001B21AEEF2C.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8E223222-E146-E511-810F-0025905C3E36.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A21FD15A-E946-E511-9814-D4AE526DF550.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A8EBF409-1049-E511-88B6-001E67A3FD26.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/BCA39DBF-3049-E511-B301-002590D6004A.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CABAC2F1-5A48-E511-BC8D-0025905A610A.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D012734B-E046-E511-B4CC-6CC2173BBEC0.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D4EC4FAF-C948-E511-854E-6C3BE5B51238.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F817E43B-8248-E511-9D72-00259020083C.root',
       '/store/mc/RunIISpring15DR74/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC8AD1C0-8448-E511-BB3E-0CC47A13CB62.root' ] );


secFiles.extend( [
               ] )

