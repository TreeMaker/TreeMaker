import FWCore.ParameterSet.Config as cms

#Three options to define/calculate an event weight:
weightProducer = cms.EDProducer('WeightProducer',
   #Option 1:
   weight = cms.double( -1.0 ),          # If >0 use this weight

   #Option 2:
   weightName  = cms.InputTag('weight'), # Name of an existing weight-variable in the event

   #Option 3: Weight computed from num evts, xs, and target lumi
   Method = cms.string(""),              # "Constant" to calculate a weight = L*XS/N,
                                         # "PtHat" to calculate a weight from pthat variable for 'flat' samples
   XS = cms.double(1.),                  # XS in pb
   NumberEvts = cms.double(-1.),         
   Lumi = cms.double(100.),              # Lumi in 1/pb
   Exponent = cms.double(-4.5),          # used (only) for 'PtHat'-weighting


   #The final calculated weight is scaled by the following factor.
   #This can be used e.g. to scale the luminosity by +-1sigma.
   LumiScale = cms.double( 1.0 ),

   # Data PU distribution. If a file name is specified,
   # a multiplicative PU weight factor is applied.
   FileNamePUDataDistribution = cms.string("NONE"),
   
   ## use this for different PU scenarios as described at
   ## https://twiki.cern.ch/twiki/bin/view/CMS/Pileup_MC_Gen_Scenarios                 
   ##  0: Flat10
   ##  1: for Fall11
   ##  2: Summer12 S7
   ##  3: Summer12 S10                                
   PU = cms.int32(0)
)
