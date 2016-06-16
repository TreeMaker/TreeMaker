import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0623F713-3A04-E611-88A0-A0369F3016EC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24F2842D-8704-E611-9754-842B2B18158E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C07B1C4-F103-E611-970A-0CC47A4D7662.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/4E832C44-EB03-E611-9ACF-141877412793.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/5CAE12C4-F103-E611-B44D-0025905B8586.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7ACA821A-8704-E611-BBAD-001E675A659A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7C1FE3CB-8803-E611-A2DE-0025905B8582.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7CA554CA-F103-E611-B020-0025905B8610.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/801A6083-EB03-E611-9923-782BCB2100C5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/8A0D53BF-F103-E611-AC92-0CC47A4D75EE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/9681ACC2-F103-E611-B2C0-0CC47A4D7638.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/AA8F2B46-EB03-E611-B09D-1418774121A1.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B453EEC2-F103-E611-AA77-0CC47A4C8EE2.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/C0567DC5-F103-E611-B894-0CC47A4D7698.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D42644C5-F103-E611-BFCF-0025905B85DE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D63052BF-8803-E611-8D63-00248C55CC9D.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/E671EA2C-EB03-E611-945F-1418774118F6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/02F5621C-6604-E611-B1B7-0CC47A6C063E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/105C4479-A903-E611-A23E-0025905A608C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/328E64E5-A003-E611-BAF5-782BCB5094C5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/445E9112-BF03-E611-AF47-0025905B8574.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/526851F7-3E03-E611-9273-0025905A613C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/62B253B4-4704-E611-9EAF-008CFA197CF0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/7003CDA3-7004-E611-8B6A-782BCB53A0C1.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/74C218E4-3603-E611-B0DF-0CC47A4D768C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/828DC9C7-A503-E611-BFED-0CC47A4C8ECA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/8845638E-B403-E611-AF45-0025905AA9CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/94091CDF-8F03-E611-BD2C-549F3525D084.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/A487AE0C-BF03-E611-96F2-0025905B85BC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C02ECD0C-3204-E611-8ABF-002590D9D8C4.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C6239F0D-BF03-E611-A1C3-0025905B8612.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D61598F1-B203-E611-82EE-0CC47A4D760C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D85E93F5-3603-E611-B056-0025905A6088.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D86E01F7-3E03-E611-9214-0CC47A4D7600.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D8B8D91B-9303-E611-834B-782BCB5094C5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/DAC8F5EB-B203-E611-A3CE-0025905A6056.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/18576205-CF03-E611-B80D-0025905A606A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1E0BF64E-9104-E611-9619-24BE05C4D821.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/30B1CA37-9404-E611-B231-0CC47A6C1034.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/425D17A2-E303-E611-9D74-0025905A612A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/462A0879-C303-E611-9ED7-0025905A6132.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/56349185-C303-E611-81E4-0025905A60A0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/567B6AA4-E303-E611-A18B-0CC47A4D76A2.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/58778B1F-2604-E611-A8D8-842B2B180CC3.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/68798279-C303-E611-B5D9-0025905A607E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/788A06AF-6504-E611-A492-0CC47A78A408.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/90962E18-9204-E611-A671-001E675A6AB3.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9CEC9814-CF03-E611-8B20-0025905AA9CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A08F0907-CF03-E611-8376-0025905A608C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CEC8D68E-DB03-E611-8F64-0CC47A4D76D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E8EF1403-CF03-E611-B9DF-003048FFD7AA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/EA174979-C303-E611-AA79-0CC47A4D76B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/10669873-8303-E611-ACDE-0025905A60DE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/18700248-A103-E611-834E-0025905B85CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/262D5930-DD03-E611-ADD8-003048FFD722.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/2A1E633C-7303-E611-900A-002618FDA207.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/460EAF70-7303-E611-A27E-0025905AA9CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/465C7E44-7303-E611-B341-0025905B85DE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/4A8BFD0E-6F03-E611-8668-0CC47A4D76B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/4CFE443F-7303-E611-97D3-0CC47A4D76AC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5642A40E-6F03-E611-8E73-0025905B8580.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/609F12F5-2504-E611-805E-001E67DFF735.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/6CD3606E-8303-E611-AED2-0025905A60A8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/84F92A48-A103-E611-85B3-0025905B85CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/A2529C6E-8303-E611-884F-0025905A60A6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/B83B9AF1-2504-E611-9D7A-B083FED42A1A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/BE36A970-8303-E611-ACDA-0025905A6094.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/DE13DA7F-150C-E611-98DF-C81F66B782DD.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/DE33C034-2604-E611-8CFF-549F3525AE58.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/E06AFE10-6F03-E611-B110-0025905A608C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F0621CE8-2504-E611-8A68-0002C94CD13C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F857308F-DC03-E611-BAD4-1418774120C3.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1254D029-D203-E611-BC52-001E67DFF6E0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/144CEE20-D203-E611-8296-001E67A3EAB1.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1C9E036D-BC03-E611-8EC8-0CC47A4D7616.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/34930875-F703-E611-A380-001517FAD640.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/3C64EB6C-BC03-E611-B734-0025905B8576.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/463091BE-9E03-E611-9B13-0025905B85CC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/5043D36E-BC03-E611-A3C0-0025905A609E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/52749E75-D503-E611-A1CC-0CC47A78A468.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/5EB5F26C-BA03-E611-BBE6-D4AE52AAF583.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7688BD6E-BC03-E611-9F15-0025905A60DE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7EF7986C-BC03-E611-8380-0025905A6132.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/80CA9786-BA03-E611-84CE-001E67A400F0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/84E5C3D3-8716-E611-AD1E-C81F66B7EBF5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/886EF21B-1404-E611-A698-14187741212B.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9A77923B-BC03-E611-A778-001E67DDC119.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A832DF1C-BB03-E611-B91C-001E67A3F3DF.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B049886C-BC03-E611-9BC2-0025905B85F6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B478321D-BB03-E611-9969-001E67DDBFF7.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E48D051E-BB03-E611-A67A-90B11C056AAD.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F0CED81B-BB03-E611-A725-001E67DDD0B9.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F4561207-7804-E611-88EC-0002C94D5502.root',
] )
