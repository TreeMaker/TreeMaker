import FWCore.ParameterSet.Config as cms
import os
import tarfile

def getEventListFilter(fileName,date,filter):
    # create filter
    EventListFilter = cms.EDFilter('EventListFilter',
        inputFileList = cms.string(''),
        TagMode = cms.bool(True)
    )
    
    #dict of datasets & corresponding tar files
    cur_dir = os.getcwd()
    tar_dir = "data";
    datasets = [
        "DoubleEG"      ,
        "DoubleMuon"    ,
        "HTMHT"         ,
        "JetHT"         ,
        "MET"           ,
        "SingleElectron",
        "SingleMuon"    ,
        "SinglePhoton"  ,
    ]
    
    #find the right dataset
    for n in datasets:
        if n in fileName:
            #go to data directory
            os.chdir(tar_dir)
            #make tar name
            tname = n+"_"+date+".tar.gz"
            #untar
            tfile = tarfile.open(tname,'r:gz')
            tfile.extractall('.')
            #set txt list name
            listname = n+"_"+filter+".txt"
            EventListFilter.inputFileList = cms.string(tar_dir+"/"+listname)
            print "Using event list filter: "+tar_dir+"/"+listname
            #go back to working directory
            os.chdir(cur_dir)
            break

    return EventListFilter