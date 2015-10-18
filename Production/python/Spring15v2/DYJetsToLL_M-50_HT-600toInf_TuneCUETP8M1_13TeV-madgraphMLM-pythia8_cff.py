import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/14BDA3BB-CA6D-E511-BF7C-0025905C3D6A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/162A4EC0-CA6D-E511-A084-002590E3A2D6.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1A11D0C1-CA6D-E511-9DBB-003048344C1A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/24E498BC-CA6D-E511-86CD-0CC47A13CD9C.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/26E058C7-CA6D-E511-B86B-0025900B5648.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4CA53B44-CB6D-E511-AAB8-0CC47A13CECE.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/52B2C6D3-CA6D-E511-9AC7-002590E39D90.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/62AC50B8-CA6D-E511-BEF6-002590E3A0D4.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7A297EBE-CA6D-E511-B8A9-0CC47A13CEF4.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7AC4F9BB-CA6D-E511-AB33-002590E2F65E.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7E3B39C0-CA6D-E511-804D-003048F59728.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/86026CBE-CA6D-E511-AF4F-002590E3A0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8E74D5BC-CA6D-E511-9BDB-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BE80F7BD-CA6D-E511-AD97-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FE23C4B8-CA6D-E511-BE42-0CC47A13CB62.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/9A45BA05-CA6D-E511-9E33-002481DE4A28.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/0828962E-CA6D-E511-A3EE-001E6739825A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/56310B21-CA6D-E511-A0FC-00266CF82C98.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/56A62FE5-CB6D-E511-B09F-0025905A613C.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/64C80E2D-CA6D-E511-B921-002590CB0B5A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/74A0D9C3-CB6D-E511-AA82-00259059642A.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/905D00E7-CB6D-E511-9286-0025905938A8.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/AA81A4CD-CB6D-E511-A83C-003048FFD760.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/B084B797-216E-E511-9F6A-44A842CFC9A5.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/BAF673DD-CB6D-E511-87A0-0025905A6126.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C46158E8-CB6D-E511-85FD-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C81201B8-CB6D-E511-A81C-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/EC8C7FD8-CA6D-E511-A09D-20CF3027A5A3.root' ] );


secFiles.extend( [
               ] )

