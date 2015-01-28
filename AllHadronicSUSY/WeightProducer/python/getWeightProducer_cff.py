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



    ## --- Adjust WeightProducer for Summer12_5_2_X MC samples --------------------

    # For ttbar
    if "TTJets_TuneZ2star_8TeV-madgraph-tauola" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(234)
        weightProducer.NumberEvts = cms.double(6736135)         

    # For WJets
    if "WJetsToLNu_HT-250To300_8TeV-madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(57.26)
        weightProducer.NumberEvts = cms.double(1634582)         
    if "WJetsToLNu_HT-300To400_8TeV-madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(45.68)
        weightProducer.NumberEvts = cms.double(1698744)         
    if "WJetsToLNu_HT-400ToInf_8TeV-madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(30.08)
        weightProducer.NumberEvts = cms.double(1647807)         

    # For ZJets
    if "ZJetsToNuNu_50_HT_100_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(452.75)
        weightProducer.NumberEvts = cms.double(4053786)         
    if "ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(190.39)
        weightProducer.NumberEvts = cms.double(4416646)         
    if "ZJetsToNuNu_200_HT_400_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12-PU_S7_START52_V9-v3" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(49.28)
        weightProducer.NumberEvts = cms.double(5066608)         
    if "ZJetsToNuNu_400_HT_inf_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12-PU_S7_START52_V9-v1" in fileName:
        mcVersion = "Summer12_5_2_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(6.26)
        weightProducer.NumberEvts = cms.double(1006928)         

# For QCD
    if "QCD_Pt-15to3000_TuneZ2star_Flat_8TeV_pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method = cms.string("PtHat")
        weightProducer.XS = cms.double(2.99815997e+10)
        weightProducer.NumberEvts = cms.double(9991674)
        weightProducer.Exponent = cms.double(-4.5)
    if "QCD_HT-100To250_TuneZ2star_8TeV-madgraph-pythia" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method = cms.string("Constant")
        weightProducer.XS = cms.double(1.036e+7)
        weightProducer.NumberEvts = cms.double(50129518)
    if "QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method = cms.string("Constant")
        weightProducer.XS = cms.double(276000.0)
        weightProducer.NumberEvts = cms.double(27062078)
    if "QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method = cms.string("Constant")
        weightProducer.XS = cms.double(8426.0)
        weightProducer.NumberEvts = cms.double(30599292)
    if "QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method = cms.string("Constant")
        weightProducer.XS = cms.double(204.0)
        weightProducer.NumberEvts = cms.double(13843863)
        

    ## --- Adjust WeightProducer for Summer12_5_3_X MC samples --------------------

    # For ttbar
    if "TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(234)
        weightProducer.NumberEvts = cms.double(6923750)
    if "TT_CT10_TuneZ2star_8TeV-powheg-tauola" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v2" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(234)
        weightProducer.NumberEvts = cms.double(21675970)
    if "TTJets_SemiLeptMGDecays_8TeV-madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A_ext-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(102.50) # BR(lh) = 0.438048
        weightProducer.NumberEvts = cms.double(25424818)

    if "TTJets_FullLeptMGDecays_8TeV-madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v2" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(24.56) # BR(ll) = 0.104976
        weightProducer.NumberEvts = cms.double(12119013)
	
    if "TTJets_HadronicMGDecays_8TeV-madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(106.94) # BR(ll) = 0.104976
        weightProducer.NumberEvts = cms.double(31223821)

        # BR(hh) = 0.456976
        

    # For wpj
    if "WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v2" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(36257.2)
        weightProducer.NumberEvts = cms.double(57709905)
    if "WJetsToLNu_HT-400ToInf_8TeV-madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(30.08)
        weightProducer.NumberEvts = cms.double(6471225)
	
    if "WJetsToLNu_HT-300To400_8TeV-madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(45.68)
        weightProducer.NumberEvts = cms.double(1699486)

    # For ZJets
    if "ZJetsToNuNu_50_HT_100_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(452.75)
        weightProducer.NumberEvts = cms.double(4040980)
    if "ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(190.39)
        weightProducer.NumberEvts = cms.double(4416646)         
    if "ZJetsToNuNu_200_HT_400_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(49.28)
        weightProducer.NumberEvts = cms.double(5055885)         
    if "ZJetsToNuNu_400_HT_inf_TuneZ2Star_8TeV_madgraph" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(6.26)
        weightProducer.NumberEvts = cms.double(1006928)         

    # For QCD
    if "QCD_Pt-15to3000_TuneZ2star_Flat_8TeV_pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("PtHat")
        weightProducer.XS         = cms.double(2.99913994e+10)
        weightProducer.NumberEvts = cms.double(9991674)
        weightProducer.Exponent   = cms.double(-4.5)
    # For WW,ZZ,WZ
    if "WW_TuneZ2star_8TeV_pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(54.838)
        weightProducer.NumberEvts = cms.double(10000000)
    if "WZ_TuneZ2star_8TeV_pythia6" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(33.21)
        weightProducer.NumberEvts = cms.double(10000283)
    if "ZZ_TuneZ2star_8TeV_pythia6_tauola" in fileName and "Summer12_DR53X-PU_S10_START53_V7A-v1" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(8.059)
        weightProducer.NumberEvts = cms.double(9799908)
	#Signal samples
    if "T1qqqq" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(0.0038872)
        weightProducer.NumberEvts = cms.double(31111)
    if "T1qqqqHV" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(0.010005)
        weightProducer.NumberEvts = cms.double(30335)
    if "T2qq" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(0.06397336)
        weightProducer.NumberEvts = cms.double(29289)
    if "T1tttt" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(0.0038872)
        weightProducer.NumberEvts = cms.double(121389)
    if "T5VV" in fileName:
        mcVersion = "Summer12_5_3_X"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(0.0038872)
        weightProducer.NumberEvts = cms.double(30436)
        
    print "---------------------------------------------------------------"
        # 13 TeV miniAOD samples
        #csa14
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
        print "WJetsToLNu_HT-600toIn : '"+fileName+"'"
        applyWeight = True
        weightProducer.weight = cms.double(-1.)     

    if "QCD_Pt-470to600_Tune4C_13TeV_pythia8" in fileName and "PU20bx25_POSTLS170_V5-v1" in fileName:
        mcVersion = "Spring14miniaod"
        weightProducer.Method     = cms.string("Constant")
        weightProducer.XS         = cms.double(587.1)
        weightProducer.NumberEvts = cms.double(2907137)  
        print "WJetsToLNu_HT-600toIn : '"+fileName+"'"
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

                
#phys14
#Signal
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
			weightProducer.XS         = cms.double(0.085)
			weightProducer.NumberEvts = cms.double(100322)  
			print "SMS-T1tttt_2J_mGl-1500_mLSP-100 : '"+fileName+"'"
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

#BKG
    if "QCD_HT-250To500_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(6.705e+5)
			weightProducer.NumberEvts = cms.double(663953)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
			applyWeight = True
            		weightProducer.weight = cms.double(-1.)

    if "QCD_HT-500To1000_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(2.674e+4)
			weightProducer.NumberEvts = cms.double(849033)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
			applyWeight = True
            		weightProducer.weight = cms.double(-1.)
    if "QCD_HT-1000ToInf_13TeV-madgraph" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(769.7)
			weightProducer.NumberEvts = cms.double(333733)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
			applyWeight = True
            		weightProducer.weight = cms.double(-1.)
    if "TBarToLeptons_t-channel_Tune4C_CSA14_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(16.9)
			weightProducer.NumberEvts = cms.double(1999800)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
			applyWeight = True
            		weightProducer.weight = cms.double(-1.)
    if "TBarToLeptons_s-channel-CSA14_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(1.0)
			weightProducer.NumberEvts = cms.double(250000)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
			applyWeight = True
            		weightProducer.weight = cms.double(-1.)
    if "TToLeptons_t-channel-CSA14_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(45.0)
			weightProducer.NumberEvts = cms.double(3991000)  
			print "TToLeptons_s-channel-CSA14_Tune4C_13TeV : '"+fileName+"'"
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
			print "TTJets_MSDecaysCKM_central_Tune4C_13TeV : '"+fileName+"'"
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
    if "ZJetsToNuNu_HT-200to400_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(100.8)
			weightProducer.NumberEvts = cms.double(4546470)  
			print "ZJetsToNuNu_HT-200to400_Tune4C_13TeV '"+fileName+"'"
			applyWeight = True
			weightProducer.weight = cms.double(-1.)
    if "ZJetsToNuNu_HT-400to600_Tune4C_13TeV" in fileName and "PU20bx25_PHYS14_25_V1-v1" in fileName:
			mcVersion = "Phys14DR"
			weightProducer.Method     = cms.string("Constant")
			weightProducer.XS         = cms.double(11.99)
			weightProducer.NumberEvts = cms.double(100)  
			print "ZJetsToNuNu_HT-400to600_Tune4C_13TeV: UPDATE NUMBER OF EVENTS NOT YET AVAILABLE '"+fileName+"'"
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
				
        
    ## --- PU Reweighting and Lumi ------------------------------------------------
         
    if mcVersion == "Summer12_5_3_X":
        weightProducer.weight = cms.double(-1.)
        weightProducer.Lumi = cms.double(19466)
        weightProducer.PU = cms.int32(3) # PU S10
## weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/AdditionalInputFiles/DataPileupHistogram_RA2Summer12_5_2_X_190456-196531_8TeV_PromptReco_WOLowPU.root")
        # grid-control requires additional input files to be in the data directory
        weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/WeightProducer/data/DataPileupHistogram_RA2Summer12_190456-208686_ABCD.root")
        applyWeight = True
	
	## use this for PU SU7
#    if mcVersion == "Summer12_5_3_X":
#        weightProducer.weight = cms.double(-1.)
#        weightProducer.Lumi = cms.double(19466)
#        weightProducer.PU = cms.int32(2) # PU S7
## weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/AdditionalInputFiles/DataPileupHistogram_RA2Summer12_5_2_X_190456-196531_8TeV_PromptReco_WOLowPU.root")
        # grid-control requires additional input files to be in the data directory
        weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/WeightProducer/data/DataPUProfile_2013Jan22_XS69400_PixelLumiCorr_MediumMass.root")
        applyWeight = True
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer

    
