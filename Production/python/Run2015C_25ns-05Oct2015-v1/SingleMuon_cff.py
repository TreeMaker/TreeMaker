import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/06D8AEE6-1274-E511-82D0-0025905A60CA.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/1AD4B8EA-1274-E511-934C-003048FF9AA6.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/2CCAF4E6-1374-E511-8625-0025905A6132.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/363966E4-1274-E511-BAE4-0025905A60A0.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/363E4EE8-1274-E511-9D7E-0025905A48C0.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/38540B71-1474-E511-9549-0025905B85AA.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/560B29C0-1374-E511-B607-0025905A606A.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/5A756EE5-1274-E511-ABA9-0025905A6110.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/5E95E2E8-1274-E511-95E8-0025905B85D6.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/68CB03EC-1274-E511-9F4C-0025905964B2.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/6CD3B8E9-1274-E511-8011-0025905B85AA.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/7EFE3BE2-1374-E511-9D45-0025905A6092.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/981673ED-1274-E511-ADFF-0025905964C2.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/9CBD87E7-1274-E511-8F1E-0025905B8572.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/9E1DAAE5-1274-E511-A290-002618943949.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/A81A1EE8-1274-E511-BC56-0025905B8598.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/AAC7E1E8-1274-E511-886D-0025905A60C6.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/AAF3CBEB-1274-E511-A342-0025905964A6.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/B802C4E5-1274-E511-A732-0025905A60BE.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/BAB74309-1374-E511-A9A0-0025905A6132.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/BECF9EE7-1274-E511-8311-002618943800.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/C80F1FEB-1274-E511-B8F7-003048FFCB8C.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/CA9F53E8-1274-E511-BD78-0025905A60DE.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/D6EE89F2-1274-E511-A672-0025905A610A.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/D8E621ED-1274-E511-AE76-0025905A6118.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/E0BE4FCF-1374-E511-BA5A-0026189438BF.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/F2126D7D-1474-E511-8E6E-0025905A610A.root',
       '/store/data/Run2015C_25ns/SingleMuon/MINIAOD/05Oct2015-v1/50000/FCAB7AE7-1274-E511-9CC5-0025905A60B6.root' ] );


secFiles.extend( [
               ] )

