// -*- C++ -*-
//
// Package:    TreeMaker/TreeMaker
// Class:      TreeMaker
// 
/**\class TreeMaker TreeMaker.cc TreeMaker/TreeMaker/src/TreeMaker.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger
//         Created:  Fri, 03 Dec 2014 13:48:35 GMT
//      Updated by:  Kevin Pedro
//
//
#include "TreeMaker/TreeMaker/interface/TreeMaker.h"
#include <set>

using namespace std;
using namespace edm;
using namespace reco;
using namespace pat;

//
// constructors and destructor
//
TreeMaker::TreeMaker(const edm::ParameterSet& iConfig) :
	tree(nullptr),
	VarTypeNames{
		"VarsBool","VarsInt","VarsDouble","VarsString","VarsTLorentzVector",
		"VectorBool","VectorInt","VectorDouble","VectorString","VectorTLorentzVector",
		"VectorVectorBool","VectorVectorInt","VectorVectorDouble","VectorVectorString","VectorVectorTLorentzVector",
		"VectorRecoCand"
	},
	VarTypes{
		t_bool,t_int,t_double,t_string,t_lorentz,
		t_vbool,t_vint,t_vdouble,t_vstring,t_vlorentz,
		t_vvbool,t_vvint,t_vvdouble,t_vvstring,t_vvlorentz,
		t_recocand
	}
{
	usesResource("TFileService");

	// general parameters
	treeName = iConfig.getParameter<string>("TreeName");
	doLorentz = iConfig.getParameter<bool>("doLorentz");
	sortBranches = iConfig.getParameter<bool>("sortBranches");
	//loop over all var type names to initialize TreeObjects
	set<string> nameSet;
	stringstream skipMessage;
	stringstream message;
	for(unsigned v = 0; v < VarTypeNames.size(); ++v){
		vector<string> VarNames = iConfig.getParameter< vector<string> >(VarTypeNames.at(v));
		message << VarTypeNames.at(v) << ":" << "\n";
		for(const auto & VarName : VarNames){
			//check for an exact repeat of an existing name
			if(nameSet.find(VarName)!=nameSet.end()){
				skipMessage << VarName << "\n";
				continue;
			}
			else nameSet.emplace(VarName);
			//check for the right type
			TreeObjectBase* tmp = nullptr;
			switch(VarTypes[v]){
				case TreeTypes::t_bool     : tmp = new TreeObject<bool>(VarName); break;
				case TreeTypes::t_int      : tmp = new TreeObject<int>(VarName); break;
				case TreeTypes::t_double   : tmp = new TreeObject<double>(VarName); break;
				case TreeTypes::t_string   : tmp = new TreeObject<string>(VarName); break;
				case TreeTypes::t_lorentz  : tmp = new TreeObject<TLorentzVector>(VarName); break;
				case TreeTypes::t_vbool    : tmp = new TreeObject<vector<bool> >(VarName); break;
				case TreeTypes::t_vint     : tmp = new TreeObject<vector<int> >(VarName); break;
				case TreeTypes::t_vdouble  : tmp = new TreeObject<vector<double> >(VarName); break;
				case TreeTypes::t_vstring  : tmp = new TreeObject<vector<string> >(VarName); break;
				case TreeTypes::t_vlorentz : tmp = new TreeObject<vector<TLorentzVector> >(VarName); break;
				case TreeTypes::t_vvbool   : tmp = new TreeObject<vector<vector<bool>>>(VarName); break;
				case TreeTypes::t_vvint    : tmp = new TreeObject<vector<vector<int>>>(VarName); break;
				case TreeTypes::t_vvdouble : tmp = new TreeObject<vector<vector<double>>>(VarName); break;
				case TreeTypes::t_vvstring : tmp = new TreeObject<vector<vector<string>>>(VarName); break;
				case TreeTypes::t_vvlorentz: tmp = new TreeObject<vector<vector<TLorentzVector>>>(VarName); break;
				case TreeTypes::t_recocand : tmp = new TreeRecoCand(VarName,doLorentz); break;
			}
			//if a known type was found, initialize and store the object
			if(tmp) {
				tmp->Initialize(nameCache,consumesCollector(),message);
				variables.push_back(tmp);
			}
		}
	}
	//print info
	if(!skipMessage.str().empty()) edm::LogInfo("TreeMaker") << "Skipping repeated branches:\n" << skipMessage.str();
	edm::LogInfo("TreeMaker") << message.str();
}

TreeMaker::~TreeMaker() {}

//
// member functions
//

// ------------ method called to produce the data  ------------
void
TreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{ 
    //set variables to default
	runNum = 0;
	lumiBlockNum = 0;
	evtNum = 0;

	// Event information
	const edm::EventAuxiliary& aux = iEvent.eventAuxiliary();
	runNum       = aux.run();
	lumiBlockNum = aux.luminosityBlock();
	evtNum       = aux.event();
	
	// get all variable values
	for(auto & variable : variables){
		variable->FillTree(iEvent);
	}
	
	tree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
TreeMaker::beginJob()
{
	if( !fs ) {
		throw edm::Exception(edm::errors::Configuration, "TFile Service is not registered in cfg file");
	}
	tree = fs->make<TTree>(treeName.c_str(),treeName.c_str());  
	tree->SetAutoSave(10000000000);
	tree->SetAutoFlush(1000000);
	tree->Branch("RunNum",&runNum,"RunNum/i");
	tree->Branch("LumiBlockNum",&lumiBlockNum,"LumiBlockNum/i");
	tree->Branch("EvtNum",&evtNum,"EvtNum/l");
	
	//sort TreeObjects (if desired)
	if(sortBranches) sort(variables.begin(),variables.end(),TreeObjectComp());
	
	//add branches to tree
	for(auto & variable : variables){
		variable->SetTree(tree);
		variable->AddBranch();
	}
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TreeMaker::endJob() {
	//memory management
	for(auto & variable : variables){
		delete variable;
	}
	variables.clear();

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TreeMaker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TreeMaker);
