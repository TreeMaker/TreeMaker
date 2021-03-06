import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/02AC8866-A1B7-E911-B521-801844DEEC30.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/04A9CFF8-27B8-E911-BB21-001E67792598.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/0A21F236-BFB5-E911-8A8B-EC0D9A8221E6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/0C3B8F04-52B5-E911-8C54-AC1F6B0DE2E6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/0C4EE4AE-E4B5-E911-9CAE-0025905B8562.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/0C705955-AFB7-E911-B819-20040FE9AD58.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/12604210-9FB5-E911-8387-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/142ACD0C-A9B7-E911-8FD8-1866DAEB1FC8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/1631E123-9FB5-E911-9AD8-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/180E30DA-6FB5-E911-B247-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/1AA1124D-7BB5-E911-A59E-AC1F6BAC7C16.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/1EEAD23D-64B5-E911-87D7-A4BF0112BD4E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/20C8E381-AFB7-E911-B0F2-842B2B180922.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/223A9B56-AFB7-E911-862D-20040FF469D4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/2690EF92-CBB5-E911-82FB-AC1F6BAC7EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/282EA526-26B8-E911-91B9-A0369FD0B228.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/2A0D4B7A-A1B7-E911-96AF-1866DAEA8218.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/2AE78507-52B5-E911-828F-0090FAA57E64.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/341D2222-A9B7-E911-9AF8-801844DEED78.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/34F2958B-2BB5-E911-9D96-A4BF01159248.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/366C2CDF-6FB5-E911-9FA3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/38806084-E4B5-E911-89E7-0CC47A4C8E98.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/3E977CBC-A5B5-E911-9FAE-001E67E71381.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/46E94323-50B5-E911-BC74-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/4A0A0F1E-A9B7-E911-9062-90B11C0BCF42.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/4AC53726-24B5-E911-AD8C-AC1F6B0F676C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/500B7AD3-6FB5-E911-BBA9-002590AB3A82.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/52BBF114-50B5-E911-955F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/54A684E9-C3B5-E911-945E-A0369FE2C1B0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/54F8CFE6-92B5-E911-822C-0CC47A4C8EB6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/5A202214-7CB5-E911-8870-AC1F6BAC7D16.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/60471CD1-6FB5-E911-ACD6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/60B6889C-37B5-E911-8E0A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/60EF0709-E0B5-E911-A623-E0071B7A7830.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/66F3EB72-7DB6-E911-9206-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/68D0BB04-52B5-E911-AF8D-AC1F6B0DE45A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/7232310A-3EB5-E911-B426-0CC47A4D75F8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/763313B6-D7B5-E911-9F20-AC1F6BAC8070.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/7873B141-B2BA-E911-9978-24BE05CE1E31.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/7A6A1AD2-6FB5-E911-B34A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/80FE0855-04B6-E911-9932-E0071B7A18F0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/84C85111-50B5-E911-9499-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/88279E72-A1B7-E911-8774-B083FED42B3A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/94F20C2A-A9B7-E911-86D5-A4BADB22A4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9A3342CB-6FB5-E911-8D83-0CC47A57D086.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9A405026-9FB5-E911-B785-002590AB3A82.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9A5F58CA-74B5-E911-BEEA-AC1F6BAC7C1A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9ABAECBA-23B8-E911-8C1B-001E67A3F92F.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9ADACB32-50B5-E911-9FD4-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9C1ECD17-26B8-E911-8D7B-0CC47A0AD498.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9E288B98-6DB7-E911-A95A-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9E6BDD30-A9B7-E911-B1C1-001C23BEBF14.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/9E7CF754-AFB7-E911-8007-20040FE9AD58.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/A2C983A8-85B5-E911-9C6C-A0369FE2C014.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/A4B9D501-52B5-E911-BB1F-A0369FD0B1F4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/A6D979A3-44B5-E911-A340-0CC47A78A3B4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/AA843CE5-4FB5-E911-B305-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/B6D3426D-DEB5-E911-8A51-0CC47A57D036.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/BCA8B789-F3B6-E911-9020-506B4BB16AB6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/C042D543-CFB5-E911-960C-E0071B73C630.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/C25F5363-74B8-E911-B2B1-AC1F6BAC7EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/C6B4DA30-24B5-E911-9BCA-A0369FD0B144.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/C8A9FBDA-84B5-E911-99E6-F02FA768CFD8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/C8AC09F9-91B5-E911-B2EE-0025905A48F2.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/CA074865-A1B7-E911-BD19-801844DEEC30.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/CC62609F-A1B7-E911-AC9F-001EC94A8EF1.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/D01476B4-47B8-E911-A3D9-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/D49DCB09-9FB5-E911-9F86-0CC47AA477B6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/D65EF019-52B5-E911-ACBA-0090FAA56994.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/D6B98DEC-4FB5-E911-A245-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/D8BF79BD-A1B7-E911-9B2E-B083FED42FE3.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/DA2E6F71-AFB7-E911-9C1F-20040FE8E8A0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/DCC2D1C4-26B8-E911-8CCB-001EC94BA117.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/DE13BC48-D1B5-E911-9EDB-0025905A611E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/DE1B4083-A9B7-E911-9FD3-1866DAEEB0C0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/DE673933-57B5-E911-BA9D-0025901AC3DE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/E2450C0C-A9B7-E911-A5EC-20040FF492AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/ECA877EB-AFB7-E911-AA34-14187741120B.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/EEC7BF42-3CB6-E911-95F3-001E67E69E05.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F0762B02-3EB5-E911-99FD-001E67792608.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F205D36D-A1B7-E911-A361-1866DAEB4100.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F2A14909-50B5-E911-85F7-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F6302867-10B7-E911-A0B0-0CC47A4C8E26.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F6A8E51E-C0B5-E911-B7FA-0CC47A7C34A0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-TChiHH_HToBB_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/260000/F809730D-50B5-E911-8A13-0242AC130002.root',
] )
