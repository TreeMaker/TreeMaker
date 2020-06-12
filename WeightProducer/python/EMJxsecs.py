import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
XSValues = MCSampleValuesHelper.XSValues
EMJxsecs = {
"mMed-1000": {"CrossSection":XSValues(XS_13TeV=0.020490, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1200": {"CrossSection":XSValues(XS_13TeV=0.005100, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1400": {"CrossSection":XSValues(XS_13TeV=0.001419, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1500": {"CrossSection":XSValues(XS_13TeV=0.000771, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1600": {"CrossSection":XSValues(XS_13TeV=0.000426, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
}