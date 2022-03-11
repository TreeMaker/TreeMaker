import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
XSValues = MCSampleValuesHelper.XSValues
EMJxsecs = {
"mMed-1000": {"CrossSection":XSValues(XS_13TeV=0.020490, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1200": {"CrossSection":XSValues(XS_13TeV=0.005100, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1400": {"CrossSection":XSValues(XS_13TeV=0.001419, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1500": {"CrossSection":XSValues(XS_13TeV=0.000771, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") },
"mMed-1600": {"CrossSection":XSValues(XS_13TeV=0.000426, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
"mMed-1800": {"CrossSection":XSValues(XS_13TeV=0.0001353, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
"mMed-2000": {"CrossSection":XSValues(XS_13TeV=4.44e-05, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
"mMed-2200": {"CrossSection":XSValues(XS_13TeV=1.50e-05, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
"mMed-2400": {"CrossSection":XSValues(XS_13TeV=5.13e-06, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
"mMed-2500": {"CrossSection":XSValues(XS_13TeV=3.00e-06, XSSource_13TeV="SUSY XS - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (x3 for color)") }
}
