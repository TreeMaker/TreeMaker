import FWCore.ParameterSet.Config as cms

#Three options to define/calculate an event weight:
weightProducer = cms.EDProducer('WeightProducer',
   #Option 1:
   weight = cms.double( -1.0 ),          # If >0 use this weight

   #Option 2:
   weightName  = cms.InputTag('weight'), # Name of an existing weight-variable in the event

   #Option 3: Weight computed from num evts, xs, and target lumi
   Method = cms.string(""),              # "Constant" to calculate a weight = L*XS/N
   XS = cms.double(1.),                  # XS in pb
   NumberEvts = cms.double(-1.),         
   Lumi = cms.double(1.),              # Lumi in 1/pb

   # Data PU distribution. If a file name is specified,
   # a multiplicative PU weight factor is applied.
   FileNamePUDataDistribution = cms.string("NONE"),
)
