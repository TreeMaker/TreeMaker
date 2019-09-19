import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/005BC4EB-F419-E911-B280-002590DE6E28.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/30B035CD-FE19-E911-AC7C-001EC9ADFCC5.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3CD66FED-F419-E911-B7A4-1866DA89061C.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5CF17E5F-651A-E911-8E00-001EC9ADFCAC.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/18AA0602-BD0A-E911-AB51-AC1F6B0DE45C.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/1E0D71DD-E811-E911-A9BD-7CD30AD0A750.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/2600F9CC-EC0E-E911-91AC-0CC47AB64A5A.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/2AD16D9B-F911-E911-BC57-0CC47A4C8F0C.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/2C676D0F-C80A-E911-BD29-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/36C1ACD9-3A11-E911-94EE-008CFA0A5830.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/3E75F718-1311-E911-961D-0CC47AFC3C18.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/4001D02A-380A-E911-8778-008CFAF52264.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/40C7A178-0011-E911-BA17-0025905C9742.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/4C7D145F-7409-E911-9D18-A4BF01287D43.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/50A40CBC-3211-E911-A857-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/586AD247-2707-E911-8895-AC1F6B23C846.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/5AEE06D4-C30A-E911-98C7-AC1F6B0DE3F4.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/5CCCFFAE-CE0A-E911-9480-48FD8E2824C9.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/6C94915F-0811-E911-ABEF-002590E3A286.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/746A8E1D-9108-E911-9F04-3417EBE70663.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/8CB9772B-B30A-E911-8F4D-AC1F6B0DE338.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/908B5817-A20A-E911-95EE-AC1F6B0DE338.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/92746B32-FB10-E911-B622-D4AE526A048B.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/9E0FABE2-7F0E-E911-BDD7-F04DA274CAA9.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/9E156B4B-FF0A-E911-ADA1-AC1F6B0DE4A8.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/9E94610D-0811-E911-8AA7-A4BF01125DDE.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/A0C21F02-FD10-E911-9660-509A4C83D54F.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/AE324B3F-F40A-E911-95AA-F4CE46B27A1A.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/B238B71E-910E-E911-A0A7-0CC47A4DED92.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/B23D0C73-FE10-E911-9633-00259029E920.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/DA7501F5-E60A-E911-AF45-AC1F6B0F71D2.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/DE0120C9-E10A-E911-8A73-48D539D3335B.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/E2117B32-880E-E911-9A75-0023AEEEB559.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/E6DA18B4-0211-E911-8428-00259073E39C.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/EC3504A3-1211-E911-BD19-00266CFCCC38.root',
       '/store/mc/RunIIFall17MiniAODv2/tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/F423DE33-0C11-E911-9FE5-008CFA197DB8.root',
] )
