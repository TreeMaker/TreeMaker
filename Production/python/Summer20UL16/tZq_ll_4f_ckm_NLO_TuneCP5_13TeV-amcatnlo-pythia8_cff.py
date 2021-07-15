import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/02990CBA-86FA-DD46-81CC-46CC2C891651.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/08C09D4B-3AB9-A540-B152-B58C99A0E505.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/127D2F19-2607-3241-9B52-D3F1FCB151D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/15E1AE10-8CCF-984B-9B1B-68A458069A8E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/16C6D820-ED5F-6849-A3ED-BB7A9058BEAD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/199793AD-BEB3-FA46-BFAC-41596D4765CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/1FA81797-D6BD-4C45-A34E-A4B6EE672734.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/2EB8A1D1-F5E6-D748-AACC-87749A249A21.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/2FDEB885-3100-0346-A41C-F98054AE0063.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/3512373D-26FC-A84C-8D9A-C8E7418E58DE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/3C167A7F-966B-D24B-9FF7-02ACB06DD859.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/3C965C3A-7523-8E46-80B4-1645DC81ABB7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/4A273638-CC17-EF4A-ACC1-05986C838EE4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/536DF0D3-77FC-C945-BBBC-CF44555B4473.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/53D7DD94-6048-5641-B24F-0FD12F16FA06.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/563735B4-7544-7441-87F4-81555C29FAB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/5646BD13-7238-6047-AF64-285220839D0A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/623ED9CF-1C85-6F4B-86FD-0A4A0933DE7E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/635FC634-086E-E74A-A552-99515354FDDB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/669F0B02-096C-4D4B-9186-02B659087342.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/687271B5-738D-F343-922A-B6226176D7A3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/70680166-29AA-6B4F-A835-5A16657C2457.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/73D0A600-2EE5-BD45-B491-8010021B860D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/77351908-F987-7340-9DE9-C25540219BFF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/86365F3F-A349-4C4C-8070-D8C7D7A7D94F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/96390B9E-DEAB-BB40-B50C-495EB71F13D2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/9FF20218-C440-414B-9159-C17CFD1AC50D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/A1067054-395E-DA4B-9A35-57DCA7568C41.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/A401518F-7595-B14D-AFC5-0B0DA43743AB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/B0445CC4-A7CD-234F-9E25-2F1FF010182E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/CC780832-9331-7748-9DD4-7F05767DC0A4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/CCC2435A-8058-454A-892C-81435C86D887.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/D2A05FD0-2162-7A4E-83C7-AA8E589BD483.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/D6192119-49F5-2B4C-BF36-09F50436FDE9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/D63DEBE4-3567-5945-9EC3-310C422500C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/D85C2B68-BF6D-E342-BC83-07494EA17E88.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/DD983995-0CEB-AC46-987E-A10F04E727D2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/EC035CC9-6F88-2D44-82DA-1524FDF22194.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/F6E94AD7-EE98-CF40-8177-C0EC5D8D85BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/F8823C8B-1441-734B-9B16-6AB9A6DB1657.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/F9E68DFD-728F-5F4D-B2A2-FEA86D90E03D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/00000/FB79EE9E-B830-C841-ADE4-C5B947180927.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/05F88824-2707-DA40-8D48-A0414B384C2B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/0A2087E1-71D0-1043-93B8-1FBE338077D7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/0AA8234A-C111-6D47-BE73-86841C26311D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/0AD1AD48-1AAF-7447-9565-A17A8E466050.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/172FDC2A-75D1-5B46-B19A-028884BE551E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/17C8EBE9-8716-6541-9A6F-61068C9B6128.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/1CE19D3E-7A61-7848-97E5-F3BE62081514.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/22F70996-1E35-E342-9826-A891CD09944A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/277DC36C-3E3F-AB4E-9C14-CBB216994E6E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/35B67EE1-C5C2-B047-B8B1-5A4D6673F6B3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/38013592-C7B8-6C43-AECB-0B3DA125C864.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/3E498252-B9D4-0748-9A25-7A36ED9C6D93.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/4FEAD554-EAB7-B94E-B405-4240127838A8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/52027695-5981-D943-A2AD-6D62ACBBDFEB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/5C479332-7FDD-374C-98DF-BD98CD965109.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/606C80EB-0F79-C242-89A1-252C1A3805ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/60B8401D-E8C2-4C4F-9B74-5006ED5AAC5E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/62BFDF3C-EC49-C84C-87D2-9EB0C6A39BA0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/65625225-2240-764C-BE21-26E3CB144880.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/66478460-5E43-964D-8E81-3295B24FDD11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/672BA85B-1E58-6940-8218-5951A491127E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/67D18B3B-EB00-1D47-B6E8-446E045028D6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/72A368CF-9C9B-6548-AF02-3C9B99749E16.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/731D6F2D-B60B-CF49-A2E0-E94EE89A8D33.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/73F133A3-CFD9-2747-870A-0A4B3F40D40E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/74FFA345-1441-9341-AD69-9A79DC5D8DED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/75393111-7788-9F42-9A3F-BA17A676B7C9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/7AFEE022-39AB-C84B-BB8E-55D19C3ED852.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/7F9E3AC3-C6E0-3542-93B5-38BEE470C40F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/80ACD623-902A-E744-9917-23A04924A86F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/81446A94-AABD-E343-AC45-DB48A1B6B5C7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/81BC52E0-0A3E-2E44-B6E8-276E7E56E4AF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/90666818-DE3B-0840-8806-C9F61FEA867E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/931C4307-5DE4-9540-9314-F9643E924C0A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/956F9073-5FC8-D44F-AD95-2EA5C826EA70.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/9739076D-D3ED-3C45-A2C6-5434C8267751.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/9A6EFFCC-6A9F-EE4F-96EF-EE892E251490.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/9B751B4F-2B09-FC47-8386-E2DF0CC83976.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/A18332AC-332D-CF40-B9FB-8AAF2D7F4CA7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/A2AD939B-5D4E-B141-92B9-348F531CD4E9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/A97621BE-B150-F248-A050-E68BC21DF8F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/B309F42C-B8FC-B342-BF8E-D5F752FB81CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/B42176A3-2DF9-7D47-99E6-D2F758897E9C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/B8E6BB62-DAB2-8A47-8D99-7FD5D18AB99E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/BD9B3F3B-0F4D-6344-AA48-B20EB98BA1A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/BF8DF2E6-82A1-CC46-938F-9FF166D28B3E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/BFC110D2-E331-BF45-80F8-3792C9DA5503.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/C0957A1F-DE41-0742-918A-DFA8A2EA1A81.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/C27BFFE5-1629-5B41-9425-03C0D9B3D5BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/C2FEA38D-00A8-6743-B0B0-FD423B836B0E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/C9CDD2D6-5387-A846-ABC7-205E61D62006.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/D0A7073F-9616-E14F-946F-6C8A4791388E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/D165EB0E-CE5A-5740-B300-F4284B35E781.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/D34A03DE-37C2-994D-A96D-0617987B3ACB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/D5D7697E-8404-5F4F-8078-A4A42878A5F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/D71C0EA6-1E74-004C-8A29-14913B43411A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/DC5D425E-6CD6-AD4F-A911-4FB637994551.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/DCFA5D3D-D2D3-C541-8627-A3126D5D6F53.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/DDE1AE24-5C6E-0E4D-AC1C-F81BA1C9E463.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/DE4F4BA0-7DB0-0544-A633-4287E76609BE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/E24235F2-6589-0941-B63A-2426F906C5D7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/E35537A9-B0BC-B246-A3CB-B0223337AEF7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/E46A5AC3-95C2-8043-986E-88AE1F055C9E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/E7EE15A3-F860-834B-9192-98CE531D47B8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/E83D5290-0D23-604E-A444-33FA5D0324C1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/EA8B5488-E4C5-3748-84E1-32238AAF8FDB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/EE439827-48D0-0F42-B8E0-B05F2814C44C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/F0EC0314-9B4A-1F4F-847E-C51FEE42C669.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/F23D6351-9780-F64B-B789-0DED54362A19.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/F2F0FA49-E53B-134D-B626-6C1D62F03D76.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/F5D0B925-E614-0041-BFB3-C097CB307B69.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/F7524890-9A7F-4D47-9F1A-0781C23CAA59.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/FB1254F9-A80F-704E-8680-EAA656F5C557.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/10000/FD74FC20-17E3-6241-8B59-91437D23DE0B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/002CC2AE-2526-4647-B4C7-68B0BB9AE24B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/076558FD-3B16-E345-B3DE-E03658E623E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/07EA8DB8-6E93-DC47-BC53-D988E989465A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/0D33D56E-0E4A-8740-8800-5CBB8E93591E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/11740477-0C8A-F94C-9519-3DDA5436E9FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/1310BC91-0946-DA43-B2EC-D63676F665BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/13AD3F5E-E870-3643-978F-D00F5B193B7C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/163CC8A4-7698-FB44-82AF-A09DF99E9794.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/1F932D03-5228-CB4D-91CA-EA0C628EE9B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/1FA68901-0220-8E43-8D48-B37C3F034EC4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/208B7669-EB05-0746-B018-1A3AC9600137.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/219BF596-3CB4-E142-81D6-6EA6560DC572.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/2FF6DC00-0967-E04E-A11F-FFFD4833F554.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/31032FE9-8E85-6E4B-94AD-A9FE124A5C20.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/31075E0F-6C55-734D-9DAD-730563589362.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/31BA1222-CE15-DC4C-A3AD-71E8EDA36C2E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/35BE4505-7368-DB47-A5CD-F6C74F49A012.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/3833F99D-0925-DC43-A5BE-91EB54E8FA39.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/39BA67AC-7F1C-B347-8110-5CC5E65EC5B5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/3A5B700A-06F8-4241-9BAB-208E8A2B2AE0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/4002E7F1-FA97-1A42-867C-FE99437A2208.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/44EDA252-F16E-AE42-95D9-173373A94724.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/4D4C119B-D189-7F43-B97A-7D8ADDCA669D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/4DA3A59F-012F-6448-96E5-ADCFED244B49.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/4DDC5156-3E3A-6B43-8A82-0BC63F5BB530.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/5257F5F2-D797-1D42-9BF2-393F3D7A9FFB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/54E1AA8E-193D-804F-82B1-BDF4D4DAB52A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/55CE7897-FBFA-FD4C-B082-85A4D843F536.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/5BBA89C3-2375-9449-B083-5618E02A6721.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/5BD5682A-0D83-5F46-85F7-7CDBD9A77F86.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/5DB20931-5111-D14B-90F1-C3D73D633B46.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/5DBF302D-F252-7E4C-B7D4-6F8A8BBE2148.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/632731E9-1B1A-FC49-AE30-82C75348F726.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/6847BF1E-A768-BA4E-8417-BBFD31BDA17D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/6A387B49-B38A-E145-84ED-0E12C673C06D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/7644F1D0-3B30-8545-883A-7BC639FCC366.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/7AB25BFC-ED08-514F-88E6-79BF819694F8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/7AB770A0-166E-2946-B6B7-BA94A1F1459B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/7B455A09-7F3B-1844-8766-3389C9AABD9E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/7CA97E92-1AFA-CE4C-9D26-C50EA80E73E0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8710C266-DABD-2C4E-A709-0210B07283E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8923D487-9A7B-0545-908E-9218F8BEE2A9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8940937F-FDE5-0D4D-969B-371C5A11E492.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8A21039E-BA62-584B-B490-0EBD1D319021.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8A3BC659-F1BA-7741-A644-803579B8459F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8A4F5E0D-C098-3E4F-B8D1-255B04CCA900.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/8DB2A92B-5AF9-F049-93E6-43797A142F11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/900F416F-9376-7E4F-A6F8-2907E047DA3B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/9026BCA6-9DFB-3244-91EF-720CF290A3C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/914260BD-08FC-FD4C-8B0C-FEC691665AF5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/93B7832F-855E-5C47-BC9F-9347CD368AF8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/9D5783D3-CF96-B749-8499-E87D9BE9B01C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/9E896EA4-6D29-DA4F-8BEE-65BBF51B9EEA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/9F050788-086D-2C48-8E7E-6F0963220CC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/A650B246-252F-274E-BB3D-5DA758448700.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/A674DA78-6A24-304F-A7CE-CE1F788B83B4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/A7F29A7C-2BBD-4443-ABBA-274DE163727B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/B27E2820-E61F-984B-A079-82FCBA9B31A9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/B4686199-E3D2-9C4F-A090-6D57D9A18011.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/B88B0B65-8F4E-A046-B9CA-360E968E1FDE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/BAE79273-F800-354A-8855-5CC9E0D01B9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/C1798F3B-498F-DE4E-8C39-540ECC0C8B80.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/C5901471-B27F-BF4D-AAF8-1570980EF984.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/CB503F76-2662-B845-9985-F0AC1365E205.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/CC8E365B-22B9-6B40-AB55-8BDE37DD67C6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/CFB5213E-D430-5A4D-AAA0-1B27777CB1CB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/D0E40718-7A94-8349-871B-8F4609B64EAE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/D9699BBF-2065-684B-9D12-6C7FBC74D4CA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/DEDE5782-E25C-6941-80A1-07E84FF4701D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/E39000B3-D732-C04E-87AE-592B12DF3008.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/E4086F04-B4E4-4348-A682-8AD3CA5DDFB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/E9B610C7-9F82-0448-8068-46361070D318.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/EB5CFC2B-B967-5A48-96A2-B2F958E65360.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/EBC9D3A5-B770-2C4A-9EB6-2F7E91E38079.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/EF71998F-2C52-634D-875D-075B78234D79.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/F11A3B72-FA24-6E46-A718-C61560E73C8E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/F3980781-3D69-7D4C-886E-EB512CED7A9B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/F6194434-2D9A-B74E-9C18-AEB62BB71F5F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/F8463703-A0AC-1041-A1A4-2EF553D61C35.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/F9CBCD22-7D77-E946-A60B-C8FAFE215588.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/FD170141-9919-624D-A138-B576D724161B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/20000/FF035F29-605D-4643-B760-DAE8648B4953.root',
] )
