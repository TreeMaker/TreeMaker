// -*- C++ -*-
//
// Package:    LeptonProducer
// Class:      LeptonProducer
//
/**\class LeptonProducer LeptonProducer.cc RA2Classic/LeptonProducer/src/LeptonProducer.cc
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

#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TVector2.h"

//
// class declaration
//



class LeptonProducer : public edm::EDProducer {
public:
	explicit LeptonProducer(const edm::ParameterSet&);
	~LeptonProducer();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	float MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi);
	double getPFIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
												const reco::Candidate* ptcl,
											 double r_iso_min, double r_iso_max, double kt_scale,
											 bool use_pfweight, bool charged_only)
	{
		if (ptcl->pt()<5.) return 99999.;
		double deadcone_nh(0.), deadcone_ch(0.), deadcone_ph(0.), deadcone_pu(0.);
		if(ptcl->isElectron()) {
			if (fabs(ptcl->eta())>1.479) {deadcone_ch = 0.015; deadcone_pu = 0.015; deadcone_ph = 0.08;}
		} else if(ptcl->isMuon()) {
			deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01;
		} else {
			//deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01; // maybe use muon cones??
		}
		double iso_nh(0.); double iso_ch(0.);
		double iso_ph(0.); double iso_pu(0.);
		double ptThresh(0.5);
		if(ptcl->isElectron()) ptThresh = 0;
		double r_iso = std::max(r_iso_min,std::min(r_iso_max, kt_scale/ptcl->pt()));
		for (const pat::PackedCandidate &pfc : *pfcands) {
			if (abs(pfc.pdgId())<7) continue;
			double dr = deltaR(pfc, *ptcl);
			if (dr > r_iso) continue;
			////////////////// NEUTRALS /////////////////////////
			if (pfc.charge()==0){
				if (pfc.pt()>ptThresh) {
					double wpf(1.);
					if (use_pfweight){
						double wpv(0.), wpu(0.);
						for (const pat::PackedCandidate &jpfc : *pfcands) {
							double jdr = deltaR(pfc, jpfc);
							if (pfc.charge()!=0 || jdr<0.00001) continue;
							double jpt = jpfc.pt();
							if (pfc.fromPV()>1) wpv *= jpt/jdr;
							else wpu *= jpt/jdr;
						}
						wpv = log(wpv);
						wpu = log(wpu);
						wpf = wpv/(wpv+wpu);
					}
					/////////// PHOTONS ////////////
					if (abs(pfc.pdgId())==22) {
						if(dr < deadcone_ph) continue;
						iso_ph += wpf*pfc.pt();
						/////////// NEUTRAL HADRONS ////////////
					} else if (abs(pfc.pdgId())==130) {
						if(dr < deadcone_nh) continue;
						iso_nh += wpf*pfc.pt();
					}
				}
				////////////////// CHARGED from PV /////////////////////////
			} else if (pfc.fromPV()>1){
				if (abs(pfc.pdgId())==211) {
					if(dr < deadcone_ch) continue;
					iso_ch += pfc.pt();
				}
				////////////////// CHARGED from PU /////////////////////////
			} else {
				if (pfc.pt()>ptThresh){
					if(dr < deadcone_pu) continue;
					iso_pu += pfc.pt();
				}
			}
		}
		double iso(0.);
		if (charged_only){
			iso = iso_ch;
		} else {
			iso = iso_ph + iso_nh;
			if (!use_pfweight) iso -= 0.5*iso_pu;
			if (iso>0) iso += iso_ch;
			else iso = iso_ch;
		}
		iso = iso/ptcl->pt();
		return iso;
	}
	bool MuonID(const pat::Muon & muon, const reco::Vertex& vtx);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag MuonTag_, ElecTag_, PrimVtxTag_, metTag_;
	double minElecPt_, maxElecEta_, minMuPt_, maxMuEta_;
	bool useMiniIsolation_;
	double muIsoValue_, elecIsoValue_;
	
	
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
LeptonProducer::LeptonProducer(const edm::ParameterSet& iConfig)
{
	//register your produc
	MuonTag_ 				= 	iConfig.getParameter<edm::InputTag >("MuonTag");
	ElecTag_ 				= 	iConfig.getParameter<edm::InputTag >("ElectronTag");
	PrimVtxTag_=iConfig.getParameter<edm::InputTag>("PrimaryVertex");
	minElecPt_=iConfig.getParameter<double>          ("minElecPt");
	maxElecEta_=iConfig.getParameter<double>          ("maxElecEta");
	minMuPt_=iConfig.getParameter<double>          ("minMuPt");
	maxMuEta_=iConfig.getParameter<double>          ("maxMuEta");
	useMiniIsolation_ = iConfig.getParameter<bool>("UseMiniIsolation");
	muIsoValue_=iConfig.getParameter<double>          ("muIsoValue");
	elecIsoValue_=iConfig.getParameter<double>          ("elecIsoValue");
	metTag_   = iConfig.getParameter<edm::InputTag> ("METTag");
	
	const std::string string1("IdMuon");
	produces<std::vector<pat::Muon> > (string1).setBranchAlias(string1);
	const std::string string2("IdIsoMuon");
	produces<std::vector<pat::Muon> > (string2).setBranchAlias(string2);
	produces<std::vector<int> >("MuonCharge");
	//   const std::string string2b("IdIsoMuon_DeltaR");
	//   produces<std::vector<double> > (string2b).setBranchAlias(string2b);
	const std::string string3("IdElectron");
	produces<std::vector<pat::Electron> > (string3).setBranchAlias(string3);
	const std::string string4("IdIsoElectron");
	produces<std::vector<pat::Electron> > (string4).setBranchAlias(string4);
	produces<std::vector<int> >("ElectronCharge");
	//   const std::string string4b("IdIsoElectron_DeltaR");
	//   produces<std::vector<double> > (string4b).setBranchAlias(string4b);
	produces<std::vector<double> >("MuIDMTW");
	produces<std::vector<double> >("MuIDIsoMTW");
	produces<std::vector<double> >("ElecIDMTW");
	produces<std::vector<double> >("ElecIDIsoMTW");
	produces<int>("");
	/* Examples
	 *   produces<ExampleData2>();
	 *
	 *   //if do put with a label
	 *   produces<ExampleData2>("label");
	 *
	 *   //if you want to put into the Run
	 *   produces<ExampleData2,InRun>();
	 */
	//now do what ever other initialization is needed
	
}


LeptonProducer::~LeptonProducer()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
LeptonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	
	std::auto_ptr<std::vector<int> > MuonCharge(new std::vector<int>());
	std::auto_ptr<std::vector<int> > ElectronCharge(new std::vector<int>());
	
	std::auto_ptr<std::vector<double> > muIDMTW(new std::vector<double>());
	std::auto_ptr<std::vector<double> > muIDIsoMTW(new std::vector<double>());
	std::auto_ptr<std::vector<double> > elecIDMTW(new std::vector<double>());
	std::auto_ptr<std::vector<double> > elecIDIsoMTW(new std::vector<double>());
	edm::Handle< edm::View<pat::MET> > MET;
	iEvent.getByLabel(metTag_,MET); 
	reco::MET::LorentzVector metLorentz(0,0,0,0);
	if(MET.isValid() )
	{
		metLorentz=MET->at(0).p4();
	}
	else std::cout<<"LeptonProducer::MetTag Invlide Tag: "<<metTag_.label()<<std::endl;

	int Leptons=0;
	edm::Handle<pat::PackedCandidateCollection> pfcands;
	iEvent.getByLabel("packedPFCandidates", pfcands);
	
	std::vector<pat::Electron> isoElectrons_, idElectrons_;
	std::vector<pat::Muon> isoMuons_, idMuons_;
	edm::Handle<reco::VertexCollection> vtx_h;
	iEvent.getByLabel(PrimVtxTag_, vtx_h);
	edm::Handle<edm::View<pat::Muon> > muonHandle;
	iEvent.getByLabel(MuonTag_, muonHandle);
	if(muonHandle.isValid())
	{
		for(unsigned int m=0; m<muonHandle->size(); ++m)
		{
			if(muonHandle->at(m).pt()<minMuPt_ || fabs(muonHandle->at(m).eta())>maxMuEta_) continue;
			
			if(MuonID(muonHandle->at(m),vtx_h->at(0)))
			{
				idMuons_.push_back(muonHandle->at(m));
				muIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
				float ChgIso=muonHandle->at(m).pfIsolationR04().sumChargedHadronPt;
				float ChgPU=muonHandle->at(m).pfIsolationR04().sumPUPt;
				float NeuIso=muonHandle->at(m).pfIsolationR04().sumNeutralHadronEt+
				muonHandle->at(m).pfIsolationR04().sumPhotonEt;
				float dBIsoMu= (ChgIso+std::max(0., NeuIso-0.5*ChgPU))/muonHandle->at(m).pt();
				if(useMiniIsolation_) dBIsoMu = getPFIsolation(pfcands, dynamic_cast<const reco::Candidate *>(&muonHandle->at(m)), 0.05, 0.2, 10., false, false);
				if(dBIsoMu<muIsoValue_)
				{
					Leptons++;
					isoMuons_.push_back(muonHandle->at(m));
					muIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi()));
				//	std::cout<<"muIDIsoMTW: "<<MTWCalculator(metLorentz.pt(),metLorentz.phi(),muonHandle->at(m).pt(),muonHandle->at(m).phi())<<"\n";
					MuonCharge->push_back(muonHandle->at(m).charge());
				}
			}
		}
	}
	edm::Handle<edm::View<pat::Electron> > eleHandle;
	iEvent.getByLabel(ElecTag_, eleHandle);
	if(eleHandle.isValid())
	{
		for(unsigned int e=0; e<eleHandle->size(); ++e)
		{
			if(fabs(eleHandle->at(e).superCluster()->eta())>maxElecEta_ ||eleHandle->at(e).pt()<minElecPt_)continue;
								const pat::Electron aEle = eleHandle->at(e);
			const reco::Vertex vtx = vtx_h->at(0);
			float sieie         = aEle.full5x5_sigmaIetaIeta();
			bool convVeto       = aEle.passConversionVeto();
			int mhits 		 = aEle.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);;
			float dEtaIn        = aEle.deltaEtaSuperClusterTrackAtVtx();
			float dPhiIn        = aEle.deltaPhiSuperClusterTrackAtVtx();
			float hoe           = aEle.hadronicOverEm();
			float ooemoop       = fabs(1.0/aEle.ecalEnergy() - aEle.eSuperClusterOverP()/aEle.ecalEnergy());
			float d0vtx         = 0.0;
			float dzvtx         = 0.0;
			reco::GsfElectron::PflowIsolationVariables pfIso = aEle.pfIsolationVariables();
			// // Compute isolation with delta beta correction for PU
			float absiso = pfIso.sumChargedHadronPt
			+ std::max(0.0 , pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt - 0.5 * pfIso.sumPUPt );
			
			d0vtx = aEle.gsfTrack()->dxy(vtx.position());
			dzvtx = aEle.gsfTrack()->dz(vtx.position());
			absiso=absiso/aEle.pt();
			if(useMiniIsolation_) absiso = getPFIsolation(pfcands, dynamic_cast<const reco::Candidate *>(&aEle), 0.05, 0.2, 10., false, false);
								
			if(aEle.isEB())
			{
				if(sieie< 0.011586 && fabs(dEtaIn)< 0.013625 && fabs(dPhiIn)< 0.230374 && hoe< 0.181130 && ooemoop< 0.295751 && fabs(d0vtx)< 0.094095 && fabs(dzvtx)< 0.713070 && mhits<=2 && convVeto)
				{
					// id passed
					idElectrons_.push_back(eleHandle->at(e));
					elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
					if(absiso<elecIsoValue_ && useMiniIsolation_)
					{
						// iso passed
						isoElectrons_.push_back(eleHandle->at(e));
						elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
						Leptons++; 
						ElectronCharge->push_back(eleHandle->at(e).charge());
						
					}
					if (absiso<0.158721 && !useMiniIsolation_)
					{
						// iso passed
						isoElectrons_.push_back(eleHandle->at(e));
						elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
						Leptons++;
						ElectronCharge->push_back(eleHandle->at(e).charge());                  
					}
				}
			}
			else{
				if(sieie< 0.031849 && fabs(dEtaIn)< 0.011932 && fabs(dPhiIn)< 0.255450 && hoe< 0.223870 && ooemoop< 0.155501 && fabs(d0vtx)< 0.342293 && fabs(dzvtx)< 0.953461 && mhits<=3 && convVeto)
				{
					// id passed
					idElectrons_.push_back(eleHandle->at(e));
					elecIDMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
					if(absiso<elecIsoValue_ && useMiniIsolation_)
					{
						// iso passed
						isoElectrons_.push_back(eleHandle->at(e));
						elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
						Leptons++;
						ElectronCharge->push_back(eleHandle->at(e).charge());
					}
					if (absiso<0.177032  && !useMiniIsolation_)
					{
						// iso passed
						isoElectrons_.push_back(eleHandle->at(e));
						elecIDIsoMTW->push_back(MTWCalculator(metLorentz.pt(),metLorentz.phi(),eleHandle->at(e).pt(),eleHandle->at(e).phi()));
						Leptons++;
						ElectronCharge->push_back(eleHandle->at(e).charge());
					}
				}
			}
		}
	}
	const std::string string1("IdMuon");
	const std::string string2("IdIsoMuon");
	const std::string string3("IdElectron");
	const std::string string4("IdIsoElectron");
	
	std::auto_ptr<int> htp(new int(Leptons));
	iEvent.put(htp);
	std::auto_ptr<std::vector<pat::Muon> > htp1(new std::vector<pat::Muon>(idMuons_));
	iEvent.put(htp1,string1);
	std::auto_ptr<std::vector<pat::Muon> > htp2(new std::vector<pat::Muon>(isoMuons_));
	iEvent.put(htp2,string2);
	
	std::auto_ptr<std::vector<pat::Electron> > htp3(new std::vector<pat::Electron>(idElectrons_));
	iEvent.put(htp3,string3);
	std::auto_ptr<std::vector<pat::Electron> > htp4(new std::vector<pat::Electron>(isoElectrons_));
	iEvent.put(htp4,string4);
	
	iEvent.put(ElectronCharge,"ElectronCharge");
	iEvent.put(MuonCharge,"MuonCharge");
	
	iEvent.put(muIDMTW,"MuIDMTW");
	iEvent.put(muIDIsoMTW,"MuIDIsoMTW");
	iEvent.put(elecIDMTW,"ElecIDMTW");
	iEvent.put(elecIDIsoMTW,"ElecIDIsoMTW");
}

// ------------ method called once each job just before starting event loop  ------------
void
LeptonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LeptonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
LeptonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
LeptonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
LeptonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
LeptonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

float LeptonProducer::MTWCalculator(double metPt,double  metPhi,double  lepPt,double  lepPhi)
{
	float deltaPhi =TVector2::Phi_mpi_pi(lepPhi-metPhi);
	return sqrt(2*lepPt*metPt*(1-cos(deltaPhi)) );
}

bool LeptonProducer::MuonID(const pat::Muon & muon, const reco::Vertex& vtx){
	//tight WP
	//return muon.isTightMuon(vtx);
	
	//medium WP + dz/dxy cuts
	bool goodGlob = muon.isGlobalMuon() && 
					muon.globalTrack()->normalizedChi2() < 3 && 
					muon.combinedQuality().chi2LocalPosition < 12 && 
					muon.combinedQuality().trkKink < 20; 
	bool isMedium = muon.isLooseMuon() && 
					muon.innerTrack()->validFraction() > 0.8 && 
					muon.segmentCompatibility() > (goodGlob ? 0.303 : 0.451);
	bool isMediumPlus = isMedium && muon.dB() < 0.2 && fabs(muon.muonBestTrack()->dz(vtx.position())) < 0.5;
	return isMediumPlus; 
}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonProducer);
