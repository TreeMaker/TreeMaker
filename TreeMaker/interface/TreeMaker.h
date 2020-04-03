// CMSSW headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

//ROOT headers
#include "TString.h"
#include "TBranch.h"
#include "TTree.h"
#include <TFile.h>
#include "TLorentzVector.h"
#include "Math/GenVector/LorentzVector.h"

//STL headers
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

//enum with known types
enum TreeTypes { 
	t_bool=0, t_int=1, t_double=2, t_string=3, t_lorentz=4, t_xyzv=5, t_xyzp=6,
	t_vbool=100, t_vint=101, t_vdouble=102, t_vstring=103, t_vlorentz=104, t_vxyzv=105, t_vxyzp=106, t_vfloat=107,
	t_vvbool=200, t_vvint=201, t_vvdouble=202, t_vvstring=203, t_vvlorentz=204, t_vvxyzv=205, t_vvxyzp=206,
	t_recocand=1000
};

//forward declaration of helper class
class TreeObjectBase;

//
// class declaration
//

class TreeMaker : public edm::one::EDAnalyzer<edm::one::SharedResources> {
	public:
		explicit TreeMaker(const edm::ParameterSet&);
		~TreeMaker() override;
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		void beginJob() override;
		void analyze(const edm::Event&, const edm::EventSetup&) override;
		void endJob() override;
		// ----------member data ---------------------------
		edm::Service<TFileService> fs;
		string treeName;
		TTree* tree;	
		bool doLorentz, sortBranches, debugTitles;
		vector<string> VarTypeNames;
		vector<TreeTypes> VarTypes;
		map<string,unsigned> nameCache;
		// general event information
		UInt_t runNum{};
		UInt_t lumiBlockNum{};
		ULong64_t evtNum{};
		vector<TreeObjectBase*> variables;
		map<string,string> titleMap;
};

//base class for tree objects
class TreeObjectBase {
	public:
		//constructor
		TreeObjectBase() : tempFull(""), branchType("") {}
		TreeObjectBase(string tempFull_, string title_ = "") : tempFull(tempFull_), nameInTree(tempFull_), tagName(tempFull_), title(title_), tree(nullptr) {}
		//destructor
		virtual ~TreeObjectBase() {}
		//functions
		virtual string GetNameInTree() const { return nameInTree; }
		virtual void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC, stringstream& message) {}
		virtual void SetTree(TTree* tree_) { tree = tree_; }
		virtual void AddBranch() {}
		virtual void AddTitle() { if(branch && !title.empty()) branch->SetTitle(title.c_str()); }
		virtual void SetDefault() {}
		virtual void FillTree(const edm::Event& iEvent) {}
		
		//common helper function
		virtual void FinalizeName(map<string,unsigned>& nameCache, stringstream& message){
			auto nameIt = nameCache.find(nameInTree);
			if(nameIt != nameCache.end()){
				stringstream ss;
				ss << nameInTree << "_" << nameIt->second;
				nameInTree = ss.str();
				message << "Warning: name in tree already defined, alternating name... " << nameInTree << "\n";
				//increment count for this name
				nameIt->second++;
			}
			else {
				//add this name to the cache
				nameCache[nameInTree] = 1;
			}
		}
		
	protected:
		//member variables
		string tempFull, nameInTree, tagName, branchType, title;
		TTree* tree{};
		edm::InputTag tag;
		TBranch* branch{};
};

//comparator (case-insensitive sort)
class TreeObjectComp {
	public:
		bool operator() (TreeObjectBase* b1, TreeObjectBase* b2) const {
			string s1 = b1->GetNameInTree();
			transform(s1.begin(),s1.end(),s1.begin(),::tolower);
			string s2 = b2->GetNameInTree();
			transform(s2.begin(),s2.end(),s2.begin(),::tolower);
			
			return s1 < s2;
		}
};

//class template for tree objects
template <class T>
class TreeObject : public TreeObjectBase {
	public:
		//constructor
		TreeObject() : TreeObjectBase() {}
		TreeObject(string tempFull_, string title_) : TreeObjectBase(tempFull_,title_) {}
		//destructor
		~TreeObject() override {}
		//functions
		void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC, stringstream& message) override {
			//case 1: x      -> tag = x,   name = x
			//case 2: x:y    -> tag = x:y, name = y
			//case 3: x(y)   -> tag = x,   name = y
			//case 4: x:y(z) -> tag = x:y, name = z
			
			size_t pos1 = tempFull.find('(');
			size_t pos2 = tempFull.find(')');
			size_t pos3 = tempFull.find(':');
			
			//case 3/4
			if(pos1!=string::npos && pos2!=string::npos){
				tagName = tempFull.substr(0,pos1);
				nameInTree = tempFull.substr(pos1+1,pos2-(pos1+1));
			}
			//case 2
			else if(pos3!=string::npos){
				nameInTree = tempFull.substr(pos3+1);
			}
			//case 1, nothing to do
			//(constructor assumes this case by default)
			else { }
			
			message << "full name: " << tempFull << " -> tag: " << tagName << " nameInTree: " << nameInTree << "\n";
			//make tag
			tag = edm::InputTag(tagName);
			SetConsumes(std::move(iC));
			
			//finalize name to avoid duplicates
			FinalizeName(nameCache,message);
		}
		virtual void SetConsumes(edm::ConsumesCollector && iC){
			tok = iC.consumes<T>(tag);
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle<T> var;
			iEvent.getByToken(tok,var);
			if( var.isValid() ) {
				value = *var;
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << tagName << " is NOT valid?!";
			}
		}
		//these will be implemented below for specializations
		void AddBranch() override {}
		void SetDefault() override {}
		
	protected:
		//member variables
		T value;
		edm::EDGetTokenT<T> tok;
};

//specialize!

template<>
void TreeObject<bool>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/O").c_str()); }
template<>
void TreeObject<int>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/I").c_str()); }
template<>
void TreeObject<double>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/D").c_str()); }
template<>
void TreeObject<string>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<TLorentzVector>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<math::XYZVector>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<math::XYZPoint>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<vector<bool> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<bool>",&value,32000,0); }
template<>
void TreeObject<vector<int> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<int>",&value,32000,0); }
template<>
void TreeObject<vector<float> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<float>",&value,32000,0); }
template<>
void TreeObject<vector<double> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<double>",&value,32000,0); }
template<>
void TreeObject<vector<string> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<string>",&value,32000,0); }
template<>
void TreeObject<vector<TLorentzVector> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0); }
template<>
void TreeObject<vector<math::XYZVector> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<math::XYZVector>",&value,32000,0); }
template<>
void TreeObject<vector<math::XYZPoint> >::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<math::XYZPoint>",&value,32000,0); }
template<>
void TreeObject<vector<vector<bool>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<bool>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<int>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<int>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<double>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<double>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<string>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<string>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<TLorentzVector>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<TLorentzVector>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<math::XYZVector>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<math::XYZVector>>",&value,32000,0); }
template<>
void TreeObject<vector<vector<math::XYZPoint>>>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),"vector<vector<math::XYZPoint>>",&value,32000,0); }

template<>
void TreeObject<bool>::SetDefault() { value = false; }
template<>
void TreeObject<int>::SetDefault() { value = 9999; }
template<>
void TreeObject<double>::SetDefault() { value = 9999.; }
template<>
void TreeObject<string>::SetDefault() { value = ""; }
template<>
void TreeObject<TLorentzVector>::SetDefault() { value.SetXYZT(0,0,0,0); }
template<>
void TreeObject<math::XYZVector>::SetDefault() { value.SetXYZ(0,0,0); }
template<>
void TreeObject<math::XYZPoint>::SetDefault() { value.SetXYZ(0,0,0); }
template<>
void TreeObject<vector<bool> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<int> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<float> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<double> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<string> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<TLorentzVector> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<math::XYZVector> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<math::XYZPoint> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<bool>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<int>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<double>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<string>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<TLorentzVector>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<math::XYZVector>>>::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<vector<math::XYZPoint>>>::SetDefault() { value.clear(); }

//derived version of vector<TLorentzVector> for RecoCand
//with switch for vector<double> pt, eta, phi, energy instead
class TreeRecoCand : public TreeObject<vector<TLorentzVector> > {
	public:
		//constructor
		TreeRecoCand() : TreeObject<vector<TLorentzVector> >() {}
		TreeRecoCand(string tempFull_, string title_="", bool doLorentz_=true) : TreeObject<vector<TLorentzVector> >(tempFull_,title_), doLorentz(doLorentz_) {}
		//destructor
		~TreeRecoCand() override {}
		
		//functions
		void SetConsumes(edm::ConsumesCollector && iC) override{
			candTok = iC.consumes<edm::View<reco::Candidate>>(tag);
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle< edm::View<reco::Candidate> > cands;
			iEvent.getByToken(candTok,cands);
			if( cands.isValid() ) {
				if(doLorentz){
					value.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						value.emplace_back(iPart->px(), iPart->py(), iPart->pz(), iPart->energy());
					}
				}
				else{
					pt.reserve(cands->size());
					eta.reserve(cands->size());
					phi.reserve(cands->size());
					energy.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						pt.emplace_back(iPart->pt());
						eta.emplace_back(iPart->eta());
						phi.emplace_back(iPart->phi());
						energy.emplace_back(iPart->energy());
					}
				}
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << tagName << " is NOT valid?!";
			}
		}
		void AddBranch() override {
			if(tree){
				if(doLorentz){
					tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0);
				}
				else {
					tree->Branch((nameInTree+"Pt").c_str(),"vector<double>",&pt,32000,0);
					tree->Branch((nameInTree+"Eta").c_str(),"vector<double>",&eta,32000,0);
					tree->Branch((nameInTree+"Phi").c_str(),"vector<double>",&phi,32000,0);
					tree->Branch((nameInTree+"E").c_str(),"vector<double>",&energy,32000,0);
				}
			}
		}
		void SetDefault() override {
			if(doLorentz){
				value.clear();
			}
			else{
				pt.clear();
				eta.clear();
				phi.clear();
				energy.clear();
			}
		}
	
	protected:
		//member variables
		edm::EDGetTokenT<edm::View<reco::Candidate>> candTok;
		bool doLorentz{};
		vector<double> pt, eta, phi, energy;
};
