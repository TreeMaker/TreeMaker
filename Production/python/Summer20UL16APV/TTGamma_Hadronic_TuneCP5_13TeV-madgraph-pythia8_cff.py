import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/210FB322-F997-3948-95A4-B2E78B8A7A32.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/361FDC75-3363-744A-8491-3A1BD43CBF3A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/6410C117-6D17-5E43-BDFF-25C075D015F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/9E5DC949-C516-CE4E-AE81-FA1C2BFCBACF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/B9001519-0E22-1248-A0D1-9D59D7197D8A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/CFE9C12E-57F7-4B40-A7E5-6EBB0E8BA0C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/EBB6157F-CDE4-7F45-8A80-81B874EF7897.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/EFC341C1-3C30-EF4E-BE9B-C9CC39A098E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/F0DD99AE-BBE2-2D4E-8498-A3AC35F8E21D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/453471DE-2C69-3B4D-8E57-AA8A71707947.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/4C70F948-D2B1-0D43-BBEE-73FDF36673BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7E743B7A-FEFB-F743-9CED-EE7309AC3580.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C045A1A1-40DE-4E4E-B312-7D363B839CAD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E3020838-EB80-AC4D-8CEB-DC2B005A8A43.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/10B13595-45FC-FA41-8B70-EAAA73746EB7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/284E4B24-990A-A34C-A0AD-ECBCDB62607F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3085B858-0F8A-5647-AC14-1B80AC276C8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3971618A-80E0-3844-8F13-C6D234EF9770.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/49E9ECA5-7B0E-A243-873E-F4FAADD523C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/526F12C2-42CB-8446-89D4-01769D92A060.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8C266251-6F23-A440-B3D8-DB5C0493B299.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/906DD209-8CE4-4642-9DBC-88C99BD607E6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9078A289-D14A-9342-9171-B18A528B99C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/91FBF6C8-EDDA-D84C-883D-11F5C8D54276.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9DD1F52C-353A-6842-AC4C-1D6C3EA8ACB5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B3ED1FBB-082E-4144-8E57-2BF8BF483098.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B7D96D48-4106-E44F-AF75-F0995B18CE8F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DB713BDE-FA8D-7E4D-8425-2C9F8FDDC592.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F6770BD8-D6BA-D141-A55F-10BBE8253804.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/172A0335-72A1-E84A-B8F2-4242DA280C41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/46CF7CC8-4D4D-F94C-8AB1-7FDA9F6DB8E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/537658E9-A089-CB47-A419-24B03F1B2235.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/59E30174-828F-B040-98AF-E3D0E964C007.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/00907146-5B5E-8C45-9B01-05413624267D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/056024B2-DDB9-4F43-A3AE-426E1601EBDB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/08538CF7-19A0-1847-9F37-A9B10FA3F997.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0A3EFA1E-C96C-274A-9941-6BDADA4D1423.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0DEDAF65-DF44-B24B-B485-A10D427C8399.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0F45AE9D-5372-FF4B-A5B0-F62327998DDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0F63A73E-F0E3-D545-A1E5-C65033E08D68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/10B30098-B8A2-1B48-903A-DA82E9EABA0A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1695AD7E-4FA2-3547-8C77-F245D0E220CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1A53895E-428E-334F-AE82-EA0031EE8835.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/2EF2A2B9-3CC9-FA44-80E9-D5098E3094CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/343950B1-0125-924A-B2D2-237AF2D47BF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/34944C01-AB84-2342-B780-D0810E63AAC8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/498A1748-7C65-3645-B42F-EC2BA8FF935D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/4D14438A-EF84-D04C-8B78-49E3FBD299C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/4F062E04-008C-B44B-BFD4-B7804AE71597.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/559CBC8C-7902-B649-BFD9-3592F740C2B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/58BD60AB-7A63-0B45-972F-E2FB0E4794F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/59FC62A3-2488-E84C-ABDB-5F38C53B3CBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5ECE7D88-A45D-A841-BA07-10667E0B431F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/61AC5251-87E0-824D-B549-7BCF63BC3606.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/67657111-12D3-E94D-9240-004359057659.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6CF3DEC4-C15F-8D42-9466-7A4DFBD36E5D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6D14812F-C6D1-8A47-950C-CCAEF2DBF60D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6F6B20B4-4D07-5B4E-A377-29687557B47F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/70ABC272-0C70-5743-ABE1-BA973860085D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/74492B48-D5EE-D345-B0D6-30C84018BC35.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/83E5CA46-5330-F348-8D27-2EF52907E7ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8D7026F2-DB17-9249-B73F-A21F4E9487A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/8FE4F04A-F353-6F43-9EF7-32F4587C4063.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/93223762-006C-C847-ACDB-0EC267E56583.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/968B0F9A-7B6C-1449-8C73-8C0056FEE1B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/99056A26-3E74-0344-9F7C-A11AB3C19C21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9C0FFCBA-5753-1642-A34F-B65BD4B344B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9F71E666-1915-C04D-9BC5-9164D1A713BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A90E59AA-C338-1949-8D71-EC38E58A5FC6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AC428E91-90A8-884A-84A3-8F8DAF43AB2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B72B55B9-A142-5B4A-A5AA-3EB6EBD7CCBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D0FFEAAA-69AC-FD49-88DF-49774086FC50.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E10D7C73-BD0A-0044-B135-66CECAC4DE29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EE4BAD5B-C968-9A4C-AE1F-44E438CFD023.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F3E83E3D-A12A-504F-BD70-1DE4F2A23383.root',
] )