// CMSSW headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
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
enum TreeTypes { t_bool=0, t_int=1, t_double=2, t_string=3, t_lorentz=4, t_vbool=100, t_vint=101, t_vdouble=102, t_vstring=103, t_vlorentz=104, t_recocand=1000 };

//forward declaration of helper class
class TreeObjectBase;

//
// class declaration
//

class TreeMaker : public edm::EDProducer {
	public:
		explicit TreeMaker(const edm::ParameterSet&);
		~TreeMaker();
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() override;
		virtual void produce(edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;
		// ----------member data ---------------------------
		string treeName;
		TTree* tree;	
		bool debug, doLorentz, sortBranches;
		vector<string> VarTypeNames;
		vector<TreeTypes> VarTypes;
		map<string,unsigned> nameCache;
		// general event information
		UInt_t runNum;
		UInt_t lumiBlockNum;
		ULong64_t evtNum;
		vector<TreeObjectBase*> variables;
};

//base class for tree objects
class TreeObjectBase {
	public:
		//constructor
		TreeObjectBase() : tempFull(""), branchType("") {}
		TreeObjectBase(string tempFull_) : tempFull(tempFull_), nameInTree(tempFull_), tagName(tempFull_), tree(NULL) {}
		//destructor
		virtual ~TreeObjectBase() {}
		//functions
		virtual string GetNameInTree() { return nameInTree; }
		virtual void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC) {}
		virtual void SetTree(TTree* tree_) { tree = tree_; }
		virtual void AddBranch() {}
		virtual void SetDefault() {}
		virtual void FillTree(edm::Event& iEvent) {}
		
		//common helper function
		virtual void FinalizeName(map<string,unsigned>& nameCache){
			auto nameIt = nameCache.find(nameInTree);
			if(nameIt != nameCache.end()){
				stringstream ss;
				ss << nameInTree << "_" << nameIt->second;
				nameInTree = ss.str();
				cout << "Warning: name in tree already defined, alternating name... " << nameInTree << endl;
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
		string tempFull, nameInTree, tagName, branchType;
		TTree* tree;
		edm::InputTag tag;
};

//comparator (case-insensitive sort)
class TreeObjectComp {
	public:
		bool operator() (TreeObjectBase* b1, TreeObjectBase* b2){
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
		TreeObject(string tempFull_) : TreeObjectBase(tempFull_) {}
		//destructor
		virtual ~TreeObject() {}
		//functions
		virtual void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC) {
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
			
			cout << "full name: " << tempFull << " -> tag: " << tagName << " nameInTree: " << nameInTree << endl;
			//make tag
			tag = edm::InputTag(tagName);
			SetConsumes(std::move(iC));
			
			//finalize name to avoid duplicates
			FinalizeName(nameCache);
		}
		virtual void SetConsumes(edm::ConsumesCollector && iC){
			tok = iC.consumes<T>(tag);
		}
		virtual void FillTree(edm::Event& iEvent){
			SetDefault();
			edm::Handle<T> var;
			iEvent.getByToken(tok,var);
			if( var.isValid() ) {
				value = *var;
			}
			else {
				cout << "WARNING ... " << tagName << " is NOT valid?!" << endl;
			}
		}
		//these will be implemented below for specializations
		virtual void AddBranch() {}
		virtual void SetDefault() {}
		
	protected:
		//member variables
		T value;
		edm::EDGetTokenT<T> tok;
};

//specialize!

template<>
void TreeObject<bool>::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/O").c_str()); }
template<>
void TreeObject<int>::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/I").c_str()); }
template<>
void TreeObject<double>::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/D").c_str()); }
template<>
void TreeObject<string>::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<TLorentzVector>::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<vector<bool> >::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<bool>",&value,32000,0); }
template<>
void TreeObject<vector<int> >::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<int>",&value,32000,0); }
template<>
void TreeObject<vector<double> >::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<double>",&value,32000,0); }
template<>
void TreeObject<vector<string> >::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<string>",&value,32000,0); }
template<>
void TreeObject<vector<TLorentzVector> >::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0); }

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
void TreeObject<vector<bool> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<int> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<double> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<string> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<TLorentzVector> >::SetDefault() { value.clear(); }

//derived version of vector<TLorentzVector> for RecoCand
//with switch for vector<double> pt, eta, phi, energy instead
class TreeRecoCand : public TreeObject<vector<TLorentzVector> > {
	public:
		//constructor
		TreeRecoCand() : TreeObject<vector<TLorentzVector> >() {}
		TreeRecoCand(string tempFull_, bool doLorentz_=true) : TreeObject<vector<TLorentzVector> >(tempFull_), doLorentz(doLorentz_) {}
		//destructor
		virtual ~TreeRecoCand() {}
		
		//functions
		virtual void SetConsumes(edm::ConsumesCollector && iC){
			candTok = iC.consumes<edm::View<reco::Candidate>>(tag);
		}
		virtual void FillTree(edm::Event& iEvent){
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
				cout << "WARNING ... " << tagName << " is NOT valid?!" << endl;
			}
		}
		virtual void AddBranch() {
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
		virtual void SetDefault() {
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
		bool doLorentz;
		vector<double> pt, eta, phi, energy;
};