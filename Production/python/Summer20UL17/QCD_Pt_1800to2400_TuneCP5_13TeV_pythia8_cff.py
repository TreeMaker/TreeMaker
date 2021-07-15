import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0108840E-FAA7-A54E-AEB8-6A3F4F325147.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/014A2D34-7377-E74E-A6DE-D4ACE60DED1A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/02D592A1-4B87-334C-B30C-93E354CBEE40.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/02F13F58-1C86-5243-91A3-AE39BBB4CE4C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/03D002F3-0BAB-6C48-89F6-900E03D48E89.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/051FD344-2547-F141-A399-64DE80A4D922.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0728AF94-7EBA-3941-B2FC-3AB1190EE8CE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0A40755F-26FA-C842-9650-1588B3818C3D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0A954155-1808-C043-BD47-121DC668B045.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0CBDA038-C524-4A4A-B216-033BDB1471FB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/0DD1E24D-9129-3A4C-AC57-33F1257E5D8F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/1147D127-AFED-0B4D-B3D6-2C6FECBC8520.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/1253D01C-C016-2848-9993-4C36EA62DD12.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/1A00F97D-B61A-4A47-A7B0-FBDED3CD65A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/1BE293EB-4C33-A443-8818-BA912B55AAE9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/1D0A4FEC-6B2A-3F46-9131-B2A059B7BA59.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/21E00A90-E515-0449-85F7-2F33ABC7C785.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/23686EDF-831D-524E-BBCA-0A362C17D6FD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/2A057468-C35C-D549-8DDF-81BBC29B3303.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/2A3A8144-FDA9-D244-BF0E-0AF87967E47A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/2D6D0DF3-CDA2-D149-A279-A13274DC9EB1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/2F44E3D9-0FCA-8E4A-9A84-F6AFF5C10506.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/2F9C3D1F-79AA-CF45-8D01-2F6C5D09261B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3147A375-1D86-1F4E-BE9E-18DDD20767A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3443FD62-F40E-754A-9C18-45BE1065DFFB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/34456CC0-C0AC-844D-8E4B-481DB85F1FCC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/346C3FC7-12AB-5D4A-A3BF-0B0166E86507.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/35D88DEB-8A60-764D-A18C-1AC355CDBA2F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3A023373-D749-FC49-87C1-36C8964EB51A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3A1D861D-53C7-A34E-B0C7-D0D25B32E032.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3B0C633E-39D7-494B-BCD5-4A15C39D512E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3C969B40-C2C7-D946-B0F4-A60AF29F54EF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/3DED9D40-D14D-A644-9609-820860ABA313.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/418BB252-18A2-4F44-A08D-7B626A4AA4B8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/42E3BB53-C43C-B247-B419-16DD29B500D8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/43321E1A-F2EA-AD42-A41B-4E37D446330A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/445CEE55-0482-E14C-BE72-C47E15B68DE4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/4484D0E8-C1CA-FD45-BED4-EBBAD538A1A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/45DC8CBD-6F34-FA48-BE2D-285DDB632DE4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/468B7D8B-2827-E244-8CFA-4E6E24AF593C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/4746E0D5-04D8-BF4F-99D9-8A69556DC9AB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/484B9038-7404-0946-99F9-2F7085434355.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/48A13435-E84D-8C44-AE80-03EF6614C6BF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/499D2EDA-021B-6840-86D0-A212AB003C88.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/49A2B481-D485-E549-B6DF-0AB20FB886AE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/49A4D6E9-71D5-5740-ADAA-C4947A6EF68C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/4AE4E62B-466A-954D-8942-89242FFB31B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/4FB9E54F-1305-2F4C-BB72-9845A783ADFF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/501BC7A0-C5FF-BD43-A2B3-7DA3EABD65A8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/516A45D0-BE4D-6849-96B0-9E39F95795AC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/51C621BB-9CC1-4941-8815-9707D081DE13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/53AEBEB4-B7BB-8A4A-A154-12675DA4AAEC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/55A7EBEA-031D-894B-BC12-14009936BEAE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/5644991D-A74C-3E41-A7E2-07AE621DC668.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/56DC9247-D7F9-CC46-B272-9240937ED040.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/5802937A-7678-D04D-BCD4-494E2CE04C59.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/58A79124-01A1-FD42-AC59-B6D4D0AACF02.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/58CB3F58-9A08-DE44-B72F-8690231BC55F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/6110989E-F259-B34D-A20B-A8A289AB135B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/61C82D10-2F18-4F44-A258-52B121F9EAC9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/625B7689-4315-C54E-8429-A20DD10161A3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/63D198BE-8575-B748-A5E0-76D3DFEF76C5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/63D9D72C-9846-2A49-B7BC-C11D9ABE7301.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/6593819F-D12D-084A-9703-8B41CBC9255B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/65C77263-B070-2C4D-81CE-50C2787C7B22.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/6887C5A4-7972-1642-814D-A1D7C21B93CA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/6A161F50-3401-2D4C-84CE-A8FE4F8648BB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/6D69924D-0854-4540-8FE4-D16A7D0B1111.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7110125F-8075-DE47-9A6D-28A05C0EE41C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/71469454-0DA2-C840-9B30-AEEA78E2F1DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/71B1232F-D8EB-A640-8821-FDB3967FBAE6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/758F61CD-CAAD-1143-AE4D-593F304F86CE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/75994543-0F50-0642-AC2D-650D7C6677A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/76F6E69C-3EA1-8A40-9FB9-D253DE252ED8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7788066B-2C18-B942-95E4-A06BDA14CA98.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/77FCF2DD-9731-BC45-8561-4C836A904183.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/799B0A47-7F83-1B46-9914-41A226A74928.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/79BAEA8C-D1F6-E642-B7F3-53C098769AF9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/79FFF872-FA66-4A41-8CB6-6CF6EFC3A274.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7BB8B9AF-4789-BA4B-8CF6-02C1FA248782.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7C8E9866-3368-054E-B2E2-51A6A44C0455.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7F35A3DF-ECB0-6B40-9DC8-85D35C771911.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/7FE055BC-1B7A-D442-B989-33746CB0F837.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/81284A4C-FA85-2047-9673-6AF4AA47AA36.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/83FC626E-B7E3-AD49-A764-35EB3FE6CEB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/858BD1DA-64E6-2443-8886-7EE1978852BA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/85E4EB82-9DA9-8E41-A36B-0FB9BEBBDB0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/86830E7B-744D-C541-A48E-F286B31E94CD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/87FCA5FE-74FF-4843-A9D0-061243F8CADD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/8A60B072-6B58-794B-B88C-548C0B4B2599.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/8F32A438-C184-F244-ABDB-0BB703AAB00B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/90331DB4-95C5-AA4D-B909-D9B3DA3E2257.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/92A31A40-D064-134B-AA85-53870F1F85C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9335A2BE-0C3D-D844-B672-E8CA4A66CD7B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/95895534-38FF-7A4D-AA04-D3CACBCDB422.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/95D585B5-D681-5C4D-9D8E-2FEA0AE10557.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/986DBFF1-73A1-8B4D-89C4-01757F2EFE13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9B74C576-3EEA-A440-8A3A-FD935C9B6E71.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9C0F104E-2D6D-1C46-AF1F-24C0B48FDCFA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9CA5222C-0E3C-A748-8CFA-0D4F64A5FF44.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9D29EFA3-9F2D-0342-94DA-81A392A25431.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9EB3903E-8CCA-1743-8CB5-DDF5C6538607.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9EB6C776-5F2F-F548-AC2C-BC6EF5FC3BD2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/9EC9F182-E428-4048-8E61-2654A6D68191.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A344BC97-79FD-E446-AFC7-787FBDB6EB33.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A49E10C3-C532-A74E-99C3-594E2B825842.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A589C5D1-8C5C-284F-B6CA-B07574D456B3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A692F3BF-7373-E54B-9CC8-5E12B79A2FB1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A694AAEC-1736-274A-BA52-7C30CDEFF47F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A924C9C3-1C8A-3B44-B0B7-CE1F59571A73.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/A9E4F39A-614E-144C-9AD6-927A9AFB380D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/AAE36BEF-DBE5-D343-A20D-D01484255844.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/ABBF605B-DBF0-0940-8B3F-0B969D769A0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/AC0A8E66-A28A-084C-B0FC-6A7C49A98C48.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/AFBDB67C-4311-3F44-987C-8154E9A36F68.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B2C13C72-0706-274C-A1F0-2E2558542831.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B3114C1F-B650-AE4F-B259-DB924FFFC31C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B3CC4C64-4A1E-0A47-B7A4-B2C964F55CB0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B4A6E2F3-E06C-8F48-AABC-B66357E5EBCE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B834E2C9-83D7-C741-9B94-5E9A8D118D93.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/B8427390-05A9-9344-AC56-74848B3A537E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C00F0852-5280-3147-A2CE-24974D606F77.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C205AD31-6034-684A-B3BD-085EBC411082.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C3801F10-946D-BF42-AA42-ECE8CAB0F41A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C3FE129C-9BC9-EA43-B959-0015C95A0657.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C62547C1-AF8C-384C-B429-4DC2A14E85F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/C9EF8FF7-99F3-284B-AC88-F1A964AEA375.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/CA190E2C-CC99-644C-BCB8-6FF6D4B832D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/CA5B3FC5-4A9F-C84D-96A2-BBE63D7CF952.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/CC5439AB-ED70-7445-9575-8CF543772358.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D13AA31B-1CB0-924F-B16F-3790C5B3EA16.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D1F37F84-5526-514F-9909-93D2C72F3D55.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D31B356C-ED02-1A48-BE29-47EC94A3BEFB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D476F8C3-9598-F342-8020-558FA8A82841.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D4B014E6-051D-9048-BCC7-C65359409F53.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/D56C93E4-7F73-EF43-883E-A970010E9BA5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/DA32D0C3-5E5A-F341-A599-1160E840EE2F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/DD02DBDE-7A03-2A42-9F22-D27949F6ADEB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/DD44D297-8A62-6A40-B7C2-D9223C54F9C7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/DDBA1DDE-4CC6-C042-AF68-1B62364B0FF6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/E5E8CCEF-A36D-5D49-A807-CDA52EC15D86.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/E85CE673-1073-AC4C-9DA6-A0E98FFE9EF7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/E9B1A44B-A23C-FB4B-8333-D6581E383DC1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/EB6C3EE6-4057-3447-8A33-0E7E274046E0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/EB86BDBB-F13F-C549-8A79-6B04AD9FCF3F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/ED526094-A2F4-B448-8897-11C0DF6E00AA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/EE01D5F6-725D-DF4F-B744-7F6BAA39A1D4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/EEED4F59-AF36-2F41-98E3-5E425362435F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/EFE6E648-8C6E-4E47-9F7A-0173BBF256F2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/F474E7FF-0E58-C449-BD38-3BAEC329644A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/F59194D0-2699-DD45-888F-8EC969BF4F69.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/F5A9B5E9-CCEB-A94D-AF73-5423C62613A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/F7DA87F9-5A94-174C-A803-F188F66FFAAA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/F8A48FF2-C516-3648-AF69-A39751D7FE77.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/FB8B83F3-483D-B34D-8304-5F28EDBCB4EA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/FD630650-12F1-5440-9245-209E34C48CEE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/00000/FFB83A4F-9264-9842-B30A-80CDF29DD536.root',
] )
