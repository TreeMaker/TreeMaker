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
  /*
        TF1*bcSF;
	TF1*lSF[3];
	TF1*lminSF[3];
	TF1*lmaxSF[3];

	TH1F*ptBasedShifts;

	float ptBins[14]={
	20,30, 40, 50, 60, 70, 80,100, 120, 160, 210, 260, 320, 400};
	float ptBinErr[13]={ 0.0918443,
 0.0282557,
 0.0264246,
 0.0242536,
 0.0218046,
 0.0207568,
 0.0207962,
 0.0208919,
 0.0200894,
 0.0258879,
 0.0270699,
 0.0256006,
 0.0438219};         
  */		 	
	
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
	/*
        produces<double>("MTProb0ShiftUp");
        produces<double>("MTProb1ShiftUp");
        produces<double>("MTProb2ShiftUp");
        produces<double>("MTProb3ShiftUp");

        produces<double>("MTProb0ShiftDown");
        produces<double>("MTProb1ShiftDown");
        produces<double>("MTProb2ShiftDown");
        produces<double>("MTProb3ShiftDown");
	*/
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
        //double MTproductUp = 1;
	// double MTproductDown=1;
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
	/*
        double MTProb0ShiftUp=1.0;
        double MTProb1ShiftUp=0.0;
        double MTProb2ShiftUp=0.0;
        double MTProb3ShiftUp=0.0;

        double MTProb0ShiftDown=1.0;
        double MTProb1ShiftDown=0.0;
        double MTProb2ShiftDown=0.0;
        double MTProb3ShiftDown=0.0;
	*/
	if( Jets.isValid() ) {

		for(unsigned int ij=0; ij<Jets->size();ij++)
		{

		  double Eff=1.0; double SF=1.0; double SFUp=1.0; double SFDown=1.0;
		  //double MTSFUp=1.0; double MTSFDown=1.0;
		  FillEffSF(Jets->at(ij),Eff, SF,SFUp,SFDown);		 

		  
		   
		   //shift b/c sf
		   double eps_i=Eff*SF;
	           double epsUp_i=Eff*SFUp;
		   double epsDown_i=Eff*SFDown;	
		   //mistag sf for light jets
		   //   double MTepsUp_i=Eff*MTSFUp;
		   //   double MTepsDown_i=Eff*MTSFDown;		  

		   Prob0=Prob0*(1-eps_i);
		   Prob0ShiftUp=Prob0ShiftUp*(1-epsUp_i);
		   Prob0ShiftDown=Prob0ShiftDown*(1-epsDown_i);
		   //   MTProb0ShiftUp=MTProb0ShiftUp*(1-MTepsUp_i);
		   // MTProb0ShiftDown=MTProb0ShiftDown*(1-MTepsDown_i);
//		   std::cout<<"Eps nom "<<eps_i <<" eps shift up "<<epsUp_i<<" eps shift down "<<epsDown_i<<std::endl;
//                   std::cout<<"Prob nom "<<Prob0 <<" Prob shift up "<<Prob0ShiftUp<<" Prob shift down "<<Prob0ShiftDown<<std::endl;
//		   std::cout<<"Jet Pt, Eta "<<Jets->at(ij).pt()<<", "<<Jets->at(ij).eta()<<" flavor "<<Jets->at(ij).partonFlavour()<<std::endl;
		   double subprob=0;
		   double subprobUp=0;
		   double subprobDown=0;
		   //   double MTsubprobUp=0;
		   //    double MTsubprobDown=0;
	        product=1.0;
		productUp=1.0;
		productDown=1.0;
		//   MTproductUp=1.0;
		//   MTproductDown=1.0;	
	   for(unsigned int ik=0; ik<Jets->size(); ++ik){
		     Eff=1.0; SF=1.0; SFUp=1.0; SFDown=1.0;
		     FillEffSF(Jets->at(ik),Eff, SF,SFUp,SFDown);
		     double eps_k=Eff*SF;
		     double epsUp_k=Eff*SFUp;
		     double epsDown_k=Eff*SFDown;
                     //double MTepsUp_k=Eff*MTSFUp;
                     //double MTepsDown_k=Eff*MTSFDown;
		     if(ik!=ij){
			product=product*(1-eps_k); 
			productUp=productUp*(1-epsUp_k);
			productDown=productDown*(1-epsDown_k);
			//	MTproductUp=MTproductUp*(1-MTepsUp_k);
			//	MTproductDown=MTproductDown*(1-MTepsDown_k);
		    }
		     if(ik > ij){
			 double subproduct = 1;
			 double subproductUp = 1;
			 double subproductDown = 1;
                         //double MTsubproductUp = 1;
                         //double MTsubproductDown = 1;
			 for (unsigned int jj=0; jj<Jets->size(); ++jj) {
				 if(jj != ik && jj != ij){
                                 Eff=1.0; SF=1.0; SFUp=1.0; SFDown=1.0; 
				FillEffSF(Jets->at(jj),Eff, SF,SFUp,SFDown );
			         double eps_j=Eff*SF;
				 double epsUp_j=Eff*SFUp;
				 double epsDown_j=Eff*SFDown;
				 //     double MTepsUp_j=Eff*SFUp;
				 //     double MTepsDown_j=Eff*SFDown;			       	
                    		   //std::cout<<"eps_j "<<eps_j<<std::endl; 	
				   subproduct=subproduct*(1-eps_j);
				   subproductUp=subproductUp*(1-epsUp_j);  
				   subproductDown=subproductDown*(1-epsDown_j); 
				   //   MTsubproductUp=MTsubproductUp*(1-MTepsUp_j);
				   //    MTsubproductDown=MTsubproductDown*(1-MTepsDown_j);
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
	//  MTProb3ShiftUp=1-MTProb0ShiftUp-MTProb1ShiftUp-MTProb2ShiftUp;
        Prob3ShiftDown=1-Prob0ShiftDown-Prob1ShiftDown-Prob2ShiftDown;	

	//	MTProb3ShiftDown=1-MTProb0ShiftDown-MTProb1ShiftDown-MTProb2ShiftDown;
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
	/*
        std::auto_ptr<double> m0up(new double(MTProb0ShiftUp));
        iEvent.put(m0up, "MTProb0ShiftUp");
        std::auto_ptr<double> m1up(new double(MTProb1ShiftUp));
        iEvent.put(m1up, "MTProb1ShiftUp");
        std::auto_ptr<double> m2up(new double(MTProb2ShiftUp));
        iEvent.put(m2up, "MTProb2ShiftUp");
        std::auto_ptr<double> m3up(new double(MTProb3ShiftUp));
        iEvent.put(m3up, "MTProb3ShiftUp");

        std::auto_ptr<double> m0down(new double(MTProb0ShiftDown));
        iEvent.put(m0down, "MTProb0ShiftDown");
        std::auto_ptr<double> m1down(new double(MTProb1ShiftDown));
        iEvent.put(m1down, "MTProb1ShiftDown");
        std::auto_ptr<double> m2down(new double(MTProb2ShiftDown));
        iEvent.put(m2down, "MTProb2ShiftDown");
        std::auto_ptr<double> m3down(new double(MTProb3ShiftDown));
        iEvent.put(m3down, "MTProb3ShiftDown");
	*/

//	std::cout<<"BTagProb0 Nominal "<<Prob0<<" BTagProb0 Shift Down "<<Prob0ShiftDown<<std::endl;
}

// ------------ method called once each job just before starting event loop  ------------
void 
BTagScale::beginJob()
{
	InitTagEff(btagEffFile_);

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
  //std::cout<<"Jet Eta pt "<<jeteta<<" "<<jetpt<<" "<<aJet.partonFlavour()<<std::endl;
  BTagEntry::JetFlavor jetFlavor=BTagEntry::FLAV_B;
  if(abs(parton)!=5 && abs(parton)!= 4) jetFlavor=BTagEntry::FLAV_UDSG;
  BTagCalibration calib("csvv2", CSVSFFile_.c_str());
  //std::cout<<"Build the Calibration "<<std::endl;
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
 // std::cout<<"Booked the Calibration Reader "<<std::endl;
if(abs(parton)!=4){
    SF=reader.eval(jetFlavor,jeteta, jetpt);
    SFUp=readershiftup.eval(jetFlavor,jeteta, jetpt);
    SFDown=readershiftdown.eval(jetFlavor,jeteta, jetpt);
   // std::cout<<"Scale Factors "<<SF<<" +/- "<<SFUp<<" "<<SFDown<<std::endl;
}
//else{
//	std::cout<<"Jet Eta pt "<<jeteta<<" "<<jetpt<<" "<<reader.eval( BTagEntry::FLAV_B,jeteta, jetpt)<<std::endl;

//}
//std::cout<<"Evaluated SF "<<std::endl;
    //fill Efficiency
  // std::cout<<"Jet Eta pt "<<jeteta<<" "<<jetpt<<" "<<aJet.partonFlavour()<<std::endl;

    if(abs(parton)==5)Eff=btagEff->GetBinContent(btagEff->FindBin(jetpt,jeteta) );
    if(abs(parton)==4)Eff=ctagEff->GetBinContent(ctagEff->FindBin(jetpt,jeteta)  );
    if(abs(parton)!=4 &&abs(parton)!=5  )Eff=ltagEff->GetBinContent(ltagEff->FindBin(jetpt,jeteta)  );
//std::cout<<"Read the Eff Map "<<std::endl;	    
	/*
    if(jetpt>400)jetpt=400;
    int parton=aJet.partonFlavour();
    if(abs(parton)==5){
	Eff=btagEff->GetBinContent(btagEff->FindBin(jetpt));
        SF=bcSF->Eval(jetpt);
	float sfErr=ptBasedShifts->GetBinContent(ptBasedShifts->FindBin(jetpt));	
	SFUp=SF+(sfErr);
	SFDown=SF-(sfErr);
	MTSFUp=SF;
        MTSFDown=SF;
	}

    if(abs(parton)==4){
	Eff=ctagEff->GetBinContent(ctagEff->FindBin(jetpt));SF=bcSF->Eval(jetpt);
	float sfErr=2*ptBasedShifts->GetBinContent(ptBasedShifts->FindBin(jetpt));
	SFUp=SF+(sfErr);
        SFDown=SF-(sfErr);
        MTSFUp=SF;
        MTSFDown=SF;
	}
    if(aJet.pt()>1000)jetpt=1000;
    else jetpt=aJet.pt();
    if(abs(parton)<4 || parton==21){
	Eff=ltagEff->GetBinContent(ltagEff->GetXaxis()->FindBin(fabs(aJet.eta())),ltagEff->GetYaxis()->FindBin(jetpt));
        if(fabs(aJet.eta())<0.8){
	SF=lSF[0]->Eval(jetpt);
	SFUp=SF;
        SFDown=SF;
	MTSFUp=lmaxSF[0]->Eval(jetpt); 
	MTSFDown=lminSF[0]->Eval(jetpt);
	}
        if(fabs(aJet.eta())>0.8 && fabs(aJet.eta())<1.6 )
	{
	SF=lSF[1]->Eval(jetpt);
        SFUp=SF;
        SFDown=SF;
	MTSFUp=lmaxSF[1]->Eval(jetpt);
	MTSFDown=lminSF[1]->Eval(jetpt);
	}
        if(fabs(aJet.eta())>1.6 && fabs(aJet.eta())<2.4 ){
	SF=lSF[2]->Eval(jetpt);
        SFUp=SF;
        SFDown=SF;
	MTSFUp=lmaxSF[2]->Eval(jetpt);
	MTSFDown=lminSF[2]->Eval(jetpt);
	}
    }
	*/
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
	/*
	bcSF=new TF1("bcSF", "((0.939238+(0.000278928*x))+(-7.49693e-07*(x*x)))+(2.04822e-10*(x*(x*x)))",20,400);	
	float ptmax=1000;
   	lSF[0] = new TF1("lSF0","((1.06212+(0.00223614*x))+(-4.25167e-06*(x*x)))+(2.42728e-09*(x*(x*x)))", 20.,ptmax);
	lSF[1] = new TF1("lSF1","((1.04547+(0.00216995*x))+(-4.579e-06*(x*x)))+(2.91791e-09*(x*(x*x)))", 20.,ptmax);
    	lSF[2] = new TF1("lSF2","((0.991865+(0.00324957*x))+(-9.65897e-06*(x*x)))+(7.13694e-09*(x*(x*x)))", 20.,ptmax);

	lminSF[0]=new TF1("lminSF0", "((0.903956+(0.00121678*x))+(-2.04383e-06*(x*x)))+(1.10727e-09*(x*(x*x)))",20.,ptmax);
	lmaxSF[0]=new TF1("lmaxSF0", "((1.22035+(0.00325183*x))+(-6.45023e-06*(x*x)))+(3.74225e-09*(x*(x*x)))",20., ptmax);

        lminSF[1]=new TF1("lminSF1", "((0.900637+(0.00120088*x))+(-2.27069e-06*(x*x)))+(1.40609e-09*(x*(x*x)))",20.,ptmax);
        lmaxSF[1]=new TF1("lmaxSF1", "((1.19034+(0.00313562*x))+(-6.87854e-06*(x*x)))+(4.42546e-09*(x*(x*x)))",20., ptmax);

	lminSF[2]=new TF1("lminSF2", "((0.868875+(0.00222761*x))+(-6.44897e-06*(x*x)))+(4.53261e-09*(x*(x*x)))",20.,ptmax);
        lmaxSF[2]=new TF1("lmaxSF2", "((1.11481+(0.00426745*x))+(-1.28612e-05*(x*x)))+(9.74425e-09*(x*(x*x)))",20., ptmax);
	ptBasedShifts=new TH1F("ptBasedShifts", "", 12, 	ptBins);
	for(int i=1; i<=12; ++i)ptBasedShifts->SetBinContent(i, ptBinErr[i]);	
	*/
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
