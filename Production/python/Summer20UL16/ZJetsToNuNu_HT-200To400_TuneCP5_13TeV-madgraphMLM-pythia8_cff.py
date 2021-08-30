import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/045E4C8D-AE33-DA4D-9FB0-917646F9EA5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/05BC9E29-1F89-874D-B413-0F8E55CD5C0C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/15F8D7F3-9532-044B-B877-42A845ACEF17.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/24E0213C-F214-564A-A646-A2C018CB4612.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/39A287FA-AD2E-D842-BD28-13C7B443B692.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/3ED57ED6-C0D3-A143-894C-8C1F2719DD67.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/481D4D79-B8F3-F94E-8C03-F50BB4F6C7E6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/5559AEFB-8199-0A4A-96EB-7CC5FB4CAB2E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/5B4AE332-3503-6743-8687-27FA2448A906.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/64A57675-EE73-3A40-911E-A436A08A042D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/6B72D4E2-0192-EE46-A75D-B1DEDE5A161D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/6BB42A30-8ACC-E540-92A7-8399DB2F367F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/8C6748BF-9E63-DA4B-AA83-8C59D5360CC7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/90649F04-CD89-864B-889C-07AEE5747DA7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/9D56A612-34FA-D145-866F-C4BEA4FAEBEB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/9E1CA28D-925B-6246-9A96-251C5BD8568E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/AA456733-17FF-F946-9A8B-5EF481564FE2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/AE957A70-E39D-7C49-A58A-383F4C59F027.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/B168D7D7-745F-D940-9C4B-A5F4CBB51710.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/B56975CF-7E79-AB44-872B-3095711F5D4E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/BFDD490F-27BE-D147-87B5-E5A94032A1F1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/C0BEA008-7543-114D-BE15-3EEC05E1B45C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/CC5F12D2-2415-1A4D-B167-3B7347F267F6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/E6133A7D-49D3-F24F-A528-C592A80204D4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/E84B5BB1-CB76-9142-A7D4-072C386E2B29.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/00000/ECB48291-0786-3146-AAC6-68CBD4CE08BA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/010000/0C5788FE-948F-7845-BB49-912B44B63B65.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0235447E-0C70-904F-AFFA-B4972B4E14B8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0242DF44-B5DD-D940-9467-0A83CE05CEB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/08EC10D0-4149-DD4F-8847-DDB4B42BEE7B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/09CD9FD3-DA65-AF42-9D9E-28096FA0AFE9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/12C44DD4-292B-0C45-98BD-9B18C95643A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1A03CD1A-B932-3D46-A339-6DC8A5007150.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/24C4CBF7-7E05-1E43-A944-87176D809989.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/25190D6D-CDEB-5C4C-AE1B-B4707803E63A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/29E6F616-800B-FA48-AFCD-C8BCB381D2A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/31123502-D4D2-674D-8DF2-9D1126BDFA8B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/345BDC6E-BFBD-8145-A1BD-CA4673AD5100.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3528BA15-4BE7-BF4A-96AB-C5D3264B503C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/37CE9E47-7466-F04E-89F8-86D3AFE58B03.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/382C835D-9CEA-AB44-B56A-7F7BB927DE71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/38E54AA3-1A42-044A-8897-7649A6EBEC94.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3A6ADE55-45B2-BA45-955A-38BEFAB4E05E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3B85498B-4B39-184D-AE5B-7CC453CFA752.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3E444DA5-826D-7940-92ED-302A1F124BF9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/42D068AA-8AED-0641-8EF4-DDBB6A44B9D6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4428A83D-BC9E-3543-9C2F-A728309B8F25.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4901DE79-0279-2947-9C28-A2A7F8F82AB3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4E5C6CE1-EF77-A94F-A0DD-D88E9E048BF7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4E84ED46-774C-2B4D-A3C0-EAF7DF6C83C8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5DF9B252-5F98-8447-A27B-4C16DD463BF8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/661B738B-7A25-864E-B199-A8F6C14DDEC6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/66E94677-01FC-8C4B-82AA-AD0D03D8DE80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/71B32432-906D-874C-9FB0-4CE875CA8176.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/72EE8972-C064-C64E-B5B9-5F3667684D2C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7C443382-60CC-E640-85B1-33B4EFA6E83C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7D06F114-7CAE-A441-9F2C-D53B22489D26.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/82CC977C-3773-1E48-AEAD-1CA9C53EDEDD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8753F4D8-57E7-134B-9ED8-5F2C93C64A29.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8E6085F0-2FF8-AB4B-A5EB-64674B7BD8EA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/92D9C84C-7EF8-A14B-B9A1-2C38366D9396.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9463515B-ED78-6846-8B6E-8D952A182C35.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/97910A7D-E5F4-9F46-B2BD-7669BCBF8953.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9A3F129C-B1AC-3B4A-9841-D43D9B7FC096.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9B4D5B5D-B7CE-B94C-902D-C2D666A20490.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9F93D518-432C-0548-AFFC-73EE02AE70F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A31EB011-8B38-2044-9CFE-CE233FDC7EA7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AEE9CA12-367D-3D40-9E6A-0313B6F47E31.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B47DED62-8FA5-904B-91F3-4E1E42A6041D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B76C3425-4B58-AF48-A9CE-C122B7E8554B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D1F7FA16-E571-A049-91EE-96A8EE88963B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DA0F1A38-F407-2F4B-9D27-3488A080C3EB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E1342A60-3332-E94C-9638-A85115EE6439.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E306A58B-33D5-0342-A476-7C4A3426760F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EE030C44-FBAC-3C4B-955F-9484B3869B15.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F2766B8D-41FD-E44A-BF61-7DFD6DB5C219.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F2B4D124-79C8-2F4E-ABF5-7F02C51B92AE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F6561A31-5542-884E-9598-F09A3069F22A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FE2D93A8-EE09-6E44-8000-56C169CF9646.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FE57C1DC-DB66-7843-80D4-5AB76E457C7F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/00232F67-32BA-DE46-AD0A-92CB26A35BEE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/02669E1D-DC39-6B4E-B671-7192A392B9C3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/04430CF3-9910-CD49-B89A-7C2AAD325AED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/0DFD422A-5914-914B-927C-B67603DA2E90.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1AF19DF6-77AA-CF4F-BC76-9D0FE942A480.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2370BFAB-2C1A-9743-BAEA-A886F770DD65.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/25964D7D-F508-B047-A3AF-BA2DCED805CE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2DCD2001-AED0-114A-8031-9CA9FE79EC98.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/33C61B8A-E474-454E-BB47-42210E2B8FF6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/352CA581-E9F5-4E4B-989A-0C9A31FD2440.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/38D017C6-41E9-A841-8E3C-59798463D067.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3A4901ED-887D-3E46-B25B-0327BC1D4D8A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3B2CAE48-B42F-2844-B155-1BFF8403F116.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3D2240AF-26C0-2B4C-9E71-098B0D93EBC8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3F3AB194-0115-6F46-A92C-A2952076836B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/4561EB4D-C405-564C-9060-236136418AEA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/544D59ED-E4AF-5C45-81CF-32D9ED034318.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/5516813D-CA07-0B45-97DF-F1AA9DA68E91.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/55E4EE95-F379-C34E-9199-ADE4DF94D568.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/571A765F-F00C-3340-999B-FCD94605A544.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/61AEDE2F-AEC0-724E-B550-3F2BCDF4A448.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/73566A36-BD4D-B543-97EC-2F4D6318EA49.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/9021B56E-AAA2-404F-86BA-B04A9FBD5723.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/91DB2DF2-A26A-0E4D-BB10-7E3F1ED1C0DA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/9689C238-03C0-4A40-80BF-33FE7ED51F6A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A12E4C83-5D46-D845-8B8D-50C128EAB542.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A2AFE495-3BA1-7C4C-AD65-38BB424F434E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AA4E99AA-5A13-384A-AE17-513756BE9E4C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/ABBE2A8C-C02F-8A48-9181-230DB2CBCC66.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AEE27738-4799-9F4E-AF37-81E3281142A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B93689A1-D7CC-0E44-AB98-BDBD4A14AC4C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/BC589D60-78AC-A04D-ACB4-05E69A30177C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/BD2FFA3F-E8C0-684C-BD7D-05B707CB33B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C2A5808D-5F70-244B-B2C8-FA105E353A2C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C8CCB77B-EDBB-5346-9E58-AF523AE888B2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/CF6404E1-DAF8-D646-A14C-5FA8A393EA1E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D277F12E-8C28-DB47-AA06-ACAD6677EFDE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D2C6E227-352E-6042-85E2-86F0C6A849F3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D37B874D-D249-5542-BACD-8A355C45A043.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/D4084F53-169D-3B42-914A-898D63883FB4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/DD9315C8-6E95-E84C-BDBB-438EB4B58AB4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/EE7193ED-E37F-4244-88CE-38055C906C74.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/EF865490-FD04-1643-99F0-E97BC4D9D5C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F1378CFB-AB80-3F44-B59D-9500839981F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F36467BB-AD13-2E49-A2D5-FF82F202C181.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F399BB8D-C3B7-1445-9711-2FEF3ED218DE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FF92A087-28FA-8545-B983-25929698861D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/003BEB66-3BB2-1047-8D31-C9B5AEEF4715.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0075F281-9ABC-AD47-957E-741E2219731D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/052B6D21-83ED-B948-A1A2-A3F3B5C510FD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0CE62772-0105-D745-9E0D-6867843B624D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0FA1EC38-D9A8-AE47-9CE1-03ED5B6C2BEC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1068A128-5FED-AA4A-A118-251F7CAAB736.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/11F6AA0A-8803-9846-B494-F4C57CB07663.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/14761655-1FE1-ED4F-AD38-494A8ED7E4FE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/155AB6B9-FB77-814B-B37F-DA77B0AC5229.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1DFEB862-7A95-9A4C-9127-015DF2FC8731.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/23E4E190-FCB9-F243-B53C-00E039B33983.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/24F51A98-FE08-AA4B-9222-8509FAACBF89.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2D3B9913-C577-D445-8CA7-E99618C94E4E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2EA7687E-6A10-A446-A1EC-C6662C76B437.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2F99F0A4-53C4-D842-BE83-EE52A25A33BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/35C4F44E-FD98-2B44-AE5C-7B1896190C10.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3691BA17-7885-2C4D-BA6D-8CA3197A4409.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/3E926625-2055-4E42-BB9D-E094F47D4099.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4059458E-513F-AA4B-BFC3-64C54D75CC21.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4119268D-743E-244B-AFE7-23CF909E3B8E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/49F8FB4A-A77F-6648-831F-611F01EF7567.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4F793065-D542-6146-A2F5-A9CEAB30F016.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5462CA06-0799-7740-93E0-CC3445C85D32.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/54C3B7EC-6A15-0243-AA35-3989DE9BE0F7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5598B737-6622-0641-83F7-6CAD5C7D5E4C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/604349A4-75FC-BD47-BEB7-C370E145EF30.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/62C67038-0715-BB4A-89BF-40FA800ABF37.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6618A179-7AE8-9A48-8824-86AEB0CC0095.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6E06E717-1D92-5C4C-B727-642D812BAADE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6F0051F5-A3F1-4141-A28D-BB09AF5AA8C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/77E18489-05BF-BD4D-B48B-F3D4710A513E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7D9960EB-0B78-994D-86F0-AD8B8625C99B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/82C5D1E6-F9F3-1F41-BD04-ED42B013468E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/918C8089-4A52-C047-B8AA-DC9255164FF3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A54AF069-29D5-6A47-9343-3E3FBAC0AC14.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A86052D0-43E2-2041-9940-F0CC5158844F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B0033A52-FB2E-0943-B2E6-41ED9418BCA3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B52CBEC8-45F7-DD49-B5EE-5D1BBE9092F3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B745AD21-5183-FE4F-AAF5-923232FC43DB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B95E11C1-675E-B846-A212-3907371BC477.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BB9E8AAC-FB62-004F-BB67-24E8A142D420.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BCB6626D-143A-3444-9320-689D7BFD3AE1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BF0136A7-5946-0F49-979A-9CF5677A7ED9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D568C3ED-6C78-054E-8C3C-B6735ADFCCEE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D7217A72-C13E-6045-92CB-A2D0EEB06FBB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DAB2B490-78A9-DD4D-9555-2912AD9D51F3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DBE4AAB7-CEFF-7449-995E-E6264D8304A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DDAAD2D8-500C-214A-96A1-DFBCA6A56B5D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/DEC8506E-D7EB-A74B-AD6A-992EB30732D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E5D1B710-73F3-8E40-95AE-EFBBA538AD0A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EC8B14F7-9019-344F-9CF6-B35CFB968262.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EEDB540E-7476-D640-BBDF-FA2ED1F4A537.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EF30589C-CF0E-0345-8A6F-5B38E23AE76C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F007ECAA-7A4A-F14A-9907-4DFAC1E88E02.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F4F03854-6D21-CE47-88B6-D6EC784822DA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F7483EA0-44D0-2743-AC3A-06F79C97EE71.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F7FFD1F1-7FA8-AB4C-8461-C1727F6748BD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/F86976C4-AF5E-EE49-8B92-3578BF23B5FE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/FB11429E-BCD2-6547-AB57-D22416263895.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/FC562695-2D5F-584E-A583-0FC8E50E26FF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/FD8A22F0-E061-EA43-8A8C-B6BEE7777845.root',
] )