//
//  RA2bBin.cpp
//  
//
//  Created by Christian Sander on 02/06/15.
//
//

#include "RA2bBin.h"

std::string BinName;

RA2bBin::RA2bBin(std::string BinName_, int Ntries_, int NJets_low_, int NJets_high_, int NBJets_low_, int NBJets_high_, double MHT_low_, double MHT_high_, double HT_low_, double HT_high_, bool DeltaPhiMin_) {

   BinName = BinName_;
   Ntries = Ntries_;
   MHT_low = MHT_low_;
   MHT_high = MHT_high_;
   HT_low = HT_low_;
   HT_high = HT_high_;
   NJets_low = NJets_low_;
   NJets_high = NJets_high_;
   NBJets_low = NBJets_low_;
   NBJets_high = NBJets_high_;
   DeltaPhiMin = DeltaPhiMin_;
   
   count_exp = 0.;
   sumw2_exp = 0.;
   
   count_pred.resize(Ntries);
   sumw2_pred.resize(Ntries);
   
   std::fill(count_pred.begin(), count_pred.end(), 0.);
   std::fill(sumw2_pred.begin(), sumw2_pred.end(), 0.);
   
}

bool RA2bBin::FillPred(int set, int NJets, int NBJets, double MHT, double HT, bool minDeltaPhi, double weight){
   //cout << "0 " << MHT_low << " " << MHT_high << " " << HT_low << " " << HT_high << endl;
   //cout << "1 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   if (HT < HT_low || HT >= HT_high) return false;
   //cout << "2 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   if (MHT < MHT_low || MHT >= MHT_high) return false;
   //cout << "3 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   if (NJets < NJets_low || NJets > NJets_high) return false;
   //cout << "4 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   if (NBJets < NBJets_low || NBJets > NBJets_high) return false;
   //cout << "5 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   if (minDeltaPhi != DeltaPhiMin) return false;
   //cout << "6 " << set << " " << NJets << " " <<NBJets << " " <<MHT << " " <<HT << " " <<minDeltaPhi << " " <<weight << endl;
   count_pred.at(set) += weight;
   sumw2_pred.at(set) += weight*weight;
   return true;
}

bool RA2bBin::FillExp(int NJets, int NBJets, double MHT, double HT, bool minDeltaPhi, double weight){
   if (HT < HT_low || HT >= HT_high) return false;
   if (MHT < MHT_low || MHT >= MHT_high) return false;
   if (NJets < NJets_low || NJets > NJets_high) return false;
   if (NBJets < NBJets_low || NBJets > NBJets_high) return false;
   if (minDeltaPhi != DeltaPhiMin) return false;
   count_exp += weight;
   sumw2_exp += weight*weight;
   return true;
}

bool RA2bBin::GetPred(double& mean, double& var){
   double sum = 0;
   for (int i = 0; i < count_pred.size(); ++i) {
      sum += count_pred.at(i);
      //cout << count_pred.at(i) << endl;
   }
   mean = sum / count_pred.size();
   
   double sq_sum = 0;
   for (int i = 0; i < count_pred.size(); ++i) {
      sq_sum += (count_pred.at(i) * count_pred.at(i));
   }
   double sq_sum_ave = sq_sum / count_pred.size();
   var = sqrt(sq_sum_ave - mean*mean);
   return true;
}

bool RA2bBin::GetExp(double& mean, double& var){
   mean = count_exp;
   var = sqrt(sumw2_exp);
   return true;
}

RA2bBin::~RA2bBin(){
   
}

