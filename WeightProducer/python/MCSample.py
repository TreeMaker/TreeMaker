from TreeMaker.WeightProducer.MCSampleValues import MCSampleHelper,MCSampleValuesHelper

class MCSample():

    '''
    Example use:
from TreeMaker.WeightProducer.MCSample import MCSample
m = MCSample("WJetsToLNu_HT-70To100_13TeV","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10139950, 0)
n = MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10139950, 0)
print m
print n
    '''

    from TreeMaker.WeightProducer.SVJxsecs import SVJxsecs
    __helper = MCSampleHelper()
    __val_helper = MCSampleValuesHelper(SVJxsecs)

    def __init__(self, name, production, mcVersion, Method, NumberEvtsTotal, WrongPU = False, NumberEvtsDiff = None):
        self.name = name
        self.process = self.__helper.get_minimal_name(self.name)
        self.production = production
        self.mcVersion = mcVersion
        self.year = self.__helper.get_year(self.mcVersion)
        self.energy = self.__helper.get_cm_energy_by_year(self.year)
        self.Method = Method
        self.XS = self.__val_helper.get_xs(self.process,self.year,self.energy)
        self.kFactor = self.__val_helper.get_kfactor(self.process,self.year)
        self.NumberEvtsTotal = NumberEvtsTotal
        self.WrongPU = WrongPU
        self.NumberEvtsDiff = NumberEvtsTotal if NumberEvtsDiff==None else NumberEvtsDiff

    def get_effective_lumi(self):
        '''
        NumberEvtsTotal = NumberEvtsPos + NumberEvtsNeg
        NumberEvtsDiff = NumberEvtsPos - NumberEvtsNeg
        NumberEvtsTotal - NumberEvtsDiff = 2 * NumberEvtsNeg
        ==>NumberEvtsNeg = (NumberEvtsTotal - NumberEvtsDiff) / 2
        lumi_eff = N_all/xs * (1-2*(N_neg/N_all))^2
        '''
        NumberEvtsNeg = (self.NumberEvtsTotal - self.NumberEvtsDiff)/2.0
        return (self.NumberEvtsTotal/self.XS)*((1.0-(2.0*(NumberEvtsNeg/self.NumberEvtsTotal))) ** 2)

    def __repr__(self):
        rep = ""
        if self.NumberEvtsTotal==self.NumberEvtsDiff:
            rep = "%s(%r, %r, %r, %r, %i, %r)" % (self.__class__.__name__, self.name,self.production,self.mcVersion,self.Method,self.NumberEvtsTotal,self.WrongPU)
        else:
            rep = "%s(%r, %r, %r, %r, %i, %r, %i)" % (self.__class__.__name__, self.name,self.production,self.mcVersion,self.Method,self.NumberEvtsTotal,self.WrongPU,self.NumberEvtsDiff)
        return rep

    def __str__(self):
        dict_of_members = self.__dict__
        list_of_keys = dict_of_members.keys()
        list_of_values = dict_of_members.values()
        max_len_keys = max(len(str(x)) for x in list_of_keys)
        max_len_values = max(len(str(x)) for x in list_of_values)
        key_format="{:<"+str(max_len_keys)+"}"
        value_format="{:<"+str(max_len_values)+"}"
        rep_format = "MCSample("
        for ikey, key in enumerate(list_of_keys):
            if ikey != len(list_of_keys)-1:
                rep_format += (key_format+": "+value_format)
                rep_format += ("\n{:<9}")
            else:
                rep_format += (key_format+": {:<"+str(len(str(self.NumberEvtsDiff)))+"}")
                rep_format += ")"
        return rep_format.format('name',self.name,' ','process',self.process,' ', 'production',self.production,' ','mcVersion',self.mcVersion,' ', \
                                 'year',self.year,' ','energy',self.energy,' ','Method',self.Method,' ','XS',self.XS,' ','kFactor',self.kFactor,' ', \
                                 'NumberEvtsTotal',self.NumberEvtsTotal,' ','WrongPU',self.WrongPU,' ','NumberEvtsDiff',self.NumberEvtsDiff)
