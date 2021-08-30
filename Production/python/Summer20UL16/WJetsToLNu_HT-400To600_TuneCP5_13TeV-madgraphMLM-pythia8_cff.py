import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/01E0A744-97AE-9147-BB17-6A19C0D0C065.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/02F35F39-52C5-EB42-A1E1-D66039A608C5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0FCE5818-3554-CE43-8686-0C3BE5078647.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/157023F0-2496-CB4F-9268-F0CE22C67E6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/167442ED-AC91-FD40-AC44-F27D45BCF1A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1D9E2B1E-4750-BB44-8C3A-DD74C079135D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/216AB442-14A2-584C-92BD-7712F18A3AC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2822D91C-93F8-A941-A418-2E9AA9A78F64.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2BD80F6C-1B6F-1946-9D0D-1DC48B1A1C96.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2DD1300A-DFFF-CB47-90D5-233A060E2A68.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3588CB93-93D8-3448-9E02-123D8C91CCB3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/37707EEC-22F2-074B-BEAA-31111E1D7AFA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3AFE23DF-84F1-6347-BFEE-07181E0B73E0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3BE47ECA-649D-9F47-A00C-7D388EEBA964.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5494940D-E320-3E4E-966C-6640C284C639.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5F674665-22BF-524B-8D47-C466B129BA11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/705CD2DF-D6A8-8945-A52A-1CE0CDA1A3F4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/74096722-4EC1-6D49-AF8B-3869A5B60CB4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7E3F70DC-22BC-704A-B8E5-AC6063DDF6D7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/964A6559-4985-2C49-9867-A36A3D035F72.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/97E19F14-6E1D-2E4E-A298-AB613A62B6DA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9A93734B-BF6B-CD45-8EFC-C3B844343B04.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A11E4C49-5160-164C-9A30-93752C354C84.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A207E6C1-4F35-BF47-8864-94B812A270C5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A907BCA6-558D-304F-BBD1-B8A2977BCC8F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AB14CB70-8874-314D-B74A-0FBAF9C2698C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B59AB083-CECB-FD41-82EE-C81A48A26E80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B84A3E36-852B-9F47-8DAD-4CEEAD36C44A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B90AC7A8-E9B3-DD4E-9237-B34607FD44C1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BB163F8A-ABAC-CB49-9DA9-00BCCD7CB468.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BDE5CF7E-D98E-2447-AC4E-A9FCA4DD7B5E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C9D3AF3C-6F95-EE47-AA46-09FB0279F443.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D3B89DE9-99B7-8747-B607-8A6CAB4F27E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D3C5CD1B-FAAC-D847-A484-B4DC84299754.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D603B9BF-E157-664C-9DA9-B19509C3A4A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E6B5E84E-9FD4-B344-94BB-A8373021E224.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/ECE97986-56F3-2145-8A5A-E5F7C4A3214A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0498484E-B823-D141-B269-DFF784793949.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0626C46F-10A8-9242-A2CA-1E667DE30227.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0CE5AB6D-CBAC-7C48-8BA2-BBBB2F7B9155.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/15C49F07-4581-FE42-8CB8-296F4FE6452F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1BA277A3-103E-1941-8613-30A3E6AFB82C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1C7367D4-3020-484D-B1B6-9305D85759A5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/1DBA3053-8E52-2F42-9DA7-AA95B454D423.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/20046877-9168-FF4D-8216-02FB1B0E680F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/215DA5FE-27B8-3642-9B73-FFDD16977748.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/227DFEA0-7CD9-224C-BDE4-C29002DA89ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/24E8A786-2F7F-304C-9217-1EBB3827DFA6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/280EE66B-9B4E-3F46-87E2-E099A5F21B5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/29CDD24E-17A8-B64F-A77E-C429A3F8FCAF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2B5150CA-6158-DC49-BFEC-9B952B2496EB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2BDDF161-4D29-C743-AB98-56128B45FA65.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/2D822E72-10BE-B849-A791-633306DB408F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/39C9015E-CF29-FF43-B642-4840E80930E9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/442BC74C-BC58-394B-81FB-377A497B47E5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/44E9BCA2-8079-654A-B384-EEFCAEA1EE20.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/47CC7FB9-B5D8-7E47-9E7F-A743FBBD0F37.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/492C633C-A339-ED4B-857C-9AD4BFE99F09.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4C6BE446-43BB-D140-9FF9-5CB07159F2BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4ED0C9A9-3F22-2C4D-B6F2-2BD320FCE667.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/4F1913CF-D9DE-B24E-AE83-4F1F07932223.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/59133DCE-A2A0-3045-8E4E-1A4C02C51030.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5DF52134-6FE0-A44B-BA69-D4A5C6BF53DD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/5F3B0AF2-1CA4-CC43-904D-D91F26596362.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/62203B69-BB78-A141-A5B0-504ED9182F46.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/65BDB755-66B9-884A-B91D-45552DF98241.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/66423623-7CF2-6C4C-99D1-3737A340D8BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/67C326B1-ECB5-1042-95BD-D7CD8699478B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6D50AC52-0CEB-9D40-AE5A-A09C16F77E72.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/6D94D173-14AF-E746-A031-EE1ED7BD28CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/714D12E2-AF3A-E042-B699-A918A7C25810.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/751DD60B-0BDB-944E-AEB7-C6743BC0E493.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/78C1B595-7086-2747-AE6D-CF0AE0D2B15F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/796CEEEF-8881-CB4B-93A5-86D63F060EBC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/7E32CFAB-0493-A84C-90CC-EA2F250ACAA2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/865AA2E9-9F6B-EB4E-B78A-6B8C9C61FCD9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/889EFE81-D88D-B041-9A07-7339FE7D8B97.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/8950BDEB-83A2-1444-B6E4-474BAA1D0092.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9ACB4380-74AB-0C45-9A43-76AAF9445C42.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9D8BC2E9-0FB5-0345-88F1-9C412458B3D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/9FD779DC-CB9B-CF44-B786-1FE6CACB8CA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A1BB5FE4-BE49-4841-84D2-380122EAFA4D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A29436EC-5E04-264A-B9E0-C8418DC8D4D1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A36B235A-51EC-C14A-9A97-994A53EED662.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A5D413EF-6719-EE4B-BBF6-98270F1BFF3C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A69B983C-A35A-AE42-9486-1C395BB98900.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/A95BDF52-810A-7F4D-BD21-9DD03470221D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AAE99E03-45BC-A044-ABA3-61D261642CB3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/AD922586-0D12-234B-A18E-59B210117866.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B6B3DB32-84BD-3C46-AA7F-F2D46BAA6C98.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B8FDCF61-387B-F141-8F35-62E75BE9836D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/B91A4212-BD54-B84D-AD9E-4BBEE87E9BD0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BA345B61-C03D-FF4F-B235-84359D8C61E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BC481547-395D-7B43-9FEF-4482AD2E5204.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/BF874F31-B195-5746-8A29-ADEA1FE5BC2F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/C27C0975-8B69-8046-97B9-840803076EF5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/CF3A501C-58B4-5845-8D8C-257EA2302B67.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/D220E615-3F3D-9640-8A06-B38B64F02F3F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E070627E-1B43-2446-8715-8539B8822E60.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/E5C742D3-740E-8943-93CC-42ADA431C0FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EA85BF84-1196-F746-9A8A-F1BFDE2B445D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EB467F92-38F4-0844-9385-D0967792B8D7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/EDE62C48-61E9-CC41-BCFA-DE62ECC44A96.root',
       '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/FA54A6C3-D0FF-0844-B1EB-35A6BBCD206A.root',
] )