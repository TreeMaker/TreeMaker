import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/00BB2061-E66D-E511-9973-002590AC4FC8.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/00FE4562-E66D-E511-A8B0-047D7BD6DE24.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/02622360-E66D-E511-828B-001E67E6F990.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1C7BCD64-E66D-E511-BA39-001E673C7FB1.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1C803D63-E66D-E511-A1E1-38EAA7A0EEF8.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/1CB4B264-E66D-E511-8F37-001E6739AC71.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/20A63D66-E66D-E511-868C-9CB654AD73FC.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/24601E63-E66D-E511-AAE1-38EAA7A30576.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/248D4767-E66D-E511-9056-002590200B6C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/2A07CCFD-E66D-E511-8633-001E67E6F92C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/2AA38675-E66D-E511-B9F6-001E67E6F4A9.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/340E9461-E66D-E511-8F11-38EAA7A6DCE8.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/34EA568B-E66D-E511-9E09-001E67C8050C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/36D5FE64-E66D-E511-84C6-047D7BD6DE62.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/44414F72-E66D-E511-9FBB-F04DA23BBCCA.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/46CC57E1-E66D-E511-8F83-38EAA7A2FED6.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/48F8DA62-E66D-E511-BAC5-001E6739AFB9.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4A11FC8A-E66D-E511-B9E6-001E6739A781.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/5259FE60-E66D-E511-9B4B-001E673C84B9.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/54481973-E66D-E511-8008-002590A80DE0.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/56C7F46B-E66D-E511-8932-0025904B144E.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/66861E64-E66D-E511-A175-001E67397058.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/68DB8762-E66D-E511-9658-002590A82B8E.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6A422F61-E66D-E511-8F8F-9CB65404EEF0.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6CA5B264-E66D-E511-A6EE-002590A3711C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/7257FD61-E66D-E511-93BC-002590AC4FDC.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/80619363-E66D-E511-9496-9CB654AEAC82.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/809A2273-E66D-E511-9FA6-001E6739A751.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/86516163-E66D-E511-9195-001E6739B849.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/90FE6764-E66D-E511-868F-002590200840.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/942DAA67-E66D-E511-B3E6-002590DB923C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/9A93D561-E66D-E511-93C7-001E673D0679.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AA372F63-E66D-E511-9470-38EAA7A31AFA.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AE3C9A76-E66D-E511-9D11-001E67396D10.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/BA8C2166-E66D-E511-A495-9CB654AD7314.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/C2B92C67-E66D-E511-B4E5-002590DB052A.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CC4A4CA2-E66D-E511-A11E-001E6739811F.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CEEDEA63-E66D-E511-ADB9-9CB654AD7998.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D0630464-E66D-E511-804A-001E6739BB01.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D8FF2463-E66D-E511-820F-9CB654AD7358.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DC73F263-E66D-E511-A7A9-001E6739AC59.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DEFF5063-E66D-E511-A1D5-38EAA7A30576.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E205756C-E66D-E511-8837-001E6739B0D9.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E6F3778B-E66D-E511-A535-001E67396707.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EA563869-E66D-E511-B759-00259020081C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/ECFD7262-E66D-E511-A5ED-38EAA7A6DC7C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EE17EF74-E66D-E511-836F-001E6739CBC9.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F270C262-E66D-E511-8BAF-0025907FD2BA.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F6666264-E66D-E511-AF45-38EAA7A6D65C.root',
       '/store/mc/RunIISpring15MiniAODv2/WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/F8935867-E66D-E511-BB7A-001E67398633.root' ] );


secFiles.extend( [
               ] )

