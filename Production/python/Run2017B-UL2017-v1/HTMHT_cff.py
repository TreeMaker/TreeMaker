import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/D0D51F0D-B5E6-904A-ACD1-BC9DD27D37EE.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/35301203-00C0-2442-ADDE-B849638D5DFF.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/E6C301FC-C92C-A04B-8105-DF667B483E76.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/5C764F4D-25AD-B94E-9AF3-551E5F287A04.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/39272046-6FB9-1B42-A28C-1224222280FF.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7B71AD80-8537-414E-9DF2-5CA1CDB23644.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/07299E7E-BE31-5F4D-BA8C-A282FAA03A68.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A2B2CD1D-2DDC-B944-875D-96F5CE2C9F45.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D91A2990-E03C-D649-923E-66F0A7B51A11.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/36D1B226-2ABF-0F47-AA4B-13CCE02D996F.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D7269458-04E4-EA4E-87FD-2D6866A4881A.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DF251BA7-F809-3D4B-A40A-B37ABBFF7568.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/567CB972-6494-124C-9D28-35FE9D997633.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4148702F-FEF9-A545-B416-B424C50009AE.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4AF626B4-2BB9-3F46-8493-6E25ACAD8D68.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D5F37A43-AB9F-AF49-8F47-A9787C1997F3.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/23ECB6F8-AC49-114B-AD7B-6EB6CBB46DBA.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2864444B-898E-7F48-AA61-B61A5DF24A94.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/0BCD3251-1DC7-7E4D-99DA-808DAAACD8A4.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/889EB86B-791C-A54E-97AF-C11486D22403.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4A73416F-A115-F543-A0C4-3FB09288214A.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/ECD93268-B228-FF44-A37A-E029D9CE98DF.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/FAF749AD-9E64-524B-BE3E-FAC1D9B1EE5D.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2E38FAED-90A6-1241-8A64-2C5C51AE5726.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A851675F-3C21-C54E-8591-4FF9B58308F1.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/96994800-C3DF-FC4E-8243-6A4FFFC368FD.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/701EC607-5772-8041-94B0-C007B9142BEC.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/1075577D-D32D-0C43-9008-B8F0FE2061F5.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/F5123087-E37F-654F-A131-ED68A75DBB45.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7D66DE7C-EF5F-CD4F-AC72-BE4B102FBF71.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/11C4E6A0-D8FF-BC42-86EE-B3750F8D9E88.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5011DF91-874F-6043-BF49-E3718956836A.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/18D9246B-55AB-AD42-873D-F97412D649C3.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8E54B7C3-EBC6-4243-BA47-2C7CA01CB021.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/FBEF632A-F713-E845-AEA6-C83C448B6185.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/04C158C7-FC22-8840-98C5-908076890382.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/ACB648E7-0889-1741-BB3D-3C0DF50A3CC3.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/881AF981-D0F9-6741-ACF7-FECA50BF4A61.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/ADFB4093-37AB-2342-BAEE-6D57AEC1775C.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/AA9C0123-2D73-B241-A482-52649B4B8A0D.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/77DE6CF9-47C1-8746-AD1D-753132C718F4.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/D22AFCDF-2B88-DE43-BA17-AADE5F8F5613.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/2DFD4525-E7D7-CF4B-8291-26F542DDFF59.root',
    '/store/data/Run2017B/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/0B0E7AD2-BEC7-B244-B099-8214DD5EDDD8.root',
] )