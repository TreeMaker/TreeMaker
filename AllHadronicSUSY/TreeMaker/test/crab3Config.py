from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'PU20bx25_TTJets'
#config.General.requestName = 'T1tttt_2J_mGl-1500_mLSP_100_PU20bx25'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runMakeTreeFromMiniAOD_cfg.py'
#config.JobType.allowNonProductionCMSSW = False 
config.JobType.allowUndistributedCMSSW = False # Parameter JobType.allowNonProductionCMSSW has been renamed to JobType.allowUndistributedCMSSW

config.section_("Data")
config.Data.inputDataset = '/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM'

config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'  # Parameter Data.dbsUrl has been renamed to Data.inputDBS
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
config.Data.publishDataName = 'Spring14miniaod-141029_PU40bx50_PLS170_V6AN2-v1'

#config.Data.outlfn = '/store/user/lpcsusyhad/CSA14/PU_S14_TTJets_MSDecaysCKM_with_grooming/'
#config.Data.outLFN = '/store/user/borzou/ntuples/Apr02'  # Parameter Data.outlfn has been renamed to Data.outLFN
config.Data.outLFNDirBase = '/store/user/borzou/ntuples/Apr02'  # Data.outLFN has been renamed to Data.outLFNDirBase

config.Data.ignoreLocality = True
#config.Data.totalUnits = 2 ##To get full statistics comment this out.

config.section_("Site")
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Baylor'
#KH (this whitelisting is not necessary. we can use any T2/T3 for running jobs. we can still send output to Baylor) config.Site.whitelist = ['T3_US_Baylor']

config.General.transferLogs=True 
