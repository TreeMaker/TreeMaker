import FWCore.ParameterSet.Config as cms

# basically a copy of https://github.com/cms-sw/cmssw/blob/master/Configuration/StandardSequences/python/Eras.py

class TMEras(object):
    def __init__(self):
        allEras = [
            'TMUL2016',
            'TMUL2016APV',
            'TMUL2017',
            'TMUL2018',
        ]

        for e in allEras:
            eObj=getattr(__import__('TreeMaker.TreeMaker.Era_'+e+'_cff',globals(),locals(),[e],0),e)
            self.addEra(e,eObj)

    def addEra(self,name,obj):
        setattr(self,name,obj)


TMeras = TMEras()
