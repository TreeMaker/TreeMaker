import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/002AEC99-1003-E511-A57F-0CC47A4DEE12.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0669419B-0B03-E511-BEE7-008CFA58074C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/104E7503-1203-E511-8D9A-008CFA064760.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/14497FDB-3003-E511-898A-008CFA582D78.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/1E45CDEE-1E03-E511-8B06-0025905B85EE.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/227BF337-3403-E511-A637-0025905A60E4.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/30D20B0A-2B03-E511-A993-008CFA0A57B8.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/363C6DD8-1C03-E511-81D8-002590D0AFC8.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/3A20D2AC-1403-E511-A189-008CFA064700.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/3C620D9E-2B03-E511-B6D0-0025905B8562.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/40A70519-4C03-E511-AFD1-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/4A2DA515-2503-E511-8E25-008CFA05E8F0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/5C434544-2403-E511-8601-0025905A48C0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/62F8448B-2C03-E511-B6BF-0025905B8596.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/6EE1FC17-1B03-E511-973E-002590D0AF58.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/7034BF19-1603-E511-B485-E0CB4E553659.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/72BA90AB-2003-E511-AD19-008CFA064778.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/80D83D1A-4C03-E511-99ED-0025905A60BC.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/86FC35CD-4903-E511-A337-0CC47A4DED86.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/96096402-2903-E511-9A4C-008CFA1980B8.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/A048FEF1-1903-E511-BB65-008CFA05E9E0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/A42187E0-2903-E511-85CC-0025905A48EC.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/A82E8FC9-3103-E511-B037-0025905A6084.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/B49F6745-2903-E511-B5A1-0025905B857C.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/CA971E49-2E03-E511-9509-0025905AA9F0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/CE98D3C4-2A03-E511-94B1-0025905A48F2.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D02B23B6-2703-E511-882E-0025905A608E.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D4E89AAA-2703-E511-A5FD-0025905A60F4.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/DC7C1A80-0E03-E511-AA6E-3417EBE4E882.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/DE65270A-1903-E511-BA5D-002590D0B020.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/EAAE2BAB-2D03-E511-B18F-0025905A60AA.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/F07391CF-4B03-E511-9290-008CFA0A59E0.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/F61DF9BD-2203-E511-A075-0025905A48D8.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/FAF64FB2-2203-E511-99C5-0CC47A4DEE02.root',
       '/store/mc/RunIISpring15DR74/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/FCB8A12C-1F03-E511-BE38-00259073E37C.root' ] );


secFiles.extend( [
               ] )

