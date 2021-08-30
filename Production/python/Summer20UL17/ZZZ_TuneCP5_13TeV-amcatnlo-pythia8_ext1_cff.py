import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/050D8276-1D9C-E54B-9B78-0C96B079CCB4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/06A3AFCE-A31D-0B42-8F02-9E9C27E55EE2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/076CA00A-263B-ED41-AC07-1A18476EB548.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/0A737881-DD41-A441-A217-45627D114ECF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/0CB7EB5A-5821-C04D-BE3C-4470A87F58B6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/0D40E7C0-105B-494D-BD3D-AD1B8E388D74.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/0E594E60-8BC9-B949-951A-E6BFC5169E07.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/0F8C043D-A50E-EF41-8885-64A46D9F56F4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/10D4E6D1-587B-9443-8424-5817E6889B92.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/12C7BCBD-B853-0A43-88F9-84B8E47654BE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/1DE0B627-2367-2F4A-8D08-4CDC5D16DEC5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/1EB07697-93E0-8C40-A270-A1A997A5E222.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/21AAFFB3-7F12-E44C-BA36-56DBC04D9360.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/27A794EC-C555-1B46-81E6-B1C0C4D1E364.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/291F9F7B-C18A-AA47-970A-7AD6F35301E1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3015B2DE-BDAF-7948-A054-05EB4E02A4B1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/340089ED-E0C9-F648-8CE2-FF21A8953CEB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/37C45468-876A-D64A-9E2B-CD3384B3A824.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3B27BEBB-4024-444C-8B3E-A90A6AAE694C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3C02E0B0-782A-0442-BAD1-37C3B2610A30.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3C47C093-A948-2646-8722-30A299430299.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3DF90551-4393-4241-8D7A-D10894E5875F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/3E2EA3F6-C2D6-3B49-9F06-B28595A32FAE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/415596C5-C8AC-6A45-976E-5B4C88B71FBC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/41DB15B2-9106-C547-B8F9-07310F762000.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/4251CAAA-5EF6-E548-9EA6-23147B3FFA97.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/438E92FF-829E-0F45-BC5C-D954C129031D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/45DED96C-CA83-FE47-A373-424EA0D15084.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/4633C946-545E-1646-9B60-A742AA84C36F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/4810E5F0-A10A-FB44-8DC6-D53F545E3980.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/490A8F80-3748-104C-A327-08E5F91F3CC8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/49409AED-E406-E543-8D39-2D64A2DB035B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/4AAAC47B-8E92-8D49-855F-BCBF71BB90C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/4C177D48-08DE-1D4D-AEDC-0FA6F4AA9F4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/5217F941-D1DF-1C43-8423-664F4CED9B20.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/53C027AA-FFD1-3E4E-BBB5-CE07D10CF427.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/5806642F-B231-C244-92D2-8CFA92027F8B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/581B026D-534E-034E-BEE6-D66745B828BB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/59A6EB68-C449-5D49-B4B4-253B39B160C2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/5A7290F2-F272-F848-9D84-51983A83703B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/5C3379F7-4FB2-D748-AF69-F0312CD34133.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/61AA3DB1-FC93-3348-8F10-0BAC0313775E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/64623035-1E1D-E348-AB1D-9E05C98B3DAF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/652FAF2E-0A65-D344-8463-722EACFA0E2A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/6DFFD350-8DF7-A646-81F7-8E6C8B168458.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/6ED41114-4FCB-584C-8FD7-BDF27BCDEAC9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/6FA01EB5-791E-124C-9513-15ADD1B288DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/736B86EC-CA08-3849-92F2-FA7C69D88870.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/747083FD-F5B7-074B-8919-8CFCEF376F43.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/74ED7969-D109-404B-BD36-EC2FCEC90269.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/7503F7BF-75F9-BE46-83DC-AD3A57A48E4D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/7538A7F8-BA7B-5148-B6E1-05AC6AB01AD6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/75EE4FBF-C795-B141-929C-A4DA8CEADFD4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/76464149-1A27-F243-82AC-1BFE8B416844.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/7A898903-3CEA-5849-A0DA-4EA5A674E753.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/7BC3A79B-9CE9-3F47-8106-8F75F68B49E5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/7CEE9513-E1C0-264A-8FA7-4AD67AA4AAAA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/8007FCD6-3FAD-0C41-A6AA-D3034D93C9F6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/876F711D-1DA1-204B-A219-E9D2276E3299.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/88A5AA71-71FB-8D40-B467-A2E62CBE6242.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/8B5E3442-2A0A-2942-B443-2C4742674B04.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/8D231B23-2330-214B-B56C-EECB5EB5A25F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/9052D694-BCF4-8B45-9998-BDA5AF572BD0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/91CC45DE-9035-3B45-BAE5-190400D8A25A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/92350777-9707-4746-B5A5-1D0B87EAAF1A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/93462E57-42D9-5E4C-87A3-F06E9B90D9F0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/93FBDC13-EF25-BE40-8B26-04E92731BDA7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/98424F5A-7499-7148-BB4A-3758A05A05E0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/9932826F-171F-3940-A39B-6EDDC85A3FC6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/9B738C9D-B186-2348-A9F5-F2E5299525D7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/9D2583DB-982B-C549-A153-93015659F6B2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/A008A192-03DF-1A43-A6B0-68238CE27E3D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/A1FC3674-1EF7-744E-B05C-7C0ADFB1EE12.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/A509EBFC-4C85-AF48-97DC-204300B63EA4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/A7BA8EC6-8309-4347-A430-BA412417E0FC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/AC87E655-643F-294A-8E82-5122A4762781.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/AD3B0251-9CFC-134E-AC7E-AC1F40BD6127.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B0A80660-F4CF-B541-A187-9FB5523E1513.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B3140CED-D469-2048-949A-E81967B100C9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B400E923-5F91-A649-B948-72A80D7F7A08.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B7B08551-68C2-1643-9B28-CEA77489B66B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B7C1704B-C932-214A-AF9B-0D90A291F95C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/B943961F-0217-A849-93E0-EC11EF5923F1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/BA3BD63F-371E-ED4F-A26E-9A96D763C31A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/C32153F4-DCB4-6846-8F3A-279DDCF6B95E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/C42C6921-3843-694A-928C-400690BF6AEB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/C71B795C-AABF-0248-9AB4-8E96D4D88D76.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D04C7CAD-8E71-B644-ABDE-AE93A6CE133E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D1BBAAF5-BA62-CC46-B3F9-F27BDA792387.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D3460B28-DAD4-B64F-950B-6C4FBEF538B4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D5FDB052-EEF7-2140-A2EE-6F3BE1EA327A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D87A70EF-7764-DA40-8310-E2DC6050C8B8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D918FA20-DD60-8247-AD8A-D553B5C9ED2D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/D9623578-D42B-6F41-81D8-F9A1E4132673.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/DAA8F9FD-755B-C145-8C0A-192491712C13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/DC271221-5ED9-4E4C-9C95-45B4D8D588BF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/DE20AFAE-9819-0E48-AE0C-FB1B63334B6F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/DF29CB6B-87A4-C74F-BAF3-2464CEC8D4D9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E0C65329-46C9-3040-80C7-B6355980BD5F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E167BA9F-9567-2149-8E02-099B74EBAFBA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E37CBF74-89AC-414F-A1BB-FEFCA0253714.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E42BC0D8-D9DF-B24F-842A-056352B2A2BE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E432721B-E080-9D44-8CF8-0D590DB6706D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E4D6C228-AD33-864F-B082-64CD6D88D5E7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E680691C-45AF-E347-8618-A938C69BFB09.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/E8A161DC-3534-6646-8445-1B8945D75484.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/EAB3433E-89D4-F142-A4D0-571E4CAD862D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/EC1BD1DA-F357-5B41-BA50-3BCE2CDDC54A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/EE8755A2-B0BA-764C-A907-503F8C7D7E9D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F0B283B6-6857-8046-822A-81A411DF7F3D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F1526181-38AD-C443-9C0B-1C4E60623085.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F165DD0A-AB56-DD45-B3B9-223A100C3B6E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F3B3FE58-20B1-A14C-954B-8C2E43840EAD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F483260E-5660-D14C-838D-7DA87BB0E6B4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F72D5D1A-AAB2-2F4F-A658-EACAF56200F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/F8E4B392-9B39-E547-8971-653C89F78F19.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/FDDD7135-45BA-F343-AEAF-37A89F7DE818.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/FF3B62CE-C240-1F48-9E28-D34D61BBB47E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/FFB2FC6D-5FF0-EE4C-AAB4-04EBB6136A8A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/270000/FFBBFE6D-01B3-AF42-878C-33438ACB5374.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/0034859D-85F7-0145-8171-F49941F88525.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/028B04C8-8DA3-0C4C-A6D0-290D8243CDD3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/06D18601-F822-4F46-896C-046E3767059C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/0869F21D-7575-C347-BC5D-F8854ACE8523.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/090416B5-B86E-274B-9ED4-9B5DE0E86AD6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/09F58CF7-2E89-2E4C-9841-C8D501BED5D0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/0A20B6D7-DAD0-4B4B-B436-0058F0D6B6B1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/0F244C27-3689-AF49-82A3-49F45C1A446B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/13562E4B-19E3-084A-88B2-198DE919338E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/16D054E0-327A-024A-BCFE-7C2AB513DC4C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/171BD925-AFA4-B24C-82F2-4A48101DF971.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/1777311F-389C-AD4C-AFAA-A87EC1817903.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/1C88406E-5B59-8747-AD88-980841673247.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/1CA5626B-CC48-3D48-9648-97FFA67D66DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/1D97A5FE-B571-474B-BB2C-8DAB34819990.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/1E2D2955-A0D9-044B-8473-A502D0BBBCC7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/235BA02C-03E3-C54B-93B2-E7C5EB479E77.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/23C1E21F-9AF0-784C-AC39-99C41AC6579F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/248F96B8-AFBC-9A40-9869-AC1A6303B3CE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/28C54A72-9E73-0648-BB2D-8309F9A83101.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/2B4CB71F-BB4D-604C-9EEC-29A6EB83242B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/2D442AB3-F631-274A-9F72-1BD1905329B3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/312DD237-FB6E-4A4F-AE37-C5A3B338AB63.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/324DD44C-66D9-3747-A1EA-F66C86D83165.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/3AF53393-E89A-D94A-85A5-21A73BAD6775.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/3BD509EA-88A7-3749-95B1-47BE6508A0FD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/3CD813C1-50DD-C14C-BD79-8748A1908A80.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/3F920423-1BF0-3E4D-B8D2-28EAFFF721BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/47C780F1-FFAF-8C4A-9DBA-82D2CBEFE48C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/4813A7F0-9B96-3842-A9D4-9DE8D3F305D3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/48A4F204-EF49-F943-8727-5FB785B22088.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/4B03C299-4B70-014F-8AE7-70A7E7CE4344.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/4C98B229-57A9-8E46-9C77-83D9FB96AE70.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/4DD7E4E5-F413-CC48-BF3E-0779388E3EB0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/4F208AD7-7B44-024C-9F9D-A277D4711723.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/532393EA-DDBC-B548-A878-15F1B175A0DB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/5639B4F7-3FD6-6648-BDC7-854E5E179DC7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/57F37123-DBFF-1C45-B479-C0B1DD491D13.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/5C021A53-67A5-6F4A-9FD0-4C21090D0F8A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/5F256F1C-CE97-8C41-822D-4C06CEC0C5C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/608F2DAA-933E-6C41-9A32-D3569D11EC74.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/66A5F851-2A8B-404F-837C-C593FF551CE0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/6785AB0C-B942-0245-BC48-650034837567.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/68A62554-5F9D-7844-AD63-353BD9019CF7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/6BA8C3BA-85B6-134D-A2E4-C53879F87907.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/6EBA3AC1-3D7B-FE4D-A126-F8CE59216A64.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/6FFA4E40-C073-C347-9653-5358F4A896CF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/714CE25C-8FFE-CB4B-8D9D-945B88872665.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/72D902F2-5255-CE47-8B0E-092A93448A6F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/754B74BD-1684-354C-BB10-28603E02F38B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/75F9F04A-0187-314A-9F2F-92A030DCB3A9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/7705877A-4E9D-6547-B4C2-294B2E39991F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/78DD18E5-E593-CE47-9C1B-3CE6131DA6C9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/7D848BD1-FBB1-9C41-BCA1-A5E3FD458243.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/8733032D-A96C-C341-BC37-D839C6B44DA2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/8AA10EAB-323D-0B44-98C5-9D701C6D4E5E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/8DC8D33E-5953-774C-A54C-67B58006BEFE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/8FF90BBC-4794-7747-929E-EE2193628822.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/91566890-97D3-C54F-82B9-ECECC135F370.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/9810C4E3-D3AA-DB4E-A214-FB0FBCDA3707.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/987FD9D6-C81B-DE40-A9EB-283101EC97B5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/9CD73505-17A4-474E-AC17-36570628DFD6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/9EF6F181-2757-6740-8858-A4D7DF9DD6B5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/9F01B464-3DF7-2540-8B68-4F5B103FD2CA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/A0AC4D8A-FFF4-AA4A-94C4-5B7FA59DA639.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/A1442859-BAEF-C94E-91A9-AE4E61C2B7AD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/A225E108-8D1D-5E49-A607-195EBC4674ED.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/A2ED6CD0-4D8F-6A44-B137-5D1F4E2CB648.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/A39A849F-000E-AB4B-B552-4D4D1B51CAC0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/AAA654F9-D0E8-4549-8511-12B75E2BCF30.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/ABA62F2B-0011-9A48-A36F-3E53DFCC4E4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/AF9F26CB-D1A1-724B-8EF9-8E0FD8726EC0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/B125EDC6-C94C-D340-BF6E-51A41E2CE382.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/B8720BD7-94F6-7A4A-BF17-9F5D4B856205.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/B89BA0E3-79FB-D54F-AA40-EBFC83C1BCCB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/B8EB4C9B-790C-014E-894B-60B25AB33831.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/B941C38D-D483-5042-B099-354A36B1197E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/BB28DA97-81AB-C94B-8DE4-F03CB66484E1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/BCEA04C5-75C4-0246-B0B4-46041FA29ACA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/BE6B6DDB-57D2-7F4D-9507-EF9A455D28C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/C3D20437-EDAD-A64D-BA61-A708C79826B2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/C5E7B7BF-B027-D043-88A6-B302EFE538D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/C7E075A3-7EDA-294A-8EED-22CC04412511.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/C946FCE6-DC63-B645-A2BC-5CF7EC2445C8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/CAE7585A-14A0-0148-9D75-8A72C761342B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/CBD16B48-C90B-B54C-9BFB-76D80CFE423D.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/CEB33B4D-C759-D745-B96A-B8C551CC804E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/CF3046AA-7AB5-124D-9FB6-5759113F01F7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D010C661-9634-3F4A-BAE9-85F194F259D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D161C21F-C392-4C4A-B39C-D5F3C5CB05E7.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D3318259-C5BF-124F-AB31-B9929B058868.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D53F7F8D-9C6D-094E-B653-B622A27EBB8B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D8A45BF9-6119-6D43-B8AC-DA9F26FA1597.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D8A7EC3A-A7EF-DF48-AC5F-536D1B173587.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/D9F84E95-FE09-014D-8E14-9B40CBDBC472.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/DEABA8FD-761D-404A-80BF-50FA9F6E125E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/E85A5757-E10D-4446-A280-77CDAAC5C2F9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/E93D61A0-318F-B94F-AE5D-F00ED5564BB6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/EE4E87C3-095B-254A-9D80-22A6E7D6DFD3.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/EFB055B2-B918-F14B-8742-A2B7CD225CEF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/F392D245-063C-5A40-8891-C56BA76A9640.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/F55F00D8-1BE9-EE4E-B8AA-A94BAD3D06DA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/F6846F6A-A952-2842-813D-6616D089AB7B.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/F7115EF2-4BD0-1144-B578-E4FEAB785B6F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/FBB624C1-8C3A-074E-9290-F70FCE622E05.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6_ext1-v2/280000/FD172172-A539-B345-9475-AA96C3A6DB40.root',
] )