#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

enum isoType {pfCh,pfNu,pfGam,coneCh,coneNu,coneGam,NisoTypes};

class effArea{

public:
  vector<double> etaHigh;
  vector<double> etaLow;
  vector< vector<double> > effA;

  effArea(double etaLow_,double etaHigh_,double effA_pfCh_,double effA_pfNu_,double effA_pfGa_){

    addEffA(etaLow_, etaHigh_, effA_pfCh_, effA_pfNu_, effA_pfGa_);

  };

  effArea(){};

  void addEffA(double etaLow_,double etaHigh_,double effA_pfCh_,double effA_pfNu_,double effA_pfGa_){

    etaHigh.push_back( etaHigh_ );
    etaLow.push_back( etaLow_ );
    vector<double> temp;
    temp.push_back(effA_pfCh_);
    temp.push_back(effA_pfNu_);
    temp.push_back(effA_pfGa_);
    effA.push_back( temp );

  };

  double rhoCorrectedIso(isoType isoType_, double isoVal, double eta, double rho){

    int iEta = -1;

    // find the relevant eta range
    for( unsigned int i = 0 ; i < etaHigh.size() ; i++ ){

      if( fabs(eta) < etaHigh[i] && fabs(eta) >= etaLow[i] ){
	iEta = i;
	break;
      }

    }

    if( iEta < 0 ){

      edm::LogWarning("TreeMaker") << "AHHHHH: couldn't match eta region... eta=" << fabs(eta);
      return 99999. ;

    }else 
      return max( isoVal - effA[iEta][isoType_]*rho , 0. );

  };

};
