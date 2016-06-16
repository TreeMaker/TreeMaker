import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/20328CBD-AEFF-E511-A226-008CFAF2059C.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2284B156-79FF-E511-888C-5065F38182E1.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/362014EA-14FF-E511-AC42-008CFA1C645C.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3A688B61-B1FF-E511-8A6B-02163E0165FC.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/40EBB0D6-ABFF-E511-9D86-001E675A69DC.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/540253E1-ABFF-E511-AB93-0CC47A57CC42.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6CE3AA7C-84FE-E511-AC67-002590D9D8BC.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7EFAE31E-ACFF-E511-9148-549F3525DB98.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/82829064-79FF-E511-A4CB-0CC47A13CEF4.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/82E3009E-2DFF-E511-A3E9-0CC47A78A4B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/860CE0EF-ABFF-E511-B0B7-0025907277FE.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/867413FC-C7FF-E511-976C-0CC47A01CAEA.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A006F448-86FE-E511-8D51-0CC47A78A4A6.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/AC6060F3-30FF-E511-A34F-549F3525C4EC.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/AEA2C8C5-CBFE-E511-9BEC-0CC47A57D036.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/BC9B17E0-14FF-E511-8834-001E67A3EA89.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D40454C9-54FF-E511-99F8-02163E0178FA.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D4F7D664-B1FF-E511-BF5C-008CFA1974A0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/DA9361C6-2DFF-E511-9FB0-008CFA110DD8.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E431EA1A-D0FF-E511-B602-002590747E40.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/EE61E9AB-9DFE-E511-91B5-0025901ABB72.root',
       '/store/mc/RunIISpring16MiniAODv1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F25DA76B-84FE-E511-A913-0025901AA5AE.root',
] )
