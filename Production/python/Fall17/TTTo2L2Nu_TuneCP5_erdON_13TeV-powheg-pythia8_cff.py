import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/2644002F-639F-E911-8E1D-0CC47AFF0464.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/323A8814-2DA2-E911-9FEE-008CFA197D10.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/347A2B6D-30A2-E911-8D78-D48564591B68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/34E1ADB9-C59F-E911-82E3-0242AC1C050A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/461B3952-77A1-E911-B3E3-E0071B889698.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/68285F6D-959F-E911-B429-0242AC1C0507.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/7CF84FC6-2DA2-E911-A3E0-0CC47A5FC619.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/8EFD9E30-35A2-E911-BAC3-AC1F6BB1780A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A00DF50F-29A2-E911-805E-008CFAE452EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A083BBDA-3CA0-E911-93E8-0CC47AFCC416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A41F2EFA-35A2-E911-A1B0-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/AEB03A33-769F-E911-B999-0242AC1C0505.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/B4B4FCEF-30A2-E911-853E-0090FAA59E44.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/BC6AF8A5-39A2-E911-9BC9-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C0DCBF44-2BA2-E911-B541-001CC4A6AD5E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/CAE2AC0F-3BA2-E911-A488-6CC2173D8740.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/DE0D4BCC-8F9F-E911-941A-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/E6E53971-319E-E911-9758-EC0D9A0B3310.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/E898E840-3BA2-E911-8A79-14187741121F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/02702DC9-FB96-E911-967D-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/045371DE-FB6C-E911-BC83-28924A35056E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/0878CFFA-ED7C-E911-BF97-A0369FF88422.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/0E692F15-6792-E911-AA62-0CC47AFF24BA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/141A0361-0370-E911-8954-001E67792786.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1608F85E-0F9A-E911-A639-AC1F6B1AF002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/16666E82-A773-E911-A0CB-0025905A60E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1A59F304-456E-E911-B871-40F2E9C6B000.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1AE576D2-967B-E911-A1B3-1866DA7F95A6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1C578664-1F6A-E911-9441-0CC47A0093EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1CBB4B1A-4191-E911-A30F-0CC47AFCC3CE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/1EF73871-906F-E911-992A-A0369FE2C01E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/24C3025D-C36E-E911-B462-6CC2173D46A0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/26EC7CEC-6E7F-E911-A1FC-0242AC1C0507.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/287C44D0-E66A-E911-9294-3417EBE7009F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/2ADB0CDD-EB84-E911-8749-20CF305B0624.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/2AF8427F-5274-E911-A4E7-0CC47A78A408.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/301C68AB-D86D-E911-A6BF-0026B9278644.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/30380984-056F-E911-AA34-A4BF0112BC06.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/32E46993-2D6F-E911-A885-AC1F6B0F6758.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/3419A8CD-876F-E911-A90E-AC1F6B0DE45C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/34AA5951-0F9A-E911-A951-A0369FD0B38E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/34C1428E-456D-E911-977B-FA163E2F5EF2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/3612A80A-5E70-E911-BACC-A0369FE2C05C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/36386DD1-967B-E911-8F44-484D7E8DF06B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/36DEA4D4-0F9A-E911-A511-E0071B791111.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/38E10711-4291-E911-BA62-0CC47AFF0134.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/3EA96281-456D-E911-8957-FA163EF4913C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/403520E4-0F9A-E911-83FF-0CC47AC17506.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/42EAD4E6-0F9A-E911-A2F4-A4BF01013F8D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/445E1DD7-109A-E911-9F44-44A842CF061A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/44FF48D8-109A-E911-9E1F-0CC47A1E0470.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/4601B742-2D74-E911-AC23-0CC47A78A414.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/48FAFA72-ED76-E911-9BF3-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/4E93D523-4F6D-E911-BDFE-FA163EA67301.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5093A569-7A98-E911-9397-0CC47A5FC679.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/50F54590-456D-E911-A9FC-FA163E89276D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5440EF41-806F-E911-871E-A4BF01125810.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/544AD263-DE84-E911-B25F-B083FED13C9E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5657B9F0-8398-E911-BE83-E0071B88B988.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5AA52B2C-0973-E911-9F25-0CC47A5FC2A5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5CCEC4B8-9883-E911-A2A8-246E96D1AC20.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/5E7C74BB-208A-E911-BA54-7CD30ACE1318.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/62EDCFD6-109A-E911-B876-28924A35056A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/64AF5A77-E46D-E911-B038-0025904404EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6663CAEB-D57D-E911-B685-A0369FF884EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6698A447-2F6E-E911-8B2A-FA163E3228D0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/66A33220-136E-E911-926B-3417EBE34D08.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/66AEB359-9C83-E911-963C-B083FED426E4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6852D5CF-109A-E911-8D54-0CC47A5FC491.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/689BB5C8-236F-E911-87C3-AC1F6B0DE456.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6A61C25A-0F9A-E911-AD7B-0CC47A78A3EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6E8D4969-106F-E911-91B8-B026283464B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/6E9D5B91-377B-E911-B2D9-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/761690D4-109A-E911-A683-7CD30ABD295A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/76931499-6F70-E911-AB07-6CC2173D6E60.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/7AD22959-0F9A-E911-851C-3417EBE6463F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/8054031B-396B-E911-AA87-0CC47A7E69D8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/80BACFC6-906C-E911-B215-A4BF01287CF8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/80DBA69B-9E91-E911-8B60-C0BFC0E56836.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/80F68FEB-536F-E911-857B-1CB72C1B6568.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/842600CD-876F-E911-9EC3-AC1F6B0DE294.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/865FD970-B96C-E911-A7C8-3417EBE7047A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/8678763D-6C6E-E911-A2B6-008CFAE45240.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/86F8F1C1-109A-E911-A19F-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/882CF9CF-109A-E911-95CF-7CD30AD094B4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/88746144-0F9A-E911-85BB-0CC47A7FC72C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/8A7F2F78-B76F-E911-BF8A-20CF305B066B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/8CE0F6F6-7F71-E911-A31F-484D7E8DF0B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/92EFF1CB-FA66-E911-BE43-3417EBE70684.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/94144ACF-1C6D-E911-A51E-6C3BE5B58198.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/945E20D9-AF6E-E911-AF2C-44A842CFC9BF.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/94B765C0-1E84-E911-B2A1-AC1F6B0DE3E8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/968057CE-CC6F-E911-B1AC-405CFDFF481B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/986DBACC-109A-E911-8850-B4969109F230.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/98FDDCDD-0285-E911-BAC4-6CC2173D8740.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/9C00F728-4F6D-E911-881A-FA163E557D56.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A06715E8-4970-E911-A7BF-6CC2173D6140.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A06F4BD7-109A-E911-A891-00259021A2AA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A090EECE-2F6F-E911-92EE-B02628342560.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A295B9C9-E76C-E911-867F-001E677926B6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A629B2EC-866F-E911-81EE-44A842CFD65A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/AC7F7E63-A674-E911-80B0-44A842CFD674.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/AE4698C9-2377-E911-84CF-0025905B8562.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/B64CB9AF-7C77-E911-922F-B499BAABFEB0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/B6694ECA-746C-E911-8DDD-A4BF012881D0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/B6E3DA3C-026B-E911-B52B-FA163EA42BDA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/B818FA2C-6783-E911-B21E-A0369FE2C174.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/B8A4AF98-3A76-E911-AE88-6C3BE5B5B078.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/BA0C2E19-716D-E911-95A0-38EAA78D89AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/BA6BB1AD-626E-E911-BCE1-40F2E9C6ADBA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/BCE8FCFF-126F-E911-B7FC-008CFAF35AC0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/C25715DC-3583-E911-B014-48D539F3863E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/C8FB194C-9C6C-E911-AB8C-A4BF012835C2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/CA53859A-4087-E911-BBB1-3417EBE669D4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/CE86CF88-456D-E911-BB93-FA163EFD58CC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/D66FE04F-4185-E911-B3CE-D8D385AF8B64.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/DCCCA5CD-FC6E-E911-853C-44A842B4CC98.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/E414BB6E-EC7D-E911-AFF8-AC1F6BAC7C4A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/E629A219-7F6F-E911-BA67-A0369FD0B3CA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/E6C1D6E3-0697-E911-891B-AC1F6B23C848.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/E83A675F-4C6B-E911-9217-0CC47A7E6972.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/EAC774DE-109A-E911-9B0C-441EA161DC8E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/EECAC5CA-426F-E911-BBA2-A0369FD0B170.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/F0A57F2E-697B-E911-BF50-B496910A80F4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/F0BD0926-A997-E911-A430-24BE05C4C891.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/F41D0768-1470-E911-821F-509A4C74D08E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/FAB71982-377B-E911-8F3D-AC1F6BAC7ACC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/FCB1A32A-DE96-E911-BB45-0017A4770454.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/FE1499D8-127D-E911-B370-0025904B5FAA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04B93E35-C3A2-E911-ADE4-0017A477105C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04C34B2C-C5A1-E911-8CDC-002590FD5E70.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0C002FA4-B99E-E911-9ED1-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0EA59930-58A3-E911-ABF4-68B5996B43C4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/10F13403-EFA0-E911-9663-901B0E542804.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1238DD42-519F-E911-8679-0CC47AD99148.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/18C3873F-0F9F-E911-89C5-D0946626135C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/302097F7-C9A2-E911-A6D5-44A842CFC9F3.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/36950943-C3A2-E911-B2D4-506B4BB134FE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/38573752-79A0-E911-885D-AC1F6B595F6E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/424A2576-C7A2-E911-AFBD-AC1F6BAC7D14.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/4C42D6B1-5AA3-E911-8C8A-506B4BB16AB6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/4C59F2A7-96A2-E911-A49F-AC1F6B8DD1F8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/52E2C93F-C5A2-E911-87CC-AC1F6B0F71D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5C8C99E5-039F-E911-A1FB-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/70714B77-34A0-E911-9DDB-F4E9D4AF8BA0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/76E49433-BFA0-E911-A193-20040FE9CF50.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/80ED833F-C3A2-E911-BEF9-00266CF830FC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8657CB6F-CF9F-E911-A201-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/947200C9-C4A2-E911-83FF-246E96D14C3C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/964C715C-84A3-E911-ABE5-001E67DBE80A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9C3644C8-C4A2-E911-B3FF-0CC47A1DF620.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9E06282A-C6A2-E911-B54B-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/AA8D9CDD-9A9F-E911-B8B4-E0071B73C640.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/AE001937-C3A2-E911-8E9C-20CF3027A59F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B2A1313A-519F-E911-A845-0CC47AD9901E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B8B1C77F-3BA0-E911-8854-A0369FE2C1A6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BEC20211-C9A2-E911-B643-141877411EA2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/CCA04CE1-A5A1-E911-BD1B-90E2BACBB038.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D292D2AC-CEA2-E911-9366-0026B94DBE31.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DCC6E16A-C3A2-E911-B903-003048F596AE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F0939947-E29F-E911-8FD6-0CC47AFC3CA2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FEED87F6-9EA1-E911-BB6E-B49691386CFC.root',
] )
