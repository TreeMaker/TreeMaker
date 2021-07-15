import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/052D6AF5-5093-9441-87D9-0A025DDA417B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/10B29305-BCC0-9C49-9352-E2FB088A6904.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/14B7BD46-3D1E-6243-B5DC-E61F73345835.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/1A42A956-0915-AB47-B523-25559BBDAC24.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/1AD014BE-B308-584A-955A-AC487022C048.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/1B7C8595-1AC2-EC4B-B253-0E73968A1A6D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/228C9CDA-D24D-7845-A44A-84F2787B7ECC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/28456189-7D8F-E14F-B583-24D60CAC00A9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2F417A93-19F9-A341-9493-D07704D02499.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/36BA049F-784D-0C4F-95F0-8DC3194762B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3760C53E-7D86-9D44-B7EE-053579E35501.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/39A4DC7F-037B-C54B-B2EB-0F4FCA087F6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3DDE318C-F518-B44B-B152-0044B148B8DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3EDB543A-A86F-B54D-BFDD-BE0E34F96887.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/4F4BC187-6A99-2E42-95B7-21BF4B5564AD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/5B8E7B7E-C3F8-C04E-B737-18C3DD226D18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/5E2F79F4-16D5-7C4F-BBF3-187F47FD6FE5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/72970C61-DB93-554A-B5DB-947AC5BE08F6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/72EF6BFF-F54E-DA43-A481-31030FECD164.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/79E2B792-7115-A44D-82C1-9681EE0A3AA9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7ADB0696-6084-F94D-B7DD-DE5325329970.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7F7B10F0-D614-6049-9F96-791CC3CA8CFB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7F9382E8-A191-EC4D-8550-A59CE6870013.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/80AC8F3C-2483-0C4C-BA5A-BE9F74D1D762.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/81CD011B-A44F-104A-9AAF-65632B45F823.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/9185CBF5-8376-F449-93DF-53A2C9860EC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/945B3FE7-3F48-1B4C-AEC0-CB2F140F47E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/9B40C5F5-D52A-0A44-A996-681CD7443E9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A024266A-8F79-3547-8CF5-C73D5405EAFE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A33314F1-D8A5-E54A-BAE9-0191F865E559.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A617A4A1-0C15-2B46-9796-E7214B91F505.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/AE930ED1-864F-5C4F-8123-5B436E301769.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B169EE7D-C608-3B4F-94D0-475A305C1217.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B2CD40A6-BFEE-8D4A-87F0-9BAA635DB4BE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B96A6E0B-02B9-1A41-AB1E-9A6C536F7DB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BBEB4C60-1EF3-BE40-8408-2BFA57F78D16.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BEEF8F97-F6E2-D040-9AA0-F62A1B4D3395.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/CE8838EE-29ED-5348-A7D0-4C9A94CC6347.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D01FED94-B8FD-1B41-9BE0-91B2C8DB76DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DCEC0D84-40C7-3845-9F46-42578EFDE953.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/EBB271DC-0019-964D-BBA1-78242ED5DBE7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F5633E4C-9E06-2741-9957-B7EDF53F1B56.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F91BEE95-00CE-A84C-86D9-FF19B6E136E5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F94A56C1-B705-C740-BA75-C916B4CD4B14.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/70000/FCA67513-8DAE-EB47-86DB-8080504AD189.root',
] )
