import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/629/00000/E2B8C5F0-F45E-E511-ADC8-02163E01410C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/630/00000/7413EB59-1A5F-E511-BC4E-02163E014792.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/672/00000/1C758C5C-F45E-E511-9510-02163E012800.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/673/00000/D6A3FFFF-F95E-E511-A430-02163E0139D3.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/674/00000/DE7BE8F5-035F-E511-9FA0-02163E01478E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/675/00000/4AA27F21-8B5F-E511-9AED-02163E014472.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/675/00000/D44C0C15-8B5F-E511-BCD8-02163E014178.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/02657C39-BA5F-E511-9533-02163E0145EC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/30EF462F-BA5F-E511-B0CC-02163E013692.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/36166449-BA5F-E511-A4E5-02163E014520.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/56B2FA2D-BA5F-E511-8341-02163E0137AE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/78D63A2A-BA5F-E511-8943-02163E0143F2.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/822CBE2D-BA5F-E511-98E2-02163E013708.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/DE35842F-BA5F-E511-96E2-02163E0135EE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/1889D9AA-345F-E511-8078-02163E01374B.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/746A90AC-345F-E511-9FB9-02163E0123C5.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/EC03B297-345F-E511-BDC4-02163E01184F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/725/00000/7A55B3B1-205F-E511-9117-02163E011FBF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/727/00000/543E874E-385F-E511-83F2-02163E01350A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/728/00000/0091808E-3C5F-E511-AB2D-02163E014708.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/1A59B4EF-1960-E511-8A9B-02163E011FEF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/30E7F1F4-1960-E511-B10B-02163E01475F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/32F792EC-1960-E511-A2E6-02163E011F0C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/3C9A2DF5-1960-E511-A6FC-02163E01474C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/4E68D3F6-1960-E511-BAE6-02163E01385B.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/5CA7EAF1-1960-E511-9B85-02163E014552.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/6ABE7B95-1A60-E511-A9AD-02163E01466A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/6AEB0DF0-1960-E511-A241-02163E0123FC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/8651AA0D-1A60-E511-BA5A-02163E0141C4.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/92BE40F4-1960-E511-8EFD-02163E014364.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/981FA415-1A60-E511-95A3-02163E0143FA.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/BC25D4F7-1960-E511-8CA6-02163E0135D9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/C66B1CF6-1960-E511-B961-02163E011928.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/E4B119EF-1960-E511-8A50-02163E01188A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/2E6633ED-DB5F-E511-8C11-02163E0140E6.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/BEBE436C-DC5F-E511-88B3-02163E014213.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/D6B6CBC6-7F60-E511-AC7D-02163E0134EC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/EC27C1C2-7F60-E511-9D52-02163E0134CE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/834/00000/70FEF702-FF5F-E511-AABA-02163E0122FF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/842/00000/B6BC66BA-4260-E511-935C-02163E0142FC.root' ] );


secFiles.extend( [
               ] )

