import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-1.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-2.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-3.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-4.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-5.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-6.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-7.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-8.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-9.root',
       '/mnt/hadoop/cms/store/group/EMJRunII/2016/step4_MINIAOD_mMed-1600_mDark-20_kappa-0p28_aligned-down_n-500_part-10.root',
] )
