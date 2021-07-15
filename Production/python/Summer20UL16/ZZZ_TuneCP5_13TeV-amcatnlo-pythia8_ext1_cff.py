import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/018DE679-0138-664C-97FB-B123B39920D5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/019E236A-B65B-4C4B-BA8F-A78F6BB5EDA9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/01D29BE1-2ACF-1D46-893B-15E984FEB560.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/062F8E32-E77F-984F-B030-C9A94B00B13C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/066A13C9-CF48-E743-AC4A-49C2B1E4D663.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/073D7786-EE06-0A48-8086-70A40CFA60BA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/07FF5FB2-123A-0443-A13F-CAE8DFFCCC4D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0841F583-9765-1A4A-B124-68DFF0BF379B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0B1FE3B3-5396-C245-9FCA-69A1191CDB05.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0B6D0377-D7D1-EA42-B067-E410BD3CF2FE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0C5E8F3E-78DD-B34E-B8F9-2B7F2E6FC42C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0D9BE9FD-ED5B-E04E-9EBE-023E3DE3AA78.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0DD366C7-91EA-BB45-82CB-C9F05E2BA87A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0EAA16DF-2E75-F34B-9CB8-A1ADEAC2A01B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0FEF3BA3-9D26-214D-8CB2-94D8F6E25184.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/0FF68AF0-22B7-E445-944A-C32D84EC9850.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/18260C5F-ACC8-EC40-95A8-7E2B4FB8EB7D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/185C7335-3DF6-F44D-802D-EA8308074CE3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/19F1191A-4CE9-6B4F-B3A4-6740C9657E50.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/1A037873-DF7C-AC4E-B131-7F034EF54AF0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/1A65510B-9C09-7146-848D-FC050757FC41.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/1E1B417E-4815-3C40-8463-C8F7BCA9BF0C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/1E85DC26-ACAD-694E-B9A0-7029CE4FC1F1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/20B25BBE-A63A-7C4A-AFAA-516D70E3495C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/21DD53B1-56C8-2B43-AD1B-15AE689414CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/248E37F2-47B5-C444-8BA2-59C80E8E8FDA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/25403B47-865E-6740-B375-3520FCF87D1B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/2652E3B6-47B0-8842-B48A-F2032CFB9FB5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/2B0F9DFB-AD85-2E4A-A2C2-1F65B310FA0D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/2B95C28C-DF22-6D4D-9CB3-C09A3D93C806.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/2C5499CE-F8AF-C94F-BF14-232F97AEC217.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/308E6B1C-23D0-5248-AC1C-CEB5045D7C60.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/32CBDAFB-A472-4D43-BC23-284866CC80F7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/33BDA2DE-7B36-BB48-9140-ED6769A0D67A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/36E5467A-1B75-B844-A608-974E0994F401.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/37DBB913-3A5A-4740-8565-A950ED664075.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/382E46F1-21A6-014D-8246-E5374E8913F3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/3842E6BA-F35C-824D-A24D-AF6939158CB2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/387CC9A4-CD39-4B47-B1CB-E40E963E6E52.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/3AA98263-45C7-0A44-9985-7AC54B466833.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/41B1E809-5B2B-1A44-98D4-551DEB23DDA1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/460CD7B7-2BDE-804F-8C44-B2EE3D56514D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/4B5DD4F1-9254-2645-A7A7-9C72F8BFE475.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/4BE71372-5798-204E-85F7-2A1A5CF0E327.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/4BED5F74-CA66-FE41-8443-70BCBA45FCF9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/4DCE6414-2657-BB40-92BB-2929EBB516C8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5035D9F3-0BEA-8941-9D2A-008584B8B274.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/50C4C8E7-1ECD-8848-B50B-46597D17FD59.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5176F6EA-2C68-CD48-B4F5-F664BB2B4582.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/528364C1-C088-3C42-9E41-65E53C296015.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/53B12EC4-E090-114E-816C-99FB38312DC7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/560529E8-DFDF-E74A-84ED-F511840B6B2A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/57CB7059-BB57-1049-9060-1E273FADA8F0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5806406E-5FF8-8B44-A8FF-EABEA9388590.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5A94B4F6-BD1D-2D4A-A3FB-DCDBD38363C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5B7FF1EA-AC07-9D47-A00C-C9D8C98FA146.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5BAC14EF-288D-774A-9972-9298297F2177.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/5F7BFF89-D752-E644-A7D1-D381743EF79D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/638AE4DF-BD83-EE4B-ABF3-72E5E61DF78F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/64889842-9866-8749-81EB-7D9F8E64DBB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/64E2294C-F28D-B84C-9AB3-31A693072F36.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/65EBE402-0E7C-E641-919D-85491C74E0B3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6681A1E2-5F4B-6848-8669-237DF669E84A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6760C765-9072-8A42-A2AB-A858B4F78B71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/67EC3440-4F41-5B46-946B-68D349CC72C9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6B0229DE-2E49-A940-9789-FC0638ECB131.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6B5D5684-93AB-9540-B3C9-153203CA5574.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6CA4E919-1DD5-BD45-AEF3-F528625DB2F2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/6CC66B7C-72E3-2C49-8FCF-872AEC59C9B5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/727427A3-DC96-9C4A-98B3-DB37148A27FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/72823535-5269-054E-B339-0E64EFD8464A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/746754C1-7BAC-BE41-8A8C-1C6C2BE1F3F6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/7515A0A1-765C-8440-B156-BD95BD4A490E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/765A3918-E0FE-F240-B94A-ECDD794228EA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/773DABAA-24EF-FC4D-85F9-06693AA92DC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/7AA8631A-CB37-EC45-9AA7-1F41C3364F7F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/7DCBDBCE-B9A8-4A4D-9840-C200DF6DBBF4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/7E843D57-C9C4-A748-B641-441D789A5EA5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/7ECBF457-EEAD-A444-8D42-7E9E80E90EAE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/804E85FD-039D-184F-9D4B-80650805D9C4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/81083E99-EA99-0440-B0A3-6F0AB1A1C280.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/824EB3FF-44EB-8B4D-B2B3-7B2A1A475A09.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/899B74CD-8F74-2C4C-A478-847D1F2AC60A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/89FAE52E-6242-1743-823C-E6995EB502C8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/8B9E2090-B9E2-6541-BAAA-1E8D2CE82C67.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/8BC99576-A718-1445-878C-A088A0EE3376.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/8E2B38D9-3471-674A-8681-DB730E4B2CD2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/91745E9E-213A-5B4A-8247-DD9D17683395.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/97FF3346-BE36-6144-B10D-8F5607DF6D38.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/9BB4E97F-2084-3143-9592-E74DEC2EFBF0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A0904B63-F7BC-564A-88B0-2BBDAA26256C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A095ACC3-C32C-7D47-B4B7-691E3A1E8479.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A180F518-EEB3-964E-8586-2EEE7C1B2A87.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A32E9E69-63C2-8F42-B678-489B3E3956A3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A4CE5B94-5530-824F-BFB4-6F2A6264FED5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A66B89AE-3CD4-4047-872F-0B2EF3182F44.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/A98C777C-A0D5-4448-B6B5-6EB1FC378EB2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/AC2493C9-527F-234A-98E5-A3AC2BBFEFEF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/AD15A82F-C963-C347-B626-75115CFFB1BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/AD1690BC-6DAA-B841-B2FC-BFB13B78398E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/AEE8AD74-E444-5646-B02B-1812AC2E64D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/AF0A3992-8C77-4D41-9811-93A4E7DCEDE2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/B288F4CA-FEBC-2B4A-983E-217E50EA61BD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/B29306D4-EF0B-5C43-9D13-4D06531FD972.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/B5AD1A0C-DD63-494C-AAEE-1706E27588D3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/B7DA835D-5960-F842-B0A8-97B8F75D6821.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/B8F6F9F8-B919-0243-A4BD-B0D87656DE8E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/BC07616E-2216-3549-9CAD-38270E5F3887.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C1CCB116-2B5D-1F4C-99D4-BC366E2ECE64.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C394422F-46A0-3E4A-BC37-518F983FA1DB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C4894597-87FA-D441-AFD7-A0F67D1A1ADE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C50C187D-C28D-5B4B-BDAC-2F543D5218FF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C8C34B25-7534-2F40-919B-4CC2C8FDB67C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C908C420-D7AF-2A49-9697-9D971A5AC916.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C91D9EFA-7CA7-B34B-AE66-EA76DBB142E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C92AC1B1-B692-9C4C-83A4-A067E08AF7E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/C9660473-D5B8-EA4C-9235-262957EE9743.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CAF1C614-E46C-A849-8603-99FE1C4E38DE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CBBA00FC-3CAF-9946-AA8F-24ECE0E6D478.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CCAAE283-D929-0F4F-9CD3-C9CA6DA9DDBC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CD09AFBE-AB4B-B344-8C56-738E9B40557F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CFE93BF8-2602-1546-94A4-8466FC0818B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/CFF422A7-746D-4940-80A2-B6F5EC2AC1DB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/D2D3D41E-1896-0640-8CA8-5AE2B605C056.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/D2F72A89-E32C-B444-98B6-4F59020CECA9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/D3AB574C-F04B-6145-A894-2AD82AB1FFDD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/D8406E64-692A-B149-B6DF-D1195EE7ED02.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/DA1098CA-CA09-2547-B786-1F9E50F5DBA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/DA16C0E3-06B4-334F-8FF5-00E9BE571AF5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/DB72A164-0615-4A46-BD37-066AE5B51326.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/DD765443-667B-7F41-8B85-0DF22C243CA6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/DD9A466F-8FC7-574E-A352-49966850B7A9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/E6945D03-F91F-9145-9C72-008795EDB93C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/E7F4966D-CA40-F943-B9D0-FFA74F52871B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/E9D26DF6-59DC-1749-8FC1-1DE4188E2DCE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/ECA2F10A-1DA3-5542-90F8-0608D7BEC0DF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/EE959D51-8E60-FB40-AA3D-5EC027DF7A3C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/EF9168CA-D6A6-DF49-ABE1-94A1FF375942.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/EF9AAD1A-1BE6-084E-B875-56B9E6B9CFBD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/F06AD635-19D4-BA43-9062-AAEACF99FBA2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/F8A774C6-4B17-324E-AF39-04966FA2ABD7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/F95AF513-4E4A-0043-A43D-D909AE11DADF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/FC312DC4-6E56-CD4A-9E74-697DE7DB4CCA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13_ext1-v2/120000/FDA60165-D70F-F14A-A926-5C5ACEE60C16.root',
] )
