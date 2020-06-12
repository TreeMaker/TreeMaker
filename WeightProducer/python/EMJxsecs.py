import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
XSValues = MCSampleValuesHelper.XSValues
EMJxsecs = {
"mMed-1000": {"CrossSection":XSValues(XS_13TeV=0.02049) },
"mMed-1200": {"CrossSection":XSValues(XS_13TeV=0.0051) },
"mMed-1400": {"CrossSection":XSValues(XS_13TeV=0.001419) },
"mMed-1500": {"CrossSection":XSValues(XS_13TeV=0.000771) },
"mMed-1600": {"CrossSection":XSValues(XS_13TeV=0.000426) }
}