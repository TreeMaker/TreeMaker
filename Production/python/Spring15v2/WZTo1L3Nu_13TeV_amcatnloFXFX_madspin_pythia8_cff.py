import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/263270C2-CF6D-E511-88CA-0025905C3D96.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/268B36C1-CF6D-E511-9515-0025905C96EA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/28BAC178-CF6D-E511-BE3B-6C3BE5B513E0.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3840FBC1-CF6D-E511-9498-0025905C43EA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/528C36C1-CF6D-E511-8C88-0025905C96EA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/563470C2-CF6D-E511-9A24-0025905C3D96.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/808B36C1-CF6D-E511-B64A-0025905C96EA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/A00212C2-CF6D-E511-9167-0025905C3E66.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D6CC0FC4-CF6D-E511-A71F-0025905C2CBA.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/DC4A8075-CF6D-E511-849C-6C3BE5B59210.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E29A6ACB-CF6D-E511-8F71-6C3BE5B5F228.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E85C0C16-D06D-E511-867D-B499BAAC04E6.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/EA335DC4-CF6D-E511-B3DB-0025905C2C84.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/184DF00D-CF6D-E511-8ED1-6C3BE5B533A8.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/8A26940A-CF6D-E511-BC11-C4346BC78D10.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/AAA6C614-CF6D-E511-85C6-C4346BC0F3E0.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5E13BEB5-E36D-E511-8D60-6C3BE5B50180.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C0F2D0FF-B16F-E511-9D90-44A842CFC9CC.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/F001F24F-6B6F-E511-BB88-B499BAAC064E.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/04224C2D-9B6F-E511-8B67-6C3BE5B58000.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/04B3592A-9B6F-E511-8E86-44A842CF058B.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/12153313-9B6F-E511-A241-B499BAAC09D2.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/286EA10B-B66F-E511-92A9-6C3BE5B533A8.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/300C1E7A-9D6F-E511-9920-44A842CFC98B.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/34EDCE69-5672-E511-8AA9-001F2908AF72.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3CEF70F9-9A6F-E511-8332-B499BAAC064E.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/56EB6020-9B6F-E511-AFD9-44A842CFD640.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5ABB0FDA-9A6F-E511-8BB7-6C3BE5B50210.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/664DC12A-9B6F-E511-9C73-001CC4A62CD0.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6A0B94FA-9A6F-E511-A33E-001F29086E48.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8CF26717-846E-E511-8683-02163E014F63.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/92B38B47-CC6F-E511-B3C0-6C3BE5B51168.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/96ADB92E-9B6F-E511-B1F6-6C3BE5B50180.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A41FF081-606E-E511-AC65-001E67398BE7.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A47CA4A3-8471-E511-8E55-6C3BE5B56498.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A48A0FDA-9A6F-E511-8E99-6C3BE5B50210.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B295F336-A56F-E511-B0A6-6C3BE5B59050.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B2C95D39-9B6F-E511-A421-44A842CFCA1A.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BAC9DF1C-E86E-E511-A3FE-02163E010C13.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C2B04728-9E6F-E511-A55B-44A842CFC9D9.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C60E4DF6-9A6F-E511-AB8C-B499BAAC014E.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C85A974E-A56F-E511-9469-009C02AB98A6.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/CCE99996-AE6F-E511-A713-6C3BE5B593F8.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E02502F1-A56F-E511-BFBD-001CC4A6DC88.root',
       '/store/mc/RunIISpring15MiniAODv2/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/EC0B04D0-6B72-E511-8A71-009C029C178C.root' ] );


secFiles.extend( [
               ] )

