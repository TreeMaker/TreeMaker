import FWCore.ParameterSet.Config as cms
import os
import tarfile

def getEventListFilter(fileName):
    # create filter
    EventListFilter = cms.EDFilter('EventListFilter',
        inputFileList = cms.string(''),
        TagMode = cms.bool(True)
    )
    
    #dict of datasets & corresponding tar files
    cur_dir = os.getcwd()
    tar_dir = "data";
    datasets = {
        "DoubleEG"       : [ "DoubleEG_Oct29.tar.gz"       , "eventlist_DoubleEG_csc2015.txt"       ],
        "DoubleMuon"     : [ "DoubleMuon_Oct29.tar.gz"     , "eventlist_DoubleMuon_csc2015.txt"     ],
        "HTMHT"          : [ "HTMHT_Oct29.tar.gz"          , "eventlist_HTMHT_csc2015.txt"          ],
        "JetHT"          : [ "JetHT_Oct29.tar.gz"          , "eventlist_JetHT_csc2015.txt"          ],
        "MET"            : [ "MET_Oct29.tar.gz"            , "eventlist_MET_csc2015.txt"            ],
        "SingleElectron" : [ "SingleElectron_Oct29.tar.gz" , "eventlist_SingleElectron_csc2015.txt" ],
        "SingleMuon"     : [ "SingleMuon_Oct29.tar.gz"     , "eventlist_SingleMuon_csc2015.txt"     ],
        "SinglePhoton"   : [ "SinglePhoton_Oct29.tar.gz"   , "eventlist_SinglePhoton_csc2015.txt"   ],
    }
    
    #find the right dataset
    for n, f in datasets.iteritems():
        if n in fileName:
            #go to data directory
            os.chdir(tar_dir)
            #untar
            tfile = tarfile.open(f[0],'r:gz')
            tfile.extractall('.')
            #set txt list name
            EventListFilter.inputFileList = cms.string(tar_dir+"/"+f[1])
            print "Using event list filter: "+tar_dir+"/"+f[1]
            #go back to working directory
            os.chdir(cur_dir)
            break

    return EventListFilter