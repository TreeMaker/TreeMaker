import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/00CE10D9-8152-4146-B299-0BD59335E0DD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/04467922-EEFA-9844-BACD-E53A42836EE9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/04BE4614-C0C3-8A45-963B-1324FD02E5B4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/08F2C87D-9A35-B247-89D2-BA4D53015943.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/0B27795D-8D40-4E4B-9B42-E91EE4ADBF61.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/0E050352-1982-254D-97C6-E966868249CE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/10F8BA47-B69A-3D45-A044-27C0B55B5DFD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/125ADB8E-F4A6-DF4E-ABEC-A7988CA823B4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/13C3B3EF-625E-004D-95F3-5D85012BA2DE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/144007A6-3220-5844-AB68-1E67FA59AB6F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/14EA0AA3-7FB2-714F-B45A-6A2CA1BB1BC3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/16FA456A-CD2D-1C4D-BBE0-A337A47DD701.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/17E8780E-5186-6B46-B621-967E27821860.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/196B7A9F-C044-8249-A57A-DF3D946DF93C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/1A214329-F1CB-2141-AA59-05259DFED728.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/1A818859-89CC-FB44-B4A7-3FA2A2BA7FEC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/1C7302DD-D057-5D4C-AD07-ED8762E83A5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/1EF4A76D-FE50-B441-B0BF-9D884FCC4151.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/1F0142F2-4F78-B747-B3F4-01D904E8F331.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/208BA0C0-AFCE-F44B-B8EC-459706AEA0FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/249A7928-C192-5C44-9E9C-7BECE95D8C57.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/24F9EC49-BB7F-0F47-BFDA-14A61F2EFA7F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/258D19A9-2A2E-484D-842C-1811C7DD0E41.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2887FE5B-54C6-B04C-BC9F-C24AA6BE5A27.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/293AAC02-4560-784C-85CA-41B176BF919B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2A172138-5099-014A-972F-E806FFAA94C3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2AC00E0E-270E-E849-89F0-196414024D7E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2B77F7E8-467D-E343-A4D2-16BE83940AA1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/2BB0F167-2404-8349-84D4-2B8913C256E5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/30BDC013-60B2-8E4B-9087-E8AB58701F2C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/3647F588-5788-2E49-A0D4-84B83BFABFE0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/38A8CD37-EA8F-1743-8453-83D8FCA50A92.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/3DFF8927-EBF6-B64A-B014-80C2B4A0BE02.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/3E380698-6320-B74D-A1E1-A12175CC7DB6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/3F9980EA-BCA4-4D44-8A66-18BBE6029B90.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/41BB3071-D664-AD4A-82EC-34C174E43AA4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/448006B0-1EB6-E74A-ADA2-4D3D90D460CE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/44AE1194-5C06-A64B-A0B4-14DE03CB6652.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/487BFB9F-4336-B94C-A948-136E6CAF23B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/4A44E29B-6A19-2D4D-8992-3E032FD9AC90.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/4C7F7996-C8AC-854D-92A5-5421313B3FF4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/510C406D-8233-5D48-A723-983AFA71024C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/51F4804D-C303-0542-8433-F598BD13EF7F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/525C0EB4-1DCA-F742-A838-84EB6B07EC53.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/52D57C4E-F336-5D4E-B379-39B6532B5B75.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/534AD0AF-7480-3148-AA9F-078EEA954BB0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/568B4787-148A-4C41-BAD7-935745B99D80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5A3F1148-0B72-C44D-969C-B3131B71A515.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5AAC1ADC-E539-A245-84BA-751484766F71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5B71ABB1-F9B6-5146-86BD-7569DE2D0E80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5BA8E26C-1624-3743-87AA-E02EA4915454.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5D13D7AC-D58E-ED40-87F7-750FFA5E4A48.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/5DE4157E-9040-C14F-8535-C4C416F44866.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/61E38ECF-B90C-8643-A301-3307E1E4E58D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/642A141B-9FA1-1549-A52C-3B05FAFC4666.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/670D918D-C202-F043-954C-5152FC4B75E6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/678BE064-E10B-9E42-8846-3D249404B3D4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/68A7E7DD-17C0-8E49-BF50-88FBC4E700D2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/6984D112-19E3-754B-A257-AC4ABD8A80B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/6FF3AF49-A051-2744-B64D-E528B5DC579D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/71F84D1E-4ED6-3249-A4C6-83A1DC2CFBC4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/72136F25-4415-CD4D-ACF6-BC3A4BEE7D54.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7412B632-43A1-2F4A-8858-FCD2169C927A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/751F53E3-9D19-8948-973C-366346D645C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7602C374-9F24-2A44-BD66-CEEA2B223C72.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/768856BA-7C9B-0149-A191-8DC5737A86CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/76ED032E-0619-D24D-AE76-59D4D94C8300.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7996EB50-EFB0-1749-ACC4-BF4D606995FB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/79F7265D-4ECF-764A-BA9F-297804260F23.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7E2B344B-BC65-5043-AB26-04900C647946.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7EA895E2-0BD4-D844-9A89-7D84FE3F579F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7F3B1F18-8CB4-2B48-A781-F41B654A5908.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/7F990264-D724-4C49-BE33-269FE8F8A955.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/81B0D328-FB9D-9F47-BB04-9E9B62EDAC44.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/839AD656-A75D-E14E-95A2-7B668EDC79DA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/84646B7A-1D09-834A-BAA2-615AF7E90C05.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/8522E5D5-8A7E-3C47-A75E-453A4D29439F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/8965CC51-3AEF-6A48-BCDE-95CEF45CFAE0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/901B39F1-DFB5-4145-A72F-BD434C4ADD81.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/908E5ECB-A09C-5A4B-BE86-9FDCAC9D38A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9098E247-1640-8A45-A7CE-4811B356AF5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/93D1580B-55BE-4D4A-B19D-9B51C34D4FD0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/95B0E22A-0FDE-244C-A6BD-EADA368E8121.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9665312A-04AD-9645-B80D-C8F13F75DAD5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/96D20C10-92CF-D443-A69B-414D39A27526.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/973FDDB8-E681-D64D-BD4A-385CD84103D3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/97F0E2A9-A874-6A4E-B930-F2424A2ADF0F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9AE0990D-FD56-D94D-BDD1-54EA436F358C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9C3E8976-3CEF-A344-AEF2-AC8AFA470339.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9D45E59D-8426-BD45-9448-DA4A99472BAD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/9F4A12F6-2905-AB4E-A35C-E3E20625115A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/A15B1683-394C-2248-8A5B-66EFFE66DFAE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/A2A6F905-CA04-684B-A5C5-BB969662C32D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/A5E2CE1B-3DC3-AE46-A3CA-B6437DADF75E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/AD0976F1-AE33-3040-A2E3-C71633896AF4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/ADCD66EF-F1B3-DF4F-8EFA-14AA86E27589.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/AE6EE9C4-9BAD-FA40-A1EE-3E5183459434.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B24CB433-73F1-CE4F-AE18-CC12BFAC3567.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B57AAEDB-5F0F-7B4F-A789-B86E684CD101.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B65CF91A-C906-0A40-AE3A-B45EF313A2F1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/B9E21B7C-FAE4-2441-BE8A-FE429C9CBD11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/BA32F670-1328-244E-BD66-66DA32F0EFF1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/BCEA43F0-B33D-E744-A040-43359C3D8B06.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/BE47B237-31B0-0440-8606-02321091A1E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C144E1BD-B2ED-814E-AE58-582268C7B40D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C4A2CA37-EC3E-1E47-B824-6D5CB3AB2BAA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C5915528-34AA-BE4E-9142-20853AD81029.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C718A698-8730-DC47-9775-1245518B8C5E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C7FCBBE2-BD59-474C-BA24-81F0D2313CBB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C8611E9E-FFA4-CE41-A555-822DD303A51E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/C936B063-B4EA-8D44-8228-1C46239D0631.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/CBFACAF2-234C-CF4E-A6B4-D54919848C34.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/CC108505-C767-8940-8012-373CC3339AD6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/CFCFD600-29EC-B743-B980-2D0FDAE49916.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/D00AF1DC-04A2-AC4A-9BC5-2AD1E9C9532C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/D0C0F5F3-D20F-0244-A51B-D5B387D9897D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/D6BD1CB5-1378-B247-B5FB-3F9448D5DD02.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/D6D1D61A-DB7F-D440-9C97-F279D63993FF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/DB32263D-FBA1-BB46-93E9-9AAE3F229F6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/DCED17EC-7648-A74C-A09B-9D99DE56A6D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/E8289C2B-A5E9-EC4B-83C6-AD9298B7AF5B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/E893FF5B-B887-0448-A9BD-90C658318EFB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/EB831163-AE9C-2D41-96EA-6220C6A6AD6E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/EBDDCBFD-C0F9-4D4C-8563-42672791F7EA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F01C3D8D-CC92-EC46-A173-5BF824DE63A8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F0842287-6509-B54A-AA6D-75BD41947E57.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F0CDBBF9-7962-0044-BDE2-397E8ECC717E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F0E80023-BEAA-CA4D-8787-9BEA93032369.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F11928B8-85AA-B442-85A4-F53B34C39E6A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F1FF2C11-9E45-FB46-940C-079B03F78FB0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F245B344-68C0-344F-89D4-8761F07F3FEA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F353A007-CCB6-D34C-A0C4-CDB407596119.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F3F85390-728F-364F-BD9D-DDF491D48E5C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F63BA007-A28A-8446-8364-B0553B2D45DC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/F889F774-36A5-564C-9466-885A6648C9AA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/FBF539C9-C64A-0E46-BA6F-0D3F0313DDD5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/140000/FE571F3D-C591-BF4B-B67A-09F5D37B51C4.root',
] )
