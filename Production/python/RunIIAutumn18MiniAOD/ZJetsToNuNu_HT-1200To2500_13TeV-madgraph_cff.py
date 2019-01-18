import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/744F7268-5997-3444-9F34-F6DE34AF6297.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9213CD07-783D-9046-9D0E-C99ADB35AA83.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/EDE4FABE-AD66-1C45-BF31-1937C5501AC4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F52759B7-293F-1247-8D03-D284730F11DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/0373F62F-56A9-734E-883E-CDA1FA0126A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/109DF5DB-1956-4045-B1A9-E1F86856479F.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/17586396-3DD7-494E-8004-89F1BFDE6B02.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/17E682FE-AB30-8940-8D42-632D4922B3D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/1B2CECA0-BA5F-C246-8D97-F810AA24B583.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/1C75A360-9481-F645-992F-8E14C5FFCA15.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/2D01888E-F42C-AC4A-B8DD-A8ADF0E7E432.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/46B7C118-A28F-434E-89BC-9282C30118B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/4DF88040-E042-594D-8431-162D58C66F8C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/5A436698-B64A-7744-B80A-C1A9FCDA4C0E.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/6342CB7F-09AA-6043-B033-9EB5F72644CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/799AA43D-CC32-BE43-9C33-ED38B652B51A.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/84FE1CC9-1DAC-8247-992F-021172A061B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/A0CE84EF-33CF-9C41-9B17-BCF30CA602D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/D2F47A28-3CF2-BD43-B4B0-ECA8153DDE51.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/E143C3C0-CE8B-D242-852B-731AC4E60773.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/FA7B2A73-6D91-D74D-8636-3C0A298D1CB3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/FACEA0A9-6D04-5045-82DA-F106C34ADF9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/FDDF69BB-CACA-9241-8FC9-CB8E67BDCE10.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/6ED38EF4-C543-DF42-95BA-C41454A92051.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/A7873DC3-55C3-394A-8AEF-08B92EA83ACB.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/DCB63F1E-ECAE-2E42-A927-B60A2FB46846.root',
] )
