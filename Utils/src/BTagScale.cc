// -*- C++ -*-
//
// Package:    BTagScale
// Class:      BTagScale
// 
/**\class BTagScale BTagScale.cc RA2Classic/BTagScale/src/BTagScale.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files
#include <memory>
// user include files

#include "CondFormats/BTauObjects/interface/BTagCalibration.h"
#include "CondFormats/BTauObjects/interface/BTagCalibrationReader.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"


#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#

#include "TFile.h"
#include "TH1F.h"
#include "TH2D.h"
#include <TF1.h>
//
// class declaration
//

class BTagScale : public edm::EDProducer {
public:
  explicit BTagScale(const edm::ParameterSet&);
  ~BTagScale();
		
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void InitTagEff(std::string fname);
  virtual void FillEffSF(const pat::Jet &aJet, double&Eff, double&SF,double&SFUp, double&SFDown);
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  edm::InputTag JetTag_;
  std::string   btagEffFile_;
  std::string   CSVSFFile_;
  //fill these based on the Mass Point (Mg,mLSP)
  TH2D*btagEff;
  TH2D*ctagEff;
  TH2D*ltagEff;
	 	
	
  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
BTagScale::BTagScale(const edm::ParameterSet& iConfig)
{
  //register your produc

  JetTag_ = iConfig.getParameter<edm::InputTag>("JetsTag");
  btagEffFile_=iConfig.getParameter<std::string>  ("BTagEffInput");
  CSVSFFile_=iConfig.getParameter<std::string>("CSVTag");
  InitTagEff(btagEffFile_);
  //now do what ever other initialization is needed
  produces<double>("BTagProb0");	
  produces<double>("BTagProb1");
  produces<double>("BTagProb2");
  produces<double>("BTagProb3");

  produces<double>("BTagProb0ShiftUp");
  produces<double>("BTagProb1ShiftUp");
  produces<double>("BTagProb2ShiftUp");
  produces<double>("BTagProb3ShiftUp");	

  produces<double>("BTagProb0ShiftDown");
  produces<double>("BTagProb1ShiftDown");
  produces<double>("BTagProb2ShiftDown");
  produces<double>("BTagProb3ShiftDown");

}


BTagScale::~BTagScale()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
BTagScale::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  using namespace pat;
  //int BTags=0;
  edm::Handle< edm::View<pat::Jet> > Jets;
  iEvent.getByLabel(JetTag_,Jets);
	
	
  double Prob0=1.0;
  double product = 1;
  double productUp = 1;
  double productDown=1;

  float Prob1=0.0;
  float Prob2=0.0;
  float Prob3=0.0;

  double Prob0ShiftUp=1.0;
  double Prob1ShiftUp=0.0;
  double Prob2ShiftUp=0.0;
  double Prob3ShiftUp=0.0;

  double Prob0ShiftDown=1.0;
  double Prob1ShiftDown=0.0;
  double Prob2ShiftDown=0.0;
  double Prob3ShiftDown=0.0;

  if( Jets.isValid() ) {

    for(unsigned int ij=0; ij<Jets->size();ij++)
      {

	double Eff=1.0; double SF=1.0; double SFUp=1.0; double SFDown=1.0;
	FillEffSF(Jets->at(ij),Eff, SF,SFUp,SFDown);		 

	//shift b/c sf
	double eps_i=Eff*SF;
	double epsUp_i=Eff*SFUp;
	double epsDown_i=Eff*SFDown;	
	//mistag sf for light jets
		  

	Prob0=Prob0*(1-eps_i);
	Prob0ShiftUp=Prob0ShiftUp*(1-epsUp_i);
	Prob0ShiftDown=Prob0ShiftDown*(1-epsDown_i);

	double subprob=0;
	double subprobUp=0;
	double subprobDown=0;

	product=1.0;
	productUp=1.0;
	productDown=1.0;

	for(unsigned int ik=0; ik<Jets->size(); ++ik){
	  Eff=1.0; SF=1.0; SFUp=1.0; SFDown=1.0;
	  FillEffSF(Jets->at(ik),Eff, SF,SFUp,SFDown);
	  double eps_k=Eff*SF;
	  double epsUp_k=Eff*SFUp;
	  double epsDown_k=Eff*SFDown;

	  if(ik!=ij){
	    product=product*(1-eps_k); 
	    productUp=productUp*(1-epsUp_k);
	    productDown=productDown*(1-epsDown_k);

	  }
	  if(ik > ij){
	    double subproduct = 1;
	    double subproductUp = 1;
	    double subproductDown = 1;

	    for (unsigned int jj=0; jj<Jets->size(); ++jj) {
	      if(jj != ik && jj != ij){
		Eff=1.0; SF=1.0; SFUp=1.0; SFDown=1.0; 
		FillEffSF(Jets->at(jj),Eff, SF,SFUp,SFDown );
		double eps_j=Eff*SF;
		double epsUp_j=Eff*SFUp;
		double epsDown_j=Eff*SFDown;

		//std::cout<<"eps_j "<<eps_j<<std::endl; 	
		subproduct=subproduct*(1-eps_j);
		subproductUp=subproductUp*(1-epsUp_j);  
		subproductDown=subproductDown*(1-epsDown_j); 

	      }
	    }
	    subprob += eps_k*subproduct; 
	    subprobUp += epsUp_k*subproductUp;
	    subprobDown += epsDown_k*subproductDown;
	    //    MTsubprobUp += MTepsUp_k*MTsubproductUp;
	    //  MTsubprobDown += MTepsDown_k*MTsubproductDown;
	  }	
	} 
	Prob1+= eps_i*product;
	Prob2+= eps_i*subprob;
		  	  
	//MTProb1ShiftUp+= MTepsUp_i*MTproductUp;
	//MTProb1ShiftDown+= MTepsDown_i*MTproductDown;
                  
	//MTProb2ShiftUp+=MTepsUp_i*MTsubprobUp;
	//MTProb2ShiftDown+=MTepsDown_i*MTsubprobDown;
		  
	Prob1ShiftUp+= epsUp_i*productUp;
	Prob1ShiftDown+= epsDown_i*productDown;

	Prob2ShiftUp+=epsUp_i*subprobUp;
	Prob2ShiftDown+=epsDown_i*subprobDown;	 

      }

  }
  else std::cout<<"BTagScale::Invalid Tag: "<<JetTag_.label()<<std::endl;

  Prob3=1-Prob0-Prob1-Prob2;
  Prob3ShiftUp=1-Prob0ShiftUp-Prob1ShiftUp-Prob2ShiftUp;
  Prob3ShiftDown=1-Prob0ShiftDown-Prob1ShiftDown-Prob2ShiftDown;	

  std::auto_ptr<double> b0(new double(Prob0));
  iEvent.put(b0, "BTagProb0");
  std::auto_ptr<double> b1(new double(Prob1));
  iEvent.put(b1, "BTagProb1");
  std::auto_ptr<double> b2(new double(Prob2));
  iEvent.put(b2, "BTagProb2");
  std::auto_ptr<double> b3(new double(Prob3));
  iEvent.put(b3, "BTagProb3");
	

  std::auto_ptr<double> b0up(new double(Prob0ShiftUp));
  iEvent.put(b0up, "BTagProb0ShiftUp");
  std::auto_ptr<double> b1up(new double(Prob1ShiftUp));
  iEvent.put(b1up, "BTagProb1ShiftUp");
  std::auto_ptr<double> b2up(new double(Prob2ShiftUp));
  iEvent.put(b2up, "BTagProb2ShiftUp");
  std::auto_ptr<double> b3up(new double(Prob3ShiftUp));
  iEvent.put(b3up, "BTagProb3ShiftUp");

  std::auto_ptr<double> b0down(new double(Prob0ShiftDown));
  iEvent.put(b0down, "BTagProb0ShiftDown");
  std::auto_ptr<double> b1down(new double(Prob1ShiftDown));
  iEvent.put(b1down, "BTagProb1ShiftDown");
  std::auto_ptr<double> b2down(new double(Prob2ShiftDown));
  iEvent.put(b2down, "BTagProb2ShiftDown");
  std::auto_ptr<double> b3down(new double(Prob3ShiftDown));
  iEvent.put(b3down, "BTagProb3ShiftDown");


  //std::cout<<"BTagProb0 Nominal "<<Prob0<<" BTagProb1 "<<Prob1<<" BTag Prob2 "<<Prob2<<std::endl;
}

// ------------ method called once each job just before starting event loop  ------------
void 
BTagScale::beginJob()
{


}

// ------------ method called once each job just after ending the event loop  ------------
void 
BTagScale::endJob() {

}

// ------------ method called when starting to processes a run  ------------
void 
BTagScale::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
BTagScale::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
BTagScale::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
BTagScale::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}
void BTagScale::FillEffSF(const pat::Jet& aJet, double&Eff, double&SF,double&SFUp, double&SFDown){
    
  float jetpt=aJet.pt();
  if(jetpt>1000.)jetpt=999.;
  float jeteta=aJet.eta();
  
  int parton=aJet.partonFlavour();
  //  std::cout<<"Jet Eta pt "<<jeteta<<" "<<jetpt<<" "<<aJet.partonFlavour()<<std::endl;
  BTagEntry::JetFlavor jetFlavor=BTagEntry::FLAV_B;
  if(abs(parton)!=5 && abs(parton)!= 4) jetFlavor=BTagEntry::FLAV_UDSG;
  BTagCalibration calib("csvslv1", CSVSFFile_.c_str());
  // std::cout<<"Build the Calibration "<<std::endl;
  BTagCalibrationReader reader(&calib,
			       BTagEntry::OP_MEDIUM,
			       "comb",
			       "central");//central Valie
  BTagCalibrationReader readershiftup(&calib,
				      BTagEntry::OP_MEDIUM,
				      "comb",
				      "up");	
  BTagCalibrationReader readershiftdown(&calib,
					BTagEntry::OP_MEDIUM,
					"comb",
					"down"); 
  //std::cout<<"Booked the Calibration Reader "<<std::endl;
  //if(abs(parton)!=4){
  SF=reader.eval(jetFlavor,jeteta, jetpt);
  SFUp=readershiftup.eval(jetFlavor,jeteta, jetpt);
  SFDown=readershiftdown.eval(jetFlavor,jeteta, jetpt);
  if( abs(parton)== 4){
    SFUp=((SFUp-SF)*2) +SF;
    SFDown=SF-((SF-SFDown)*2);
  }


  if(abs(parton)==5)Eff=btagEff->GetBinContent(btagEff->FindBin(jetpt,jeteta) );
  if(abs(parton)==4)Eff=ctagEff->GetBinContent(ctagEff->FindBin(jetpt,jeteta)  );
  if(abs(parton)!=4 &&abs(parton)!=5  )Eff=ltagEff->GetBinContent(ltagEff->FindBin(jetpt,jeteta)  );

}
void BTagScale::InitTagEff(std::string fname){
  TFile *TagEffFile = new TFile(fname.c_str(), "READ");
  TH2D*numB=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Num_b");
  TH2D*numC=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Num_c");
  TH2D*numl=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Num_udsg");
  
  TH2D*denB=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Denom_b");
  TH2D*denC=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Denom_c");
  TH2D*denl=(TH2D*)TagEffFile->Get("bTaggingEffAnalyzerAK5PF/h2_BTaggingEff_Denom_udsg");


  numB->Divide(denB); 
  numC->Divide(denC); 
  numl->Divide(denl);
  btagEff=(TH2D*)numB->Clone("btagEff"); 
  ctagEff=(TH2D*)numC->Clone("ctagEff");
  ltagEff=(TH2D*)numl->Clone("ltagEff");
  delete TagEffFile; 

}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BTagScale::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BTagScale);
