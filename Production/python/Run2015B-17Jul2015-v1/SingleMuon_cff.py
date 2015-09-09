import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/16B50792-172E-E511-B0C8-0025905C43EC.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/18DDE791-172E-E511-82A7-0025905C3D6A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/20A12A92-172E-E511-9EBB-0025904C68DC.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/2A679E94-172E-E511-B36C-0025905C96A4.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/32CA1C92-172E-E511-BD1F-0025904C68DC.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/3A314794-172E-E511-BACB-0025905C2CB8.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/5AC60C92-172E-E511-8161-0025904CF93C.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/685CF492-172E-E511-82C3-0025905C96A4.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/760EDD94-172E-E511-B801-0025905C2D9A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/76384094-172E-E511-833C-0025905C2D98.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/7E1D2E96-172E-E511-B304-0025904CF100.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/7ED0F296-172E-E511-A7D8-0025905C94D2.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/8835A890-172E-E511-9456-0025905C2CBA.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/8C8B7A91-172E-E511-B582-0025905C3DF6.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/960C8C77-172E-E511-8303-0025904C66E6.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/96C17592-172E-E511-98F9-0025904B7C40.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/A8016493-172E-E511-8A21-0025905C42B8.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/AC31B090-172E-E511-A9CF-0025905C2CE8.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/BEBDE260-172E-E511-97AA-0025905C3D3E.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/D0C57E91-172E-E511-8B70-0025905BA736.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/D43EF291-172E-E511-99D2-0025905C3D6A.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/E43DA791-172E-E511-BB8B-0025905BA736.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/FC24B692-172E-E511-8421-0025905C2CBE.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/FC32DF92-172E-E511-AD49-0025905C42B6.root' ] );


secFiles.extend( [
               ] )

