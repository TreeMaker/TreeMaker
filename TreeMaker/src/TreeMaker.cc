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

using namespace std;
using namespace edm;
using namespace reco;
using namespace pat;

//
// constructors and destructor
//
TreeMaker::TreeMaker(const edm::ParameterSet& iConfig)
: tree(0),
  VarTypeNames{"VarsBool","VarsInt","VarsDouble","VarsString","VarsTLorentzVector","VectorBool","VectorInt","VectorDouble","VectorString","VectorTLorentzVector","VectorRecoCand"},
  VarTypes{t_bool,t_int,t_double,t_string,t_lorentz,t_vbool,t_vint,t_vdouble,t_vstring,t_vlorentz,t_recocand}
{
	// general parameters
	treeName = iConfig.getParameter<string>("TreeName");
	debug = iConfig.getParameter<bool>("debug");
	doLorentz = iConfig.getParameter<bool>("doLorentz");
	sortBranches = iConfig.getParameter<bool>("sortBranches");
	//loop over all var type names
	VarNames.reserve(VarTypeNames.size());
	for(unsigned v = 0; v < VarTypeNames.size(); ++v){
		VarNames.push_back(iConfig.getParameter< vector<string> >(VarTypeNames.at(v)));
	}
}

TreeMaker::~TreeMaker() {}

//
// member functions
//

// ------------ method called to produce the data  ------------
void
TreeMaker::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{ 
    //set variables to default
	runNum = 0;
	lumiBlockNum = 0;
	evtNum = 0;

	// Event information
	edm::EventAuxiliary aux = iEvent.eventAuxiliary();
	runNum       = aux.run();
	lumiBlockNum = aux.luminosityBlock();
	evtNum       = aux.event();
	
	// get all variable values
	for(unsigned t = 0; t < variables.size(); ++t){
		variables[t]->FillTree(iEvent);
	}
	
	tree->Fill();
	if(debug) cout << "Done filling tree" << endl;
}

// ------------ method called once each job just before starting event loop  ------------
void 
TreeMaker::beginJob()
{
	edm::Service<TFileService> fs;
	if( !fs ) {
		throw edm::Exception(edm::errors::Configuration, "TFile Service is not registered in cfg file");
	}
	tree = fs->make<TTree>(treeName.c_str(),treeName.c_str());  
	tree->SetAutoSave(10000000000);
	tree->SetAutoFlush(1000000);
	tree->Branch("RunNum",&runNum,"RunNum/i");
	tree->Branch("LumiBlockNum",&lumiBlockNum,"LumiBlockNum/i");
	tree->Branch("EvtNum",&evtNum,"EvtNum/l");

	//initialize TreeObjects
	for(unsigned v = 0; v < VarNames.size(); ++v){
		cout << VarTypeNames[v] << ":" << endl;
		for(unsigned t = 0; t < VarNames[v].size(); ++t){
			//check for the right type
			TreeObjectBase* tmp = NULL;
			switch(VarTypes[v]){
				case TreeTypes::t_bool     : tmp = new TreeObject<bool>(VarNames[v][t],tree); break;
				case TreeTypes::t_int      : tmp = new TreeObject<int>(VarNames[v][t],tree); break;
				case TreeTypes::t_double   : tmp = new TreeObject<double>(VarNames[v][t],tree); break;
				case TreeTypes::t_string   : tmp = new TreeObject<string>(VarNames[v][t],tree); break;
				case TreeTypes::t_lorentz  : tmp = new TreeObject<TLorentzVector>(VarNames[v][t],tree); break;
				case TreeTypes::t_vbool    : tmp = new TreeObject<vector<bool> >(VarNames[v][t],tree); break;
				case TreeTypes::t_vint     : tmp = new TreeObject<vector<int> >(VarNames[v][t],tree); break;
				case TreeTypes::t_vdouble  : tmp = new TreeObject<vector<double> >(VarNames[v][t],tree); break;
				case TreeTypes::t_vstring  : tmp = new TreeObject<vector<string> >(VarNames[v][t],tree); break;
				case TreeTypes::t_vlorentz : tmp = new TreeObject<vector<TLorentzVector> >(VarNames[v][t],tree); break;
				case TreeTypes::t_recocand : tmp = new TreeRecoCand(VarNames[v][t],tree,doLorentz); break;
			}
			//if a known type was found, initialize and store the object
			if(tmp) {
				tmp->Initialize(nameCache);
				variables.push_back(tmp);
			}
		}
	}
	
	//sort TreeObjects (if desired)
	if(sortBranches) sort(variables.begin(),variables.end(),TreeObjectComp());
	
	//add branches to tree
	for(unsigned t = 0; t < variables.size(); ++t){
		variables[t]->AddBranch();
	}
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TreeMaker::endJob() {
	//memory management
	for(unsigned t = 0; t < variables.size(); ++t){
		delete (variables[t]);
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