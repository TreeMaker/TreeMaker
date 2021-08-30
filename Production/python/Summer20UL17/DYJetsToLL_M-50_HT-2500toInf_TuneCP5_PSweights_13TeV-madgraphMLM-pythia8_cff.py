import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/204F5C68-BD8C-494C-8CD6-D7FABA4E42ED.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/24C197A0-5D6F-534D-80F0-265AF48CC5DA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/2CCC171E-ABE0-5D49-86E1-BEEE2E78FEF3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/2DA8A362-F14D-8441-BDDF-544549FC0118.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/34350DAF-E9E1-EF41-A2F7-F69E7BC48C7F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/4798AD31-6520-404A-9C6F-F5EEC6AB897D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/48BA0D27-7C93-824D-BC24-9BB37D39A5A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/4D9073B0-25E3-0F4E-85DE-3CABF19D0097.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/4FBA95CA-E70D-034C-B0E4-07E1643EE688.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/50E68E43-68E1-D54D-AA58-EA40DC5560AB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/53E9BD57-14D0-7246-B893-4C835087BB50.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/5C83FC75-0454-B14A-987D-294F99C1173B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/5EBE0C29-9906-8143-BE49-DFFBD92FBA1A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/64E6DBE2-F2FD-7F4F-82B3-3219622F0F5D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/683C5CFA-1074-8345-9F4C-399305D73A1F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/68ACF153-6CDE-784D-B0F7-3D311E6BE641.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/7036F856-EA7C-514A-9861-2C68754D0E59.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/8019CDFB-5BFB-B249-B990-8FE8AEF0B45E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/8174351F-6271-7F46-A865-95D0562FB8CD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/9161DCA4-93D6-A044-BA82-5814B7E2B0C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/9A15203B-1510-BB41-9345-4A47B6948755.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/9CECDCDC-0E2F-B24F-A811-77B304B9880D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/A3619748-AED4-5F44-BCB7-5147AA8519BB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/BF234E01-5369-6449-8ACA-DE58F0964666.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/C1AE85D5-0818-194C-8F5A-83B162306BAB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/C288F51F-C03F-6D4D-9E2E-EC6A15500E04.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/C9D8DC80-244C-5242-9540-10A38CC965A7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/D019CDF7-BD42-CD46-B8D8-B71021D7BE62.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F0C7DA4C-2931-0547-945E-BD3EA5351A39.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F947E9FF-261E-1347-8C67-306483BB5D2D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/00000/F97A0D24-BB73-F54D-A862-D1A316998FCC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/00C36F94-1EF6-2A40-807A-2149EE904AC9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/07C33E29-A3A3-8C40-9F68-0E4DDEFD190B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/07F198C1-25D6-2343-9BCD-190376B5C3C7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/1009AB47-8669-3E46-8426-64A47BE8AA0A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/122FA2CE-6034-1F4A-B9B8-B98D6AD25595.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/19B9F08B-DBF3-0946-95CE-C7F43AEAB9C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/2C43080B-C020-3943-BB45-733D598840E2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/37C26214-7816-FC4D-A996-D2EEAEE54C2C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/3B118726-6E7C-1C40-AFC1-FC4CC64FDE34.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/443FF02A-0CB6-8D42-9A12-E5C8C93396A2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/58421DD6-84D3-7441-A0E3-9624D20B440A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/5BB996EA-3DD1-304D-9D8A-9D0B4BE0E8AC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/611B0B16-4812-6647-A6C7-10478DE8974D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/6406F58C-5EDA-1848-AAD9-A1FD9E82FA04.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/75442BC1-0532-B046-9B6E-7B1CB6C488BA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/81315574-C26F-3D4E-9DB9-B2F0DC306A59.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/874EFB1D-2819-E440-B657-4C0A384B7900.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/8FF87E79-8ED4-9F48-A243-D931FE26FCF1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A72CFEFB-186B-0E4B-B879-1AB403DA5BE3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/A9FA867E-9682-F540-9A61-4941CFC9DA91.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/AD92CBC6-2BFC-A84A-B4FD-5D646EB9248D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C6A4A21B-7C41-9947-8D98-8D5F560F1418.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/C9BC673F-411B-D943-857E-8C788D05B754.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D3FED771-9E50-EE41-BAA6-74585C1951C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/D6637C93-EA9E-3B4B-BD61-6BC457F46701.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DAFE2E9C-2A2D-CF4A-951F-8EFA8A0C0C5D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/DEFA8FD1-1FAC-AD41-93B4-5F80EAB86E35.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/E043BBA9-60D2-AC49-87E1-2539A7FDE404.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/E9E49D13-50F7-834D-AC7F-155481D81CDB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F2CEBB4F-6437-DD4D-A941-77D16934EB49.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F7346F43-E8D5-EF46-97A2-76C993786825.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/240000/F8891271-03E1-A042-84F5-A5DFDCD1F095.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/24918F86-4FDF-3641-840C-11EE0D694F05.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/2607B62D-ABC4-1946-B3C2-1389D24AB22B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/33A134FB-CEEE-E64E-A488-50E05F4A5C21.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/3AA7538B-9C25-9848-B492-35619777DC86.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/3F714FFB-711F-ED40-ABF3-15D1BEC06D73.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/42882DDE-9086-BA41-AD7D-18DE526C7362.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/546D1ABE-BBA2-4843-B3FD-BE2DA44A265A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/5FBFE80B-354A-364A-945D-2D57894E91D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/643F027C-5A1C-C349-BE41-37A1489DFF33.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/64DB5939-E1BF-A44C-A1F0-C08C05719738.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/6639584F-4ADE-3048-AA89-F49593AD9EBD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/6F9BBBDC-426F-0D4B-AB0E-C18D4D400D97.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/96BFE4DD-1D64-354F-B83A-52C0EBFCE446.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/A2504E69-9863-A84F-8ABF-998E35A02BCE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C09B1AC3-EB91-D240-8205-14125E1D8145.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C3CD7EB5-0C52-6A40-B1B9-81DD8A093110.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C5F6FCA7-F1D7-C349-AE96-C02C077EDA96.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/C678FE20-0012-A94B-9E77-E3F279DA5258.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/EA4FFE40-8244-5F4B-A9F4-2D7C335F3818.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/EB55D44C-E5DA-4440-9EE5-E20867D6CCF8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/270000/FD3DE599-7AAC-A54F-B045-8BB03864A688.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/03D02166-FA2D-E646-B95E-5E85C05CABB4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/0EDABDC8-29FD-804F-860A-A7793B49F68F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/0F75A97F-8B91-6340-9A81-70F6B691A13F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/1885C670-11F8-2E49-A406-6CCFF1B4769F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/1E62B284-A580-0A4C-A040-B1E892B1BFBD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/29BE9477-201A-0F4E-95A0-4E1D15CBAC35.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/3469C1F6-8C12-EB46-AE7B-C0BBD41870D8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/395FB0CD-7421-1144-A6FE-D86AEF5F597C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/40935819-DE1B-F142-BA5B-4F3EAF9FFEFC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/4736A5BA-4F0B-1948-B68D-0C47BA39248F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/4B47ECA9-261E-3844-BAD3-F40F858B5A9B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/5999E503-D22A-6241-8F19-6E2D0C1B0F56.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/5B59AEB2-7EF3-1B43-9E1B-B2A0C63FDAE6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/5D5E364B-217D-3949-9CD4-196177C0A0C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/5D7859D3-0BFE-0340-8ECB-7D89671F03CB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/680B9407-A8F8-684F-875B-D36E9D223D5D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/90A953B6-CAEB-1744-8129-11FF2FEE8C4F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/93C93A12-E7C0-B247-AD05-69BEBD73B96C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/A395757B-18B4-9B4C-9B23-6893E786B0CE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/A4179E92-8753-BE49-A3AC-ADB67C7B03B2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/A42D23D5-CA55-EF45-B21F-969A7D1F4490.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/AC8B7316-9DCF-F847-B68A-2C2300CBEAFF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/AD1A699E-07D5-E944-ACE3-0308AE4E2719.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/C6A83C14-7996-794E-ACEF-3C07AA67FBF3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/C80C2672-A7F3-2A40-8048-AC3DF24FB19F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/E1D8D370-DE2E-7448-B685-83EE18D72F26.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/E749B7A0-C32B-B245-AC8F-44DDA463B93B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/EB110191-382B-8D4D-B149-D73B870FF71C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/F7FC3CF8-798C-CD45-8581-7293E7C2A1A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/F9F04B5B-C999-694B-B0EA-0F2CE5EEF3F1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/FBD15F60-CD6E-FA43-ADAB-56EE2B2FF165.root',
       '/store/mc/RunIISummer20UL17MiniAOD/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v1/30000/FBFB3E62-30F3-C748-94E1-3D8647759B55.root',
] )