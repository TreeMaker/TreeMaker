import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00E16912-0CAE-E611-88F8-C4346BC7EE18.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0E51268C-11AE-E611-864D-00266CFEFDEC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1434A71B-13AE-E611-BF5C-C4346BC8C638.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/164B4BE7-16AE-E611-BD29-001E675A690A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/18AFADC9-16AE-E611-B108-002481DE4BF0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2614E3B8-E8AD-E611-AC96-5065F37DD491.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/28A9FAE5-16AE-E611-8DEB-C4346BC8C310.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/36F4703C-05AE-E611-84C3-00266CFEFDEC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/38826348-08AE-E611-A141-00266CFEFC5C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3AA078EB-16AE-E611-8E10-02163E01769A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40D7D5E4-05AE-E611-909E-001E67F12486.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/50EB2F15-02AE-E611-9468-00266CFEFDE0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58E91394-07AE-E611-8DE1-00266CFEFC38.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/641DDE36-0AAE-E611-8C75-C4346BBF3E78.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6E752FE5-16AE-E611-90BF-0025905C53DC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7CB43FE7-0CAE-E611-87FA-008CFAF293FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8C98D0D0-16AE-E611-B26E-24BE05C44BB1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/90D60AD2-16AE-E611-ACFA-0CC47A1DF60C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B658D705-0FAE-E611-A768-C4346BC8C638.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B8B4A2A4-0FAE-E611-A0B2-001E67E5E889.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BA18F2F1-16AE-E611-B2BF-0025901D08B8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BADBC8EE-16AE-E611-9E88-FA163EA2BDE9.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2B736E0-0AAE-E611-A1BD-00266CFEFC38.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CCA5F241-0EAE-E611-9327-00266CFEFC5C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D8B10F87-16AE-E611-80C0-002590D9D896.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F25B5270-0DAE-E611-8B99-C4346BBF3E78.root',
       '/store/mc/RunIISummer16MiniAODv2/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FAD56FD1-16AE-E611-A74B-7845C4FBB6C8.root',
] )
