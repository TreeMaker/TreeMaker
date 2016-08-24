import os
import subprocess
import array
from optparse import OptionParser
import FWCore.ParameterSet.Config as cms

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

def DtoF(file,get):
    hD = file.Get(get)
    hF = TH1F()
    hD.Copy(hF)
    return hF

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-o", "--outname", dest="outname", default="PileupHistograms.root", help="output filename for PU histos (default = %default)")
    parser.add_option("-j", "--json", dest="json", default="data/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt", help="golden JSON for data (default = %default)")
    parser.add_option("-l", "--latest", dest="latest", default="data/pileup_latest.txt", help="latest pileup file (default = %default)")
    parser.add_option("-s", "--scenario", dest="scenario", default="SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi", help="CMSSW python file for pileup scenario (default = %default)")
    parser.add_option("-m", "--minbias", dest="minbias", default=71300, help="minbias xsec in mb (default = %default)")
    parser.add_option("-u", "--uncertainty", dest="uncertainty", default=0.0485, help="minbias xsec uncertainty (default = %default)")
    parser.add_option("-b", "--nbins", dest="nbins", default=50, help="max number of bins for histos (default = %default)")
    (options, args) = parser.parse_args()

    from ROOT import *
    
    # get scenario
    mix = getattr(__import__(options.scenario,fromlist=["mix"]),"mix")
    probvalue = mix.input.nbPileupEvents.probValue
    
    # generate pileup histograms in data
    minbias = float(options.minbias)
    uncertainty = float(options.uncertainty)
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(minbias)+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" RA2CentralPileupHistogram.root")
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(minbias*(1+uncertainty))+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" RA2UpPileupHistogram.root")
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(minbias*(1-uncertainty))+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" RA2DownPileupHistogram.root")
    
    # open files
    fc = TFile.Open("RA2CentralPileupHistogram.root","read")
    fup = TFile.Open("RA2UpPileupHistogram.root","read")
    fdown = TFile.Open("RA2DownPileupHistogram.root","read")
    fout = TFile.Open(options.outname,"RECREATE")
    
    # get histos
    hdata_central = DtoF(fc,"pileup")
    hdata_up = DtoF(fup,"pileup")
    hdata_down = DtoF(fdown,"pileup")

    # scale histos
    hdata_central.Scale(1/hdata_central.Integral(1,int(options.nbins)))
    hdata_up.Scale(1/hdata_up.Integral(1,int(options.nbins)))
    hdata_down.Scale(1/hdata_down.Integral(1,int(options.nbins)))

    # save histos
    hdata_central.SetName("data_pu_central")
    hdata_up.SetName("data_pu_up")
    hdata_down.SetName("data_pu_down")
    hdata_central.Write()
    hdata_up.Write()
    hdata_down.Write()

    # MC histo
    hMC25ns = TH1F("hMC25ns", "", int(options.nbins), 0, int(options.nbins))
    for b in xrange(0,int(options.nbins)):
        hMC25ns.SetBinContent(b+1,probvalue[b] if b < len(probvalue) else 0)
        hMC25ns.SetBinError(b+1,0)
    hMC25ns.Scale(1/hMC25ns.Integral(1,int(options.nbins)))
    hMC25ns.Write()
    
    # divide histos
    hPUWeightsCentral = hMC25ns.Clone("pu_weights_central")
    hPUWeightsUp = hMC25ns.Clone("pu_weights_up")
    hPUWeightsDown = hMC25ns.Clone("pu_weights_down")
    hPUWeightsCentral.Divide(hdata_central, hMC25ns, 1., 1.)
    hPUWeightsUp.Divide(hdata_up, hMC25ns, 1., 1.)
    hPUWeightsDown.Divide(hdata_down, hMC25ns, 1., 1.)
    hPUWeightsCentral.Write()
    hPUWeightsUp.Write()
    hPUWeightsDown.Write()
    
    fout.Close()
