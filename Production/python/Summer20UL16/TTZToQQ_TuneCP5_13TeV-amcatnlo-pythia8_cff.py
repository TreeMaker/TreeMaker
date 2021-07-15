import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0228F59A-C482-AA49-B055-469027943C45.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/03DEA9C6-7E5C-C645-B6A6-0DCADCC83E59.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0526C073-482B-294A-807C-1077C812CE91.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/067A5731-65FC-374F-8F2F-ADCFCF740A41.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/06DC0D7C-9E67-744A-B93A-D1F2A655AA00.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/07C66EC9-570A-C741-BE27-59D8CA2535D5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/085F1FFE-19CD-7E4D-9B25-560DD0F44F98.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0BD8793B-6D2B-EB49-9ADC-01B723E8CF1B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0C377634-1AB8-C849-81FA-30EA8CC21791.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0CE24CF9-B563-1E4C-B126-A9FFEE667E39.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/0F6096B9-1331-284B-A11E-032540992584.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/11A7EC61-5579-0C48-9B9B-CB2A0F0BA745.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/121EA96B-BF1A-C744-9465-AAFF07A9D082.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/135B129A-D761-8148-943B-EF562CB802E7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/14366FE9-F9CA-1942-89EE-6F8131FB1D9D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/14793A00-F3ED-5F4C-AC3F-DB17241066B4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/17556E4D-ED62-F64C-8EC3-DDDC6BA51A6D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/17976DBC-E268-8549-8817-F14BB620FF2D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/18842027-2912-6A4C-A56E-0906368C06B6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/189B1923-3F40-004E-9818-29124D5C0B0E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1F25C2BD-52C1-874B-8619-F6B8FAFCD2AE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1FB5A8D0-D65C-8048-914D-36D355D7E88E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/22E8DFFE-FF41-0048-ADC2-005C2AD93901.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/237C3410-8146-4B45-9EBD-FC0A95246602.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/24187DED-BE43-8C44-8181-C3835CBFDD40.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/24ACEFDC-400A-FE48-8FF4-0D3C4A62F03F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/24D41C0D-937C-CB44-8616-B850F131E60E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/24EC1A75-EC49-964A-B49C-AE007CB5D786.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2660DA7F-7843-134D-9F58-4BB6516D2165.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2A45BD6C-7DC7-8E40-9874-CEA6A7304A7A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2DAF8F07-A5C2-C044-8CF4-E16182BCEAD0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2EEEA505-478F-FD4B-86CC-16BE6A37F06F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/2F51AEAF-9BE5-164C-A520-74F097BE9CB6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/30ADE767-3376-6C41-93F5-EA6EF833BD34.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/31E4559F-E51D-4F4F-B934-3A4F279FD61A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/32335628-52B4-E140-B9E8-53BB9AA44DBA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3537B141-2504-FE4E-AE01-DF9596120D0C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/35C1D0C3-361C-964E-B702-C1FFF7A3E45E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/366DAA32-07B8-E64F-AF35-F6FCC03CA2A1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/383DC2E6-4300-AC42-8698-5B676B209A73.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3A338870-4EE2-B942-A1A6-A6097FF5CB8D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3A9E6CA5-4692-3648-937B-46F46BC6E487.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3AF6F979-65C4-B942-AE19-13F1D96760FD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3D20B166-CCF9-4348-9728-1E151A7E87B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3E747C89-9319-7940-A7E4-11859F436337.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/3FCBACFA-FD0A-904D-96E3-B48DFC8B1E36.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/43AF6E93-3CFC-F645-9C68-B74BF9E5153C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/44D45EDD-2731-3F4E-BABD-1E3B2A875CD4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4515B426-5734-834D-9A5B-01575D550491.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/45CDB733-4165-9442-BE95-F2A6326E2D5A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/462FA7E6-BFFC-2E4B-B3DC-D51EBA69327C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4645D952-3809-3A4C-B0C4-B89420B55A31.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/476C4C31-7C30-CA4A-AFBD-D4E7699B54D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/47E737EF-63B1-4947-819E-BD50AF87AA2B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/47EF3540-BA95-0A40-9EE7-BBD21B70A98C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/48EFC7F0-3D3E-DB48-827D-CCEDFFE4409B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/491FCF0A-ECE7-AE4A-824E-7AA6912E0F58.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4A0956DD-EF69-2641-B546-C7A658AABA6B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4AAC242A-7555-FB48-971A-CF35C32FEFC6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4AE49BFB-1B64-EE4C-826C-B42F8B3CF938.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4E241E38-7F25-654D-8419-E97F289ED733.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4EC8B8C4-2817-764D-97AA-72A322715897.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/4FB70922-4B9B-4348-86F6-749077F56F4F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/512072BD-3AC8-714E-9487-BA424CC53E16.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/526944CA-4CB8-2A42-BE9D-B1A4DEE1879B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/52DE47A3-D704-B443-A406-CE91629A9B57.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/54B0E36A-7496-0544-93CD-1A6C045E24A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/56E987FB-9B31-B440-81A4-22443E489296.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/5DC9FE42-5A52-4144-846F-9F7D716D90A2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/5E93044C-2AE4-CC43-AF01-F4B374E11315.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/5FE7780B-B924-BB4B-BE34-EF2751FB6947.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/618142C4-7DEE-6F42-A539-DC6DCC631C39.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/61AA64A9-D783-C84A-943E-8382903D4612.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/637A7FDE-CE19-D543-8EF8-F8F6671F9590.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/6450A52A-F054-8747-A930-C96D23462640.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/64779889-B1AD-DC49-9A27-0F14D89727B8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/64ADA5C7-71FD-0A41-9288-A2116F2C1C78.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/689C4FFC-7ADB-C941-9CF2-E17E6823AC23.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/6954160E-ED87-F741-8477-43FD994A7F1F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/6A6DDC72-77B8-4547-B98B-19C26A408A61.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/6CD182AA-85FF-A145-8AEF-639EF6FF94CD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/6EE7BE07-3A53-D348-AEFD-D7D1BE52E465.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/72EBCBD6-BEE6-6145-A26E-5EA5CE5A9182.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/73F4987C-2B15-834C-9795-A1C191F08F63.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/760D89BB-FE68-CC4D-B181-1CEBDDEA672E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/777972FC-D34E-1745-BCCD-73FDB6DE21E8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/779AA0E1-337B-6246-BBC2-519473D95008.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/779FA6B6-52B7-5A4C-BB10-D92ED3ADFFC4.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/782E5FDF-C385-0347-ADAC-6B2BF42488C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7B1C415D-AFAC-8C4A-BD23-25B36C3C5AAA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7B213209-85C8-024D-9AEE-94D4AC982FA2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7C0348F2-4F3B-F74B-9FDE-76AD786A875D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7C0D7DC7-D2E7-4E47-B453-7BB49B5E9FDE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7CFC7871-C220-BA4A-BE47-63DC4B94B784.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7D5C89B0-6C47-0447-804F-4D06B6AA3398.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7DAE4444-971C-A040-857B-CAB14D3D7B79.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7E1A670E-243D-E04D-83B7-0C02D9FB931B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/7E48E1DE-5059-CD4D-B2CD-37FCD79DB150.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8007CA20-1F00-B846-9D81-C4E34A408575.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/82FCD40C-7428-7F44-9273-6447F71916E5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/859020D5-CC65-7147-A702-66CD8494BFD3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/85F09FAD-57E0-4B47-A56C-32D43ED814F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/866050CD-14F8-9340-86D9-9479A5669734.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8765B111-F352-F74E-8827-A0CA77596574.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8929D18B-0FFD-C948-83B4-0DB5358268D0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/89C10589-80EF-BD42-BA7E-2F80FD8201A7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8CACA9E3-9C4E-9941-86ED-D9AD00820D6D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8CCBBD41-9AFC-6D4B-9EB9-D25C4DBBE484.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8CE5DB54-BC05-DC4E-86C8-91BB30D079B6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/8D8EE8E1-80A2-274F-BBCD-B81D226805AC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9303F29E-7C31-D047-8B4B-E66345C8DE10.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/948EF6DF-997A-F54C-9219-865F2FFE819A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/952B3820-4EDE-D946-A18B-2997020D8FCE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9578A62C-331F-4C42-A9EC-FD89CC9DDEDD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/95E93609-E88D-3D4C-BACD-A88BD81EA2E1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/96B2FB7C-CAD7-6143-84E8-15EDC6476BBE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/98AB3A1E-1221-4E4A-94E9-0DEB6B3F1CC1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9B9D597B-45B4-A641-A04D-58A90F2DF7B2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9BB74227-A3FC-AA4A-87A5-4B001545E2D5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9D0D90CD-5122-E741-99CD-135D94219303.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9DBC93A0-AE93-9140-B1CA-9FA5BAC9D72F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9E03B28C-1906-5F40-81EB-BE20D811023B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9EDA6C5C-B665-7A42-B89E-DAE2E84D4EB8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/9F908A0C-4EC9-7444-9AB2-6E1DA519F50E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A545199F-EBD7-1240-B5A3-59C3CEF0FB18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A58E2FD8-5737-684A-90AF-68A4014C96FF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A5E4966A-1B7B-A846-A59A-4781245B05A3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A60F3BC5-4364-214A-9309-3428795843AE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A61A550F-68EC-7444-9844-E49A1A920E5F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A691D724-E54C-744C-9E98-BAF2F9EA3D6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A71EFA87-AE7F-7C43-B090-8EB0F523B3F8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A82D16A1-6071-324E-8A56-32179A0879BB.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A8A91D75-A99C-DC4E-A093-3B42BA72A90C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A8D3D8C0-E0DA-6345-BF3B-9633ABDCD4ED.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A8F10E03-E3A0-E843-AB29-30F5C580AC04.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A9B505BE-D080-804A-AB32-74495E8355C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/AB6F1945-C4F8-634F-A24E-E02E2DF528F1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/AE02AC45-CA36-5F47-BA74-277B4EE802C0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/AE8CCD58-B7AA-7949-A95C-EC0071E47247.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B13AB779-605E-6349-9815-CF1A1F7B78FA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B326CC4F-E2B7-F746-B7E6-A7E897060D73.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B327C0F1-B8F8-ED4C-913E-13112F3D71B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B40AA227-AB63-5A4C-8F56-4902ACDFA332.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B412DACE-D425-E746-8B12-2C1BEDA8DA3A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B9B1B7A9-E7B6-774D-9135-74C56CB2E881.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/B9D7ADE9-402D-5A4D-B894-A43C5F7138F7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/BCB4857B-BA74-F54B-BCE4-267958F485B9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C0D85178-4DAB-E24F-A3D2-FCC17136A4E3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C76FF5D8-506A-F34F-8969-A2C07C83AE00.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C77AC88D-CB8F-964C-9343-A2877962935E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C806F9C5-4B78-9540-9CA5-9488827CACF0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C88042CE-04D1-D14C-9623-A680888114A0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C8BB9A5C-3DA9-724A-964A-DC07CD4248F5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C91A4BD1-8F02-7C46-B3D6-D9DBEBE5115E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CA784950-CBCD-A34D-87BA-5AC368053E50.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CAF00064-8B9B-F144-A0A9-934A9063F223.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CB189B89-80AA-D047-BDCA-4CA9181900EF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CEEE1ECD-25B8-B545-A680-E143A77E5EA8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D0120CF9-9849-C04F-9052-759E10C169FE.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D096AA1A-0A1C-D64E-9886-F972966C375D.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D0CEB84C-4256-984D-9536-4CB9D280CDDF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D0EA2513-F8E2-8C49-B95B-666A6625E2F9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D3D51E5B-BE1D-B44D-8917-B422D066CD6C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D4648D31-7C11-A54B-8820-F0201B299726.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D7238C65-7B2D-0A46-80D1-18F42417B70E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D796B39D-1424-5748-AADF-36B1EC81A9F2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D8379969-371A-DD41-BB04-403BC4FFAB12.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D87AB4C8-18AA-7941-8109-855FC00053BD.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D98F6F6C-0718-A846-A6D4-3C1DB80F903A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DA770DB7-566D-984B-991D-8C3F58C7249B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DAA8D2EA-074C-9A4E-B2D1-2CC84FA66819.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DCB23821-C5FD-9F40-B9C8-7ACD13E72DD5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DFFC89E9-6DAA-8A45-96B7-8E2DE0786EC9.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E03577C5-1ED8-0044-8AA1-306F67C4EA09.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E4F965BD-AF65-5D4A-9BE7-D76BED4C7174.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E56BD16B-1C32-9C49-AC16-02B1B2FECF47.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E715DD7E-9A85-B044-8C27-9E9B99E0AB60.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/E9A85261-A193-314A-B1FB-3B47E9030DBC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/EA86A0D2-5716-C042-9F96-A29FEB9DCE11.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/ED36EEF9-820C-634B-8767-D520871D5D44.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/EE9EE45F-F3DC-6242-B498-2F9D4A34EFFA.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/EF805D9F-32B0-9240-9666-F0E3662D32C5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F2B99F57-9B76-504C-9750-996C0D559E1E.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F313DA76-1276-9A47-AB54-3B3DF156FED8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F37D38AB-9500-F44B-B1DE-C82ACEDA7CC6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F3E549D3-6E92-9245-A895-3CEF273E0A0F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F52133E5-8942-3C40-B274-9AF9E13AF3D8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F78CB252-8A65-2B4E-AA30-6F9A30EE8588.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/F95A4A9A-2AF0-CF44-9FEB-1109B869C033.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/FADECFEF-100F-5148-8540-2D99FB8B350C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/FEBDECAA-9FA1-0446-98D1-676764A12CDF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/FEC7EEC5-8E00-E94A-B1AC-9D23E5CBB10C.root',
] )
