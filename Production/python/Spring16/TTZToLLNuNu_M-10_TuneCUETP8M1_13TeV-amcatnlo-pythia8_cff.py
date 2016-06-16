import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/0E0E1E81-3B0D-E611-BB9E-901B0E5427AE.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/166FA656-1E0E-E611-8276-001E67E6F85F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/1EBA3E56-480D-E611-A672-20CF3019DF00.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/264FCB34-3B0D-E611-9063-001E67E7187B.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/2880B662-540C-E611-9852-0CC47A7E6820.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/28C63476-680C-E611-BFA8-0090FAA57C20.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/2C6C6405-1C0E-E611-9855-00259073E468.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/2C963CF2-000D-E611-A59C-008CFA111330.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/30E75898-520D-E611-AA5A-008CFA0A5684.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/48BC5676-6C0C-E611-BD1F-02163E013407.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/5A3DB825-780C-E611-9CF7-02163E0126EF.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/6078CA4B-9E0D-E611-8F98-008CFA1CB73C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/8A52D846-550D-E611-9018-02163E0125FE.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/8A539562-800D-E611-854C-B499BAAC3786.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/8CB06609-6C0E-E611-8F36-02163E00B486.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/9C7BE846-360E-E611-80BE-D4AE526A05F2.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/A2E41A5D-6C0C-E611-A8B4-02163E013498.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/B00A8F94-450D-E611-8043-02163E00CE08.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/C0DC596E-600C-E611-A621-3417EBE706ED.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/C238853B-3B0D-E611-906F-A4BADB1E6F27.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/D837BF65-540C-E611-B5CA-0CC47A7FC72C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/E04EE1F4-1E0D-E611-A5AD-842B2B76670F.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/E65CF100-530D-E611-8EE3-0090FAA58B94.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/EC491039-B20E-E611-8BB9-02163E01651C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/F06A947D-6C0C-E611-8A1A-02163E013592.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/F6EBD96C-600C-E611-99BF-002590747D9C.root',
       '/store/mc/RunIISpring16MiniAODv1/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/70000/F8CC8DDA-1E0D-E611-8BFC-002481CFE672.root',
] )
