import FWCore.ParameterSet.Config as cms

PDFWeightProducer = cms.EDProducer("PDFWeightProducer",
    nScales = cms.uint32(9),
    nPDFs = cms.uint32(102),
    nPSs = cms.uint32(14),
    nQCD = cms.uint32(0),
    nEM = cms.uint32(0),
    scaleNames = cms.vstring('nominal','LHE, id = 1016,  MUF=2.0  ','LHE, id = 1031,  MUF=0.5  ','LHE, id = 1006,  MUR=2.0  ','LHE, id = 1021,  MUR=2.0 MUF=2.0  ','LHE, id = 1036,  MUR=2.0 MUF=0.5  ','LHE, id = 1011,  MUR=0.5  ','LHE, id = 1026,  MUR=0.5 MUF=2.0  ','LHE, id = 1041,  MUR=0.5 MUF=0.5  '),
    psNames = cms.vstring('nominal','Baseline','isr:murfac=0.707','fsr:murfac=0.707','isr:murfac=1.414','fsr:murfac=1.414','isr:murfac=0.5','fsr:murfac=0.5','isr:murfac=2.0','fsr:murfac=2.0','isr:murfac=0.25','fsr:murfac=0.25','isr:murfac=4.0','fsr:murfac=4.0'),
    normalize = cms.bool(True),
    pythiaSettings = cms.vstring(),
    debug = cms.bool(False),
)
