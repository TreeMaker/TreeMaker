#ifndef NjettinessHelper_h
#define NjettinessHelper_h

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "fastjet/contrib/Njettiness.hh"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include <utility>

//based on RecoJets/JetProducers/interface/NjettinessAdder.h

typedef math::PtEtaPhiELorentzVector CLorentzVector;

class NjettinessHelper {
 public:
  enum MeasureDefinition_t {
    NormalizedMeasure=0,       // (beta,R0) 
    UnnormalizedMeasure,       // (beta) 
    OriginalGeometricMeasure,  // (beta) 
    NormalizedCutoffMeasure,   // (beta,R0,Rcutoff) 
    UnnormalizedCutoffMeasure, // (beta,Rcutoff) 
    GeometricCutoffMeasure,    // (beta,Rcutoff) 
    N_MEASURE_DEFINITIONS
  };
  enum AxesDefinition_t {
    KT_Axes=0,
    CA_Axes,
    AntiKT_Axes,   // (axAxesR0)
    WTA_KT_Axes,
    WTA_CA_Axes,
    Manual_Axes,
    OnePass_KT_Axes,
    OnePass_CA_Axes,
    OnePass_AntiKT_Axes,   // (axAxesR0)
    OnePass_WTA_KT_Axes,
    OnePass_WTA_CA_Axes,
    OnePass_Manual_Axes,
    MultiPass_Axes,
    N_AXES_DEFINITIONS
  };
  
  explicit NjettinessHelper(const edm::ParameterSet& iConfig);
  virtual ~NjettinessHelper() {}
  double getTau(unsigned num, const std::vector<CLorentzVector> object) const;
  
 private:
  // Measure definition : 
  unsigned                               measureDefinition_;
  double                                 beta_ ;
  double                                 R0_;
  double                                 Rcutoff_;

  // Axes definition : 
  unsigned                               axesDefinition_;
  int                                    nPass_;
  double                                 akAxesR0_;
  
  std::unique_ptr<fastjet::contrib::Njettiness> routine_; 
};

NjettinessHelper::NjettinessHelper(const edm::ParameterSet& iConfig) :
  measureDefinition_(iConfig.getParameter<unsigned>("measureDefinition")),
  beta_(iConfig.getParameter<double>("beta")),
  R0_(iConfig.getParameter<double>("R0")),
  Rcutoff_(iConfig.getParameter<double>("Rcutoff")),
  axesDefinition_(iConfig.getParameter<unsigned>("axesDefinition")),
  nPass_(iConfig.getParameter<int>("nPass")),
  akAxesR0_(iConfig.getParameter<double>("akAxesR0"))
{
  // Get the measure definition
  fastjet::contrib::NormalizedMeasure          normalizedMeasure        (beta_,R0_);
  fastjet::contrib::UnnormalizedMeasure        unnormalizedMeasure      (beta_);
  fastjet::contrib::OriginalGeometricMeasure   geometricMeasure         (beta_);
  fastjet::contrib::NormalizedCutoffMeasure    normalizedCutoffMeasure  (beta_,R0_,Rcutoff_);
  fastjet::contrib::UnnormalizedCutoffMeasure  unnormalizedCutoffMeasure(beta_,Rcutoff_);
  
  fastjet::contrib::MeasureDefinition const * measureDef = 0;
  switch ( measureDefinition_ ) {
  case UnnormalizedMeasure : measureDef = &unnormalizedMeasure; break;
  case OriginalGeometricMeasure    : measureDef = &geometricMeasure; break;
  case NormalizedCutoffMeasure : measureDef = &normalizedCutoffMeasure; break;
  case UnnormalizedCutoffMeasure : measureDef = &unnormalizedCutoffMeasure; break;
  case NormalizedMeasure : default : measureDef = &normalizedMeasure; break;
  } 
  
  // Get the axes definition
  fastjet::contrib::KT_Axes             kt_axes; 
  fastjet::contrib::CA_Axes             ca_axes; 
  fastjet::contrib::AntiKT_Axes         antikt_axes   (akAxesR0_);
  fastjet::contrib::WTA_KT_Axes         wta_kt_axes; 
  fastjet::contrib::WTA_CA_Axes         wta_ca_axes; 
  fastjet::contrib::OnePass_KT_Axes     onepass_kt_axes;
  fastjet::contrib::OnePass_CA_Axes     onepass_ca_axes;
  fastjet::contrib::OnePass_AntiKT_Axes onepass_antikt_axes   (akAxesR0_);
  fastjet::contrib::OnePass_WTA_KT_Axes onepass_wta_kt_axes;
  fastjet::contrib::OnePass_WTA_CA_Axes onepass_wta_ca_axes;
  fastjet::contrib::MultiPass_Axes      multipass_axes (nPass_);
  
  fastjet::contrib::AxesDefinition const * axesDef = 0;
  switch ( axesDefinition_ ) {
  case  KT_Axes : default : axesDef = &kt_axes; break;
  case  CA_Axes : axesDef = &ca_axes; break; 
  case  AntiKT_Axes : axesDef = &antikt_axes; break;
  case  WTA_KT_Axes : axesDef = &wta_kt_axes; break; 
  case  WTA_CA_Axes : axesDef = &wta_ca_axes; break; 
  case  OnePass_KT_Axes : axesDef = &onepass_kt_axes; break;
  case  OnePass_CA_Axes : axesDef = &onepass_ca_axes; break; 
  case  OnePass_AntiKT_Axes : axesDef = &onepass_antikt_axes; break;
  case  OnePass_WTA_KT_Axes : axesDef = &onepass_wta_kt_axes; break; 
  case  OnePass_WTA_CA_Axes : axesDef = &onepass_wta_ca_axes; break; 
  case  MultiPass_Axes : axesDef = &multipass_axes; break;
  };
  
  routine_ = std::make_unique<fastjet::contrib::Njettiness>(*axesDef, *measureDef);
}

double NjettinessHelper::getTau(unsigned num, const std::vector<CLorentzVector> object) const
{
  std::vector<fastjet::PseudoJet> FJparticles;
  for(const auto& dp : object){
    FJparticles.push_back(fastjet::PseudoJet(dp.px(), dp.py(), dp.pz(), dp.energy()));
  }

  return routine_->getTau(num, FJparticles); 
}

#endif
