import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/06DE2F38-7A84-464C-B848-9FB10B6011BC.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/0ED1A35B-6CE5-8C40-ACC1-6872C896728E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/27D847BF-9153-5848-B91D-A2AB1ACC8DE7.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/34AC1789-F1DD-6D46-854C-D729619337AB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/3B9F14EC-F403-D44F-A419-D056DE28AA44.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/419DA2F7-EF73-0943-B4F2-C122668A9CE7.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/42789F6E-EE69-5641-97BC-ABBA4BA7F289.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/4310F268-6DBE-004E-A398-AF9CF4270624.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/4979D40F-F5AF-3842-BD38-C90FC3E57E0E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/4A75C331-0536-AD46-9405-B2F8A51D8B45.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/4D665993-3156-8D4B-B618-2F3A97476480.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/5120C45C-52B8-A147-9DBB-BDB74B307407.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/5DA20679-7E63-7940-B375-55102B5EB940.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/5E67431B-408F-0E4F-9C64-1CD3BDC2CA86.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/5F51A88D-094A-BB41-A500-784CA9CEF545.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/6BF0528D-706C-4846-A90A-B5A6E4658476.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/6C7983FE-F6F5-1B44-A055-0E8BAD567720.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/7E28B812-D8CE-6B4D-822F-14F08585A63A.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/8A0BA392-07B5-5345-98DB-CCDD36F69512.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/953105D0-1768-A344-97FE-AD7B0071EEC6.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/9F89D028-BE80-CC45-BDE8-19BB1DED614D.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/A93740E5-9E37-5B47-AE85-4B90984A5C49.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/AA2E44B4-C079-794C-B291-A6DCB96073DB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/AE1578DA-8623-0D46-A262-1E5967421A67.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/B2A82E30-C9B5-F144-AC21-52F2D95CB349.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/BD0C9017-1031-1146-BA9D-C40B42E35B0E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/CF0C8048-2922-6E45-8581-760B4D466F59.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/E2C8E130-5AF1-9E4D-96CB-D2DEA9AEB049.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/E54664B6-C321-FC40-81D6-7BBFD9EC2293.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/00000/F1A279CF-A949-9F4B-AD14-5359C876A832.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/1010000/2A23A601-EFBC-8A43-AA93-74F7C4450487.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/00B49798-7C6F-914F-A134-72AF0EA3FA31.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/061D1B04-660C-1543-83BC-1877503ED049.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/0D93C190-0C04-C748-B6EE-A5E010D75F52.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/1DF37783-85CC-C04D-9830-46BAE54A162E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/24B14CCB-6BCB-0340-8CF6-B23EF171D35B.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/2FEBD581-96E0-BB49-B373-0DB7BAA1EAB5.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/3236074B-395F-754C-A338-36FA18D95ADB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/339EB96B-8F17-F840-84EA-A0779BB6F9E1.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/33FBAE15-F265-E14D-9A80-EF1AE9558090.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/3D4FDF83-8826-8543-B948-7EDDDDF6A6C7.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/4E7E876E-0784-EA4F-83CD-3F01AD33E059.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/53BAC944-1354-2E4D-9CFD-C1D97CE97F23.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/558429BD-1B98-624C-9A8A-CFFEE95A9A28.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/56C902A2-0CF3-6E41-A44D-7B34D3C50A99.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/58162E37-3375-674C-9CB5-E31A811F8AD1.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/5DAA0712-52C4-2F4A-845A-DB7BE7C2DFCE.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/61B26265-0B6C-5444-A0FE-E701DC02E342.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/74429ECD-3466-0649-85A1-4EC4D184501E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/77CB82CD-233E-2E42-9B98-288713D26CBB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/8A4CD7A4-91D8-C346-8A3E-4FA7C9ADE9C4.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/8A81CCCF-F667-F142-9393-052EFAA207A8.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/957958F2-C33B-DF43-95D8-18E7199EFCEA.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/986A0DE1-5A90-E542-989B-06E4F1FEAE89.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/A8A62561-ED79-554A-91AB-9EF6A8041D2B.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/B1B24D5C-F683-5A49-8201-8F6E97C300FB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/B62B7F26-DAF2-D344-8282-5F6B125FD473.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/BF538AD1-33D0-984A-B7A5-D9BCF986907F.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/CF6CD029-DEB2-294C-B93B-F303249E7827.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/CF6DC876-41E7-394E-8754-69EF99D887BC.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/D532BE62-5A4E-9648-8D16-12E4F88D97F7.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/D7CFF4A3-639B-6447-8327-B24ECEF72517.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/EA2324B9-6E38-0848-8DC2-470D6598A67B.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/ECFEA9D4-594E-CB47-9A07-15EFE2864987.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/ED4234E4-9B74-D648-B429-1A9A6E843F81.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/EDDB6230-E161-1545-AFB4-DC436B66CBED.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/F92F9606-6B39-2240-9F60-813CE386D1B1.root',
       '/store/data/Run2018B/JetHT/MINIAOD/26Sep2018-v1/120000/FEB926C5-5F1A-3144-BF15-E6D8980EC219.root',
] )
