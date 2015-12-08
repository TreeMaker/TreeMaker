import FWCore.ParameterSet.Config as cms
import os
import subprocess

def getEventListFilter(fileName,date,filter):
    # create filter
    EventListFilter = cms.EDFilter('EventListFilter',
        inputFileList = cms.string(''),
        TagMode = cms.bool(True)
    )
    
    #get current and data dirs
    cur_dir = os.getcwd()
    tar_dir = "data";

    #dict of datasets & corresponding tar files
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
            #make gzip name
            tname = filter+"_"+date+".txt.gz"
            #set txt list name
            listname = filter+".txt"
            #unzip
            subprocess.Popen("gunzip -c "+tname+" > "+listname,shell=True)
            EventListFilter.inputFileList = cms.string(tar_dir+"/"+listname)
            print "Using event list filter: "+tar_dir+"/"+listname
            #go back to working directory
            os.chdir(cur_dir)
            break

    return EventListFilter