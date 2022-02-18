import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B2302186-92C7-C04A-9FA4-238926167565.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A6479464-BA8D-F547-A3F2-D7136B5AAA00.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/5DF23DF0-C98A-BF48-A3B2-C5A5C1E88F5E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D099FB92-3603-AC4C-A645-CAFFAEE1C811.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/451DBC1F-4DDC-0F44-B37A-77955CF20296.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/AD9C08F8-4F5F-8F4A-9168-9DB58E0BF8CA.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D76017C6-537E-D348-954D-CB6DD286AE1C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4E3C2A67-BE35-D64F-8470-67AABCFF0263.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6E4A3DA7-B3D0-514B-BE48-19945E167575.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/399FA840-DAF0-0143-920C-70B5D2EED5C1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/7A3A9D73-A457-9F43-84AC-F05A424A7285.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0A235A43-89F0-E543-88FE-432BD6374DC2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/203E86D6-3D6B-BC47-BA3D-87A39C0AF155.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/06ACF60F-EF4B-8146-BF7D-E047AAF8387A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1BCE39A7-E14D-7A49-9FEF-B6402A1E5DC6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/91B02210-63A3-BD48-9DCE-541D10EF08F3.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/9D6908AE-75E3-504D-98CD-D333D0E7E60B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/EF73B259-3D25-994E-BDCF-259BEF41005B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1DE0D1F0-4B74-2348-86C8-CAB783434E1D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/09375DB1-4B95-2B49-9097-96B398FEDEEC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B2B1BCCC-9B28-6048-B283-83A346DA9A2D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/3CBA18DC-7AF4-4544-B377-BBB5A838DE2D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/942BC0AB-19F7-9D45-A4BD-035DC763964E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/22185179-6C8E-974B-A753-1E542DAE0BE2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/9C695AA4-5B3B-AA4C-9A5E-122BABA93A92.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B7E4D63D-0911-5B43-9F4A-A92F26880813.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4BD10AAE-6AD5-994B-8D06-BF5991302919.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/7EC69B43-C868-1C40-B6BF-427454BBACCC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/DCC755E4-8FC6-364D-AB70-3587C3977F05.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A29900D3-BE0D-5348-9D61-4DEB1426C797.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1F99DB85-E137-8440-8820-37DC88060E36.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/69A6E2A1-9BD3-FC4A-8FAF-C334534B12CC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A1299456-FB2E-3D45-AAC5-FA92D102BF05.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/519B7CE4-52E7-5A42-BAE2-5635BD4AFDA1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/2EB10A30-7DF7-7940-ADF1-AC07EC2B3FA9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/15CC3679-5FCE-FF41-B211-295D171896D4.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/960D39A2-2851-0344-A4CA-78A1BFD872CC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/610CE5CD-AB75-3B45-9B6B-8DEF79417CD7.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/611C0573-30CC-3D46-904D-D4451D036307.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/40624F70-C52B-8E45-8338-7B45B202109B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/BA697F77-B9F9-6E41-A3AF-0A94F9A2E654.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4EAAE857-7149-C944-8D04-753CA2BD28D6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/E3AC3624-37D9-E241-B765-74345A30553F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B161A838-C1AF-F14C-877B-7753D28BD883.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B0260854-EBF4-F642-9045-6BB3C8B58D1D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/AA9CB00F-5C92-9C48-9233-0A1C53EAE212.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/8C8DF7B9-FD17-5B43-ACDD-DA534DB06B2B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/7BF4FB1F-8FB4-5046-A98D-3A706298FD67.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/501AF2C3-596B-5947-AADC-F91C69E1C49F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C5700782-9051-2B45-9C51-49E531FDF2F8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/15E78878-E706-B34E-BD5D-012066F6B477.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/BF4ED21C-4D65-D540-AF2F-BC79C1A850EB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/64E75AB1-554A-ED4C-A076-AC5FCDC3091C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/854853A4-5363-4343-851A-26732ADE9C07.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C6D206A6-C116-1D43-98E6-169898AC9973.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/754D1558-A4BF-A74A-880A-CEE7F65D94EF.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C80443E5-4570-D84B-BD79-78EC255AB2E5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/22BAD115-1D0C-D945-A0D8-9F43C68F1F33.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/91308BD3-4DD3-AA4B-9091-610637ECC7D9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/F23E9510-66CB-5346-AB65-2BE1A19E802D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/606744BA-ECED-F444-BAFC-E5364325146B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/517A286B-FC66-544C-A76A-5B507C21B777.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1C4E4323-C1F3-844C-8A4F-6A1046B43F1B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/74145990-085A-C54B-9C75-D70962572B9C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B171D415-2280-E84E-99B6-7F0A9E90E303.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/983456AC-E11C-2B4F-A232-430B87399FAA.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/CB23ADF5-6BF9-4047-8A74-E901C1B9D217.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B702E2A3-74DF-2B42-8A43-C2DB8B38F871.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/53767A8B-F8A5-D940-88D6-3A27D4767F78.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1FE256AC-4F26-3744-A09B-6C2DA4EF257B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/11D20356-B1AB-CA4A-A789-B137DBF6F942.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0BFBA09D-9CCF-534D-8F46-904F06EA42CB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4FCFF914-3996-534D-A197-B005D95A9065.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/38432B60-73AA-3D4E-865A-3D86416DCB90.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/5C76DC07-BF01-ED42-B364-67ACF00A4131.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0E31589C-7B58-B748-A895-25105A26D10C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/F68948CC-C20C-2F44-B178-3DD2BC7FF307.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/32F181D9-94A1-6F43-95B5-A515229D3A7F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B825683F-19F9-BF49-B29D-3965CE99803C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/21986164-CCFE-7342-90DA-50EDA34E965F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6EC3C570-624C-8B4B-A719-82928BC223AF.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/637A0CB4-DDFD-9642-999C-2C8FC82DDC15.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/12A49B1B-3A06-2A42-85A7-EB528FEF0758.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A23DC474-361A-8541-B16E-A276FC61290B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/41D0129B-4441-D64A-885B-F11E61244B0D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/78611D6C-D8FC-2747-8D71-5958AA712054.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/537AD47D-6BB9-1940-B9C6-8DF9978E92A9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/84CB18F6-8FBB-294B-B5C4-09FD2BEE5A1E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/949F825F-E079-7A4B-9DA6-BC99A40F27BE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/CD9433BA-CBD4-E149-B60E-2AC6A4C25175.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/F28B973B-F6AA-494C-8BD2-FAEB2BCD4D2C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/67B3BE0E-5098-CA4C-AE98-20293D46E1C2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/58FCCA79-8224-254C-8201-4D76E3DEF7A2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/BA18204E-948E-8840-AEE0-EC2D19961DFE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/BEF36D0E-01A4-E147-B6DC-8406AD4286B7.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/93F95EB4-124A-2D4C-B63D-581786C1DE7E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/A3FA7211-B1B0-EC47-A24E-194CB3BABDB1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/A3A16622-0307-B147-BD98-82564D5D0FFB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/ABC03F0B-AC69-B448-8CA5-2E5722A7ACAE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/48A9AEA8-F9A0-2342-B407-897EBD378A9E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/EF42A9D5-2817-DB4A-8718-7305DBC1FC38.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/2E2CC677-21BA-4A4C-B5FB-881A91E02BC1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/DFC39510-4030-8A4C-85F8-2CE338AAC06F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/270000/A952B6EB-A73C-D944-A472-9E49E3864CA1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/EBB48D65-6036-AE45-9F45-3ED663CA35C8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D980DBA8-72EA-AB41-BDE2-B875D029BBD5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/7735E8D2-82F0-C845-9F9A-02D8743CF361.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/69E27B85-15F9-2143-9D94-F75D75AF061D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/2E0CA879-D230-4A40-82CF-64A1D07DACD0.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/E62BBD64-76CE-4649-B736-7D191C57E5ED.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D07631C9-6CDF-1645-BE20-03F3EAA7F01D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/84E8C7B7-9F67-0C42-8F9B-EE3F422A4026.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/807D2F77-7C59-7B42-80A7-5B578941B98E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D1AE9331-33B0-5643-8182-78AEC2EC6E94.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/429C2B1B-62B2-F149-8FDF-83A903C1EFA9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/48C52DF0-288D-6A43-BC7B-161801A1F573.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C18438C4-B8D9-5B43-82CD-5D0B66F50F3A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/37B99C20-A274-F644-85D2-CF1E4CDEDED9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/DAF82538-54B7-7B47-A386-EE393D9794C0.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4AB50B19-56FF-F04C-BA70-6C10364EE3A8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C604C5F9-1522-3245-B92E-EC54B6D4BA11.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/03AF436D-BC71-CA43-AC1F-A2C23FA72BA6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0ACB5BC2-8622-2E40-9A3B-510309453783.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/540DDDA1-2ABF-AC44-B77A-D735F3869322.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/2070C292-9631-F341-85E1-38EC948D8EB4.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4AF2078E-909D-DA45-BF39-14A14562415D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/ABDD1169-E717-B64F-9908-BF4EF9F8D3E7.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1A7935FC-0D21-5C43-B8AF-831F992AEC18.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/AA70784A-788F-6344-BCC6-1D1C1E5FC11A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/3A185387-CFF5-AE47-A011-41335B172B85.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/9D0B89D8-E27D-F34F-A9BB-E50DAC85420B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/389BDDE5-C5C8-C94D-9D79-F4CB23386EA4.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/9DAD8E49-222C-824C-8D87-FEDEB63176E3.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A0A45C65-0079-6B45-8211-C7136D2F1D03.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1298DE4E-1D0B-CA44-A3ED-B6149982DAA0.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/FE742E7F-9690-2746-8797-48314E762BA5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/666A7226-E680-604F-AA0A-79F404A36CE1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/F7BE660C-68B4-D443-A51D-B224629DC358.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6161D8DE-2A74-9D44-8486-C29094A8FB22.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/022F7120-B20E-2844-9A1B-114717F0DC97.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/29A9A7EF-A08B-1242-8535-A29F0D882A6B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/7CFE9756-7D29-F447-8D95-9B7AC922AAD0.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/FE98821F-466B-B942-B799-5A3BF3AE1822.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/FB190751-A2A3-8040-AC89-4E0A009F921E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/10717720-C4C3-BA40-9F82-ABD11F74532C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/94787FA7-17A3-5340-9ED8-BB1E561C4522.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/B08BB900-F104-CC4D-B1B4-8FD0610A1421.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/07E11D81-8DA2-884A-925D-6FE29A67FA6A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A47D7DEB-2C56-E349-8D6A-B956C8EE006F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/DD3EA6B5-91AF-1340-A3E6-9FA505F18031.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0B27E0A5-325A-F345-9CE4-30977ECCA68C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1BA995A1-71A1-5949-81F4-A4A1FFF889B5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/1BEFF8A3-958F-634F-BEB6-5E3C28DD4C47.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/675A97A1-DA4F-1548-947E-6FEBC67AF108.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/3E593A67-57AC-024B-A225-5391995052CF.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D9D30646-0DD4-874D-9CB6-693EE4E7BFF5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6D072A35-8BFB-A342-BB7C-B0223AD41CE6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6B913825-95A5-2440-B927-C2FA3B5AFCBA.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/2F5FEDEA-9C36-3746-A5AD-4852DD2EF354.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/672E5802-D76E-6141-BFA9-657AA6B97774.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/26CEC64B-5AB3-1042-A19D-40E56D20CBD9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/4671F25D-C59A-0F4D-B1D0-EC9DA88EF5B2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0C4B3ECE-5264-5F47-A795-646EE1D2A57E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/FFB6D22A-B65A-7943-9A32-4DFA42E52BEE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6D10F2CA-394E-D84F-A7AB-3FAC3F778014.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/0ADD115A-3031-964E-83F5-C84DF678BBF3.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/5B24ADA1-17E4-3F49-9651-4BD06DD24BCA.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6D7C40C4-7944-1146-9696-C8DC0406E19D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/6C6777AE-49E1-A14E-A5C1-BB28FE8A000E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/ABA9533B-E59B-D048-9F35-1016A406FD14.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/E74EB693-502F-9643-AA34-49AA69545617.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/F287DC23-083C-A845-BE40-21F516E37825.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A7B2458D-52C2-C04C-A05B-57023023201F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/C11F4604-C40E-274D-BF55-9549EB059AC9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/0D0C2D78-732D-4749-B2B7-2DFFFA3213FC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/A211FFDE-4E7E-B141-A9E7-5E0E6354BF9E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/8D164C54-8C67-E748-8DFE-4441E8B94DAD.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/E7DAFFC6-0A37-D440-B474-28F259116817.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C7CBB1D9-AA85-8742-8F67-F9C3255DDB85.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/3B305C1F-4F9F-8C44-A8C7-A7E38D3AF488.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/A788C693-5321-274A-BE58-59BACCB40EC9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/2ACD89A7-FD21-EC47-ADE5-B1740338C750.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/B09E2C18-E43D-4D46-BAFD-EB5731C62CA3.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/CDD15965-C7CB-934D-9EF3-2D08FA2B2C79.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/DF47FA5F-9439-6847-B4D4-9E3C4DA1BFF2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/A98272E7-E5F0-5041-AA3E-33712992CEA8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/184B9F23-6ACA-2A4E-ADF1-B47059B56DCA.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/DF782F3C-0C9F-184C-B6A9-EC2A3CD64B74.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/865FCF07-5DAC-9246-897B-3A21B9CC9E80.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/5EB916CC-AAD5-C549-9901-E1E118D9ECD5.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/C8A95CBC-D74D-A442-8FC0-49E6A9AC2E8B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/EF033F61-F51D-2849-80D6-C0FC1DEB370E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/64DFD7DF-5186-A74B-A4BA-E3755C52D9F9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/79012E53-41BA-E248-BA0F-F0D86A779DE1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/0FCD4BC9-C6F3-E14B-B388-5421CDC05A0B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/450EA67A-123D-2840-974B-0333BED7F86B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/CECF7BED-318E-F042-B91B-0A9A7CF1C61F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/A4DFC8DE-72C6-EC4F-9001-98224FA2CD94.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/8FEE3DC5-A20E-2643-9804-0A93719C0B5E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/FA0CABE3-963D-1442-A3C6-F64AD6B8462B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/985161BC-B006-154C-82C2-6D33D2AC490E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/F8987D4F-7ABD-B046-8814-FDAB7E6B9BE4.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/280000/61E9AC50-6001-6D4B-A631-567C4ACE03FC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/E9801F2E-DECE-E74A-91EE-3013B9650FCF.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/756ACE4E-8A26-F443-A2E4-95708BC52D33.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/D1C182A8-C970-9F47-A24D-6DAF8F27D20B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/31D4C746-398E-AD45-8AB4-F3433CEA1078.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C266B95A-CEBD-714B-8241-E693093B0D24.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/17C94DE8-E32C-9D4C-8525-CC2B869DC764.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/C891BB08-BD47-0F43-9534-1E8343D308A2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/03E372A2-2E9F-C540-A2E8-5BE83B85E0A9.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/001F4550-2BF1-DB4E-A2B3-0566958009EB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/8F17C05F-51C3-9442-B85F-CF7C7EC18D7A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/120000/CE61C4C0-83CE-7849-B719-F6228C020839.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/E4E62ED8-3F87-A74A-A036-F7E6243CDC20.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/9369D594-C417-6B4E-8140-3AB0D4B14EA7.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/EB3220F4-B87B-8B44-9353-102411367111.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/5633332E-E936-EA45-B11D-1D759CA20EB2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/51841A87-337C-BE41-AB25-88A7241E333A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/BD1CBC94-9BC2-E94B-BDAE-CE38AD1A55CC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/1CCB3135-92CB-C445-8640-6FE7148BCC6C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/D6DBA1D4-21CE-0E41-A485-E8F75341D53C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/A3953725-2EBA-664D-8B7B-0F937CE1C002.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/38D46214-AF57-6845-9CD2-A9B88FDFDE60.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/B0D00828-6C95-FF40-9CBA-85DB7A256E68.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/48E08BBA-6B4A-1C4E-AF50-9FA7C7FA0BC7.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/0F20C1CF-DEAF-FF4D-B465-40436AF9D081.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/EF57D5A7-38D7-3845-A057-A6018E8DF1F6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/947F8DD5-40A3-FB42-84E7-51DBEF68244E.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/7B1DC4FE-B960-3448-A949-6F0BF72BA242.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/7E725348-672B-E840-9957-71B448F1ACCB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/49E6F6A6-03FD-3148-BA8A-B35C5C56FFDF.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/18A6517F-7083-7643-8365-EB716F756114.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/94E0E16E-71BD-1E49-81C7-A5A19FBFB7DE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/E0C302A6-639A-B74B-A510-425741CFE3C6.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/51FE5BB3-F3B2-7D46-8FF5-F99D06DAD740.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/1CEB9D8D-D54F-FF45-9E91-46912CB63872.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/4CB118ED-DA17-3D48-94D8-71FD08E5E580.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/8565A67D-2B72-964D-B7E6-35D8A6BA1C66.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/81CC7917-604E-9143-8435-6F1E4BAE141C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/480E7345-7EA6-A244-8143-EE4EC693297D.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/990FF364-062C-DF4C-99F2-A50DAE11F8DE.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/773548F7-A600-184E-A1C8-8E50FC5A471A.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/2E0F92F0-465C-9443-B9E9-F07348434FCC.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/B624E791-D34E-634A-A23D-9736C8C9FDE8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/4DDEB89B-25DA-8448-80A0-A809DD1FA5B1.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/20F4A9CE-A61B-4544-A0FA-8A8EAE17005C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/11FE734F-2932-614E-A635-2EB082BA95F8.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/2A3F056C-DA0F-8243-86ED-E7DD9989896F.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/3B039B00-F49F-934B-80B1-D2D3DA216367.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/81524308-7185-CF4F-A80B-5C133A67E5D2.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/6FE6260F-A6B2-774B-9EA1-F8D4976A0D86.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/6F3A7FAA-3C8D-6B47-9D1B-66C478A2568C.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/17B951E1-00F0-3742-8F3A-CEB5F5102979.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/D47477B8-D020-B948-8DF3-1DBD1BCC6DFB.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/AAA76056-EAF0-CE48-B7E7-A57228124F63.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/9413ECDE-7A18-4349-8A95-BA2FF556DA76.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/4F196D9E-2282-6F4A-B65E-53F0209D54C0.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/EAA93A4A-50D0-D04C-932E-F394D2702183.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/33E65BCD-7E6A-1246-9692-E560C79EA81B.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/F31BB86D-AB3C-E248-A51D-12D891C51A70.root',
    '/store/data/Run2016E/HTMHT/MINIAOD/HIPM_UL2016_MiniAODv2-v1/70000/6C838E8C-B681-984D-89B2-5E980DAC12AF.root',
] )