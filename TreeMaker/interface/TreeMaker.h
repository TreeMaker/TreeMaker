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
#include "DataFormats/Math/interface/LorentzVector.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

//ROOT headers
#include "TString.h"
#include "TBranch.h"
#include "TTree.h"
#include <TFile.h>
#include "Math/GenVector/LorentzVector.h"

//STL headers
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
#include <utility>
#include <iterator>

using namespace std;

//enum with known types
enum TreeTypes { 
	t_bool=0, t_int=1, t_double=2, t_string=3, t_lorentz=4, t_xyzv=5, t_xyzp=6,
	t_vbool=100, t_vint=101, t_vdouble=102, t_vstring=103, t_vlorentz=104, t_vxyzv=105, t_vxyzp=106, t_vfloat=107,
	t_vvbool=200, t_vvint=201, t_vvdouble=202, t_vvstring=203, t_vvlorentz=204, t_vvxyzv=205, t_vvxyzp=206,
	t_avvbool=300, t_avvint=301, t_avvdouble=302, t_avvstring=303, t_avvlorentz=304, t_avvxyzv=305, t_avvxyzp=306,
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
		bool doLorentz, sortBranches, debugTitles, nestedVectors, storeOffsets, saveFloat;
		int splitLevel;
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
		TreeObjectBase() : tempFull("") {}
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
		string tempFull, nameInTree, tagName, title;
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
template <class Tin, class Tout=Tin>
class TreeObject : public TreeObjectBase {
	public:
		//make types accessible
		typedef Tin T_in;
		typedef Tout T_out;
		//constructor
		TreeObject() : TreeObjectBase() {}
		TreeObject(string tempFull_, string title_, int splitLevel_=0) : TreeObjectBase(tempFull_,title_), splitLevel(splitLevel_) {}
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
			tok = iC.consumes<Tin>(tag);
		}
		void GetValue(const edm::Handle<Tin>& var) {
			value = *var;
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle<Tin> var;
			iEvent.getByToken(tok,var);
			if( var.isValid() ) {
				GetValue(var);
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << tagName << " is NOT valid?!";
			}
		}
		//most common cases here
		string GetBranchType() { return nameInTree; }
		void AddBranch() override { if(tree) branch = tree->Branch(nameInTree.c_str(),GetBranchType().c_str(),&value,32000,splitLevel); }
		void SetDefault() override { value.clear(); }
		//implemented below for specializations (mostly primitive types)
		
	protected:
		//member variables
		Tout value;
		edm::EDGetTokenT<Tin> tok;
		int splitLevel{};
};

//typedefs for float conversions
typedef TreeObject<double,float> TreeObjectDoubleToF;
typedef TreeObject<vector<double>,vector<float>> TreeObjectVDoubleToF;
typedef TreeObject<vector<vector<double>>,vector<vector<float>>> TreeObjectVVDoubleToF;
typedef TreeObject<math::PtEtaPhiELorentzVector,math::PtEtaPhiELorentzVectorF> TreeObjectLVToF;
typedef TreeObject<math::XYZVector,math::XYZVectorF> TreeObjectXYZVToF;
typedef TreeObject<math::XYZPoint,math::XYZPointF> TreeObjectXYZPToF;
typedef TreeObject<vector<math::PtEtaPhiELorentzVector>,vector<math::PtEtaPhiELorentzVectorF>> TreeObjectVLVToF;
typedef TreeObject<vector<math::XYZVector>,vector<math::XYZVectorF>> TreeObjectVXYZVToF;
typedef TreeObject<vector<math::XYZPoint>,vector<math::XYZPointF>> TreeObjectVXYZPToF;
typedef TreeObject<vector<vector<math::PtEtaPhiELorentzVector>>,vector<vector<math::PtEtaPhiELorentzVectorF>>> TreeObjectVVLVToF;
typedef TreeObject<vector<vector<math::XYZVector>>,vector<vector<math::XYZVectorF>>> TreeObjectVVXYZVToF;
typedef TreeObject<vector<vector<math::XYZPoint>>,vector<vector<math::XYZPointF>>> TreeObjectVVXYZPToF;
//typedefs for doubles
typedef TreeObject<double> TreeObjectDouble;
typedef TreeObject<vector<double>> TreeObjectVDouble;
typedef TreeObject<vector<vector<double>>> TreeObjectVVDouble;
typedef TreeObject<math::PtEtaPhiELorentzVector> TreeObjectLV;
typedef TreeObject<math::XYZVector> TreeObjectXYZV;
typedef TreeObject<math::XYZPoint> TreeObjectXYZP;
typedef TreeObject<vector<math::PtEtaPhiELorentzVector>> TreeObjectVLV;
typedef TreeObject<vector<math::XYZVector>> TreeObjectVXYZV;
typedef TreeObject<vector<math::XYZPoint>> TreeObjectVXYZP;
typedef TreeObject<vector<vector<math::PtEtaPhiELorentzVector>>> TreeObjectVVLV;
typedef TreeObject<vector<vector<math::XYZVector>>> TreeObjectVVXYZV;
typedef TreeObject<vector<vector<math::XYZPoint>>> TreeObjectVVXYZP;
//todo: typedef the rest for consistency

//convert double to float
template<>
void TreeObjectVDoubleToF::GetValue(const edm::Handle<vector<double>>& var) {
	value = vector<float>(var->begin(),var->end());
}
template<>
void TreeObjectVVDoubleToF::GetValue(const edm::Handle<vector<vector<double>>>& var) {
	value.reserve(var->size());
	for(const auto& ivar: *var){
		value.emplace_back(ivar.begin(),ivar.end());
	}
}
template<>
void TreeObjectVLVToF::GetValue(const edm::Handle<vector<math::PtEtaPhiELorentzVector>>& var) {
	value = vector<math::PtEtaPhiELorentzVectorF>(var->begin(),var->end());
}
template<>
void TreeObjectVXYZVToF::GetValue(const edm::Handle<vector<math::XYZVector>>& var) {
	value = vector<math::XYZVectorF>(var->begin(),var->end());
}
template<>
void TreeObjectVXYZPToF::GetValue(const edm::Handle<vector<math::XYZPoint>>& var) {
	value = vector<math::XYZPointF>(var->begin(),var->end());
}
template<>
void TreeObjectVVLVToF::GetValue(const edm::Handle<vector<vector<math::PtEtaPhiELorentzVector>>>& var) {
	value.reserve(var->size());
	for(const auto& ivar: *var){
		value.emplace_back(ivar.begin(),ivar.end());
	}
}
template<>
void TreeObjectVVXYZVToF::GetValue(const edm::Handle<vector<vector<math::XYZVector>>>& var) {
	value.reserve(var->size());
	for(const auto& ivar: *var){
		value.emplace_back(ivar.begin(),ivar.end());
	}
}
template<>
void TreeObjectVVXYZPToF::GetValue(const edm::Handle<vector<vector<math::XYZPoint>>>& var) {
	value.reserve(var->size());
	for(const auto& ivar: *var){
		value.emplace_back(ivar.begin(),ivar.end());
	}
}

//specialize!

template<>
void TreeObject<bool>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/O").c_str()); }
template<>
void TreeObject<int>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/I").c_str()); }
template<>
void TreeObjectDoubleToF::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/F").c_str()); }
template<>
void TreeObjectDouble::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/D").c_str()); }
template<>
void TreeObject<string>::AddBranch() { if(tree) branch = tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
string TreeObject<vector<bool> >::GetBranchType() { return "vector<bool>"; }
template<>
string TreeObject<vector<int> >::GetBranchType() { return "vector<int>"; }
template<>
string TreeObject<vector<float> >::GetBranchType() { return "vector<float>"; }
template<>
string TreeObjectVDoubleToF::GetBranchType() { return "vector<float>"; }
template<>
string TreeObjectVDouble::GetBranchType() { return "vector<double>"; }
template<>
string TreeObject<vector<string> >::GetBranchType() { return "vector<string>"; }
template<>
string TreeObjectVLVToF::GetBranchType() { return "vector<math::PtEtaPhiELorentzVectorF>"; }
template<>
string TreeObjectVLV::GetBranchType() { return "vector<math::PtEtaPhiELorentzVector>"; }
template<>
string TreeObjectVXYZVToF::GetBranchType() { return "vector<math::XYZVectorF>"; }
template<>
string TreeObjectVXYZV::GetBranchType() { return "vector<math::XYZVector>"; }
template<>
string TreeObjectVXYZPToF::GetBranchType() { return "vector<math::XYZPointF>"; }
template<>
string TreeObjectVXYZP::GetBranchType() { return "vector<math::XYZPoint>"; }
template<>
string TreeObject<vector<vector<bool>>>::GetBranchType() { return "vector<vector<bool>>"; }
template<>
string TreeObject<vector<vector<int>>>::GetBranchType() { return "vector<vector<int>>"; }
template<>
string TreeObjectVVDoubleToF::GetBranchType() { return "vector<vector<float>>"; }
template<>
string TreeObjectVVDouble::GetBranchType() { return "vector<vector<double>>"; }
template<>
string TreeObject<vector<vector<string>>>::GetBranchType() { return "vector<vector<string>>"; }
template<>
string TreeObjectVVLVToF::GetBranchType() { return "vector<vector<math::PtEtaPhiELorentzVectorF>>"; }
template<>
string TreeObjectVVLV::GetBranchType() { return "vector<vector<math::PtEtaPhiELorentzVector>>"; }
template<>
string TreeObjectVVXYZVToF::GetBranchType() { return "vector<vector<math::XYZVectorF>>"; }
template<>
string TreeObjectVVXYZPToF::GetBranchType() { return "vector<vector<math::XYZPointF>>"; }
template<>
string TreeObjectVVXYZP::GetBranchType() { return "vector<vector<math::XYZPoint>>"; }

template<>
void TreeObject<bool>::SetDefault() { value = false; }
template<>
void TreeObject<int>::SetDefault() { value = 9999; }
template<>
void TreeObjectDoubleToF::SetDefault() { value = 9999.; }
template<>
void TreeObjectDouble::SetDefault() { value = 9999.; }
template<>
void TreeObject<string>::SetDefault() { value = ""; }
template<>
void TreeObjectLVToF::SetDefault() { value.SetXYZT(0,0,0,0); }
template<>
void TreeObjectLV::SetDefault() { value.SetXYZT(0,0,0,0); }
template<>
void TreeObjectXYZVToF::SetDefault() { value.SetXYZ(0,0,0); }
template<>
void TreeObjectXYZV::SetDefault() { value.SetXYZ(0,0,0); }
template<>
void TreeObjectXYZPToF::SetDefault() { value.SetXYZ(0,0,0); }
template<>
void TreeObjectXYZP::SetDefault() { value.SetXYZ(0,0,0); }

//derived version of vector<math::PtEtaPhiELorentzVector> for RecoCand
//with switch for vector<double> pt, eta, phi, energy instead
template <class T>
class TreeRecoCandT : public T {
	public:
		//constructor
		TreeRecoCandT() : T() {}
		TreeRecoCandT(string tempFull_, string title_="", bool doLorentz_=true, int splitLevel_=0) : T(tempFull_,title_,splitLevel_), doLorentz(doLorentz_) {}
		//destructor
		~TreeRecoCandT() override {}
		
		//functions
		void SetConsumes(edm::ConsumesCollector && iC) override{
			candTok = iC.consumes<edm::View<reco::Candidate>>(this->tag);
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle< edm::View<reco::Candidate> > cands;
			iEvent.getByToken(candTok,cands);
			if( cands.isValid() ) {
				if(doLorentz){
					this->value.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						this->value.emplace_back(iPart->pt(), iPart->eta(), iPart->phi(), iPart->energy());
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
				edm::LogWarning("TreeMaker") << "WARNING ... " << this->tagName << " is NOT valid?!";
			}
		}
		void AddBranch() override {
			if(this->tree){
				if(doLorentz){
					this->tree->Branch(this->nameInTree.c_str(),this->GetBranchType().c_str(),&(this->value),32000,this->splitLevel);
				}
				else {
					this->tree->Branch((this->nameInTree+"Pt").c_str(),this->GetBranchType().c_str(),&pt,32000,this->splitLevel);
					this->tree->Branch((this->nameInTree+"Eta").c_str(),this->GetBranchType().c_str(),&eta,32000,this->splitLevel);
					this->tree->Branch((this->nameInTree+"Phi").c_str(),this->GetBranchType().c_str(),&phi,32000,this->splitLevel);
					this->tree->Branch((this->nameInTree+"E").c_str(),this->GetBranchType().c_str(),&energy,32000,this->splitLevel);
				}
			}
		}
		void SetDefault() override {
			if(doLorentz){
				this->value.clear();
			}
			else{
				pt.clear();
				eta.clear();
				phi.clear();
				energy.clear();
			}
		}
		string GetBranchType() { return ""; }

	protected:
		//member variables
		edm::EDGetTokenT<edm::View<reco::Candidate>> candTok;
		bool doLorentz{};
		vector<typename T::T_out> pt, eta, phi, energy;
};

//specializations of type names
typedef TreeRecoCandT<TreeObjectVLVToF> TreeRecoCandToF;
typedef TreeRecoCandT<TreeObjectVLV> TreeRecoCand;
template<>
string TreeRecoCandToF::GetBranchType() {
  if(doLorentz) return "vector<math::PtEtaPhiELorentzVectorF>";
  else return "vector<float>";
}
template<>
string TreeRecoCand::GetBranchType() {
  if(doLorentz) return "vector<math::PtEtaPhiELorentzVector>";
  else return "vector<double>";
}

// Derived version of vector<vector<T>> with switch for vector<T> values and vector<int> offsets instead
template <typename BaseIn = double, typename BaseOut = BaseIn> 
class TreeNestedVector : public TreeObject<std::vector<std::vector<BaseIn>>,std::vector<std::vector<BaseOut>>> {
	public:
		// Typedefs
		typedef std::vector<BaseIn> SubIn;
		typedef std::vector<SubIn> TopIn;
		typedef std::vector<BaseOut> SubOut;
		typedef std::vector<SubOut> TopOut;

		// Constructor
		TreeNestedVector() : TreeObject<TopIn,TopOut>() {}
		TreeNestedVector(string tempFull_, string title_="", bool nestedVectors_=true, bool storeOffsets_=true, bool associated_=false, int splitLevel_=0) :
			TreeObject<TopIn,TopOut>(tempFull_,title_,splitLevel_), nestedVectors(nestedVectors_), storeOffsets(storeOffsets_), associated(associated_) {}
		// Destructor
		~TreeNestedVector() override {}
		
		// Functions
		// From: https://stackoverflow.com/questions/17294629/merging-flattening-sub-vectors-into-a-single-vector-c-converting-2d-to-1d
		void flatten(TopIn const& all, SubOut &accum, vector<int> &offsets) {
			// Don't store any offsets if there are no sub-vectors
			if (all.size() == 0) return;
			if (!associated && storeOffsets) { offsets.insert(std::end(offsets),0); }
			for(auto& sub : all) {
				accum.insert(std::end(accum), std::begin(sub), std::end(sub));
				if (!associated) offsets.insert(std::end(offsets), storeOffsets ? accum.size() : sub.size());
			}
			// This protects against the case where there were >=1 empty sub-vectors, and only empty vectors
			// Thus, nothing will be in the output (accum) vector, but the offsets would be all '0'
			if (storeOffsets && !associated && accum.size() == 0) offsets.clear();
		}
		void SetConsumes(edm::ConsumesCollector && iC) override{
			tok = iC.consumes<TopIn>(this->tag);
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle<TopIn> var;
			iEvent.getByToken(tok,var);
			if( var.isValid() ) {
				if(nestedVectors){
					this->GetValue(var);
				}
				else{
					size_t totalLength = 0;
					for(auto iOuter = var->begin(); iOuter != var->end(); ++iOuter) {
						totalLength += iOuter->size();
					}
					values.reserve(totalLength);
					if (!associated) offsets.reserve(var->size());
					flatten(*var,values,offsets);
				}
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << this->tagName << " is NOT valid?!";
			}
		}
		void AddBranch() override {
			if(this->tree){
				if(nestedVectors){
					this->tree->Branch(this->nameInTree.c_str(),GetTopType().c_str(),&this->value,32000,this->splitLevel);
				}
				else {
					this->tree->Branch((this->nameInTree).c_str(),GetSubType().c_str(),&values,32000,this->splitLevel);
					if (!associated) this->tree->Branch((this->nameInTree+(storeOffsets ? "Offsets" : "Counts")).c_str(),"vector<int>",&offsets,32000,this->splitLevel);
				}
			}
		}
		void SetDefault() override {
			if(nestedVectors){
				this->value.clear();
			}
			else{
				values.clear();
				if (!associated) offsets.clear();
			}
		}
		const string GetTopType() {
			return "vector<" + GetSubType() + ">";
		}
		const string GetSubType() {
			return "vector<" + GetBaseType() + ">";
		}
		// Default implementation
		const string GetBaseType() {
			return typeid(BaseOut).name();
		}

	protected:
		// Member variables
		edm::EDGetTokenT<TopIn> tok;
		bool nestedVectors{}, storeOffsets{}, associated{};
		SubOut values;
		vector<int> offsets;
};

//more typedefs
typedef TreeNestedVector<double,float> TreeNVDoubleToF;
typedef TreeNestedVector<math::PtEtaPhiELorentzVector,math::PtEtaPhiELorentzVectorF> TreeNVLVToF;
typedef TreeNestedVector<math::XYZVector,math::XYZVectorF> TreeNVXYZVToF;
typedef TreeNestedVector<math::XYZPoint,math::XYZPointF> TreeNVXYZPToF;
typedef TreeNestedVector<double> TreeNVDouble;
typedef TreeNestedVector<math::PtEtaPhiELorentzVector> TreeNVLV;
typedef TreeNestedVector<math::XYZVector> TreeNVXYZV;
typedef TreeNestedVector<math::XYZPoint> TreeNVXYZP;

// A specialization for each type where you don't like the string returned by typeid
template <>
const string TreeNestedVector<bool>::GetBaseType() { return "bool"; }
template <>
const string TreeNestedVector<int>::GetBaseType() { return "int"; }
template <>
const string TreeNVDoubleToF::GetBaseType() { return "float"; }
template <>
const string TreeNVDouble::GetBaseType() { return "double"; }
template <>
const string TreeNestedVector<string>::GetBaseType() { return "string"; }
template <>
const string TreeNVLVToF::GetBaseType() { return "math::PtEtaPhiELorentzVectorF"; }
template <>
const string TreeNVLV::GetBaseType() { return "math::PtEtaPhiELorentzVector"; }
template <>
const string TreeNVXYZVToF::GetBaseType() { return "math::XYZVectorF"; }
template <>
const string TreeNVXYZV::GetBaseType() { return "math::XYZVector"; }
template <>
const string TreeNVXYZPToF::GetBaseType() { return "math::XYZPointF"; }
template <>
const string TreeNVXYZP::GetBaseType() { return "math::XYZPoint"; }



