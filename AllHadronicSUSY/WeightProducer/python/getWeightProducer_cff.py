# $Id: getWeightProducer_cff.py,v 1.7 2012/11/05 14:58:14 mschrode Exp $
#
# Returns a WeightProducer module that knows at runtime
# which data sample is produced and thus, what weights
# are required. The function can be used as follows:
#
#    from RA2Classic.WeightProducer.getWeightProducer_cff import getWeightProducer
#    process.WeightProducer = getWeightProducer(process.source.fileNames[0])


import FWCore.ParameterSet.Config as cms

def getWeightProducer(fileName):

   mcVersion = "none"                  # For lumi and PU weights
   applyWeight = False


   ## --- Setup default WeightProducer ------------------------------------

   # Import weightProducer
   from AllHadronicSUSY.WeightProducer.weightProducer_cfi import weightProducer

   # Set default values to produce an event weight of 1
   weightProducer.weight = cms.double(1.0)
   weightProducer.Method = cms.string("Constant")
   weightProducer.LumiScale = cms.double(1.0)
   weightProducer.FileNamePUDataDistribution = cms.string("NONE")
   weightProducer.PU = cms.int32(0)

   # 13 TeV miniAOD samples - CSA14
    
   # backgrounds
    
   if "TTJets_MSDecaysCKM_central_Tune4C_13TeV" in fileName and "PU40bx25_POSTLS170_V5-v2" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(745.16)
      weightProducer.NumberEvts = cms.double(25478151)
      print "TTJets_MSDecaysCKM_central_Tune4C_13TeV_PU50x25_V5_v2 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TTJets_MSDecaysCKM_central_Tune4C_13TeV" in fileName and "PU20bx25_POSTLS170_V5-v2" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(818.8)
      weightProducer.NumberEvts = cms.double(25474122)
      print "TTJets_MSDecaysCKM_central_Tune4C_13TeV_PU20bx250_V5-v2 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
        
   if "WJetsToLNu_HT-100to200_Tune4C_13TeV" in fileName and "PU20bx25_POSTLS170_V5-v2" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(1817.0)
      weightProducer.NumberEvts = cms.double(5229141)
      print "WJetsToLNu_HT-100to200_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
	
   if "WJetsToLNu_HT-200to400_Tune4C_13TeV" in fileName and "PU20bx25_POSTLS170_V5-v1" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(471.6)
      weightProducer.NumberEvts = cms.double(4933933)
      print "WJetsToLNu_HT-200to400_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
        
   if "WJetsToLNu_HT-400to600_Tune4C_13TeV" in fileName and "PU20bx25_POSTLS170_V5-v1" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(55.61)
      weightProducer.NumberEvts = cms.double(4642823)
      print "WJetsToLNu_HT-400to600 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "WJetsToLNu_HT-600toInf_Tune4C_13TeV" in fileName and "PU20bx25_POSTLS170_V5-v1" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(18.81)
      weightProducer.NumberEvts = cms.double(4634811)
      print "WJetsToLNu_HT-600toInf : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-470to600_Tune4C_13TeV_pythia8" in fileName and "PU20bx25_POSTLS170_V5-v1" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(587.1)
      weightProducer.NumberEvts = cms.double(2907137)
      print "QCD_Pt-470to600_Tune4C_13TeV_pythia8 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   #signal

   if "SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0856418)
      weightProducer.NumberEvts = cms.double(100322)
      print "SMS-T1tttt_2J_mGl-1200_mLSP-800 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0141903)
      weightProducer.NumberEvts = cms.double(105679)
      print "SMS-T1tttt_2J_mGl-1500_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.325388)
      weightProducer.NumberEvts = cms.double(97584)
      print "T1bbbb_2J_mGl-1000_mLSP-900 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0141903)
      weightProducer.NumberEvts = cms.double(105964)
      print "SMS-T1bbbb_2J_mGl-1500_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.325388)
      weightProducer.NumberEvts = cms.double(97513)
      print "SMS-T1qqqq_2J_mGl-1000_mLSP-800 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU_S14_POSTLS170_V6AN1" in fileName:
      mcVersion = "Spring14dr"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0252977)
      weightProducer.NumberEvts = cms.double(103943)
      print "SMS-T1qqqq_2J_mGl-1400_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TTJets_MSDecaysCKM_central_Tune4C_13TeV" in fileName and "PU40bx25_POSTLS170_V5-v2" in fileName:
      mcVersion = "Spring14miniaod"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(745.16)
      weightProducer.NumberEvts = cms.double(25478151)
      print "TTJets_MSDecaysCKM_central_Tune4C_13TeV_PU50x25_V5_v2 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   # 13 TeV miniAOD samples - PHYS14

   # signal
   if "SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double( 0.0252977 )
      weightProducer.NumberEvts = cms.double(102891)
      print "SMS-T1qqqq_2J_mGl-1400_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
   if "SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double( 0.325388 )
      weightProducer.NumberEvts = cms.double(96681)
      print "SMS-T1qqqq_2J_mGl-1000_mLSP-800 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.325388)
      weightProducer.NumberEvts = cms.double(97584)
      print "T1bbbb_2J_mGl-1000_mLSP-900 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0141903)
      weightProducer.NumberEvts = cms.double(105964)
      print "SMS-T1bbbb_2J_mGl-1500_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0856418)
      weightProducer.NumberEvts = cms.double(100322)
      print "SMS-T1tttt_2J_mGl-1200_mLSP-800 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_tsg_PHYS14" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0141903)
      weightProducer.NumberEvts = cms.double(105679)
      print "SMS-T1tttt_2J_mGl-1500_mLSP-100 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   # backgrounds
   
   # QCD MG

   if "QCD_HT_250To500_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(6.705e+5)
      weightProducer.NumberEvts = cms.double(2668172)
      print "QCD_HT-250To500_13TeV-madgraph : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_HT-500To1000_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(2.674e+4)
      weightProducer.NumberEvts = cms.double(4063345)
      print "QCD_HT-500To1000_13TeV-madgraph : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_HT_1000ToInf_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(769.7)
      weightProducer.NumberEvts = cms.double(1464453)
      print "QCD_HT-1000ToInf_13TeV-madgraph : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   # QCD Pythia

   if "QCD_Pt-15to30_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(1837410000)
      weightProducer.NumberEvts = cms.double(1986539)
      print "QCD_Pt-15to30-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-30to50_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(161500000)
      weightProducer.NumberEvts = cms.double(1988880)
      print "QCD_Pt-30to50-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-50to80_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(22110000)
      weightProducer.NumberEvts = cms.double(2000338)
      print "QCD_Pt-50to80-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-80to120_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(3000114)
      weightProducer.NumberEvts = cms.double(2000340)
      print "QCD_Pt-80to120-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-120to170_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(493200)
      weightProducer.NumberEvts = cms.double(2001453)
      print "QCD_Pt-120to170-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-170to300_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(120300)
      weightProducer.NumberEvts = cms.double(2000704)
      print "QCD_Pt-120to170-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-300to470_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(7475)
      weightProducer.NumberEvts = cms.double(1986177)
      print "QCD_Pt-300to470-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-470to600_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(587.1)
      weightProducer.NumberEvts = cms.double(2001071)
      print "QCD_Pt-470to600-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-600to800_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(167)
      weightProducer.NumberEvts = cms.double(1997744)
      print "QCD_Pt-600to800-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-800to1000_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(28.25)
      weightProducer.NumberEvts = cms.double(1000065)
      print "QCD_Pt-800to1000-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-1000to1400_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(8.195)
      weightProducer.NumberEvts = cms.double(500550)
      print "QCD_Pt-1000to1400-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-1400to1800_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_castor_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.7346)
      weightProducer.NumberEvts = cms.double(199627)
      print "QCD_Pt-1400to1800-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-1800to2400_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.102)
      weightProducer.NumberEvts = cms.double(200079)
      print "QCD_Pt-1800to2400-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "QCD_Pt-2400to3200_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.0064)
      weightProducer.NumberEvts = cms.double(200453)
      print "QCD_Pt-2400to3200-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
   
   if "QCD_Pt-3200_Tune4C_13TeV" in fileName and "PU20bx25_trkalmb_PHYS14_25_V1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(0.000163)
      weightProducer.NumberEvts = cms.double(200200)
      print "QCD_Pt-3200-pythia : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
   
   if "TBarToLeptons_t-channel_Tune4C_CSA14_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(61.6)
      weightProducer.NumberEvts = cms.double(1999800)
      print "TBarToLeptons_t-channel_Tune4C_CSA14_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TBarToLeptons_s-channel-CSA14_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(1.0)
      weightProducer.NumberEvts = cms.double(250000)
      print "TBarToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TToLeptons_t-channel-CSA14_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(103.4)
      weightProducer.NumberEvts = cms.double(3991000)
      print "TToLeptons_t-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TToLeptons_s-channel-CSA14_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(2.0)
      weightProducer.NumberEvts = cms.double(500000)
      print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TTZJets_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(2.232)
      weightProducer.NumberEvts = cms.double(249275)
      print "TTJets_MSDecaysCKM_central_Tune4C_13TeV_PU50x25_V5_v2 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TTWJets_Tune4C_13TeV-madgraph-tauola" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(1.152)
      weightProducer.NumberEvts = cms.double(246521)
      print "TTWJets_Tune4C_13TeV-madgraph-tauola : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "T_tW-channel-DR_Tune4C_13TeV-CSA14" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(35.0)
      weightProducer.NumberEvts = cms.double(986100)
      print "T_tW-channel-DR_Tune4C_13TeV-CSA14 : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "TTJets_MSDecaysCKM_central_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(806.1)
      weightProducer.NumberEvts = cms.double(25446993)
      print "TTJets_MSDecaysCKM_central_Tune4C_13TeV : '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "WJetsToLNu_HT-100to200_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(1817.0)
      weightProducer.NumberEvts = cms.double(5262265)
      print "WJetsToLNu_HT-100to200_Tune4C_13TeV Phys14DR: '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "WJetsToLNu_HT-200to400_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(471.6)
      weightProducer.NumberEvts = cms.double(4936077)
      print "WJetsToLNu_HT-200to400_Tune4C_13TeV Phys14DR: '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "WJetsToLNu_HT-400to600_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(55.61)
      weightProducer.NumberEvts = cms.double(4640594)
      print "WJetsToLNu_HT-400to600_Tune4C_13TeV Phys14DR: '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "WJetsToLNu_HT-600toInf_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(18.81)
      weightProducer.NumberEvts = cms.double(4581841)
      print "WJetsToLNu_HT-600toInf_Tune4C_13TeV Phys14DR: '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "ZJetsToNuNu_HT-100to200_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(372.6)
      weightProducer.NumberEvts = cms.double(4986424)
      print "ZJetsToNuNu_HT-100to200_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
				
   if "ZJetsToNuNu_HT-200to400_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(100.8)
      weightProducer.NumberEvts = cms.double(4546470)
      print "ZJetsToNuNu_HT-200to400_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "ZJetsToNuNu_HT-400to600_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v2" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(11.99)
      weightProducer.NumberEvts = cms.double(4433784)
      #print "ZJetsToNuNu_HT-400to600_Tune4C_13TeV: UPDATE NUMBER OF EVENTS NOT YET AVAILABLE '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)

   if "ZJetsToNuNu_HT-600toInf_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(4.113)
      weightProducer.NumberEvts = cms.double(4463806)
      print "ZJetsToNuNu_HT-600toInf_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
      
   if "DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(194.3)
      weightProducer.NumberEvts = cms.double(4054159)
      print "DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
      
   if "DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(52.24)
      weightProducer.NumberEvts = cms.double(4666496)
      print "DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
      
   if "DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(6.546)
      weightProducer.NumberEvts = cms.double(4931372)
      print "DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
      
   if "DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
      mcVersion = "Phys14DR"
      weightProducer.Method     = cms.string("Constant")
      weightProducer.XS         = cms.double(2.179)
      weightProducer.NumberEvts = cms.double(4493574)
      print "DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV '"+fileName+"'"
      applyWeight = True
      weightProducer.weight = cms.double(-1.)
        
   ## --- PU Reweighting and Lumi ------------------------------------------------
         
   if mcVersion == "Summer12_5_3_X":
      weightProducer.weight = cms.double(-1.)
      weightProducer.Lumi = cms.double(19466)
      weightProducer.PU = cms.int32(3) # PU S10
      weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/WeightProducer/data/DataPileupHistogram_RA2Summer12_190456-208686_ABCD.root")
      applyWeight = True
	
   if applyWeight:
      print "Setup WeightProducer for '"+fileName+"'"

   return weightProducer
