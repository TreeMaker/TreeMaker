import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/0067F6F6-705E-784C-90C0-884699BE39A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/0228AC63-12A1-4F46-838D-52656E74AC9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/1DFBF21B-C37A-FE41-AF34-1941F10AE87B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/31A22A53-F305-7144-A18A-3DC4B6085DFB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/3301AF10-3796-1A4A-AFE6-0F59EBC2DAE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/346EE733-68CE-D84D-B2A6-413A12BDF34C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/500CF009-8CBB-7449-8ED9-393A02266D53.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/5B96EA1D-A5A8-CB4D-B9E3-5ECC7918E568.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/6014157E-43CC-5C47-B25D-FD405121083A.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/62B99007-1C1A-9C44-9E38-39AA826B49EB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/6B676E1E-C3AC-E24E-86F2-8F27EE755132.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/6EC12A67-4ED2-9D45-9A74-BDAEFC8314A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/70A68B21-05D6-AD41-8F64-0508230F442D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/77DC8FE6-4549-F04E-AA59-CDD4DD70F6CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/7E34D1DF-06D4-3C41-AB9C-6C895C48408F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/82FF4EEC-73FF-AF4B-8089-3E1176FA948F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/A7F61C5C-C726-984B-A3BF-10DB1FBF62F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/A8D4C432-4F94-3844-98ED-7C77657EF972.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/B0746178-227C-BB4E-9746-517BC7319D6E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/B146AB65-1860-AB43-B75A-76F0E3668BDC.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/D672BD7E-B3C6-D34C-91C0-23345F873E7C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/D7230550-676A-B54B-B96C-B37558D01CBB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/DD1BDC65-ED25-1E4B-B067-BA13BADEFE78.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E05DA420-A299-F049-ADE4-39F75CA8357B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E43BC19C-8D06-9B48-B28B-AC4539AE4012.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E56F60AD-C066-D94E-88DB-80C082EB1F99.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E5E911AF-68AF-1648-B742-FE5B8B12FF53.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E782DAAA-09E8-9C48-BAA2-9C90120B9464.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/EBD1EFDD-4115-474F-B8EF-BEA2DA88E986.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/EE25D5A3-AE8A-4340-A919-B8092D5E7119.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/EECEF0AD-3D40-7B49-9807-6C57B5E024F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/EF562343-AA0B-5C43-B217-15A0BBA25576.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/F4F8033A-6F60-3A4E-A622-7A9D97271316.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/F6EB6AAC-AB1A-5240-BE76-33794345CDE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/FA0627B6-A1A5-2D43-AF4E-88DEF495E83A.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/FA57CD1D-5F25-CB4C-9C51-D7E02A08607B.root',
] )
