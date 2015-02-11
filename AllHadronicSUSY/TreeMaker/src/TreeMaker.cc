// -*- C++ -*-
//
// Package:    AllHadronicSUSY/TreeMaker
// Class:      TreeMaker
// 
/**\class TreeMaker TreeMaker.cc AllHadronicSUSY/TreeMaker/plugins/TreeMaker.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger
//         Created:  Fri, 03 Dec 2014 13:48:35 GMT
//
//
#include "AllHadronicSUSY/TreeMaker/interface/TreeMaker.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include <memory>

// system include files

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
TreeMaker::TreeMaker(const edm::ParameterSet& iConfig)
: nMaxCandidates_(10000), tree_(0)
{
  // generell
  treeName_ = iConfig.getParameter<std::string>("TreeName");
  debug_ = iConfig.getParameter<bool> ("debug");
  // input tags for float variables eg HT MHT MET or what not
  VarsTLorentzVectorNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsTLoretzVector");
  VarsStringNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsString");
  VarsDoubleNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsDouble");
  VarsIntNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsInt");
  VarsBoolNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsBool");
  
  VectorDoubleNames_= iConfig.getParameter< std::vector<std::string> >  ("VectorDouble");
  VectorIntNames_= iConfig.getParameter< std::vector<std::string> >  ("VectorInt");
  VectorBoolNames_= iConfig.getParameter< std::vector<std::string> >  ("VectorBool");
  VectorStringNames_= iConfig.getParameter< std::vector<std::string> >  ("VectorString");
  VectorTLorentzVectorNames_= iConfig.getParameter< std::vector<std::string> >  ("VectorTLorentzVector");
  
  varsRecoCandNames_= iConfig.getParameter< std::vector<std::string> >  ("VarsRecoCand");
  
  VarsDouble_.clear();
  VarsInt_.clear();
  VarsBool_.clear();
  VarsString_.clear();
  VarsTLorentzVector_.clear();
  VectorDoubleVector_.clear();
  VectorIntVector_.clear();
  VectorBoolVector_.clear();
  VectorStringVector_.clear();
  VectorTLorentzVector_.clear();
  nameCache_.clear();
  
}


TreeMaker::~TreeMaker()
{
  
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TreeMaker::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  using namespace pat;
  setBranchVariablesToDefault();
  
  // Event information
  edm::EventAuxiliary aux = iEvent.eventAuxiliary();
  runNum_       = aux.run();
  lumiBlockNum_ = aux.luminosityBlock();
  evtNum_       = aux.event();
  if(debug_) std::cout<<"Point a"<<std::endl;
  for(unsigned int i = 0; i < VarsIntTags_.size(); ++i) {
    edm::Handle<int> var;
    iEvent.getByLabel(VarsIntTags_.at(i),var);
    if( var.isValid() ) {
      VarsInt_.at(i) = *var;
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VarsIntTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point b"<<std::endl;
  for(unsigned int i = 0; i < VarsDoubleTags_.size(); ++i) {
    edm::Handle<double> var;
    iEvent.getByLabel(VarsDoubleTags_.at(i),var);
    if( var.isValid() ) {
      VarsDouble_.at(i) = *var;
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VarsDoubleTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point c"<<std::endl;
  for(unsigned int i = 0; i < VarsBoolTags_.size(); ++i) {
    edm::Handle<bool> var;
    iEvent.getByLabel(VarsBoolTags_.at(i),var);
    if( var.isValid() ) {
      if( *var ) VarsBool_.at(i) = 1;
      else VarsBool_.at(i) = 0;
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VarsBoolTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point d"<<std::endl;
  for(unsigned int i = 0; i < VarsStringTags_.size(); ++i) {
    edm::Handle<std::string> var;
    iEvent.getByLabel(VarsStringTags_.at(i),var);
    if( var.isValid() ) {
      VarsString_.at(i) = *var;
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VarsStringTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point e"<<std::endl;
  for(unsigned int i = 0; i < VarsTLorentzVectorTags_.size(); ++i) {
    edm::Handle<TLorentzVector> var;
    iEvent.getByLabel(VarsTLorentzVectorTags_.at(i),var);
    if( var.isValid() ) {
      VarsTLorentzVector_.at(i) = *var;
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VarsTLorentzVectorTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point f"<<std::endl;
  for(unsigned int i = 0; i < varsRecoCandTags_.size(); ++i) 
  {
    edm::Handle< edm::View<reco::Candidate> > cands;
    iEvent.getByLabel(varsRecoCandTags_.at(i),cands);
    if( cands.isValid() ) 
    {
      RecoCandN_[i] = (unsigned int)(cands->size());
      for(unsigned int ii=0; ii < cands->size();ii++)
      {
	RecoCandPt_.at(i)[ii] = cands->at(ii).pt();
	RecoCandEta_.at(i)[ii] = cands->at(ii).eta();
	RecoCandPhi_.at(i)[ii] = cands->at(ii).phi();
	RecoCandE_.at(i)[ii] = cands->at(ii).energy();
	RecoCandLorentzVector_.at(i)[ii].SetXYZT(cands->at(ii).p4().X(),cands->at(ii).p4().Y(),cands->at(ii).p4().Z(),cands->at(ii).p4().T());
      }
      for(unsigned int ii=0; ii< RecoCandAdditionalFloatVariablesTags_[i].size();ii++)
      {
	edm::Handle<std::vector<double> > FloatVar;
	iEvent.getByLabel(RecoCandAdditionalFloatVariablesTags_[i].at(ii),FloatVar);
	if( !FloatVar.isValid() )
	{
	  if(debug_)std::cout<<"Warning Float variable with lable: "<<RecoCandAdditionalFloatVariablesTags_[i].at(ii).label()<<" not found!!!"<<std::endl;
	  break;
	}
	for(unsigned int iii=0; iii<cands->size();iii++)
	{
	  RecoCandAdditionalFloatVariables_.at(i)[ii][iii] = FloatVar->at(iii);
	}
      }
      // loop over int variables
      for(unsigned int ii=0; ii< RecoCandAdditionalIntVariablesTags_[i].size();ii++)
      {
	edm::Handle<std::vector<int> > IntVar;
	iEvent.getByLabel(RecoCandAdditionalIntVariablesTags_[i].at(ii),IntVar);
	if( !IntVar.isValid() )
	{
	  if(debug_)std::cout<<"Warning Int variable with lable: "<<RecoCandAdditionalIntVariablesTags_[i].at(ii).label()<<" not found!!!"<<std::endl;
	  break;
	}
	for(unsigned int iii=0; iii<cands->size();iii++)
	{
	  RecoCandAdditionalIntVariables_.at(i)[ii][iii] = IntVar->at(iii);
	}
      }
      // loop over bool variables
      for(unsigned int ii=0; ii< RecoCandAdditionalBoolVariablesTags_[i].size();ii++)
      {
	edm::Handle<std::vector<bool> > boolVar;
	iEvent.getByLabel(RecoCandAdditionalBoolVariablesTags_[i].at(ii),boolVar);
	if( !boolVar.isValid() )
	{
	  if(debug_)std::cout<<"Warning bool variable with lable: "<<RecoCandAdditionalBoolVariablesTags_[i].at(ii).label()<<" not found!!!"<<std::endl;
	  break;
	}
	for(unsigned int iii=0; iii<cands->size();iii++)
	{
	  if( boolVar->at(iii) ) RecoCandAdditionalBoolVariables_.at(i)[ii][iii] = 1;
	  else RecoCandAdditionalBoolVariables_.at(i)[ii][iii] = 0;
	}
      }
    }
    else if(debug_)std::cout<<"Warning recoCand with tag: "<<varsRecoCandTags_.at(i).label()<<" not found!"<<std::endl;
    
  }
  if(debug_) std::cout<<"Point g"<<std::endl;
  for(unsigned int i = 0; i < VectorDoubleTags_.size(); ++i) {
    edm::Handle<std::vector<double> > var;
    iEvent.getByLabel(VectorDoubleTags_.at(i),var);
    if( var.isValid() ){
      for(unsigned int j=0; j< var->size(); j++){
	VectorDoubleVector_.at(i).push_back(var->at(j));
      }
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VectorDoubleTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point h"<<std::endl;
  for(unsigned int i = 0; i < VectorIntTags_.size(); ++i) {
    edm::Handle<std::vector<int> > var;
    iEvent.getByLabel(VectorIntTags_.at(i),var);
    if( var.isValid() ){
      for(unsigned int j=0; j< var->size(); j++){
	VectorIntVector_.at(i).push_back(var->at(j));
      }
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VectorIntTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point i"<<std::endl;
  for(unsigned int i = 0; i < VectorBoolTags_.size(); ++i) {
    edm::Handle<std::vector<bool> > var;
    iEvent.getByLabel(VectorBoolTags_.at(i),var);
    if( var.isValid() ){
      for(unsigned int j=0; j< var->size(); j++){
	if( var->at(j) ) VectorBoolVector_.at(i).push_back(1);
	else VectorBoolVector_.at(i).push_back(0);
      }
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VectorBoolTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point j"<<std::endl;
  for(unsigned int i = 0; i < VectorStringTags_.size(); ++i) {
    edm::Handle<std::vector<std::string> > var;
    iEvent.getByLabel(VectorStringTags_.at(i),var);
    if( var.isValid() ){
      for(unsigned int j=0; j< var->size(); j++){
	VectorStringVector_.at(i).push_back(var->at(j));
      }
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VectorStringTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"Point k"<<std::endl;
  for(unsigned int i = 0; i < VectorTLorentzVectorTags_.size(); ++i) {
    edm::Handle<std::vector<TLorentzVector> > var;
    iEvent.getByLabel(VectorTLorentzVectorTags_.at(i),var);
    if( var.isValid() ) {
      for(unsigned int j=0; j< var->size();j++){
	VectorTLorentzVector_.at(i).push_back(var->at(j));
      }
    }else{
      std::cout<<"WARNING ... "<<i<<"th variable : "<<VectorTLorentzVectorTags_[i].label()<<" is NOT valid?!"<<std::endl;
    }
  }
  if(debug_) std::cout<<"filling tree "<<std::endl;
  // std::cout<<"Filling tree with:"<<std::endl;
  // for(unsigned int i=0; i<RecoCandN_.size();i++)std::cout<<"RecoCand["<<i<<"] Numberofentries: "<<RecoCandN_.at(i)<<std::endl;
  tree_->Fill();
  if(debug_) std::cout<<"filling tree done "<<std::endl;
}

// ------------ method called once each job just before starting event loop  ------------
void 
TreeMaker::beginJob()
{
  edm::Service<TFileService> fs;
  if( !fs ) {
    throw edm::Exception(edm::errors::Configuration, "TFile Service is not registered in cfg file");
  }
  tree_ = fs->make<TTree>(treeName_,treeName_);  
  tree_->SetAutoSave(10000000000);
  tree_->SetAutoFlush(1000000);
  tree_->Branch("RunNum",&runNum_,"RunNum/i");
  tree_->Branch("LumiBlockNum",&lumiBlockNum_,"LumiBlockNum/i");
  tree_->Branch("EvtNum",&evtNum_,"EvtNum/i");
 
  // int variables
  VarsInt_ = std::vector<int>(VarsIntNames_.size(),1);
  for(unsigned int i=0; i < VarsIntNames_.size();i++)
  {
    std::string tempFull = VarsIntNames_[i];
    std::string nameInTree = VarsIntNames_[i];
    std::string tag = VarsIntNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VarsIntNames: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VarsIntTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    std::cout<<"VarsIntNames: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    tree_->Branch((TString)nameInTree,&(VarsInt_.at(i)),(TString)nameInTree+"/I");
  }
  // double variables
  VarsDouble_ = std::vector<Float_t>(VarsDoubleNames_.size(),1.);
  for(unsigned int i=0; i < VarsDoubleNames_.size();i++)
  {
    std::string tempFull = VarsDoubleNames_[i];
    std::string nameInTree = VarsDoubleNames_[i];
    std::string tag = VarsDoubleNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VarsDoubleNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VarsDoubleTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree,&(VarsDouble_.at(i)),(TString)nameInTree+"/F");
    
  }
  // bool variables
  VarsBool_ = std::vector<UChar_t>(VarsBoolNames_.size(),0);
  for(unsigned int i=0; i < VarsBoolNames_.size();i++)
  {
    std::string tempFull = VarsBoolNames_[i];
    std::string nameInTree = VarsBoolNames_[i];
    std::string tag = VarsBoolNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VarsBoolNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VarsBoolTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree,&(VarsBool_.at(i)),(TString)nameInTree+"/b");
    
  }
  //  TLorentzVector variables
  VarsTLorentzVector_ = std::vector<TLorentzVector>(VarsTLorentzVectorNames_.size(),TLorentzVector(0.,0.,0.,0.));
  for(unsigned int i=0; i < VarsTLorentzVectorNames_.size();i++)
  {
    std::string tempFull = VarsTLorentzVectorNames_[i];
    std::string nameInTree = VarsTLorentzVectorNames_[i];
    std::string tag = VarsTLorentzVectorNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VarsTLorentzVectorNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VarsTLorentzVectorTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree,(TString)nameInTree,&(VarsTLorentzVector_.at(i)));
    
  }
  //  TString variables
  VarsString_ = std::vector<std::string>(VarsStringNames_.size(), (std::string)"");
  for(unsigned int i=0; i < VarsStringNames_.size();i++)
  {
    std::string tempFull = VarsStringNames_[i];
    std::string nameInTree = VarsStringNames_[i];
    std::string tag = VarsStringNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VarsStringNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VarsStringTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree,(TString)nameInTree,&(VarsString_.at(i)));
    
  }
  // loop over input varsFloat string to extract optional names in tree
  RecoCandN_ = std::vector<UShort_t>(varsRecoCandNames_.size(),0);
  for(unsigned int i=0; i<varsRecoCandNames_.size();i++)
  {
    RecoCandPt_.push_back (new Float_t[10000]);
    RecoCandEta_.push_back(new Float_t[10000]);
    RecoCandPhi_.push_back(new Float_t[10000]);
    RecoCandE_.push_back  (new Float_t[10000]);
    RecoCandLorentzVector_.push_back(new TLorentzVector[10000]);
    
    std::string temp = varsRecoCandNames_[i];
    std::string nameInTree = "";
    std::string ttemp ="";
    
    
    std::cout<<"RecoCand Setup: item["<<i<<"] full string: "<<temp<<std::endl;
    if(temp.find('|')<temp.size() ) temp = temp.substr(0,temp.find("|") );
    if(temp.find('(')<temp.size() && temp.find(')')<temp.size() ) 
    {
      nameInTree = temp.substr(temp.find('(')+1, temp.find(')')-temp.find('(')-1);
      temp=temp.substr(0,temp.find('('));
    }
    else nameInTree = temp;
    std::cout<<"RecoCand Tag: "<<temp<<std::endl;
    varsRecoCandTags_.push_back(edm::InputTag(temp));
    std::cout<<"RecoCand stored name in tree: "<<nameInTree<<std::endl;
    temp=nameInTree;
    if(temp.find(':')<temp.size())
    {
      temp = SeparateString(temp,":").second;
    }
    temp = FinalizeName(temp);
    tree_->Branch((temp+"Num").c_str(),&(RecoCandN_.at(i)),(temp+"Num/s").c_str());
    tree_->Branch((temp+"Pt").c_str(), RecoCandPt_.at(i), (temp+"Pt["+temp+"Num]/F").c_str());
    tree_->Branch((temp+"Eta").c_str(),RecoCandEta_.at(i),(temp+"Eta["+temp+"Num]/F").c_str());
    tree_->Branch((temp+"Phi").c_str(),RecoCandPhi_.at(i),(temp+"Phi["+temp+"Num]/F").c_str());
    tree_->Branch((temp+"E").c_str(),  RecoCandE_.at(i),  (temp+"E["+temp+"Num]/F").c_str());
//     tree_->Branch((temp+"TLorentzVector").c_str(),  RecoCandLorentzVector_.at(i),  (temp+"TLorentzVector["+temp+"Num]/F").c_str());
    std::string mainNameInTree=temp;
    temp = varsRecoCandNames_[i];
    unsigned int countBool=0;
    unsigned int countInt=0;
    unsigned int countFloat=0;
    std::vector<UChar_t*> vecUChart;
    RecoCandAdditionalBoolVariables_.push_back(vecUChart);
    std::vector<Int_t*> vecInt;
    RecoCandAdditionalIntVariables_.push_back(vecInt);
    std::vector<Float_t*> vecFloat;
    RecoCandAdditionalFloatVariables_.push_back(vecFloat);
    std::vector<edm::InputTag> tagvec;
    RecoCandAdditionalBoolVariablesTags_.push_back(tagvec);
    RecoCandAdditionalIntVariablesTags_.push_back(tagvec);
    RecoCandAdditionalFloatVariablesTags_.push_back(tagvec);
    std::string temp2="";
    std::string tag="";
    int typ=-1;
    while (temp.find('|')<temp.size() ) // loop over the posible additonal variables
    {
      typ=-1;
      temp = temp.substr(temp.find("|")+1 );
      temp2="";
      if(temp.find('|')<temp.size() ) temp2 = temp.substr(0, temp.find('|') );
      else temp2=temp;
      // check for typ definition and for optional naming
      if(temp2.find('(')<temp2.size() && temp2.find(')')<temp2.size() )
      {
	//	std::cout<<"POINT1::temp2: "<<temp2<<std::endl;
	// check for optional naming
	if(temp2.find('_')<temp2.size())
	{
	  nameInTree = temp2.substr(temp2.find('_')+1, temp2.find(')')-temp2.find('_')-1);
	  tag = temp2.substr(0, temp2.find('('));
	  if(temp2.find("b_")<temp2.size() )typ = 0;
	  if(temp2.find("I_")<temp2.size() )typ = 1;
	  if(temp2.find("F_")<temp2.size() )typ = 2;
	}
	else 
	{
	  nameInTree = temp2.substr(0, temp2.find('('));
	  tag=temp2.substr(0, temp2.find('('));
	  if(temp2.find('b')<temp2.size() )typ = 0;
	  if(temp2.find('I')<temp2.size() )typ = 1;
	  if(temp2.find('F')<temp2.size() )typ = 2;
	  
	}
      }
      else if(typ==-1)std::cout<<"Warning no typ selected for additonal input object: "<<temp2<<" of main varialbe: "<<nameInTree<<"Please use: tag(x_Name) with x=b,I,F (bool, int float) and optional Name for naming in the tree"<<std::endl;
      // std::cout<<"| TagName: "<<temp2<<std::endl;
      if(nameInTree.find(':')<nameInTree.size())
      {
	nameInTree = SeparateString(nameInTree,":").second;
      }
      nameInTree = FinalizeName(nameInTree);
      std::cout<<"Sub Typ: Tag: "<<tag<<", typ: "<<typ<< ", nameIn Tree: "<<nameInTree<<std::endl;
      if(typ==0)
      {
	
	RecoCandAdditionalBoolVariablesTags_[i].push_back(edm::InputTag(tag ) );
	RecoCandAdditionalBoolVariables_[i].push_back(new UChar_t[10000]);
	tree_->Branch((mainNameInTree+"_"+nameInTree).c_str(), RecoCandAdditionalBoolVariables_.at(i).at(countBool), (mainNameInTree+"_"+nameInTree+"["+mainNameInTree+"Num]/b").c_str());
	// 				tree_->Branch((nameInTree).c_str(), RecoCandAdditionalBoolVariables_.at(i).at(countBool), (nameInTree+"["+mainNameInTree+"Num]/b").c_str());
	countBool++;
      }
      if(typ==1)
      {
	
	RecoCandAdditionalIntVariablesTags_[i].push_back(edm::InputTag(tag ) );
	RecoCandAdditionalIntVariables_[i].push_back(new Int_t[10000]);
	tree_->Branch((mainNameInTree+"_"+nameInTree).c_str(), RecoCandAdditionalIntVariables_.at(i).at(countInt), (mainNameInTree+"_"+nameInTree+"["+mainNameInTree+"Num]/I").c_str());
	// 				tree_->Branch((nameInTree).c_str(), RecoCandAdditionalIntVariables_.at(i).at(countInt), (nameInTree+"["+mainNameInTree+"Num]/I").c_str());
	countInt++;
      }
      if(typ==2)
      {
	
	RecoCandAdditionalFloatVariablesTags_[i].push_back(edm::InputTag(tag ) );
	RecoCandAdditionalFloatVariables_[i].push_back(new Float_t[10000]);
	tree_->Branch((mainNameInTree+"_"+nameInTree).c_str(), RecoCandAdditionalFloatVariables_.at(i).at(countFloat), (mainNameInTree+"_"+nameInTree+"["+mainNameInTree+"Num]/F").c_str());
	countFloat++;
      }
      if(typ>2)std::cout<<"Error typ is: "<<typ<<" which is not defined!!! check!"<<std::endl;
    }
    RecoCandAdditionalBoolVariablesN_.push_back(countBool);
    RecoCandAdditionalIntVariablesN_.push_back(countInt);
    RecoCandAdditionalFloatVariablesN_.push_back(countFloat);
  }
  // vectors
  for(unsigned int i=0; i< VectorIntNames_.size();i++)
  {
    std::vector<int> vector;
    VectorIntVector_.push_back(vector);
	}
	for(unsigned int i=0; i< VectorIntNames_.size();i++)
	{
    std::string tempFull = VectorIntNames_[i];
    std::string nameInTree = VectorIntNames_[i];
    std::string tag = VectorIntNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VectorIntNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VectorIntTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree, "std::vector<int>", &(VectorIntVector_.at(i)), 32000, 0);
  }
  for(unsigned int i=0; i< VectorDoubleNames_.size();i++)
  {
    std::vector<double> vector;
    VectorDoubleVector_.push_back(vector);
	}
	for(unsigned int i=0; i< VectorDoubleNames_.size();i++)
	{
    std::string tempFull = VectorDoubleNames_[i];
    std::string nameInTree = VectorDoubleNames_[i];
    std::string tag = VectorDoubleNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    
    VectorDoubleTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    std::cout<<"VectorDoubleNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    tree_->Branch((TString)nameInTree, "std::vector<double>", &(VectorDoubleVector_.at(i)), 32000, 0);
  }
  for(unsigned int i=0; i< VectorBoolNames_.size();i++)
  {
    std::vector<unsigned int> vector;
    VectorBoolVector_.push_back(vector);
	}
	for(unsigned int i=0; i< VectorBoolNames_.size();i++)
	{
    std::string tempFull = VectorBoolNames_[i];
    std::string nameInTree = VectorBoolNames_[i];
    std::string tag = VectorBoolNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VectorBoolNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VectorBoolTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree, "std::vector<unsigned int>", &(VectorBoolVector_.at(i)), 32000, 0);
  }
  for(unsigned int i=0; i< VectorStringNames_.size();i++)
  {
    std::vector<std::string> vector;
    VectorStringVector_.push_back(vector);
	}
	for(unsigned int i=0; i< VectorStringNames_.size();i++)
	{
    std::string tempFull = VectorStringNames_[i];
    std::string nameInTree = VectorStringNames_[i];
    std::string tag = VectorStringNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VectorStringNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VectorStringTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree, "std::vector<std::string>", &(VectorStringVector_.at(i)), 32000, 0);
  }
  for(unsigned int i=0; i< VectorTLorentzVectorNames_.size();i++)
  {
    std::vector<TLorentzVector> vector;
    VectorTLorentzVector_.push_back(vector);
	}
	for(unsigned int i=0; i< VectorTLorentzVectorNames_.size();i++)
		{
    std::string tempFull = VectorTLorentzVectorNames_[i];
    std::string nameInTree = VectorTLorentzVectorNames_[i];
    std::string tag = VectorTLorentzVectorNames_[i];
    if(tempFull.find("(") <tempFull.size() && tempFull.find(")") <tempFull.size())
    {
      tag = SeparateString(tempFull,"(").first;
      nameInTree = SeparateString(SeparateString(tempFull,"(").second,")").first;
    }
    std::cout<<"VectorTLorentzVectorNames_: tag:"<<tag<<" nameInTree: "<<nameInTree<<" originial full name: "<<tempFull<<std::endl;
    VectorTLorentzVectorTags_.push_back(edm::InputTag(tag));
    if(nameInTree.find(':')<nameInTree.size())
    {
      nameInTree = SeparateString(nameInTree,":").second;
    }
    nameInTree = FinalizeName(nameInTree);
    tree_->Branch((TString)nameInTree, "std::vector<TLorentzVector>", &(VectorTLorentzVector_.at(i)), 32000, 0);
  }
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TreeMaker::endJob() {
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
void 
TreeMaker::setBranchVariablesToDefault() 
{
  // event information
  if(debug_) std::cout<<"starting reset Variables"<<std::endl;
  runNum_=0;
  lumiBlockNum_=0;
  evtNum_=0;
  for(unsigned int i = 0; i < VarsDouble_.size(); ++i) {
    VarsDouble_.at(i) = 9999.;
  }
  for(unsigned int i = 0; i < VarsInt_.size(); ++i) {
    VarsInt_.at(i) = 9999;
  }
  for(unsigned int i = 0; i < VarsBool_.size(); ++i) {
    VarsBool_.at(i) = 0;
  }
  for(unsigned int i = 0; i < VarsString_.size(); ++i) {
    VarsString_.at(i) = "";
  }
  for(unsigned int i = 0; i < VarsTLorentzVector_.size(); ++i){
    VarsTLorentzVector_.at(i).SetXYZT(0, 0, 0, 0);
  }
  for(unsigned int i=0; i < VectorDoubleVector_.size();i++)
  {
    VectorDoubleVector_.at(i).clear();
  }
  for(unsigned int i=0; i < VectorIntVector_.size();i++)
  {
    VectorIntVector_.at(i).clear();
  }
  for(unsigned int i=0; i < VectorBoolVector_.size();i++)
  {
    VectorBoolVector_.at(i).clear();
  }
  for(unsigned int i=0; i < VectorStringVector_.size();i++)
  {
    VectorStringVector_.at(i).clear();
  }
  for(unsigned int i=0; i < VectorTLorentzVector_.size();i++)
  {
    VectorTLorentzVector_.at(i).clear();
  }
  
  for(unsigned int i = 0; i < varsRecoCandTags_.size(); ++i) 
  {
    RecoCandN_.at(i)=0;
    for(unsigned int ii=0; ii< nMaxCandidates_; ii++)
    {
      RecoCandPt_.at(i)[ii]=-999.;
      RecoCandEta_.at(i)[ii]=-999.;
      RecoCandPhi_.at(i)[ii]=-999.;
      RecoCandE_.at(i)[ii]=-999.;
      RecoCandLorentzVector_.at(i)[ii]=TLorentzVector (0.,0.,0.,0.);
    }
    // loop over the additonal variables
    for(unsigned int iii=0; iii< nMaxCandidates_; iii++)
    {
      for(unsigned int ii=0; ii < RecoCandAdditionalBoolVariablesTags_.at(i).size();ii++)
      {
	RecoCandAdditionalBoolVariables_.at(i)[ii][iii]=0;
      }
      for(unsigned int ii=0; ii < RecoCandAdditionalIntVariablesTags_.at(i).size();ii++)
      {
	RecoCandAdditionalIntVariables_.at(i)[ii][iii]=-9999;
      }
      for(unsigned int ii=0; ii < RecoCandAdditionalFloatVariablesTags_.at(i).size();ii++)
      {
	RecoCandAdditionalFloatVariables_.at(i)[ii][iii]=-9999.;
      }
    }
  }  
  if(debug_) std::cout<<"finished reset Variables"<<std::endl;
}
std::pair <std::string,std::string> TreeMaker::SeparateString(std::string InputStr, std::string Separater)
{
  std::string first="";
  std::string second="";
  unsigned int SeparatorStart=0;
  unsigned int SeparatorEnd=0;
  if(InputStr.find(Separater) >InputStr.size()) 
  {
    std::cout<<"SeparateString:: Separater: "<<Separater<<" in: "<<InputStr<<" not found."<<std::endl;
    return std::make_pair(InputStr,second);
  }
  else 
  {
    SeparatorStart=InputStr.find(Separater);
    SeparatorEnd=SeparatorStart + Separater.size()-1;
    first = InputStr.substr(0,SeparatorStart);
    second =InputStr.substr(SeparatorEnd+1);
  }
  //std::cout<<"SeparateString:: Inputstr: "<<InputStr<<" Separater: "<<Separater<<" first: "<<first<<" second: "<<second<<std::endl;
  return std::make_pair(first,second);
}
//define this as a plug-in
DEFINE_FWK_MODULE(TreeMaker);

TString TreeMaker::FinalizeName(std::string nameInTree)
{
  bool checkName=true;
  unsigned int iteration=0;
  TString TTemp_=nameInTree;
  while (checkName)
  {
    checkName=false;
    iteration++;
    for (unsigned int j=0; j<nameCache_.size() ;j++)
    {
      if(nameCache_[j]==TTemp_)
      {
	TTemp_=nameInTree;
	std::cout<<"Warning name in Tree already defined alternating name...TTemp: "<<TTemp_<<std::endl;
	int n_;
	char buffer_[300];
	n_ = sprintf(buffer_,"_%d",iteration);
	n_++;
	TTemp_+=buffer_;
	checkName=true;
      }
    }
  }
  nameCache_.push_back((std::string)TTemp_);
  return TTemp_;
}