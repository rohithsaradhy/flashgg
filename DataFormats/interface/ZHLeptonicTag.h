#ifndef FLASHgg_ZHLeptonicTag_h
#define FLASHgg_ZHLeptonicTag_h

#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "flashgg/DataFormats/interface/Met.h"
#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/DataFormats/interface/Muon.h"

namespace flashgg {

    class ZHLeptonicTag: public DiPhotonTagBase
    {
    public:
        ZHLeptonicTag();
        ZHLeptonicTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult> );
        ZHLeptonicTag( edm::Ptr<DiPhotonCandidate>, DiPhotonMVAResult );
        ~ZHLeptonicTag();

        ZHLeptonicTag *clone() const override { return ( new ZHLeptonicTag( *this ) ); }
        
        const std::vector<edm::Ptr<Muon> > muons() const { return Muons_;}
        const std::vector<edm::Ptr<flashgg::Electron> > electrons() const {return Electrons_;}
        const std::vector<edm::Ptr<Jet> > jets() const { return Jets_;}
        const edm::Ptr<flashgg::Met>  met() const { return MET_;}

        const bool associatedZ() const { return associatedZ_; }
        const bool associatedW() const { return associatedW_; }
        const bool VhasNeutrinos() const { return VhasNeutrinos_; }
        const bool VhasLeptons() const { return VhasLeptons_; }
        const bool VhasHadrons() const { return VhasHadrons_; }
        const float Vpt() const { return Vpt_; }



        const float VHmva() const { return VH_mva;};
        void set_VHmva(const float &val) {VH_mva=val;};


        const float ZHiggs0MToGG_mva()          const {return ZHiggs0MToGG_MVA;};
        const float ZHiggs0PHToGG_mva()         const {return ZHiggs0PHToGG_MVA;};
        const float ZHiggs0PHf05ph0ToGG_mva()   const {return ZHiggs0PHf05ph0ToGG_MVA;};
        const float ZHiggs0L1f05ph0ToGG_mva()   const {return ZHiggs0L1f05ph0ToGG_MVA;};
        const float ZHiggs0L1ZgToGG_mva()       const {return ZHiggs0L1ZgToGG_MVA;};
        const float ZHiggs0L1Zgf05ph0ToGG_mva() const {return ZHiggs0L1Zgf05ph0ToGG_MVA;};

        const float Anom_MVA_pho1_eta()         const {return _Anom_MVA_pho1_eta;};
        const float Anom_MVA_pho1_phi()         const {return _Anom_MVA_pho1_phi;};
        const float Anom_MVA_pho1_idmva()       const {return _Anom_MVA_pho1_idmva;};
        const float Anom_MVA_pho1_full5x5_r9()  const {return _Anom_MVA_pho1_full5x5_r9;};
        const float Anom_MVA_pho1_ptOverMgg()   const {return _Anom_MVA_pho1_ptOverMgg;};
        const float Anom_MVA_pho2_eta()         const {return _Anom_MVA_pho2_eta;};
        const float Anom_MVA_pho2_phi()         const {return _Anom_MVA_pho2_phi;};
        const float Anom_MVA_pho2_idmva()       const {return _Anom_MVA_pho2_idmva;};
        const float Anom_MVA_pho2_full5x5_r9()  const {return _Anom_MVA_pho2_full5x5_r9;};
        const float Anom_MVA_pho2_ptOverMgg()   const {return _Anom_MVA_pho2_ptOverMgg;};
        const float Anom_MVA_mu1_pt()           const {return _Anom_MVA_mu1_pt;};
        const float Anom_MVA_mu1_eta()          const {return _Anom_MVA_mu1_eta;};
        const float Anom_MVA_mu1_phi()          const {return _Anom_MVA_mu1_phi;};
        const float Anom_MVA_mu1_energy()       const {return _Anom_MVA_mu1_energy;};
        const float Anom_MVA_mu2_pt()           const {return _Anom_MVA_mu2_pt;};
        const float Anom_MVA_mu2_eta()          const {return _Anom_MVA_mu2_eta;};
        const float Anom_MVA_mu2_phi()          const {return _Anom_MVA_mu2_phi;};
        const float Anom_MVA_mu2_energy()       const {return _Anom_MVA_mu2_energy;};
        const float Anom_MVA_ele1_pt()          const {return _Anom_MVA_ele1_pt;};
        const float Anom_MVA_ele1_eta()         const {return _Anom_MVA_ele1_eta;};
        const float Anom_MVA_ele1_phi()         const {return _Anom_MVA_ele1_phi;};
        const float Anom_MVA_ele1_energy()      const {return _Anom_MVA_ele1_energy;};
        const float Anom_MVA_ele2_pt()          const {return _Anom_MVA_ele2_pt;};
        const float Anom_MVA_ele2_eta()         const {return _Anom_MVA_ele2_eta;};
        const float Anom_MVA_ele2_phi()         const {return _Anom_MVA_ele2_phi;};
        const float Anom_MVA_ele2_energy()      const {return _Anom_MVA_ele2_energy;};
        const float Anom_MVA_jet1_pt()          const {return _Anom_MVA_jet1_pt;};
        const float Anom_MVA_jet1_phi()         const {return _Anom_MVA_jet1_phi;};
        const float Anom_MVA_jet1_eta()         const {return _Anom_MVA_jet1_eta;};
        const float Anom_MVA_jet1_energy()      const {return _Anom_MVA_jet1_energy;};
        const float Anom_MVA_jet2_pt()          const {return _Anom_MVA_jet2_pt;};
        const float Anom_MVA_jet2_phi()         const {return _Anom_MVA_jet2_phi;};
        const float Anom_MVA_jet2_eta()         const {return _Anom_MVA_jet2_eta;};
        const float Anom_MVA_jet2_energy()      const {return _Anom_MVA_jet2_energy;};
        const float Anom_MVA_cosPhiGG()         const {return _Anom_MVA_cosPhiGG;};
        const float Anom_MVA_cosPhiG1_Mu1()     const {return _Anom_MVA_cosPhiG1_Mu1;};
        const float Anom_MVA_cosPhiG1_Ele1()    const {return _Anom_MVA_cosPhiG1_Ele1;};
        const float Anom_MVA_cosPhiG2_Mu1()     const {return _Anom_MVA_cosPhiG2_Mu1;};
        const float Anom_MVA_cosPhiG2_Ele1()    const {return _Anom_MVA_cosPhiG2_Ele1;};
        const float Anom_MVA_dR_Pho1Ele1_wh()   const {return _Anom_MVA_dR_Pho1Ele1_wh;};
        const float Anom_MVA_dR_Pho2Ele1_wh()   const {return _Anom_MVA_dR_Pho2Ele1_wh;};
        const float Anom_MVA_dR_Pho1Mu1_wh()    const {return _Anom_MVA_dR_Pho1Mu1_wh;};
        const float Anom_MVA_dR_Pho2Mu1_wh()    const {return _Anom_MVA_dR_Pho2Mu1_wh;};
        const float Anom_MVA_dR_Pho1Jet1_wh()   const {return _Anom_MVA_dR_Pho1Jet1_wh;};
        const float Anom_MVA_dR_Pho1Jet2_wh()   const {return _Anom_MVA_dR_Pho1Jet2_wh;};
        const float Anom_MVA_dR_Pho2Jet1_wh()   const {return _Anom_MVA_dR_Pho2Jet1_wh;};
        const float Anom_MVA_dR_Pho2Jet2_wh()   const {return _Anom_MVA_dR_Pho2Jet2_wh;};
        const float Anom_MVA_dR_Mu1Jet1_wh()    const {return _Anom_MVA_dR_Mu1Jet1_wh;};
        const float Anom_MVA_dR_Mu1Jet2_wh()    const {return _Anom_MVA_dR_Mu1Jet2_wh;};
        const float Anom_MVA_dR_Ele1Jet1_wh()   const {return _Anom_MVA_dR_Ele1Jet1_wh;};
        const float Anom_MVA_dR_Ele1Jet2_wh()   const {return _Anom_MVA_dR_Ele1Jet2_wh;};

        void set_ZHiggs0MToGG_MVA(const float &val)           { ZHiggs0MToGG_MVA = val;};
        void set_ZHiggs0PHToGG_MVA(const float &val)          { ZHiggs0PHToGG_MVA = val;};
        void set_ZHiggs0PHf05ph0ToGG_MVA(const float &val)    { ZHiggs0PHf05ph0ToGG_MVA = val;};
        void set_ZHiggs0L1f05ph0ToGG_MVA(const float &val)    { ZHiggs0L1f05ph0ToGG_MVA = val;};
        void set_ZHiggs0L1ZgToGG_MVA(const float &val)        { ZHiggs0L1ZgToGG_MVA = val;};
        void set_ZHiggs0L1Zgf05ph0ToGG_MVA(const float &val)  { ZHiggs0L1Zgf05ph0ToGG_MVA = val;};


        void set_Anom_MVA_pho1_eta(const float &val)          {_Anom_MVA_pho1_eta = val;};
        void set_Anom_MVA_pho1_phi(const float &val)          {_Anom_MVA_pho1_phi = val;};
        void set_Anom_MVA_pho1_idmva(const float &val)        {_Anom_MVA_pho1_idmva = val;};
        void set_Anom_MVA_pho1_full5x5_r9(const float &val)   {_Anom_MVA_pho1_full5x5_r9 = val;};
        void set_Anom_MVA_pho1_ptOverMgg(const float &val)    {_Anom_MVA_pho1_ptOverMgg = val;};
        void set_Anom_MVA_pho2_eta(const float &val)          {_Anom_MVA_pho2_eta = val;};
        void set_Anom_MVA_pho2_phi(const float &val)          {_Anom_MVA_pho2_phi = val;};
        void set_Anom_MVA_pho2_idmva(const float &val)        {_Anom_MVA_pho2_idmva = val;};
        void set_Anom_MVA_pho2_full5x5_r9(const float &val)   {_Anom_MVA_pho2_full5x5_r9 = val;};
        void set_Anom_MVA_pho2_ptOverMgg(const float &val)    {_Anom_MVA_pho2_ptOverMgg = val;};
        void set_Anom_MVA_mu1_pt(const float &val)            {_Anom_MVA_mu1_pt = val;};
        void set_Anom_MVA_mu1_eta(const float &val)           {_Anom_MVA_mu1_eta = val;};
        void set_Anom_MVA_mu1_phi(const float &val)           {_Anom_MVA_mu1_phi = val;};
        void set_Anom_MVA_mu1_energy(const float &val)        {_Anom_MVA_mu1_energy = val;};
        void set_Anom_MVA_mu2_pt(const float &val)            {_Anom_MVA_mu2_pt = val;};
        void set_Anom_MVA_mu2_eta(const float &val)           {_Anom_MVA_mu2_eta = val;};
        void set_Anom_MVA_mu2_phi(const float &val)           {_Anom_MVA_mu2_phi = val;};
        void set_Anom_MVA_mu2_energy(const float &val)        {_Anom_MVA_mu2_energy = val;};
        void set_Anom_MVA_ele1_pt(const float &val)           {_Anom_MVA_ele1_pt = val;};
        void set_Anom_MVA_ele1_eta(const float &val)          {_Anom_MVA_ele1_eta = val;};
        void set_Anom_MVA_ele1_phi(const float &val)          {_Anom_MVA_ele1_phi = val;};
        void set_Anom_MVA_ele1_energy(const float &val)       {_Anom_MVA_ele1_energy = val;};
        void set_Anom_MVA_ele2_pt(const float &val)           {_Anom_MVA_ele2_pt = val;};
        void set_Anom_MVA_ele2_eta(const float &val)          {_Anom_MVA_ele2_eta = val;};
        void set_Anom_MVA_ele2_phi(const float &val)          {_Anom_MVA_ele2_phi = val;};
        void set_Anom_MVA_ele2_energy(const float &val)       {_Anom_MVA_ele2_energy = val;};
        void set_Anom_MVA_jet1_pt(const float &val)           {_Anom_MVA_jet1_pt = val;};
        void set_Anom_MVA_jet1_phi(const float &val)          {_Anom_MVA_jet1_phi = val;};
        void set_Anom_MVA_jet1_eta(const float &val)          {_Anom_MVA_jet1_eta = val;};
        void set_Anom_MVA_jet1_energy(const float &val)       {_Anom_MVA_jet1_energy = val;};
        void set_Anom_MVA_jet2_pt(const float &val)           {_Anom_MVA_jet2_pt = val;};
        void set_Anom_MVA_jet2_phi(const float &val)          {_Anom_MVA_jet2_phi = val;};
        void set_Anom_MVA_jet2_eta(const float &val)          {_Anom_MVA_jet2_eta = val;};
        void set_Anom_MVA_jet2_energy(const float &val)       {_Anom_MVA_jet2_energy = val;};
        void set_Anom_MVA_cosPhiGG(const float &val)          {_Anom_MVA_cosPhiGG = val;};
        void set_Anom_MVA_cosPhiG1_Mu1(const float &val)      {_Anom_MVA_cosPhiG1_Mu1 = val;};
        void set_Anom_MVA_cosPhiG1_Ele1(const float &val)     {_Anom_MVA_cosPhiG1_Ele1 = val;};
        void set_Anom_MVA_cosPhiG2_Mu1(const float &val)      {_Anom_MVA_cosPhiG2_Mu1 = val;};
        void set_Anom_MVA_cosPhiG2_Ele1(const float &val)     {_Anom_MVA_cosPhiG2_Ele1 = val;};
        void set_Anom_MVA_dR_Pho1Ele1_wh(const float &val)    {_Anom_MVA_dR_Pho1Ele1_wh = val;};
        void set_Anom_MVA_dR_Pho2Ele1_wh(const float &val)    {_Anom_MVA_dR_Pho2Ele1_wh = val;};
        void set_Anom_MVA_dR_Pho1Mu1_wh(const float &val)     {_Anom_MVA_dR_Pho1Mu1_wh = val;};
        void set_Anom_MVA_dR_Pho2Mu1_wh(const float &val)     {_Anom_MVA_dR_Pho2Mu1_wh = val;};
        void set_Anom_MVA_dR_Pho1Jet1_wh(const float &val)    {_Anom_MVA_dR_Pho1Jet1_wh = val;};
        void set_Anom_MVA_dR_Pho1Jet2_wh(const float &val)    {_Anom_MVA_dR_Pho1Jet2_wh = val;};
        void set_Anom_MVA_dR_Pho2Jet1_wh(const float &val)    {_Anom_MVA_dR_Pho2Jet1_wh = val;};
        void set_Anom_MVA_dR_Pho2Jet2_wh(const float &val)    {_Anom_MVA_dR_Pho2Jet2_wh = val;};
        void set_Anom_MVA_dR_Mu1Jet1_wh(const float &val)     {_Anom_MVA_dR_Mu1Jet1_wh = val;};
        void set_Anom_MVA_dR_Mu1Jet2_wh(const float &val)     {_Anom_MVA_dR_Mu1Jet2_wh = val;};
        void set_Anom_MVA_dR_Ele1Jet1_wh(const float &val)    {_Anom_MVA_dR_Ele1Jet1_wh = val;};
        void set_Anom_MVA_dR_Ele1Jet2_wh(const float &val)    {_Anom_MVA_dR_Ele1Jet2_wh = val;};


        void setJets( std::vector<edm::Ptr<Jet> > Jets ) { Jets_ = Jets; }
        void setMuons( std::vector<edm::Ptr<Muon> > Muons ) {Muons_ = Muons;}
        void setMET( edm::Ptr<flashgg::Met> MET ) {MET_ = MET;}
        void setElectrons( std::vector<edm::Ptr<Electron> > Electrons ) {Electrons_ = Electrons;}

        void setAssociatedZ( const bool &val ) { associatedZ_ = val; }
        void setAssociatedW( const bool &val ) { associatedW_ = val; }
        void setVhasNeutrinos( const bool &val ) { VhasNeutrinos_ = val; }
        void setVhasLeptons( const bool &val ) { VhasLeptons_ = val; }
        void setVhasHadrons( const bool &val ) { VhasHadrons_ = val; }
        void setVpt( const float &val ) { Vpt_ = val; }

        DiPhotonTagBase::tag_t tagEnum() const override {return DiPhotonTagBase::kZHLeptonic; }

    private:
        std::vector<edm::Ptr<Muon> > Muons_;
        std::vector<edm::Ptr<Electron> > Electrons_;
        std::vector<edm::Ptr<Jet> > Jets_;
        edm::Ptr<flashgg::Met> MET_;

        bool associatedZ_;
        bool associatedW_;
        bool VhasNeutrinos_;
        bool VhasLeptons_;
        bool VhasHadrons_;
        float Vpt_;


        //Creating a variables to add WHmva and PtV
        float VH_mva = -999;
        float ZHiggs0MToGG_MVA =-999;
        float ZHiggs0PHToGG_MVA =-999;
        float ZHiggs0PHf05ph0ToGG_MVA =-999;
        float ZHiggs0L1f05ph0ToGG_MVA =-999;
        float ZHiggs0L1ZgToGG_MVA =-999;
        float ZHiggs0L1Zgf05ph0ToGG_MVA =-999;

        float _Anom_MVA_pho1_eta = -999;
        float _Anom_MVA_pho1_phi = -999;
        float _Anom_MVA_pho1_idmva = -999;
        float _Anom_MVA_pho1_full5x5_r9 = -999;
        float _Anom_MVA_pho1_ptOverMgg = -999;
        float _Anom_MVA_pho2_eta = -999;
        float _Anom_MVA_pho2_phi = -999;
        float _Anom_MVA_pho2_idmva = -999;
        float _Anom_MVA_pho2_full5x5_r9 = -999;
        float _Anom_MVA_pho2_ptOverMgg = -999;
        float _Anom_MVA_mu1_pt = -999;
        float _Anom_MVA_mu1_eta = -999;
        float _Anom_MVA_mu1_phi = -999;
        float _Anom_MVA_mu1_energy = -999;
        float _Anom_MVA_mu2_pt = -999;
        float _Anom_MVA_mu2_eta = -999;
        float _Anom_MVA_mu2_phi = -999;
        float _Anom_MVA_mu2_energy = -999;
        float _Anom_MVA_ele1_pt = -999;
        float _Anom_MVA_ele1_eta = -999;
        float _Anom_MVA_ele1_phi = -999;
        float _Anom_MVA_ele1_energy = -999;
        float _Anom_MVA_ele2_pt = -999;
        float _Anom_MVA_ele2_eta = -999;
        float _Anom_MVA_ele2_phi = -999;
        float _Anom_MVA_ele2_energy = -999;
        float _Anom_MVA_jet1_pt = -999;
        float _Anom_MVA_jet1_phi = -999;
        float _Anom_MVA_jet1_eta = -999;
        float _Anom_MVA_jet1_energy = -999;
        float _Anom_MVA_jet2_pt = -999;
        float _Anom_MVA_jet2_phi = -999;
        float _Anom_MVA_jet2_eta = -999;
        float _Anom_MVA_jet2_energy = -999;
        float _Anom_MVA_cosPhiGG = -999;
        float _Anom_MVA_cosPhiG1_Mu1 = -999;
        float _Anom_MVA_cosPhiG1_Ele1 = -999;
        float _Anom_MVA_cosPhiG2_Mu1 = -999;
        float _Anom_MVA_cosPhiG2_Ele1 = -999;
        float _Anom_MVA_dR_Pho1Ele1_wh = -999;
        float _Anom_MVA_dR_Pho2Ele1_wh = -999;
        float _Anom_MVA_dR_Pho1Mu1_wh = -999;
        float _Anom_MVA_dR_Pho2Mu1_wh = -999;
        float _Anom_MVA_dR_Pho1Jet1_wh = -999;
        float _Anom_MVA_dR_Pho1Jet2_wh = -999;
        float _Anom_MVA_dR_Pho2Jet1_wh = -999;
        float _Anom_MVA_dR_Pho2Jet2_wh = -999;
        float _Anom_MVA_dR_Mu1Jet1_wh = -999;
        float _Anom_MVA_dR_Mu1Jet2_wh = -999;
        float _Anom_MVA_dR_Ele1Jet1_wh = -999;
        float _Anom_MVA_dR_Ele1Jet2_wh = -999;

        
    };
}

#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

