import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-1.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-2.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-3.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-4.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-5.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-6.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-7.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-8.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-9.root',
       'gsiftp://hepcms-gridftp.umd.edu//mnt/hadoop/cms/store/group/EMJRunII/2017/step4_MINIAOD_mMed-1400_mDark-20_kappa-0p3_aligned-down_n-500_part-10.root',
] )
