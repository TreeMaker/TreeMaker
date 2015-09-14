import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0262548C-9011-E511-BA21-002590A2CCE6.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/04B6C917-1013-E511-BAE4-0025905B8598.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/08ED2768-5F11-E511-AF3A-B8CA3A70A410.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0C92ACC1-8711-E511-9E42-002590494CB2.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0E46E69C-7B11-E511-9FC7-E41D2D08DF10.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/105AB03F-6711-E511-A07C-0025905822B6.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/16D4FEAE-8311-E511-80C1-003048FFD796.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/18E1A994-B012-E511-B655-047D7BD6DE60.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1C362CC1-C612-E511-B93E-008CFA166234.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1EE8AAC0-8611-E511-9941-003048F0EBBC.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/241032CE-7811-E511-B697-047D7BD6DEFA.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2AA0CA98-B012-E511-98D6-E41D2D08DD80.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2E07A4C3-6011-E511-9365-B8CA3A70A410.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3250D746-6711-E511-9771-0025905A48D6.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3257EFC1-8611-E511-B322-0025901D42C0.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3CDD4DE1-7811-E511-AC1C-0025907DC9D0.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3E32602F-8511-E511-BEFE-002590AC4C66.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/40AF9F2F-1013-E511-BCC5-0026189438ED.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/46FA9686-9011-E511-A048-002590A2CD68.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4819C17D-7B11-E511-8CDD-047D7BD6DD9A.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/48F249D9-5E11-E511-98DA-002590A88804.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4E302617-7911-E511-80ED-00266CFFA604.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5208E9BE-7311-E511-B56B-008CFA1979A0.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/569ECD03-8811-E511-A26C-047D7B881D88.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/58BEF561-1013-E511-8D19-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5A00AC0B-5F11-E511-ABEB-002590A371AA.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/64A32814-5F11-E511-BC26-001E67398223.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/74BEFFBE-6611-E511-88F9-0025905A60D6.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/826074F6-5F11-E511-A042-B8CA3A70B608.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/886366E2-7811-E511-A002-0025907DC9C4.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8A2061A2-5E11-E511-9707-0025B3E05BBE.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8AAEB54D-1013-E511-8441-001E673983F4.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9EDFBF0A-8811-E511-BC72-047D7BD6DD58.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9EF8923F-6711-E511-8588-002618943860.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A01920DD-7811-E511-AD5C-002590DB053C.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AEA88DDC-7811-E511-801A-00266CF327E0.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B4864003-6111-E511-B488-0025B3E05BBE.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B6EAE107-5F11-E511-8C75-001E673983A4.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C6202940-6711-E511-B076-0025905A60A0.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CAF626AB-8311-E511-9144-0025905B8596.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D23548E4-7811-E511-A9B4-002590DB9296.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D6167BC0-6611-E511-8C73-0025905A6138.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E8D66579-8711-E511-88D1-002590AC4C26.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EC7FBBEA-7711-E511-9A8B-001E675811CC.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EE6E6B2F-B412-E511-93B2-00259022516E.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EEA4A209-5F11-E511-B2D5-002590200828.root',
       '/store/mc/RunIISpring15DR74/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F058D14E-6711-E511-9BC7-0025905A6094.root' ] );


secFiles.extend( [
               ] )

