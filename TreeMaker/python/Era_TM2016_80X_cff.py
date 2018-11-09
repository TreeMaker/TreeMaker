import FWCore.ParameterSet.Config as cms

from TreeMaker.TreeMaker.Era_TM2016_cff import TM2016
from TreeMaker.TreeMaker.Era_TM80X_cff import TM80X

TM2016_80X = cms.ModifierChain(TM2016,TM80X)
