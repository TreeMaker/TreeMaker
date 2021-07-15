import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/110000/060BBD80-C221-6D45-BF9F-E64DC3DBC792.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/110000/8857AD97-EB0C-7444-A03D-D817A3139A9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/110000/D7BD81FC-B4F6-F743-93AD-1D6C00B7ADA3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/0650AE8F-9D66-2D40-8178-61198BF76ACC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/09BC839D-E0CF-AD4F-8D4D-B2108618A2AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/0DDA7C45-E5AA-2F42-BE5F-D3439F28F599.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/1239711C-B615-B441-AF37-5DE0C128F607.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/14CA78E0-948A-8043-ABA0-1DFE2CAE6630.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/1AB88291-9EA4-544E-BC42-F4D4B4DDB6C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/1D160D54-2BE5-AC4A-A9B5-44C1AE909930.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/2C468363-B7BB-D54B-9B7C-30AC5CC75712.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/43EED26D-3152-3C46-BFC4-79970D8CC521.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/4CEB55AB-76AB-364D-AAB5-070E2404ABB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/4E840658-A19B-2548-A5B1-F0A10B1F8509.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/5684B087-18BD-BB44-BB45-1EC3B95EE6B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/573FB15D-849D-D34B-9CB9-FCA96D8D6788.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/57D2B1B2-679A-5D42-8D73-8DEFDB5CCEBE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/5A49D4A4-2E1B-7447-9549-CC7119308F76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/5D7C410A-FADF-E843-9751-0F0B63E868D6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/64B90229-403A-7446-AAAD-777B68C42231.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/66289C40-10A9-6043-ACF8-45EA93AD6836.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/684C390F-B5E1-1D48-BBBF-F10AFA5FC434.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/688EB05D-996E-4B43-9DD7-EC43C1D3E7F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/6BAE57A9-ADE5-A740-AD0C-AE0F5A256AF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/7482CDCE-051E-9041-9B47-74603152E9E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/79E679E5-849A-3A42-A483-0516890B6843.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/8882F818-22BE-6840-AA7A-7AD6B43AF5E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/91B7EC39-BFE9-BB48-B746-E18B9534873B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/9B36A593-98F5-F841-85F4-D4737A7032C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/A32FE447-EFCD-8342-BE53-60D3430873C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/A5914BF6-420D-7048-AA9E-501AC4656F76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/A8ADD240-CFD3-9449-A780-58C6E0E49513.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/B184769F-E30D-0D43-8EA4-8CCBEF6F3537.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/B2EF3544-DF67-4D41-B2BE-3317A7DF0F34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/B9525794-AF0C-D14D-BB47-C9E9B975DAEF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/BAD33A15-0003-E64B-86C3-6F34185105A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/BC392D6F-84DE-5D4C-922C-4C8BBDBD9078.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/BDF8CD60-5DE7-9741-9106-D880D42CF6A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C24E75EB-100E-9B4D-A32E-FAFE2C31E03F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C5CF6305-B609-A648-BA08-80BE1871AE2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/C5F51299-93BA-A244-966B-67EC825B4320.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/CDE62126-893D-4B4A-BC53-9E401EEDB7FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/D1C07B52-83FD-954B-9F29-158BFC8A895F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/D752B65E-E252-E248-9C67-206EB022AD6D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/EA9AD27F-6AAB-9F47-BC42-CDF286EF2B04.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/280000/EE2139DD-05D9-FA44-AE68-CA5228076BD5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/1CC0B00F-580C-214A-9461-F59068566143.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/2833639E-298F-FD43-BEA0-A293C3CD836C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/98946B6D-7574-654F-B9DB-C9C4EC1386BD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/30000/CE49BB26-4B25-DD44-ADEA-F6872480B1A6.root',
] )
