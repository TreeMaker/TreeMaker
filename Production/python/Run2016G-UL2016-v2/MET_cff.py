import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/133307EB-4B66-EE41-9220-7B33EA9FC523.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DCD13E76-8702-CE4D-9551-5CC942529263.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/6FFE2AA6-C1C1-744F-B3B5-8F8995EB7F92.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D08007B8-B34E-C245-A262-23BDB058E9D9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DEB4811E-BBA3-9C46-8433-33336DFB80D5.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B6156F76-62A7-474D-84FC-BFD4CF9CB05C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2D663DBE-B1CD-7546-9F4D-26F75F3B2FB3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/93DACE0D-7984-4D41-B236-83153FD53710.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/124AC531-A70F-3542-85B1-80E84345EBDE.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2E09AFBE-2403-3A4E-8F14-89F8825A7EC7.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/133DD78F-6788-1746-BCCA-5B4388C808A0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7AD719B8-D87F-5447-8D88-691B1D5EA646.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/31E16394-571F-F547-A91B-342CC0AD834B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1D21838A-A1DB-9F4A-B20D-F768ED57B5A2.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A3CFAD65-7C74-264D-9C77-C627933BABB5.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C0474933-4DD3-C54C-8154-46C5629E7A04.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/52865C2F-04C4-DD4C-A257-52FBEAB2D8E1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E0B9521D-B84F-114D-BC04-25E86EA07D17.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/042269AE-A76C-0F4D-B640-2E302DECD9AC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/CCBA566B-2765-8E46-9A88-CB6E5DAB5852.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/848E3A49-5F99-4C42-A9D1-E89076E9FB49.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DAFC2D66-59F2-174E-B5F6-1BE4C5AF5AAA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5A1A4934-2AAC-F44A-8DFF-BAAB9D5624C9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1800F409-71D4-4047-8142-4CE73B197FD4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F3CF3D81-BAA0-4C44-8BB4-7A76C638887A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/281421E4-FBBA-B74E-B0CF-84053280E23B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/6659F690-1A84-1348-ABBB-2B0A8B8E2AEB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C694A118-AED7-EA4C-BF5B-BA82513DD3E6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/544DCD4D-F81A-B243-A4DE-C44959985C58.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BFA97C20-211C-4F43-B410-E817DA1E0FE8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F3F54407-65FA-0743-9C91-4705DACB3936.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C613D8C5-A186-EC44-AA5D-D2A43ACE1F85.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5BDB68CF-A04F-524F-A0B0-A66FD8D2923E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8F9BC23F-677E-5E44-9115-9C370DD08828.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/020ADD62-87D5-4B43-BAAD-C77C83D5FF8F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/71D4F0F5-5B57-8245-93F3-1D596625B71C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D1E8F769-2A75-FE4F-B959-AF18AB7653EA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7604399A-21E0-6A46-8775-C45B59F69411.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DC3FE4F7-9126-274A-A5D6-273A2D263666.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0EA5A1C0-99CA-6349-A808-BD6EFD963273.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2548F23F-A2FE-C94E-863C-BFC67B0A69A1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D8CB6A6E-5772-044A-938E-DADDABE49C0B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/87799F39-574B-F841-9732-2C3C53BF3E07.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A79C4CE7-C598-0C49-8ABA-C8D55010B5B3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F98D5C0E-598C-6246-9AD7-80751E99087C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/89E27741-85BC-C646-ACFC-90DB7DB7DED9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3871151D-97F8-3B48-BCC2-15B456B09BA3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5F207C48-8FE7-2244-B3D4-87EDF05431F2.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DC482F66-C378-9C47-ABCD-0735B056D6B9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/11843866-5D9C-034B-8615-73B32B8FA07B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8ABA3EB1-70B6-C44B-8523-99934C59DFB1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/CB6D404B-4C52-7F43-B1CE-7BF8E020B9FA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D88A5E3C-50D3-E04B-B06B-8A58E7DA9D11.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A3805EAD-FC38-634C-A45B-5FB929E7F85D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/52D3EADC-5BB9-5B42-A631-426D82A04BF0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7FDBE07E-9302-474D-A82C-BF6AA0E5CA97.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/55DC26FB-FD17-DD47-8858-F6A667A168CF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9002F1DC-E04F-AF44-96AE-33D155FBD1C3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F142DBA1-CDC4-624A-96AD-9D0668BAAA7A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3DAB4B4D-5D55-6B42-9323-505E511B3E47.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C4326FD5-1736-B841-9CD5-6CB355BD78AF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C2608E00-7B50-6B4D-B9E2-A2DFDBA6D4DA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0C30BA00-1673-1B49-97F6-AE296B745BA1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DA941071-E3DA-F64F-B49D-26C55FE705E4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/82190F54-38CC-5A44-8B1A-61E8DA8DD46A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/08B8BA37-456F-DF4E-894D-CC00B987F0C5.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F7A8E988-C7F7-3A4C-99CF-6EEF44C194F0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3610509B-BC71-604D-A4BD-770662009B11.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/661A2F81-6183-9C45-B734-91ADA9FC20C3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/6C924FAA-8B92-4547-894F-BEC51472584E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A433CBCD-3C97-7C42-AF74-AA6482066896.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/4F2EFFBB-FA53-5E49-9ACA-5A4153CED43D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C56EADEF-16E0-A74C-AB80-BD0C2787DC04.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/6E60B9A7-861B-964F-8E24-B4BE4E27EC21.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/341920EE-8E44-8F47-AC53-62E87B952FE6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A0AA6734-7DA0-6E4D-8FE2-9168D7702A91.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E4C90547-9B5F-5947-A784-36A2DDE7C2BE.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/FBAF85BF-4C0F-264A-865F-66E478DCEAC3.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1121473F-EB4A-464D-BF6D-3AF6A08A4857.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/FC502CBF-636E-AA43-A184-78D8FAE08E7A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/35EB6BEE-C91F-7C4D-B9A4-6162043511D6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/AAA7FC30-6017-EA45-AD6B-7BC88C469AC8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F5F6B59D-34B6-D84F-92A9-C9F5FEBD2CD0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1A81A09D-6FBB-B54B-BEEE-47B300A6C397.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B6009D74-CE40-0A40-91F9-DDD3E82D5976.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/4BC45D23-17DC-D345-81DA-44A9B4BEADCF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/270000/1B9500EB-A5CA-3146-BF89-5590376AAD69.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/68BF877F-156A-9949-B205-5B103776933B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1D9AEC56-552A-0146-93DE-469107E73FEB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/99C1BBBB-856B-2C4D-9B70-2020E5B08576.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/70000/EA8BD432-AC7E-0140-BE9A-4137002D8FE2.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/68F2BF73-BA57-D44C-B5C0-3F9CB3BE1B35.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/EAB13F5E-B4F9-6846-8F21-5BD64E0DF44B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3B0157EF-3A52-5840-8CE7-E82A58DA13EA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/20A5E9D9-EDDE-C341-90E5-3E98EBB2C590.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/CEE73A2F-0957-6A40-8AFD-978D79CAB4DC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8E648950-771D-934C-BD7A-ED50A61D25EA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/52C3BBF0-6EC4-B748-B603-49731BAB7137.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/34238474-42FD-164A-9762-2AD6376AABFB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/CE161493-16F4-C442-9937-9FF363D1BAAD.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E88ABDD4-5845-5C4A-AB9B-416D44AEF34F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/25F6D828-AEA2-3A4C-B259-F1814E5265BD.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BD069362-9B51-CD45-B276-D23AD5965D25.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/239BFCD9-BB9F-7545-A561-BCC776BFD2FC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5DF1823F-C194-CB43-9CBA-7CB0EBE03667.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/ECB60FF9-3AFD-1247-89DA-389385F251DD.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/ACE4F10A-5E6F-6F48-B293-13B576162BB4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7BF64687-03A2-0348-B34C-D226B9239C35.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7503D460-3443-EB42-9B7C-4C6A6A4DB3EE.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E4D3B30A-94B5-8C48-BFC0-EC7176869107.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E94324D7-CE41-4C47-A753-62766980F3FC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/FD05048F-0ED7-5E4C-AEAA-AB3E844AA81A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/68DCBE02-EBE2-8144-8FB5-27C7F8D29365.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/272C11C4-5B31-C340-9AFA-D46F784CB7D1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B38D9234-CABA-204C-901C-6E3B427C70DD.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/99F1F6E8-07FE-CB40-A68C-2AE4F13F0E16.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/50FC3281-16B6-0C40-A125-20DCEB626BF4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/93803EB2-B26F-EB46-9D04-D3A96B77040C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1AD7498B-1DBD-4246-8218-DE6ADA16956C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9D74F615-404D-5D4B-AAAC-ED8735FB424D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C5D8C872-EBAA-0148-A9D4-5F8F69A9A25D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0313FB78-4AB7-024F-9BAF-454665B7A5FF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B9E92BF1-B95B-E046-8745-2C8A95F791F8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9278DB76-7EB1-E443-8283-6A21534618AF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0ED858A0-6342-A743-99CE-0BF2C0FDF83F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B0B0E798-3607-B048-A24B-CE78278518F9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3E0B0ABE-E4CB-9D4A-8109-D52D81FC3CB0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C5F6EE98-2FEF-A541-936E-39A27C3A8156.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/47CACEFF-2831-A84C-8800-721C4752152D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5471CA87-48AC-D745-BF86-780DAD406F7F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/58791D01-6EDD-B944-8847-3423CA021033.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2C64B0FF-54EB-A946-949F-F356EE9EDE0B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8667F8F7-2EA5-9945-862F-708918A23043.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/79A4C704-C882-F049-98E6-C3CAB766A745.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D0A55188-C27E-0346-933C-CC049E8B3899.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F2901077-8760-8A42-8619-D9E9EC45CE2B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/27537373-E8A7-2E45-9B07-A7CBEB8886C4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/6F6FDE2F-CA0D-6241-B723-81217F583018.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E9669D27-2D2D-2641-A959-A7A517C2B721.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8F91DB16-254D-0141-A1E6-2E71E74BAADA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7D39E7D7-6A6F-FE47-8F65-7233D521B8BC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/FA9AE6CB-F73B-8646-9A98-FAE41868B6B1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D1ED15EE-BC57-4643-817D-FAB521A39AD6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F17149A9-12E7-694A-BEBD-A61F9D70A231.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/4C355AEA-403D-6B48-86FD-F21BB8F2A10B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D558BC56-9704-2E4F-A03A-1FD293F2BC43.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C9853D83-0BF3-9442-860E-15B111CF7A1C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8D53EAE6-EA20-C64F-A0F1-6612011CAC6B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9E775F4C-3BFA-2142-A162-21AE25578F8F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/59282CE2-CFCE-3045-8191-CAA623E6C45A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C2F7B609-D0F7-C944-B874-520C99024A6D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/520AABEF-0906-014B-BF67-75BAFAA93093.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/444EF82B-FB5C-794F-9755-6348B462DEB7.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2CC81135-952D-7D43-849A-44B6DBF1C619.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2C13B18E-9A68-D141-8882-55527BDE3082.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9E41EAF1-E7B0-D842-BA29-384D077EA166.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/FC06A990-CED6-AD49-8B25-2D1373C83B5B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/87277827-EA59-CB46-96B9-052841A62EAE.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/76708195-D034-F341-85B4-611CE85CBE31.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1F161DFA-95B5-104E-85A4-02A8DCC82EAD.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3B3CA112-2EB1-BE41-9FCE-DAB4F65EF492.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9990751E-64FB-F64B-BF89-375FAAD8BF6E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/67DA7D8E-6E73-D843-AE24-6F18FD9B76D8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D9B95AFC-AB13-B84A-9A17-771FEC4A8DA9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BCADA9FE-62A3-004B-89FE-E728ED4BF78E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/4F351655-D843-DA4F-9948-8B2FD35D4BA2.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/8B9773CF-10FF-1942-9E4C-6934AE3535EC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/B11CF441-4D0B-434D-9B70-3B0600AB351B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BE5C6F12-FC7B-AD41-8BC5-7EB47B980EF9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D0D3CC4A-DFED-A441-B0B8-E63F4EC14272.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/09C8093F-DFE2-2E44-B489-0B867DDCFF73.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/827CF4C2-E832-0C42-95AB-4AAF68462B16.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7B44B5E9-E576-7C4E-B5F2-D520EB5E878E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/95298BC5-3C35-F34D-B04A-327780FFC52A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0A0852F2-2F52-D146-B6B1-A81866A8178C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/20325F43-63E2-7D4E-AA13-B0A22D8605A6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/EC2B36AB-7DFD-584A-B156-C4339F0B587B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3C2100D8-CB40-0E43-910E-390659449DB6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7C243517-A1BA-E145-9BA8-F6CDB200ADA4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3051306D-F38E-9A4D-8CB5-E5BDB927413C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/352EF1D8-5652-F84F-B2BA-68292545EA73.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DA4A9A89-1BE1-5E4D-9A59-F3CFD5BB28D8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/500FF45B-6BD2-1947-BD99-84D8C99A6F54.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/549E83C9-B0BC-934D-B6EC-003BD81315D0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DC53FE60-DF8D-EA46-881E-1D1BA9D40F6D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/96A0F9E3-A764-3543-AD7A-F085DF716192.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/22BBE901-E933-7C4D-B862-8B2A99522F69.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2CCDC073-CFAD-FC4E-B9F8-2C9CFC6B17AA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0E1A8650-EA73-264D-8BA5-92902470681F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9A8B697A-4F4E-8641-A35B-3E30F015C36E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/897FD7A0-CCD6-9243-AAA3-A52EBBED7D9F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F214B976-7B8E-8B46-88FD-B758328B51F8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/20E72A3D-6CC9-504B-99F5-C4A125AED2FF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5448DD80-1D06-2848-ADA6-DA98BEE98273.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/926CCC42-B342-3942-9E16-F4FFE4EA0D29.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9795F4D2-43B3-0043-BCD8-ACDCDE068479.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A4C9D238-9D8E-6849-91B3-8358A7457C5A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BFC06AE9-D91B-BA4F-AA35-C771641D5990.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/85A33FF1-D65C-254A-98FB-3B9D7A3FEF32.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/08F5FE8A-27EB-EF4B-97AF-FAA69AEF8661.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C84E66A3-5C47-5D40-9D39-9660CAE89333.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/A9892DB4-C780-BF44-A9AF-C2B92494280A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/EB05A64C-75DF-9942-AA81-9A870CF11691.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/872B229C-3497-164B-98D9-EF86F27E69C4.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5F70E7D4-EA57-7D4F-9215-34302AD06836.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1C93CF6E-1A6F-F549-B572-0AA304DB4F71.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F4C49FB1-6D22-1F4A-80CE-96F2D06D7C27.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/51008529-EAC9-3D43-99D1-D72123A4079C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/99F47C2D-75F7-C041-9D51-3D2DA1BC5D60.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E1174648-69D0-B546-9490-8E34AA0B83B5.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/75533460-7768-1B49-BA38-463E292AF36D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/075659E8-84AC-3F47-A18B-5ABCA40F8C2D.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3D888657-2519-0B41-A53F-4F3B2A66EBF0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/762E7F7D-E72B-0547-83EF-667B981187F0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/82D1A00C-67EB-8642-B1E5-7BEC6DB4762A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/CC305B22-4A36-9241-B03A-18F019E8859B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F907A28B-939F-9B44-BF32-9856D4820B6E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E5095CE1-76C3-D441-A71B-1F7CA799D720.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/84141110-1BDF-4644-8547-7AD2A14A52DB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2FCBF097-5185-C24C-BAF7-930D1C9B4AEF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/93A01271-2965-614F-9EC8-4D29707EDB2A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D5420FDB-CA3C-3844-89BE-0AD692354F6C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/BD1E2C93-7253-A84D-B6AD-5C00757A8B69.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7789EA9D-463A-484F-83A9-4D4CB4B363DB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/86D1A7BE-D576-F74E-A044-8E23B3FCC9D8.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9EFEFE2B-DF96-B640-84DE-AE80DB68857F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E66A2862-797F-0341-927B-976410DD169F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7C20DC6B-C9AE-6245-9E14-D1923CD8583F.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/92787AE0-B297-8F4C-9295-8DC21654EB89.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/35366EA6-3B59-2B45-A9CD-78CE22888B0A.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/4359034B-C02F-564F-A20F-05DC1AF851B6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E428A951-75A1-3449-88C0-7A9023C265C7.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0F2F5C58-1576-254E-8E7D-1D7C592B0BDC.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7151BC23-F18A-544C-88D7-FDADA92016FB.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/86CEDACA-F1D1-9D43-BE7F-9D4C371FE6F1.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/9BBC6FAD-36E8-CB4D-B992-855C24682BF9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/2B5D127F-28A0-E543-A386-7174F1FC699C.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/3074097C-D16F-5B47-8E75-F4ABE3719BC6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7BAC936B-B561-6B48-8F32-BFB4AFE13F5E.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F4D59759-E53A-B846-A343-D41FB49F3815.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/401760D9-3A17-FD40-8253-46052E3CD420.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/1D67DF0E-3FB9-E64B-9CB9-2D232CC2B031.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F89A8DAB-49C7-EF41-A9DC-7F551DF740DA.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/90B47A8E-3022-994A-84FD-8029802591B2.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/C253233C-C16B-E34A-9391-5651690E7010.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/E611366A-624A-1A43-934B-073F1B2A0A50.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/7F6367F2-C7D5-C345-90FD-7A5527D47B55.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/D51D46A9-1014-B944-A462-2DCEF2DBF9DF.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/EFCA5831-58E7-5C4E-A092-ECC707621597.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/5815E2A6-1130-F244-9CF4-8261B39935B6.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/F4BF5D49-E2CE-144E-AF06-69479F274CB7.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/1310000/DE23F539-4FE2-FD47-8538-6EC436B6B571.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/DC18BCF7-A869-4D48-BE62-D50669A01205.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/EAEF8EE8-CAF3-424D-8576-D1BEA9B74521.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/0438B51F-9A50-8642-9963-CDB942DD12D9.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/154D5639-79E6-914A-B36C-2EE986A9A5E0.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/A070E244-088C-F241-BAF7-17B1707FD096.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/4BF81994-E99D-2D45-8C35-E5B7BDC8BB89.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/9C668317-D15E-6349-802E-07E191108980.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/120000/0C19BE88-4DB5-4D40-AA8E-312A1F08CAC7.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/130000/ED10716D-8AF9-DA43-A815-110D277A790B.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/280000/38F0C833-45C2-BE44-88AA-5362F7620269.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/280000/29FDBDDC-96B8-1C4C-80D0-BA65ACCB9E28.root',
    '/store/data/Run2016G/MET/MINIAOD/UL2016_MiniAODv2-v2/280000/30C7E7A7-2331-284A-809B-149743BA2DF4.root',
] )