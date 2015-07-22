//
//  RA2bBin.h
//  
//
//  Created by Christian Sander on 02/06/15.
//
//

#ifndef ____RA2bBin__
#define ____RA2bBin__

#include <stdio.h>
#include <vector>
#include <string>
#include <numeric>
#include <cmath>
#include <iostream>

using namespace std;

class RA2bBin{
   
public:
   
   RA2bBin(std::string, int, int, int, int, int, double, double, double, double, bool);
   ~RA2bBin();
   
   bool FillPred(int, int, int, double, double, bool, double);
   bool FillExp(int, int, double, double, bool, double);
   
   bool GetPred(double&, double&);
   bool GetExp(double&, double&);
   
   std::string BinName;

private:
   
   int Ntries;
   
   double MHT_low, MHT_high;
   double HT_low, HT_high;
   int NJets_low, NJets_high;
   int NBJets_low, NBJets_high;
   bool DeltaPhiMin;
   
   double count_exp;
   double sumw2_exp;
   std::vector<double> count_pred;
   std::vector<double> sumw2_pred;
   
   double prediction;
   double uncertainty;
   
};

#endif /* defined(____RA2bBin__) */
