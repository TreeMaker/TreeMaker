from jobSubmitterNeff import jobSubmitterNeff

def submitJobs():  
    mySubmitter = jobSubmitterNeff()
    mySubmitter.run()
    
if __name__=="__main__":
    submitJobs()
