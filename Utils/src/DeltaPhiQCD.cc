
// -*- C++ -*-
//
// Package:    QCD/DeltaPhiQCD
// Class:      DeltaPhiQCD
// 

//
// Original Author:  Amin Ghiasi
//       Created:  Sun, 6 Sep 2015 20:08 GMT
//

#include <memory>
#include <vector>
#include "FWCore/Utilities/interface/InputTag.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>
#include <utility>
#include "TLorentzVector.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/JetReco/interface/GenJet.h"


//
// class declaration
//

class DeltaPhiQCD : public edm::EDProducer {
public:
    explicit DeltaPhiQCD ( const edm::ParameterSet& ) ;
    ~DeltaPhiQCD();
    
    static void fillDescriptions ( edm::ConfigurationDescriptions& descriptions ) ;
    
private:
    virtual void beginJob () ;
    virtual void produce ( edm::Event&, const edm::EventSetup& ) ;
    virtual void endJob () ;
    
    virtual void beginRun( edm::Run&, edm::EventSetup const& ) ;
    virtual void endRun( edm::Run&, edm::EventSetup const& ) ;
    virtual void beginLuminosityBlock ( edm::LuminosityBlock&, edm::EventSetup const& ) ;
    virtual void endLuminosityBlock ( edm::LuminosityBlock&, edm::EventSetup const& ) ;
    std::vector<edm::InputTag> JetTagRecoJets_ ;
    std::vector<edm::InputTag> JetTagGenJets_ ;
    std::string   btagname_ ;      
    edm::InputTag GenParticleTag_ ;
    
    // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//
//

//
// constructors and destructor
//
DeltaPhiQCD::DeltaPhiQCD ( const edm::ParameterSet& iConfig )
{


    //register your product
    JetTagRecoJets_ = iConfig.getParameter < std::vector<edm::InputTag> > ( "JetTagRecoJets" ) ;
    btagname_       = iConfig.getParameter < std::string   > ( "BTagInputTag"   ) ;
    JetTagGenJets_  = iConfig.getParameter < std::vector<edm::InputTag> > ( "JetTagGenJets"  ) ;
    GenParticleTag_ = iConfig.getParameter < edm::InputTag > ( "GenParticleTag" ) ;


    produces < std::vector < TLorentzVector > > ( "NeutrinoLorentzVector" ) ;

    produces < std::vector < double > > ( "GenDeltaPhi"          ) ;
    produces < std::vector < double > > ( "RJetDeltaPhi"         ) ;
    produces < std::vector < double > > ( "RJetMinDeltaPhiEta24" ) ;
    produces < std::vector < double > > ( "RJetMinDeltaPhiEta5"  ) ;
    produces < std::vector < double > > ( "GenMinDeltaPhiEta24"  ) ;
    produces < std::vector < double > > ( "GenMinDeltaPhiEta5"   ) ;

    produces < std::vector < std::string > > ( "minDeltaPhiNames" ) ;

    produces < std::vector < int > > ( "NeutrinoPdg"               ) ;
    produces < std::vector < int > > ( "NeutrinoMotherPdg"         ) ;
    produces < std::vector < int > > ( "RJetMinDeltaPhiIndexEta24" ) ;
    produces < std::vector < int > > ( "RJetMinDeltaPhiIndexEta5"  ) ;
    produces < std::vector < int > > ( "GenMinDeltaPhiIndexEta24"  ) ;
    produces < std::vector < int > > ( "GenMinDeltaPhiIndexEta5"   ) ;

}


DeltaPhiQCD::~DeltaPhiQCD()
{
    
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void DeltaPhiQCD::produce ( edm::Event& iEvent, const edm::EventSetup& iSetup )
{
    
    using namespace edm;
    using namespace std;
    typedef math::XYZTLorentzVector LorentzVector;
    
    std::vector < double >  deltaphi_vector ;
    std::vector < double >  RJetminDeltaphi5, RJetminDeltaphi24 ;
    
    std::vector < int >  RJetminDeltaphiIndex24,  RJetminDeltaphiIndex5;
    
    std::vector < std::string > minDeltaphiNames ;
    
    edm::Handle < double > var ;
    
    
    std::vector<std::vector<double> > savephi(2,std::vector<double>(8,-9));
    std::vector<std::vector<double> > saveeta(2,std::vector<double>(8,-9));
    double recojetseta = -99. , recojetsphi = -99. , deltaphi = -99. ;
    double mindeltaphi3 = -9, mindeltaphi4 = -9, mindeltaphi5 = -9 ;
    double mindeltaphistar = -9, deltaphistar = -9 ;
    double mhtphi ;
    
    int mindeltaphi3jetindex = -9, mindeltaphi4jetindex = -9, mindeltaphi5jetindex = -9, mindeltaphistarindex = -9 ;
    
    edm::InputTag MHT_Phi ( "MHT" , "Phi" ) ;
    iEvent.getByLabel ( MHT_Phi , var ) ;
    if ( var.isValid() ) mhtphi = *var ;
    else { std::cout << "Warning: Can not retrieve MHTPhi" << std::endl ; mhtphi = -9 ; }

    for ( unsigned int ii = 0; ii < 2; ii++ )
    {
        edm::Handle < edm::View < reco::Jet > > src ;
        iEvent.getByLabel ( JetTagRecoJets_[ii] , src ) ;
        
        if ( src.isValid() )
        {
            
            mindeltaphi3 = -9; mindeltaphi4 = -9; mindeltaphi5 = -9; mindeltaphi3jetindex = -9; mindeltaphi4jetindex = -9; mindeltaphi5jetindex = -9;
            for ( unsigned int index = 0; index < std::min((unsigned)8,(unsigned)src->size()); ++index )
            {

                recojetsphi = src -> at(index).phi() ;
                recojetseta = src -> at(index).eta() ;
                deltaphi = std::abs( reco::deltaPhi( src -> at(index).phi() , mhtphi ) ) ;

                if (std::abs( mindeltaphi3 ) > std::abs( deltaphi ) && index < 3 ) { mindeltaphi3 = deltaphi; mindeltaphi3jetindex = index+1; }
                if (std::abs( mindeltaphi4 ) > std::abs( deltaphi ) && index < 4 ) { mindeltaphi4 = deltaphi; mindeltaphi4jetindex = index+1; }
                if (std::abs( mindeltaphi5 ) > std::abs( deltaphi ) && index < 5 ) { mindeltaphi5 = deltaphi; mindeltaphi5jetindex = index+1; }

                if ( ii == 0 ) deltaphi_vector.push_back ( deltaphi ) ;

                savephi [ii][index] = recojetsphi ; 
                saveeta [ii][index] = recojetseta ;

            }//index


            if ( ii == 0 )
            {

                std::auto_ptr < std::vector < double > > deltaphi_vector2  ( new std::vector < double > ( deltaphi_vector ) ) ;
                iEvent.put ( deltaphi_vector2 , "RJetDeltaPhi" ) ;

            }

            mindeltaphistar = -9; mindeltaphistarindex = -9;
            LorentzVector mhtLorentzstar ( 0,0,0,0 ) ;
            for ( unsigned int j = 0; j < src -> size(); j++ )
            {
                mhtLorentzstar -= src->at(j).p4();
            }//j
            for ( unsigned int i = 0; i < src -> size(); i++ )
            {
                LorentzVector mhtLorentzstar2 = mhtLorentzstar + src->at(i).p4();
                deltaphistar = std::abs( reco::deltaPhi( src->at(i).phi(), mhtLorentzstar2.phi() ) );

                if ( std::abs ( mindeltaphistar ) > std::abs ( deltaphistar ) ) { mindeltaphistar = deltaphistar; mindeltaphistarindex = i; }

            } //i

        }//if vsrc.isValid
        else 
            std::cout << "Warning Reco Tag not valid: " << JetTagRecoJets_[ii].label() << std::endl ;

        if ( ii == 0 ) 
        { 
            
            RJetminDeltaphi5 = { mindeltaphi3, mindeltaphi4, mindeltaphi5, mindeltaphistar } ;        
            RJetminDeltaphiIndex5 = { mindeltaphi3jetindex, mindeltaphi4jetindex, mindeltaphi5jetindex, mindeltaphistarindex } ;
            
        }


        else if ( ii == 1 ) 
        {
            
            RJetminDeltaphi24 = { mindeltaphi3, mindeltaphi4, mindeltaphi5, mindeltaphistar } ;
            RJetminDeltaphiIndex24 = { mindeltaphi3jetindex, mindeltaphi4jetindex, mindeltaphi5jetindex, mindeltaphistarindex } ;
            
        }


    }//ii


    minDeltaphiNames = {"Njle3", "Njle4", "Njle5", "minDeltaPhiStar" } ;


    std::auto_ptr < std::vector < double > > RJetminDeltaphi24_2      ( new std::vector < double > ( RJetminDeltaphi24      ) ) ;
    iEvent.put ( RJetminDeltaphi24_2      , "RJetMinDeltaPhiEta24"      ) ;

    std::auto_ptr < std::vector < double > > RJetminDeltaphi5_2       ( new std::vector < double > ( RJetminDeltaphi5       ) ) ;
    iEvent.put ( RJetminDeltaphi5_2       , "RJetMinDeltaPhiEta5"       ) ;

    std::auto_ptr < std::vector < int    > > RJetminDeltaphiIndex24_2 ( new std::vector < int    > ( RJetminDeltaphiIndex24 ) ) ;
    iEvent.put ( RJetminDeltaphiIndex24_2 , "RJetMinDeltaPhiIndexEta24" ) ;

    std::auto_ptr < std::vector < int    > > RJetminDeltaphiIndex5_2  ( new std::vector < int    > ( RJetminDeltaphiIndex5  ) ) ;
    iEvent.put ( RJetminDeltaphiIndex5_2  , "RJetMinDeltaPhiIndexEta5"  ) ;

    std::auto_ptr < std::vector < std::string > > minDeltaphiNames_2  ( new std::vector < std::string > ( minDeltaphiNames  ) ) ;
    iEvent.put ( minDeltaphiNames_2       , "minDeltaPhiNames"          ) ;











    std::vector < TLorentzVector > GenJetVector ;

    std::vector < double >  Gendeltaphi_vector ;
    std::vector < double >  GenminDeltaphi5, GenminDeltaphi24 ;

    std::vector < int >  GenminDeltaphiIndex5, GenminDeltaphiIndex24 ;

    double genmindeltaphi3 = -9, genmindeltaphi4 = -9, genmindeltaphi5 = -9 ;
    double genmindeltaphistar = -9, gendeltaphistar = -9, gendeltaphi = -9 ;
    double mindeltar ;

    std::string genname ;
    int mindeltarindex ;
    int genmindeltaphi3jetindex = -9, genmindeltaphi4jetindex = -9, genmindeltaphi5jetindex = -9, genmindeltaphistarindex = -9 ;

    for ( unsigned int ii = 0; ii < 2; ii++ )
    {

        edm::Handle < edm::View < reco::GenJet > > gensrc ;
        iEvent.getByLabel( JetTagGenJets_[ii],gensrc ) ;

        if ( gensrc.isValid() )
        {
            std::vector<unsigned int>  matchfound(gensrc->size(),0);
            genmindeltaphi3 = -9; genmindeltaphi4 = -9; genmindeltaphi5 = -9 ; 
            genmindeltaphi3jetindex = -9; genmindeltaphi4jetindex = -9; genmindeltaphi5jetindex = -9;

            int onoff = 0 ;
            for ( unsigned int j = 0; j < 8; j++ )
            {
                onoff = 0 ;
                mindeltar = 100; mindeltarindex = -9;
                for ( unsigned int i = 0; i < gensrc -> size(); ++i )
                {
                    if ( deltaR ( gensrc -> at(i).eta() , gensrc -> at(i).phi() , saveeta[ii][j], savephi[ii][j] ) < mindeltar && matchfound [i] == 0 && onoff == 0 && saveeta[ii][j] != -9 && savephi[ii][j] != -9 )
                    {
                        mindeltar = deltaR( gensrc -> at(i).eta(), gensrc -> at(i).phi(), saveeta[ii][j], savephi[ii][j] ) ;
                        mindeltarindex = i ;
                    //  if ( mindeltar < .25 ) onoff = 1;

                    }//if deltaR
                }//i

                if ( mindeltarindex >= 0 && mindeltarindex < (int) gensrc -> size() )
                {

                    matchfound [ mindeltarindex ] = 1 ;
                    gendeltaphi = std::abs( reco::deltaPhi ( gensrc -> at ( mindeltarindex ).phi(), mhtphi ) ) ;

                    if ( std::abs(genmindeltaphi3) > std::abs(gendeltaphi) && j < 3 ) { genmindeltaphi3 = gendeltaphi; genmindeltaphi3jetindex = j + 1; }
                    if ( std::abs(genmindeltaphi4) > std::abs(gendeltaphi) && j < 4 ) { genmindeltaphi4 = gendeltaphi; genmindeltaphi4jetindex = j + 1; }
                    if ( std::abs(genmindeltaphi5) > std::abs(gendeltaphi) && j < 5 ) { genmindeltaphi5 = gendeltaphi; genmindeltaphi5jetindex = j + 1; }

                } // if mindeltarindex
            } //j

            genmindeltaphistar = -9; genmindeltaphistarindex = -9;
            LorentzVector genmhtLorentzstar( 0,0,0,0 ) ;
            for ( unsigned int l = 0 ; l < gensrc -> size() ; l++ )
            {
                genmhtLorentzstar -= gensrc->at(l).p4() ;
            }//l
            for( unsigned int k = 0; k < gensrc -> size(); k++ )
            {
                LorentzVector genmhtLorentzstar2 = genmhtLorentzstar + gensrc->at(k).p4();
                gendeltaphistar = std::abs( reco::deltaPhi( gensrc -> at(k).phi(), genmhtLorentzstar2.phi() ) ) ;
                if ( std::abs( genmindeltaphistar ) > std::abs( gendeltaphistar ) ) { genmindeltaphistar = gendeltaphistar; genmindeltaphistarindex = k; }
            }//k
        }//if gensrc.isValid
		else 
			std::cout << "Warning Gen Tag not valid: " << JetTagGenJets_[ii].label() << std::endl ;

        if ( ii == 0 )
        {

            std::auto_ptr < std::vector < double > > Gendeltaphi_vector2      ( new std::vector < double > ( Gendeltaphi_vector ) ) ;
            iEvent.put ( Gendeltaphi_vector2 , "GenDeltaPhi" ) ;

        }


        if ( ii == 0 )
        {

            GenminDeltaphi5 = { genmindeltaphi3, genmindeltaphi4, genmindeltaphi5, genmindeltaphistar } ;        
            GenminDeltaphiIndex5 = { genmindeltaphi3jetindex, genmindeltaphi4jetindex, genmindeltaphi5jetindex, genmindeltaphistarindex } ;

        }


        else if ( ii == 1 )
        {
            
            GenminDeltaphi24 = { genmindeltaphi3, genmindeltaphi4, genmindeltaphi5, genmindeltaphistar } ;        
            GenminDeltaphiIndex24 = { genmindeltaphi3jetindex, genmindeltaphi4jetindex, genmindeltaphi5jetindex, genmindeltaphistarindex } ;

        }

    }//ii

    std::auto_ptr < std::vector < double > > GenminDeltaphi24_2      ( new std::vector < double > ( GenminDeltaphi24      ) ) ;
    iEvent.put ( GenminDeltaphi24_2      , "GenMinDeltaPhiEta24"      ) ;

    std::auto_ptr < std::vector < double > > GenminDeltaphi5_2       ( new std::vector < double > ( GenminDeltaphi5       ) ) ;
    iEvent.put ( GenminDeltaphi5_2       , "GenMinDeltaPhiEta5"       ) ;

    std::auto_ptr < std::vector < int    > > GenminDeltaphiIndex24_2 ( new std::vector < int    > ( GenminDeltaphiIndex24 ) ) ;
    iEvent.put ( GenminDeltaphiIndex24_2 , "GenMinDeltaPhiIndexEta24" ) ;

    std::auto_ptr < std::vector < int    > > GenminDeltaphiIndex5_2  ( new std::vector < int    > ( GenminDeltaphiIndex5  ) ) ;
    iEvent.put ( GenminDeltaphiIndex5_2  , "GenMinDeltaPhiIndexEta5"  ) ;






























    std::vector < TLorentzVector > neutrino_LVector;
    std::vector < int > neutrino_pdgid_vector, neutrino_mother_pdgid_vector ;

    edm::Handle < edm::View < reco::GenParticle > > genpart ;
    iEvent.getByLabel ( GenParticleTag_, genpart ) ;

    vector<double> neutrino_pt(6,-9);
    vector<double> neutrino_eta(6,-9);
    vector<double> neutrino_phi(6,-9);
    vector<double> neutrino_energy(6,-9);

    vector<int> neutrino_pdgid(6,0);
    vector<int> neutrino_mother_pdgid(6,0);

    if ( genpart.isValid () )
    {
        //sort gen neutrinos by pT
        std::multimap<double,size_t> genMap;
        for( size_t i = 0; i < genpart -> size(); i++ )
        {
            if( abs( genpart -> at(i).pdgId () ) == 12 || abs( genpart -> at(i).pdgId () ) == 14 || abs( genpart -> at(i).pdgId () ) == 16 )
            {
                genMap.insert(std::make_pair(genpart->at(i).pt(),i));
            }//if abs
        }//i
        
        unsigned i = 0;
        for ( auto genIt = genMap.rbegin(); genIt != genMap.rend() && i<5; ++genIt, ++i )
        {
            TLorentzVector dumb_vector ;
            dumb_vector.SetPtEtaPhiE(genpart -> at(genIt->second).pt(),
                                     genpart -> at(genIt->second).eta(),
                                     genpart -> at(genIt->second).phi(),
                                     genpart -> at(genIt->second).energy()
                                    );

            neutrino_LVector            .push_back ( dumb_vector                                  ) ;
            neutrino_pdgid_vector       .push_back ( genpart -> at(genIt->second).pdgId()         ) ;
            neutrino_mother_pdgid_vector.push_back ( genpart -> at(genIt->second).mother()->pdgId() ) ;            
        }//genIt
        
    } //if
    else std::cout << "Warning Neutrino Tag not valid: " << GenParticleTag_.label() << std::endl ;


    std::auto_ptr < std::vector < TLorentzVector > > neutrino_LVector2              ( new std::vector < TLorentzVector > ( neutrino_LVector             ) ) ;
    std::auto_ptr < std::vector < int            > > neutrino_pdgid_vector2         ( new std::vector < int            > ( neutrino_pdgid_vector        ) ) ;
    std::auto_ptr < std::vector < int            > > neutrino_mother_pdgid_vector2  ( new std::vector < int            > ( neutrino_mother_pdgid_vector ) ) ;


    iEvent.put ( neutrino_LVector2            , "NeutrinoLorentzVector" ) ;
    iEvent.put ( neutrino_pdgid_vector2       , "NeutrinoPdg"           ) ;
    iEvent.put ( neutrino_mother_pdgid_vector2, "NeutrinoMotherPdg"     ) ;



}//void DeltaPhiQCD



// ------------ method called once each job just before starting event loop  ------------
void 
DeltaPhiQCD::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DeltaPhiQCD::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
DeltaPhiQCD::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DeltaPhiQCD::endRun(edm::Run&, edm::EventSetup const&)

{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DeltaPhiQCD::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DeltaPhiQCD::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DeltaPhiQCD::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
      //The following says we do not know what parameters are allowed so do no validation
      // Please change this to state exactly what you do use, even if it is no parameters
      edm::ParameterSetDescription desc;
      desc.setUnknown();
      descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DeltaPhiQCD);
