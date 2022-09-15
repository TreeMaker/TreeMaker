import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DCD49C87-724A-AD40-9CD9-EC63B163C76C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B24B698C-221F-0B4F-BFB5-C0213753B595.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/61AD1B6D-A16F-7748-8F29-001808A89397.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/44AB7754-7505-2948-92FA-ABA695513A96.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F78C494C-A913-FE4F-9E83-45E81FDCE9E1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0AC06DCA-5D8B-FD45-A3A4-9E4ECA0AE7C5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/989D29EF-6CEC-F848-B18D-9ECA193FC019.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/54850256-6DA4-6841-907C-77F1FC83DCDB.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/074550B1-BA9D-074B-AEA6-AA42B2516303.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3569DB9D-D04D-6149-AB87-A40E4CB71B9E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4590836D-A5E0-D442-96E9-445F336E27EF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E9A67A2F-729B-704A-894C-C6F80D568EB2.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A5978318-D0E6-4D46-9267-EA98AD1A45E9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5DA3FB3B-3834-174D-9101-923A3D60A26C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C74AB53F-FF1B-FB4D-BF16-F1BF101D2E37.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/95B4DF80-C266-8E42-A513-580611EB0A73.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/48C82B93-0235-7945-ADEF-73AAF13C8275.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EA113B67-E62A-5E4B-AD88-4D6504AF6EA6.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/84C2293F-38E7-A24A-B4DC-BCA3848FD04F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0A1D6326-F5A1-914C-890A-EDF1169F9F72.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AE8B549F-FCB8-C94A-98F7-4C28F02BA747.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E7B56206-457A-4F45-AF24-8E0559AE56A8.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C7DF6835-F330-BB46-B4E8-6863BFA07A11.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D420BBEF-F0DE-FB4C-881C-29B75931DB51.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A986A0B2-543C-FE4E-93DA-03EEA457F83D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/034B6535-3FD7-4B41-9A81-DCA886684632.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/87B2D4F9-9BDB-0246-AEC8-AE8F24A57233.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C9CBEDEF-327B-AD4C-A98F-55D76E8E1BB1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/395778CD-ACFC-654F-AD6B-0B84D9721FC2.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D6326E6A-C971-E548-BBDA-C70BBF1B4EAB.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E1F60387-5524-2048-BAE8-FC7A59AB02AC.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/44DD2EE4-6B56-3B4B-827D-D09109AA620B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4334D477-103B-8B47-9129-C1AA41266269.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2ED09D66-06EA-BB4A-82ED-E263D31A032B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E60924BE-119C-A447-9595-F377929C63E5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9EC34D4E-BF5B-A94E-809C-8A300D45A505.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1F78FB52-0256-2744-B502-77E5813BDBDF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5DB823E3-BD0E-AE43-B67B-3FED1B8ADAF9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/19438841-ABBC-DD4D-A61A-552992DD46DE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A9305CC4-DDEC-B044-834F-9DCDDB0F7535.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3CAF2C0D-C0D4-5C4D-B957-DB1DBE65A6D2.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6D552946-3E59-DC43-9862-0346812BA163.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/31905880-85FB-7D48-B3A8-C6C147670DBF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8B280A8E-2120-8F41-9256-3B5F0A065601.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0B7A3751-DCEA-1847-AD78-B11F1B8E7917.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/88537465-1945-BC45-B5D3-FBC458FE3018.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/19E3C1F6-5042-AB41-9FE6-400FC1A29672.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/35C05903-5F31-7E4B-9A00-BE92772F1F25.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CEB36E23-3FED-CF47-A704-5EBC8D3BD48F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DDAA1E75-BAAA-A443-959E-DC138560C9C8.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E4C2D33F-E826-DB4B-9911-326D0E7CC84A.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C7F66F3E-D950-B84C-9DE0-5A85A60CB475.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D6864759-90FD-DF42-B5F5-9138696CF80E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B939969A-1CE2-B24B-8F17-697AB17432E3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1CE12159-5B30-1A40-BEBC-6F3C25F59574.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A744868A-384B-3F43-8B6D-7437C2DA486E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/46EF43F1-F832-1943-B729-7F71364380B2.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/BB53D900-BB8B-8B47-9328-73EB6FE157D4.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D9B7ABAE-97DA-0742-A886-F11B973D5FAD.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/214A73DF-FC45-1D46-8821-EE5544414CEE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C68B3996-1BA6-3647-9BC0-886969990646.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F2EE393A-EF8B-6846-AFEB-DA7513670BA3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D98B9428-DC4C-9549-8274-2C323E9E8885.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/382DEF1F-6860-2845-98C8-56634CF81EB9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B857B35E-4A84-4E4E-AAB4-A0D2EC075F71.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C7B76F7D-B945-5448-9D41-43A59B845C22.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DAC7D60B-FFEB-4A41-932D-7946BFCC5241.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4EF46E07-EFF8-A64E-8221-FBA503FE0C67.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C0221012-92E6-5143-9B2D-47CA8064EC14.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/65D5FEBC-FD6A-014D-A00E-B943AD5EFEDF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C6E32C12-AE54-F344-8329-A60311952115.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/22E63105-14B2-A046-A9FF-DCB8E02E4E20.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EEB0943B-C5BF-1246-BC5F-76449F7FC777.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8FFAD3A1-C774-F847-B4A9-876F21A7FF6C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AE1B7627-392B-8D4B-BEA3-F8AA3AA7D313.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/56600614-6C72-CD47-AE14-A7F114FECC1C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/FDBA976C-4379-3D46-8C82-33700ECD34B5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/593E688E-7E46-0C49-AE18-9ED03FB6120E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/670B583D-5DCC-8B4F-9911-B4656CDD284F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5969F29A-DD2E-8440-A2DC-3F11BAE498CE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1534922E-0120-F843-A0A5-4C7BF15701C7.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/139EE712-6A69-DC43-9C53-7B89B4E7E582.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F7E76215-C11C-5F43-9068-7F2CDE78DC60.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E6DF9D91-CFB9-E44A-ABC8-278234148BB5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/154A3ED5-FD53-0641-A375-856C2743FCB1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A929A5E4-6F5A-A44C-A7D9-8FAE8550CA50.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C8960C6C-612E-9A46-A09D-5C902EA1B07B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/05ABCCEA-5BEB-9841-B0B2-B773EFF18D55.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4F26419D-1D19-D74F-A347-3BBDBC42E55E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D06BD05F-28BD-094A-9D5A-5C572503D83D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D238D90C-C6CC-334A-95C3-7842724D8906.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/611259E1-780C-D348-95DE-EBE6C9FB8A38.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EDA5FB2D-4C72-C64F-B46B-DD83CB808AC1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/00994DB6-8A4A-F14D-BD05-0E00B0E4DCA9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AD744BB0-C4AB-0B42-93DD-B11E95A4245F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DC7A72AE-C807-E543-8E2A-1773BB6C4A2D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7EE1E2E5-0565-7D47-9B51-46F03B338D77.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2D92A6C2-CF38-E44B-9BC7-E7D4ED44B2D1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E75C211B-7B9C-9544-9829-9DF503AB0F83.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/54E9261C-6C19-F045-A012-B1B7F320DEE1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CDAD2CEA-B799-B34A-AA49-4CBDA20D5980.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/85A824DA-C441-A544-8423-BDCEC9FF4BDF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CF543A57-C575-EC46-8560-ABDAE45FD07A.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/76ED1EEF-3532-1C46-B113-BD1888B84723.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DF5326CA-1549-A24F-AFE9-A45EF8D4D780.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D812C1C7-2E13-414E-880A-7258C782670C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D0263DB7-A5ED-774D-B7EB-314DE2FAE494.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0D985978-5D4C-EE41-AC48-E0D4F5AE3336.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/398FEFBC-074F-5D43-ADEE-CA0BE83D4DE0.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F578E7B3-68F9-C34E-B210-8FE12A444206.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F7A47B48-A45F-9D4A-BA9A-69F6B1428EA8.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/83B4A109-8D9B-F248-8AE8-B3ED96FAC262.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AA2BE900-46AF-C442-93ED-2A942D466D97.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A8943D0B-0C97-9D4B-82D0-09F4FFB3802E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3DD4631C-1988-7449-8C8A-355B3E71F596.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C13FEC09-9010-AE45-BA06-38D202037EAF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/34CFBAF5-8723-D748-BF3D-B26FA5683AFE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F4AC65B6-A7C4-FB42-91D6-691B3A724E4D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D25780AD-BDD4-9444-A607-0C50BB1B1832.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/23FE794A-6D24-754D-AA89-EF87533E4B7F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5924B044-0AB9-8C4B-B7A3-155AD87DA877.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3C0F9163-B157-5643-8A4D-797C1079B15C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/52AB906C-4BC0-774A-BB38-2C5004B7C3B4.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/67547FD0-E28A-9142-9956-D7895AB596D6.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/04313D00-BB49-DC49-95C0-B5CB89475404.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/74078D0E-E43E-B94B-8546-6DAF1D4AD7E4.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DCCD6CB4-65EB-3346-8208-645A8FA1BFFE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B036874E-FBC6-AA4B-9C25-6E0202356E0F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/580C9301-7501-F14E-A6F7-A655027D12D0.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0489706A-6AC8-FB4A-84F7-91B55E5DAA05.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/986D168E-B69D-AB4D-A4AC-ADA758326DDA.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6FC515E9-0E2D-2C4A-8ECA-EC8A7FF4BBAA.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9BBA17C8-72A9-6849-9387-2D220A217CF7.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DDD45C8A-1EF9-9E47-9365-AD1759713787.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/015EBC01-E6BB-104A-B075-82CF6CA82E85.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4FEA002C-FEEA-FD44-82B2-48F19571778B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A045D6C1-F561-3142-B7A4-89539088FF06.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0EDAE4BE-E4AE-DC4E-855F-34CC4601174E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/59DD1FDA-1AE0-6B43-A40C-338DA518CDB9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7CE170AE-3139-BE40-BEE8-AA4254B91CC8.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AE3BF64C-AE08-CC43-A740-50A0FA49F6DF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/846268C7-000F-A84A-BB57-C80E87DE189E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5E421298-7C22-8C4F-9196-A0EAC2F0DA0B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1EF53E34-E312-2649-81E4-C78D3D6F76D1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/24BC1BC2-E4C7-B345-A2CE-5D0A646C78FE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C41CB7F3-8198-E940-8B35-6F30F0F36776.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/60F4FE6C-8C6F-624D-9DA1-7E25B7DDF3AF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/83D1EF0E-9B41-874D-A09C-2D9503E5618B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D2D37B96-3D9F-C542-BD9B-A04AAD09ACE4.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9783412C-3109-7F47-8E78-17430B747612.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0927D399-C61C-4C43-B113-D17948CBBD31.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F41EC1F9-F6BC-AA4A-93CF-550CEDA3C614.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CBA3B666-7C29-504C-AB8F-198DA05B7095.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C7712652-1D9C-FC4C-B426-3ABADC3D7B6C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/34670864-7555-5C41-BA82-1082B9CE6C8B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/244C107A-F58B-C543-A509-EBD9AB19E989.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/85C8C99A-B95E-BF4D-9D7D-455D25129677.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CA83B71C-7545-C842-A175-059F7E35DFFB.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F1802BCA-BA6F-724E-8D5A-EFE417D0F117.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B3033050-A0BA-4647-84A8-9360E6FD05A3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0FA817F1-01DD-9442-BF60-E14D855CBC73.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4E4A61BA-F008-924D-B3E7-4BB5ECF9F4F3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4A23CC7C-9AE0-214D-BFA5-36808CC83344.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/437724C4-EC52-F940-B592-4B8EF64C7C6F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2113F745-7FC2-1E44-9EF6-51EBB1D4E1BC.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7F4115D2-68CE-3943-8998-42791733B4E1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B89C138B-3DDB-6C42-BA77-D8DE518DA7E3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/22778AA8-E8F5-F249-93B0-47C9E04AF64D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CC767CD6-8727-3540-9E73-F1C1806567F3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D59AA520-0560-3840-B4F5-74FDFF3149D5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C73BE91B-A5F4-234D-8545-68EBB7A0F7B6.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F4F22BF8-7F50-5248-8DC2-F6B213D4749E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/97DB03FC-E66B-C047-8509-2D21673018B1.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9051FE1A-91F3-7746-A718-C8CA2E5EBD2B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/02CD1DED-D09A-6E48-A701-97858E437D39.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/59AF4ED3-6417-EB4D-A292-977C84264C03.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/33712F3D-2C96-434B-8F56-DF172614B786.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E4B5C150-E868-A74A-A30E-CB13349B5B90.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/20ED5500-A59E-4742-9CAB-1C5405E5CA5D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/1BAD9819-E926-2145-8C1D-384FE151A4FE.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/5E667510-CADD-D94D-BD00-B9572779EF3E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/60D01A60-2ED2-2E4A-83D5-CB5C434F66F3.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/850813AC-7997-C741-909C-2F86CD731CCB.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/428EC9BE-D26F-E243-8CE8-A358C5F2493F.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/C47BBE00-15BF-D440-8890-11ECA0E78BD0.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/B0B3C32E-3AA1-184D-A7A2-22C36943B04B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/F2039DB3-3373-0C4F-80D7-671DE3A08129.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/3C9330D6-1D80-D64C-BB5E-B20AE7F0BB9A.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/05BF6C67-7F96-4347-881C-A7E17C594BAB.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/F17F226B-A2B1-0843-9745-392556946686.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/2C2D2A85-8954-684F-ADFD-EDB83209AD8B.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/270000/9152FCEC-3DF6-5340-8D48-CDB681F0E42E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/130000/E23EF0DD-D14B-1C4F-883A-C8019672E513.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/130000/9B9EFF9F-AB88-5241-88B3-01EA9B29DEF9.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/130000/E0FBE6D7-79AC-0948-8660-ADA4F8C04E7C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/130000/0B1A58B1-FB1F-6B4C-95AE-B788374CE79C.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/130000/07837D66-D5A9-CC4F-AA73-2510ADAD51F5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/2810000/208BCF12-C613-0C42-8CB3-68574720536E.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/2CA60904-BA81-EA4F-9ED5-F70FBCF05EF7.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/3B1727D3-6FAA-0C4F-BE29-563C21011EA5.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/BD2DF605-CC5D-7A41-A245-ED1C821972CF.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/2810000/90AB415F-2333-4E41-82E6-69896640FF99.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/78A23081-7A54-5742-A503-63891C3AD85D.root',
    '/store/data/Run2016C/SinglePhoton/MINIAOD/HIPM_UL2016_MiniAODv2-v2/280000/7A9C881D-E090-964A-B0DB-CBBD5181ED15.root',
] )