import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/0CF92183-0DD1-E811-A6CC-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/3CF68ED6-CED1-E811-896A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/48D452F0-CFD1-E811-B6F1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/4A62B48A-CBD1-E811-911E-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/5249C53B-11D1-E811-9DDF-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/52669198-43D1-E811-AD14-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/5AB18CAE-06D2-E811-B286-EC0D9A8221FE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/5E8CC80C-0CD1-E811-B9A6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/68013BA0-D1D1-E811-AE40-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/70FD055A-D0D1-E811-B4D6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/74E61625-0DD1-E811-B632-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/767217A5-0DD1-E811-8A52-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/7A25E2AB-0CD1-E811-BEE2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/82C5D2F3-26D1-E811-9395-24BE05CEEB81.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/8CE9CA1C-28D1-E811-8DF5-24BE05C626B1.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/8E1CBD4F-CDD1-E811-9826-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/8EA1C190-D0D1-E811-81B6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/9033019B-43D1-E811-9069-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/92C2AC42-0FD1-E811-B970-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/942BFE37-12D1-E811-9154-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/9802F87C-0CD1-E811-9C9C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/9C950E27-0FD1-E811-AD27-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/B020C78B-11D1-E811-B413-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/B2222A84-1BD1-E811-9697-B8CA3A70A410.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/BCA96591-0AD1-E811-B132-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/D0CCA785-10D1-E811-9350-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/D48E360B-0ED1-E811-8DF0-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/DCCF9E03-0FD1-E811-A9A0-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/E2B47A5C-D0D1-E811-BD19-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/E409ACCB-0BD1-E811-AA95-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/00000/F2038A6E-0AD1-E811-9D7A-0242AC130002.root',
] )
