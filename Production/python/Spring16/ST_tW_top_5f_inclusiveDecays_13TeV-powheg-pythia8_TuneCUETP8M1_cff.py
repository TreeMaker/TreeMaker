import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/04C33727-AA06-E611-91A8-0025905C2CBE.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/10BD721D-AA06-E611-AD17-0025905C96A4.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/125D5872-1505-E611-B70A-0025905C4264.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1415F004-BE04-E611-9E9C-0025904E9010.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/22062DA9-C404-E611-B0D3-0025905C975C.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2A6685FB-1A05-E611-B1A4-0025905C53DE.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2C36411E-AA06-E611-8BCE-0025905C3D3E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3257EB6F-1505-E611-AFCA-0025905C3E68.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/32E3E421-AA06-E611-B057-0025905BA734.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3805491D-AA06-E611-9B31-0025905D1D78.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3867161B-AA06-E611-9556-0025904C6508.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/505AFA21-AA06-E611-8FC9-0025905C3DD8.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/563BC805-BE04-E611-9CDA-0025905C5474.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6619DBA8-C404-E611-8CAA-0025905C43EC.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/785F636D-1505-E611-819C-0025905C9726.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/78A7F51A-AA06-E611-B839-0025905C3DCE.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7ABDE91D-AA06-E611-8AEE-0025905C96A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A2C02D4E-C604-E611-BAD8-0025905C3DD8.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A6D4636A-1505-E611-B162-0025905C2CE8.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/AA6E79A8-C404-E611-97B4-0025905D1D78.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/ACF1B2FA-2605-E611-8BC8-0025904C6566.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B69697FA-1A05-E611-8849-0025905C2CE4.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B8FBD7A9-C404-E611-AA9A-0025905C9726.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C008EB05-BE04-E611-BDCF-0025904C4F52.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D0F4BF8B-2807-E611-A18E-0025905C3E38.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/DC90BBB2-C404-E611-AEDB-0025905C53F0.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F0514E5F-C206-E611-9B8D-0025905C975E.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F44EA4F3-0F05-E611-AF29-0025905C42FE.root',
       '/store/mc/RunIISpring16MiniAODv1/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/FEE58FFC-1A05-E611-A097-0025905C2CE4.root',
] )
