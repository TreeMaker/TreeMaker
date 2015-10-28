import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02695475-FE7B-E511-8B2E-0025905A48F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/048FFA74-FE7B-E511-9704-0025905B860E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0669ED73-FE7B-E511-AC87-0025905A6056.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/068D1328-327C-E511-8A55-02163E00EAE4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/06C4944C-327C-E511-9C28-02163E016683.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08B49574-FE7B-E511-ADAE-0025905A613C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1823BF56-327C-E511-83EF-02163E00C2E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30FFDD84-327C-E511-A46C-02163E00EA20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/348E9035-327C-E511-8FBC-001E67578130.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38021270-FE7B-E511-9AFD-002618943915.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A31176F-327C-E511-BA7A-02163E010CA5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4018520F-337C-E511-83A3-02163E013190.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/483D6061-327C-E511-82E5-02163E012FEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48F89949-327C-E511-8F85-02163E0160B7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E4F2D74-FE7B-E511-82C8-0025905A6132.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/506CBB2E-327C-E511-A14C-02163E00BB62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5638F667-327C-E511-A28B-02163E00C01E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/587B7D69-327C-E511-931C-02163E0168EB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58931971-FE7B-E511-AD52-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5ACA8774-FE7B-E511-9F61-0025905B85AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62398E74-FE7B-E511-9D73-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62B50859-327C-E511-BF07-02163E0166BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/62D6D86E-FE7B-E511-94BD-002618943886.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66BFB5A2-377C-E511-BCD8-00266CF3E0A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66DB36E2-327C-E511-BBF4-02163E00E67B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EC89874-FE7B-E511-8E39-0025905A60A8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7809A577-FE7B-E511-9237-0025905A60FE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7AD67530-327C-E511-AF60-02163E014FBD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C902222-327C-E511-93C9-02163E014DA9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E540768-327C-E511-99C6-02163E014B22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/84F1AC1F-327C-E511-A9A3-02163E00E7F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96C62A76-FE7B-E511-BA80-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9E966A2A-327C-E511-8BEF-02163E00B748.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A0AE384C-327C-E511-B816-02163E0138BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6FBD675-FE7B-E511-8A22-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AED26056-327C-E511-A718-02163E00F34F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B84B514C-327C-E511-8F1E-02163E00BE76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8DB543B-327C-E511-8F16-02163E00F559.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6A3D275-FE7B-E511-A76E-003048FFD752.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA3123A4-327C-E511-8514-02163E016BC0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EEEE1D71-FE7B-E511-8309-0026189438FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0AA6118-327C-E511-B15A-003048F0E852.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F2689B75-FE7B-E511-B236-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8027673-FE7B-E511-AA3B-00261894385D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA085B39-327C-E511-9CBF-02163E016BF5.root' ] );


secFiles.extend( [
               ] )

