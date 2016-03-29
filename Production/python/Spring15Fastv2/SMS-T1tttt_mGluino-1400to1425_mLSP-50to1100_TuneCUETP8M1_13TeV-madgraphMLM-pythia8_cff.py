import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0A419BD6-998A-E511-A428-02163E01510A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/0C72100E-D484-E511-9CE8-001E6757E03C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1058886D-D684-E511-B81D-02163E010DAB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/14359C3C-D684-E511-8DD2-02163E013A47.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/18797A20-D684-E511-89C2-02163E016AB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/1ED5763F-D684-E511-9015-02163E016807.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/22088FE4-D784-E511-84D2-02163E013E8D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/240A2518-9B8A-E511-BE1F-002590494C40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/24181B93-998A-E511-855A-02163E010C6B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3E988560-D284-E511-B980-D067E5F90EFD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/3ECE7CDE-D684-E511-90FB-02163E01368A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4832D9DD-1185-E511-A533-02163E012EC2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/48D509BE-998A-E511-BEFC-02163E013EBD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/4C62D306-D484-E511-BCB8-001E675050FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/563CEA5D-D284-E511-BCD1-D067E5F91E90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/56F176FA-D584-E511-AB1D-02163E013F52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/684C15FE-D584-E511-9F7C-001E67579498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/6E7B755E-D684-E511-96CA-02163E0153D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/705C29BD-998A-E511-8F6C-02163E014B98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/70D53DD7-D484-E511-8D17-02163E012F98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/74EDE421-DB84-E511-9339-001E674DA347.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/7A4AECCE-D784-E511-8906-02163E010D31.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/82661777-D684-E511-A92C-02163E01664A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/883F4C7B-DC84-E511-AA31-02163E013E66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8A112593-998A-E511-9B6F-02163E014FF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/8EC94F48-D684-E511-84F7-02163E013E66.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/924A3116-978A-E511-9D3D-02163E016913.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9AAD7FF0-998A-E511-8B1D-0025904B26B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/9C5A9ACB-D784-E511-9920-02163E0148CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/AAE228A3-998A-E511-A773-02163E016913.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C627A5C5-998A-E511-888A-02163E013F32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C87A1A5B-D684-E511-867E-0CC47A04CFFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/C8BF9509-D684-E511-8EF4-02163E01669D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/CEDB4639-3785-E511-90DC-001E675050FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D0A9C802-D684-E511-86CE-02163E011A84.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/D6908EB8-998A-E511-8FE0-02163E00EB2E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/DCF0FA9F-D684-E511-91E7-02163E014BCA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E09BF3A2-998A-E511-84AD-003048F00530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E641CB68-D884-E511-B88F-02163E016958.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E6C926A0-D684-E511-B1E9-02163E013D28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/E828A40A-008B-E511-884F-02163E010CC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F03BD336-D684-E511-90C8-02163E01325C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F0832939-D684-E511-9879-02163E010FB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F4F52CE7-998A-E511-8589-02163E01663D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/F6C59011-D684-E511-AE6E-02163E0148CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/20000/FC0EC2A4-998A-E511-99FD-02163E013562.root' ] );


secFiles.extend( [
               ] )

