import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/0D557E4B-4518-B243-833B-B0A6D9944DBC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/228AFA79-FB75-C24B-AFEE-48C09FA212C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/239D60DE-4C47-D94D-8092-67AF8FCE3ED4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/2A102080-D32B-3244-B346-4E0D83B544EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/2DD104F8-B8AE-8145-A7D5-3649417C1ADF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/342AE708-C684-4C48-9AB7-79223EB0060B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/36A10E10-162D-7740-86CE-710799033E61.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/3740ABD7-A74D-6341-9B83-27A7F2641D68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/38354971-3AB2-DD4A-898B-EB36239B0A04.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/43C2CB85-AB70-584B-8AA2-AE78F3BF5BBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/4FAA8642-173C-CE4F-AD87-EAA9490F9207.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/52C8DE48-CB03-3B44-A410-9637DEF30F22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/5586E396-8963-6E42-AEEB-D608F3A12D5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/5844A546-345C-674D-B919-4AB18B3AC115.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/5EA400CB-9FB7-954B-AFAB-E1D048FADB29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/621A2450-6400-F746-829D-FF15B904CD8B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/656171E4-1B96-8642-8284-B297724C1A05.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/66DF47B7-5EA6-6745-ACCE-E4217A6D3FDB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/716B3E7E-75FB-A747-8FE4-34BED666E3CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/7F984062-06C2-444D-95E0-ABD2977CE295.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8B7CD24C-95DA-D943-8275-CDC929013E7F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8BF40A89-EFE6-F340-8BBB-3C59F16BFACD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8C1BF63D-4047-5E41-8CEE-91338F59930F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8D2679F6-4248-B047-9912-5673A156ABC2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/8EFE1685-98A1-7941-A2D2-714DFAD72848.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/9388B1F0-3583-1746-8D17-8F188915E203.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/98E11311-F0BB-7045-A045-46CE66859C52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/9DF577B5-8595-2F42-AE3A-E01CDAC1A2CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/A9B68AE8-5D72-1C44-A66E-E0DC3E66A82F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/AD2D43C2-C817-6146-B9B2-4F1E312FB780.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/B739CAEF-DAA2-0340-8241-5920D99C3B2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/BA936304-54E9-7442-A382-B0584CFBE25D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/BACA6234-6FC7-1D4E-BF1A-F730B36EE631.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/C07E3339-F2EA-2944-8BE1-F5C3EFC7C885.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/C8F39B0A-2A7A-D244-9A03-67E06BBE889F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/D5455C18-6CC7-8545-8503-C3C4480236B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/DF12A184-4538-E14D-A222-152441986FE4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/E6367EEA-CBCD-3747-BDE0-7F13FC50E8EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/EC78A5A5-01F3-7642-AD0D-845674537376.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F106C62E-8C22-FB40-A845-931AB493F735.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F15436EB-6CBC-3849-9D2B-B92F946CC64F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F9762F30-4D3D-F841-9C80-A30FE65AE7EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/F9B64D13-A8DE-2D4D-844A-CC934C27513D.root',
] )
