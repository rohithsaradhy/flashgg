import FWCore.ParameterSet.Config as cms

#Boundary Settings for AC
wh_fa3_boundaries = cms.vdouble(
                                #Tag 0
                                1.0,0.385, #STXSBDT
                                1.0,0.79, #ACBDT
                                #Tag 1
                                1.0,0.38541667, #STXSBDT
                                0.79,-0.68, #ACBDT
                                #Tag 2                                                                               
                                0.385,0.125, #STXSBDT
                                1.0,0.89, #ACBDT
                                #Tag 3
                                0.385,0.125, #STXSBDT
                                0.89,-0.68, #ACBDT
                                ) 

wh_fa2_boundaries = cms.vdouble(
                                #Tag 0
                                1.000,0.438, #STXSBDT
                                1.000,0.263, #ACBDT
                                #Tag 1
                                1.000,0.438, #STXSBDT
                                0.263,-1.000, #ACBDT
                                #Tag 2
                                0.438,0.281, #STXSBDT 
                                1.000,0.579, #ACBDT
                                #Tag 3
                                0.438,0.281, #STXSBDT
                                0.579,-1.000, #ACBDT
                                #Tag 4
                                0.281,0.021, #STXSBDT
                                1.000,0.368, #ACBDT
                                #Tag 5
                                0.281,0.021, #STXSBDT
                                0.368,-1.000, #ACBDT
                            )

wh_fL1_boundaries = cms.vdouble(
                                #Tag 0
                                1.000,0.438, #STXSBDT
                                1.000,-0.053, #ACBDT
                                #Tag 1
                                1.000,0.438, #STXSBDT
                                -0.053,-0.895, #ACBDT
                                #Tag 2
                                0.438,0.281, #STXSBDT
                                1.000,0.368, #ACBDT
                                #Tag 3
                                0.438,0.281, #STXSBDT
                                0.368,-0.895, #ACBDT
                                #Tag 4
                                0.281,0.021, #STXSBDT
                                1.000,-0.053, #ACBDT
                                #Tag 5
                                0.281,0.021, #STXSBDT
                                -0.053,-1.000, #ACBDT
                            )   


zh_fa3_boundaries = cms.vdouble(
                                #Tag 0
                                1.0,0.229, #STXSBDT
                                1.0,-0.68, #ACBDT
                                #Tag 1
                                0.229,-0.135, #STXSBDT
                                1.0,-0.16, #ACBDT
                                )                      

zh_fa2_boundaries = cms.vdouble(
                                #Tag 0
                                1.000,0.281, #STXSBDT
                                1.000,-0.368, #ACBDT
                                #Tag 1
                                1.000,0.281, #STXSBDT
                                -0.368,-1.000, #ACBDT
                                #Tag 2
                                0.281,-0.135, #STXSBDT
                                1.000,-0.263, #ACBDT
                                #Tag 3
                                0.281,-0.135, #STXSBDT
                                -0.263,-0.789, #ACBDT
                                )

zh_fL1_boundaries = cms.vdouble(
                                #Tag 0
                                1.000,0.281, #STXSBDT
                                1.000,-1.000, #ACBDT
                                #Tag 1
                                0.281,-0.135, #STXSBDT
                                1.000,-0.684, #ACBDT
                                #Tag 2
                                0.281,-0.135, #STXSBDT
                                -0.684,-1.000, #ACBDT
                                ) 



dipho_variables=[
    "dipho_sumpt                  := diPhoton.sumPt",
    "dipho_mass                   := diPhoton.mass",
    "dipho_leadPt                 := diPhoton.leadingPhoton.pt",
    "dipho_leadEta                := diPhoton.leadingPhoton.eta",
    "dipho_leadPhi                := diPhoton.leadingPhoton.phi",
    "dipho_leadE                  := diPhoton.leadingPhoton.energy",
    "dipho_lead_sieie             := diPhoton.leadingPhoton.sigmaIetaIeta",
    "dipho_lead_hoe               := diPhoton.leadingPhoton.hadronicOverEm",
    "dipho_lead_sigmaEoE          := diPhoton.leadingPhoton.sigEOverE",
    "dipho_lead_ptoM              := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "dipho_leadR9                 := diPhoton.leadingPhoton.full5x5_r9",
    "dipho_leadIDMVA              := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
    "dipho_lead_elveto            := diPhoton.leadingPhoton.passElectronVeto",
    "dipho_leadhasPixelSeed       := diPhoton.leadingPhoton.hasPixelSeed",
    "dipho_lead_prompt            := diPhoton.leadingPhoton.genMatchType",
    "dipho_subleadPt              := diPhoton.subLeadingPhoton.pt",
    "dipho_subleadEta             := diPhoton.subLeadingPhoton.eta",
    "dipho_subleadPhi             := diPhoton.subLeadingPhoton.phi",
    "dipho_subleadE               := diPhoton.subLeadingPhoton.energy",
    "dipho_sublead_sieie          := diPhoton.subLeadingPhoton.sigmaIetaIeta",
    "dipho_sublead_hoe            := diPhoton.subLeadingPhoton.hadronicOverEm",
    "dipho_sublead_sigmaEoE       := diPhoton.subLeadingPhoton.sigEOverE",
    "dipho_sublead_ptoM           := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
    "dipho_subleadR9              := diPhoton.subLeadingPhoton.full5x5_r9",
    "dipho_subleadIDMVA           := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",
    "dipho_sublead_elveto         := diPhoton.subLeadingPhoton.passElectronVeto",
    "dipho_subleadhasPixelSeed    := diPhoton.subLeadingPhoton.hasPixelSeed",
    "dipho_sublead_prompt         := diPhoton.subLeadingPhoton.genMatchType",
    "dipho_mva                    := diPhotonMVA.result",
    "dipho_PToM                   := diPhoton.pt/diPhoton.mass",
    "sigmarv                      := diPhotonMVA.sigmarv",
    "sigmarvDecorr                := diPhotonMVA.decorrSigmarv",
    "sigmawv                      := diPhotonMVA.sigmawv",
    "CosPhi                       := diPhotonMVA.CosPhi",
    "vtxprob                      := diPhotonMVA.vtxprob",
    "pt                           := diPhoton.pt",
    "leadSCeta                    := diPhoton.leadingPhoton.superCluster.eta",
    "subleadSCeta                 := diPhoton.subLeadingPhoton.superCluster.eta"
]

ele_variables=[
    "n_ele        := electrons.size",
    "ele1_Charge  := ?(electrons.size>0)? electrons.at(0).charge           : 0",
    "ele1_Pt      := ?(electrons.size>0)? electrons.at(0).pt               : -999",
    "ele1_Eta     := ?(electrons.size>0)? electrons.at(0).eta              : -999",
    "ele1_Phi     := ?(electrons.size>0)? electrons.at(0).phi              : -999",
    "ele1_E       := ?(electrons.size>0)? electrons.at(0).energy           : -999",
    "ele1_EtaSC   := ?(electrons.size>0)? electrons.at(0).superCluster.eta : -999",
    "ele1_PhiSC   := ?(electrons.size>0)? electrons.at(0).superCluster.phi : -999",
    "ele2_Charge  := ?(electrons.size>1)? electrons.at(1).charge           : 0",
    "ele2_Pt      := ?(electrons.size>1)? electrons.at(1).pt               : -999",
    "ele2_Eta     := ?(electrons.size>1)? electrons.at(1).eta              : -999",
    "ele2_Phi     := ?(electrons.size>1)? electrons.at(1).phi              : -999",
    "ele2_E       := ?(electrons.size>1)? electrons.at(1).energy           : -999",
    "ele2_EtaSC   := ?(electrons.size>1)? electrons.at(1).superCluster.eta : -999",
    "ele2_PhiSC   := ?(electrons.size>1)? electrons.at(1).superCluster.phi : -999"
]

mu_variables=[
    "n_mu       := muons.size",
    "mu1_Charge := ?(muons.size>0)? muons.at(0).charge : 0",
    "mu1_Pt     := ?(muons.size>0)? muons.at(0).pt     : -999",
    "mu1_Eta    := ?(muons.size>0)? muons.at(0).eta    : -999",
    "mu1_Phi    := ?(muons.size>0)? muons.at(0).phi    : -999",
    "mu1_E      := ?(muons.size>0)? muons.at(0).energy : -999",
    "mu2_Charge := ?(muons.size>1)? muons.at(1).charge : 0",
    "mu2_Pt     := ?(muons.size>1)? muons.at(1).pt     : -999",
    "mu2_Eta    := ?(muons.size>1)? muons.at(1).eta    : -999",
    "mu2_Phi    := ?(muons.size>1)? muons.at(1).phi    : -999",
    "mu2_E      := ?(muons.size>1)? muons.at(1).energy : -999"
]

jet_variables=[
    "n_jets      := jets.size"
]

njet = 15
for i in range(njet):
    jet_variables.append( "jet%d_Pt  := ?(jets.size>%d)? jets.at(%d).pt      : -999" % (i+1, i, i))
    jet_variables.append( "jet%d_Eta := ?(jets.size>%d)? jets.at(%d).eta     : -999" % (i+1, i, i))
    jet_variables.append( "jet%d_Phi := ?(jets.size>%d)? jets.at(%d).phi     : -999" % (i+1, i, i))
    jet_variables.append( "jet%d_E   := ?(jets.size>%d)? jets.at(%d).energy  : -999" % (i+1, i, i))
    jet_variables.append( "jet%d_deepbtag   := ?(jets.size>%d)? jets.at(%d).bDiscriminator('pfDeepCSVJetTags:probb') + jets.at(%d).bDiscriminator('pfDeepCSVJetTags:probbb') : -999" % (i+1, i, i, i) )

met_variables=[
    "met_Pt      := met.getCorPt()",
    "met_Phi     := met.getCorPhi()",
    "met_sumEt   := met.sumEt()",
    "met_Sig     := met.mEtSig()",
    "met_RealSig := met.significance()"
]

extra_variables=[
    "minDeltaPhiJetMet := MinDeltaPhiJetMet()",
    "maxJetDeepCSV     := MaxJetDeepCSV()"
]

gen_variables=[
    "hasZ    := associatedZ()",
    "hasW    := associatedW()",
    "VhasNeu := VhasNeutrinos()",
    "VhasLep := VhasLeptons()",
    "VhasHad := VhasHadrons()",
    "Vpt     := Vpt()"
]




#Full list of variables to dump that have been previously used
#STXS MVA
stxs_vars = [
                'vh_mva :=  VHmva()'
]

whAnomVars = [
    'WHiggs0MToGG_MVA := WHiggs0MToGG_mva()',
    'WHiggs0PHToGG_MVA := WHiggs0PHToGG_mva()',
    'WHiggs0L1ToGG_MVA := WHiggs0L1ToGG_mva()',
]
zhAnomVars = [
    'ZHiggs0MToGG_MVA := ZHiggs0MToGG_mva()',
    'ZHiggs0PHToGG_MVA := ZHiggs0PHToGG_mva()',
    'ZHiggs0L1ToGG_MVA := ZHiggs0L1ToGG_mva()',
]


#Anomalous variables used for TMVA #For Debug purposes only
anom_vars_mva = [
    'Anom_mva_pho1_eta := Anom_MVA_pho1_eta()',
    'Anom_mva_pho1_phi := Anom_MVA_pho1_phi()',
    'Anom_mva_pho1_idmva := Anom_MVA_pho1_idmva()',
    'Anom_mva_pho1_full5x5_r9 := Anom_MVA_pho1_full5x5_r9()',
    'Anom_mva_pho1_ptOverMgg := Anom_MVA_pho1_ptOverMgg()',
    'Anom_mva_pho2_eta := Anom_MVA_pho2_eta()',
    'Anom_mva_pho2_phi := Anom_MVA_pho2_phi()',
    'Anom_mva_pho2_idmva := Anom_MVA_pho2_idmva()',
    'Anom_mva_pho2_full5x5_r9 := Anom_MVA_pho2_full5x5_r9()',
    'Anom_mva_pho2_ptOverMgg := Anom_MVA_pho2_ptOverMgg()',
    'Anom_mva_mu1_pt := Anom_MVA_mu1_pt()',
    'Anom_mva_mu1_eta := Anom_MVA_mu1_eta()',
    'Anom_mva_mu1_phi := Anom_MVA_mu1_phi()',
    'Anom_mva_mu1_energy := Anom_MVA_mu1_energy()',
    'Anom_mva_mu2_pt := Anom_MVA_mu2_pt()',
    'Anom_mva_mu2_eta := Anom_MVA_mu2_eta()',
    'Anom_mva_mu2_phi := Anom_MVA_mu2_phi()',
    'Anom_mva_mu2_energy := Anom_MVA_mu2_energy()',
    'Anom_mva_ele1_pt := Anom_MVA_ele1_pt()',
    'Anom_mva_ele1_eta := Anom_MVA_ele1_eta()',
    'Anom_mva_ele1_phi := Anom_MVA_ele1_phi()',
    'Anom_mva_ele1_energy := Anom_MVA_ele1_energy()',
    'Anom_mva_ele2_pt := Anom_MVA_ele2_pt()',
    'Anom_mva_ele2_eta := Anom_MVA_ele2_eta()',
    'Anom_mva_ele2_phi := Anom_MVA_ele2_phi()',
    'Anom_mva_ele2_energy := Anom_MVA_ele2_energy()',
    'Anom_mva_jet1_pt := Anom_MVA_jet1_pt()',
    'Anom_mva_jet1_phi := Anom_MVA_jet1_phi()',
    'Anom_mva_jet1_eta := Anom_MVA_jet1_eta()',
    'Anom_mva_jet1_energy := Anom_MVA_jet1_energy()',
    'Anom_mva_jet2_pt := Anom_MVA_jet2_pt()',
    'Anom_mva_jet2_phi := Anom_MVA_jet2_phi()',
    'Anom_mva_jet2_eta := Anom_MVA_jet2_eta()',
    'Anom_mva_jet2_energy := Anom_MVA_jet2_energy()',
    'Anom_mva_cosPhiGG := Anom_MVA_cosPhiGG()',
    'Anom_mva_cosPhiG1_Mu1 := Anom_MVA_cosPhiG1_Mu1()',
    'Anom_mva_cosPhiG1_Ele1 := Anom_MVA_cosPhiG1_Ele1()',
    'Anom_mva_cosPhiG2_Mu1 := Anom_MVA_cosPhiG2_Mu1()',
    'Anom_mva_cosPhiG2_Ele1 := Anom_MVA_cosPhiG2_Ele1()',
    'Anom_mva_dR_Pho1Ele1_wh := Anom_MVA_dR_Pho1Ele1_wh()',
    'Anom_mva_dR_Pho2Ele1_wh := Anom_MVA_dR_Pho2Ele1_wh()',
    'Anom_mva_dR_Pho1Mu1_wh := Anom_MVA_dR_Pho1Mu1_wh()',
    'Anom_mva_dR_Pho2Mu1_wh := Anom_MVA_dR_Pho2Mu1_wh()',
    'Anom_mva_dR_Pho1Jet1_wh := Anom_MVA_dR_Pho1Jet1_wh()',
    'Anom_mva_dR_Pho1Jet2_wh := Anom_MVA_dR_Pho1Jet2_wh()',
    'Anom_mva_dR_Pho2Jet1_wh := Anom_MVA_dR_Pho2Jet1_wh()',
    'Anom_mva_dR_Pho2Jet2_wh := Anom_MVA_dR_Pho2Jet2_wh()',
    'Anom_mva_dR_Mu1Jet1_wh := Anom_MVA_dR_Mu1Jet1_wh()',
    'Anom_mva_dR_Mu1Jet2_wh := Anom_MVA_dR_Mu1Jet2_wh()',
    'Anom_mva_dR_Ele1Jet1_wh := Anom_MVA_dR_Ele1Jet1_wh()',
    'Anom_mva_dR_Ele1Jet2_wh := Anom_MVA_dR_Ele1Jet2_wh()',
]

# We are repeating variable because we want the same name...
anom_diphoton_variables = [
    "mass            := diPhoton.mass",
    "diphoton_pt     := diPhoton.pt",
    "diphoton_mva    := diPhotonMVA.result",
    "pho1_pt         := diPhoton.leadingPhoton.pt",
    "pho1_eta        := diPhoton.leadingPhoton.eta",
    "pho1_phi        := diPhoton.leadingPhoton.phi",
    "pho1_energy     := diPhoton.leadingPhoton.energy",
    "pho1_full5x5_r9 := diPhoton.leadingPhoton.full5x5_r9",
    "pho1_idmva      := diPhoton.leadPhotonId",
    "pho1_genMatchType:=diPhoton.leadingPhoton.genMatchType",
    "pho2_pt         := diPhoton.subLeadingPhoton.pt",
    "pho2_eta        := diPhoton.subLeadingPhoton.eta",
    "pho2_phi        := diPhoton.subLeadingPhoton.phi",
    "pho2_energy     := diPhoton.subLeadingPhoton.energy",
    "pho2_full5x5_r9 := diPhoton.subLeadingPhoton.full5x5_r9",
    "pho2_idmva      := diPhoton.subLeadPhotonId",
    "pho2_genMatchType:=diPhoton.subLeadingPhoton.genMatchType",
    "pho1_ptOverMgg  := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "pho2_ptOverMgg  := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
]

# We are repeating variable because we want the same name...
anom_leptons_variables = [ 
    "mu1_pt         :=  ? muons.size()>0 ? muons[0].pt() : -100 ",
    "mu1_phi        :=  ? muons.size()>0 ? muons[0].phi() : -100 ",
    "mu1_eta        :=  ? muons.size()>0 ? muons[0].eta() : -100 ",
    "mu1_energy     :=  ? muons.size()>0 ? muons[0].energy() : -100 ",
    "mu2_pt         :=  ? muons.size()>1 ? muons[1].pt() : -100 ",
    "mu2_phi        :=  ? muons.size()>1 ? muons[1].phi() : -100 ",
    "mu2_eta        :=  ? muons.size()>1 ? muons[1].eta() : -100 ",
    "mu2_energy     :=  ? muons.size()>1 ? muons[1].energy() : -100 ",
    "ele1_pt        :=  ? electrons.size()>0 ? electrons[0].pt() : -100 ",
    "ele1_phi       :=  ? electrons.size()>0 ? electrons[0].phi() : -100 ",
    "ele1_eta       :=  ? electrons.size()>0 ? electrons[0].eta() : -100 ",
    "ele1_energy    :=  ? electrons.size()>0 ? electrons[0].energy() : -100 ",
    "ele2_pt        :=  ? electrons.size()>1 ? electrons[1].pt() : -100 ",
    "ele2_phi       :=  ? electrons.size()>1 ? electrons[1].phi() : -100 ",
    "ele2_eta       :=  ? electrons.size()>1 ? electrons[1].eta() : -100 ",
    "ele2_energy    :=  ? electrons.size()>1 ? electrons[1].energy() : -100 ",
    "nMuons         :=  muons.size()",
    "nEle           :=  electrons.size()"
]
# We are repeating variable because we want the same name...
anom_jets_variables = [
    "njets := jets.size()",
    "jet1_pt     :=  ? jets.size()>0 ? jets[0].pt : -100 ",
    "jet1_phi    :=  ? jets.size()>0 ? jets[0].phi : -100 ",
    "jet1_eta    :=  ? jets.size()>0 ? jets[0].eta : -100 ",
    "jet1_energy :=  ? jets.size()>0 ? jets[0].energy : -100 ",
    "jet2_pt     :=  ? jets.size()>1 ? jets[1].pt : -100 ",
    "jet2_phi    :=  ? jets.size()>1 ? jets[1].phi : -100 ",
    "jet2_eta    :=  ? jets.size()>1 ? jets[1].eta : -100 ",
    "jet2_energy :=  ? jets.size()>1 ? jets[1].energy : -100 ",
    "jet3_pt     :=  ? jets.size()>2 ? jets[2].pt : -100 ",
    "jet3_phi    :=  ? jets.size()>2 ? jets[2].phi : -100 ",
    "jet3_eta    :=  ? jets.size()>2 ? jets[2].eta : -100 ",
    "jet3_energy :=  ? jets.size()>2 ? jets[2].energy : -100 ",
    "jet4_pt     :=  ? jets.size()>3 ? jets[3].pt : -100 ",
    "jet4_phi    :=  ? jets.size()>3 ? jets[3].phi : -100 ",
    "jet4_eta    :=  ? jets.size()>3 ? jets[3].eta : -100 ",
    "jet4_energy :=  ? jets.size()>3 ? jets[3].energy : -100 ",
    "jet5_pt     :=  ? jets.size()>4 ? jets[4].pt : -100 ",
    "jet5_phi    :=  ? jets.size()>4 ? jets[4].phi : -100 ",
    "jet5_eta    :=  ? jets.size()>4 ? jets[4].eta : -100 ",
    "jet5_energy :=  ? jets.size()>4 ? jets[4].energy : -100 ",
    "jet6_pt     :=  ? jets.size()>5 ? jets[5].pt : -100 ",
    "jet6_phi    :=  ? jets.size()>5 ? jets[5].phi : -100 ",
    "jet6_eta    :=  ? jets.size()>5 ? jets[5].eta : -100 ",
    "jet6_energy :=  ? jets.size()>5 ? jets[5].energy : -100 ",
    "jet7_pt     :=  ? jets.size()>6 ? jets[6].pt : -100 ",
    "jet7_phi    :=  ? jets.size()>6 ? jets[6].phi : -100 ",
    "jet7_eta    :=  ? jets.size()>6 ? jets[6].eta : -100 ",
    "jet7_energy :=  ? jets.size()>6 ? jets[6].energy : -100 "
]



#dR_variables_WHLeptonic = [ "dR_Pho1Jet1_wh :=  ? jets.size() > 0 ? whleptonictags_obj.deltaRPho1Jet1 : -100"
anom_dR_variables_WHLeptonic = [
    "dR_Pho1Jet1_wh :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho1Jet2_wh :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",  
    "dR_Pho2Jet1_wh :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho2Jet2_wh :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Ele1_wh :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho1Ele2_wh :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",                           
    "dR_Pho2Ele1_wh :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
    "dR_Pho2Ele2_wh :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Ele3_wh :=  ? electrons.size() > 2 ? deltaR(electrons[2].eta, electrons[2].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Ele3_wh :=  ? electrons.size() > 2 ? deltaR(electrons[2].eta, electrons[2].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
    "dR_Pho1Ele4_wh :=  ? electrons.size() > 3 ? deltaR(electrons[3].eta, electrons[3].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Ele4_wh :=  ? electrons.size() > 3 ? deltaR(electrons[3].eta, electrons[3].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
    "dR_Pho1Ele5_wh :=  ? electrons.size() > 4 ? deltaR(electrons[4].eta, electrons[4].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Ele5_wh :=  ? electrons.size() > 4 ? deltaR(electrons[4].eta, electrons[4].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
    "dR_Pho1Mu1_wh  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho1Mu2_wh  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Mu1_wh  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho2Mu2_wh  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Mu1Jet1_wh  :=  ? (muons.size() > 0 && jets.size() > 0) ? deltaR(muons[0].eta, muons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Mu1Jet2_wh  :=  ? (muons.size() > 0 && jets.size() > 1) ? deltaR(muons[0].eta, muons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Mu2Jet1_wh  :=  ? (muons.size() > 1 && jets.size() > 0) ? deltaR(muons[1].eta, muons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Mu2Jet2_wh  :=  ? (muons.size() > 1 && jets.size() > 1) ? deltaR(muons[1].eta, muons[1].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Mu1Jet3_wh  :=  ? (muons.size() > 0 && jets.size() > 2) ? deltaR(muons[0].eta, muons[0].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Mu2Jet3_wh  :=  ? (muons.size() > 1 && jets.size() > 2) ? deltaR(muons[1].eta, muons[1].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Mu1Jet4_wh  :=  ? (muons.size() > 0 && jets.size() > 3) ? deltaR(muons[0].eta, muons[0].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Mu2Jet4_wh  :=  ? (muons.size() > 1 && jets.size() > 3) ? deltaR(muons[1].eta, muons[1].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Mu1Jet5_wh  :=  ? (muons.size() > 0 && jets.size() > 4) ? deltaR(muons[0].eta, muons[0].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Mu2Jet5_wh  :=  ? (muons.size() > 1 && jets.size() > 4) ? deltaR(muons[1].eta, muons[1].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Mu1Jet6_wh  :=  ? (muons.size() > 0 && jets.size() > 5) ? deltaR(muons[0].eta, muons[0].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Mu2Jet6_wh  :=  ? (muons.size() > 1 && jets.size() > 5) ? deltaR(muons[1].eta, muons[1].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Mu1Jet7_wh  :=  ? (muons.size() > 0 && jets.size() > 6) ? deltaR(muons[0].eta, muons[0].phi, jets[6].eta, jets[6].phi) : -100 ",
    "dR_Mu2Jet7_wh  :=  ? (muons.size() > 1 && jets.size() > 6) ? deltaR(muons[1].eta, muons[1].phi, jets[6].eta, jets[6].phi) : -100 ",
    "dR_Mu3Jet1_wh  :=  ? (muons.size() > 2 && jets.size() > 0) ? deltaR(muons[2].eta, muons[2].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Mu3Jet2_wh  :=  ? (muons.size() > 2 && jets.size() > 1) ? deltaR(muons[2].eta, muons[2].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Mu3Jet3_wh  :=  ? (muons.size() > 2 && jets.size() > 2) ? deltaR(muons[2].eta, muons[2].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Mu3Jet4_wh  :=  ? (muons.size() > 2 && jets.size() > 3) ? deltaR(muons[2].eta, muons[2].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Mu3Jet5_wh  :=  ? (muons.size() > 2 && jets.size() > 4) ? deltaR(muons[2].eta, muons[2].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Mu3Jet6_wh  :=  ? (muons.size() > 2 && jets.size() > 5) ? deltaR(muons[2].eta, muons[2].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Mu3Jet7_wh  :=  ? (muons.size() > 2 && jets.size() > 6) ? deltaR(muons[2].eta, muons[2].phi, jets[6].eta, jets[6].phi) : -100 ",  
    "dR_Mu4Jet1_wh  :=  ? (muons.size() > 3 && jets.size() > 0) ? deltaR(muons[3].eta, muons[3].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Mu4Jet2_wh  :=  ? (muons.size() > 3 && jets.size() > 1) ? deltaR(muons[3].eta, muons[3].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Mu4Jet3_wh  :=  ? (muons.size() > 3 && jets.size() > 2) ? deltaR(muons[3].eta, muons[3].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Mu4Jet4_wh  :=  ? (muons.size() > 3 && jets.size() > 3) ? deltaR(muons[3].eta, muons[3].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Mu4Jet5_wh  :=  ? (muons.size() > 3 && jets.size() > 4) ? deltaR(muons[3].eta, muons[3].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Mu4Jet6_wh  :=  ? (muons.size() > 3 && jets.size() > 5) ? deltaR(muons[3].eta, muons[3].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Mu4Jet7_wh  :=  ? (muons.size() > 3 && jets.size() > 6) ? deltaR(muons[3].eta, muons[3].phi, jets[6].eta, jets[6].phi) : -100 ",  
    "dR_Mu5Jet1_wh  :=  ? (muons.size() > 4 && jets.size() > 0) ? deltaR(muons[4].eta, muons[4].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Mu5Jet2_wh  :=  ? (muons.size() > 4 && jets.size() > 1) ? deltaR(muons[4].eta, muons[4].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Mu5Jet3_wh  :=  ? (muons.size() > 4 && jets.size() > 2) ? deltaR(muons[4].eta, muons[4].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Mu5Jet4_wh  :=  ? (muons.size() > 4 && jets.size() > 3) ? deltaR(muons[4].eta, muons[4].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Mu5Jet5_wh  :=  ? (muons.size() > 4 && jets.size() > 4) ? deltaR(muons[4].eta, muons[4].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Mu5Jet6_wh  :=  ? (muons.size() > 4 && jets.size() > 5) ? deltaR(muons[4].eta, muons[4].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Mu5Jet7_wh  :=  ? (muons.size() > 4 && jets.size() > 6) ? deltaR(muons[4].eta, muons[4].phi, jets[6].eta, jets[6].phi) : -100 ", 
    "dR_Ele1Jet1_wh  :=  ? (electrons.size() > 0 && jets.size() > 0) ? deltaR(electrons[0].eta, electrons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Ele1Jet2_wh  :=  ? (electrons.size() > 0 && jets.size() > 1) ? deltaR(electrons[0].eta, electrons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Ele2Jet1_wh  :=  ? (electrons.size() > 1 && jets.size() > 0) ? deltaR(electrons[1].eta, electrons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Ele2Jet2_wh  :=  ? (electrons.size() > 1 && jets.size() > 1) ? deltaR(electrons[1].eta, electrons[1].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Ele1Jet3_wh  :=  ? (electrons.size() > 0 && jets.size() > 2) ? deltaR(electrons[0].eta, electrons[0].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Ele2Jet3_wh  :=  ? (electrons.size() > 1 && jets.size() > 2) ? deltaR(electrons[1].eta, electrons[1].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Ele1Jet4_wh  :=  ? (electrons.size() > 0 && jets.size() > 3) ? deltaR(electrons[0].eta, electrons[0].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Ele2Jet4_wh  :=  ? (electrons.size() > 1 && jets.size() > 3) ? deltaR(electrons[1].eta, electrons[1].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Ele1Jet5_wh  :=  ? (electrons.size() > 0 && jets.size() > 4) ? deltaR(electrons[0].eta, electrons[0].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Ele2Jet5_wh  :=  ? (electrons.size() > 1 && jets.size() > 4) ? deltaR(electrons[1].eta, electrons[1].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Ele1Jet6_wh  :=  ? (electrons.size() > 0 && jets.size() > 5) ? deltaR(electrons[0].eta, electrons[0].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Ele2Jet6_wh  :=  ? (electrons.size() > 1 && jets.size() > 5) ? deltaR(electrons[1].eta, electrons[1].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Ele1Jet7_wh  :=  ? (electrons.size() > 0 && jets.size() > 6) ? deltaR(electrons[0].eta, electrons[0].phi, jets[6].eta, jets[6].phi) : -100 ",
    "dR_Ele2Jet7_wh  :=  ? (electrons.size() > 1 && jets.size() > 6) ? deltaR(electrons[1].eta, electrons[1].phi, jets[6].eta, jets[6].phi) : -100 ",
    "dR_Ele3Jet1_wh  :=  ? (electrons.size() > 2 && jets.size() > 0) ? deltaR(electrons[2].eta, electrons[2].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Ele3Jet2_wh  :=  ? (electrons.size() > 2 && jets.size() > 1) ? deltaR(electrons[2].eta, electrons[2].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Ele3Jet3_wh  :=  ? (electrons.size() > 2 && jets.size() > 2) ? deltaR(electrons[2].eta, electrons[2].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Ele3Jet4_wh  :=  ? (electrons.size() > 2 && jets.size() > 3) ? deltaR(electrons[2].eta, electrons[2].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Ele3Jet5_wh  :=  ? (electrons.size() > 2 && jets.size() > 4) ? deltaR(electrons[2].eta, electrons[2].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Ele3Jet6_wh  :=  ? (electrons.size() > 2 && jets.size() > 5) ? deltaR(electrons[2].eta, electrons[2].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Ele3Jet7_wh  :=  ? (electrons.size() > 2 && jets.size() > 6) ? deltaR(electrons[2].eta, electrons[2].phi, jets[6].eta, jets[6].phi) : -100 ",  
    "dR_Ele4Jet1_wh  :=  ? (electrons.size() > 3 && jets.size() > 0) ? deltaR(electrons[3].eta, electrons[3].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Ele4Jet2_wh  :=  ? (electrons.size() > 3 && jets.size() > 1) ? deltaR(electrons[3].eta, electrons[3].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Ele4Jet3_wh  :=  ? (electrons.size() > 3 && jets.size() > 2) ? deltaR(electrons[3].eta, electrons[3].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Ele4Jet4_wh  :=  ? (electrons.size() > 3 && jets.size() > 3) ? deltaR(electrons[3].eta, electrons[3].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Ele4Jet5_wh  :=  ? (electrons.size() > 3 && jets.size() > 4) ? deltaR(electrons[3].eta, electrons[3].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Ele4Jet6_wh  :=  ? (electrons.size() > 3 && jets.size() > 5) ? deltaR(electrons[3].eta, electrons[3].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Ele4Jet7_wh  :=  ? (electrons.size() > 3 && jets.size() > 6) ? deltaR(electrons[3].eta, electrons[3].phi, jets[6].eta, jets[6].phi) : -100 ",  
    "dR_Ele5Jet1_wh  :=  ? (electrons.size() > 4 && jets.size() > 0) ? deltaR(electrons[4].eta, electrons[4].phi, jets[0].eta, jets[0].phi) : -100 ",
    "dR_Ele5Jet2_wh  :=  ? (electrons.size() > 4 && jets.size() > 1) ? deltaR(electrons[4].eta, electrons[4].phi, jets[1].eta, jets[1].phi) : -100 ",
    "dR_Ele5Jet3_wh  :=  ? (electrons.size() > 4 && jets.size() > 2) ? deltaR(electrons[4].eta, electrons[4].phi, jets[2].eta, jets[2].phi) : -100 ",
    "dR_Ele5Jet4_wh  :=  ? (electrons.size() > 4 && jets.size() > 3) ? deltaR(electrons[4].eta, electrons[4].phi, jets[3].eta, jets[3].phi) : -100 ",
    "dR_Ele5Jet5_wh  :=  ? (electrons.size() > 4 && jets.size() > 4) ? deltaR(electrons[4].eta, electrons[4].phi, jets[4].eta, jets[4].phi) : -100 ",
    "dR_Ele5Jet6_wh  :=  ? (electrons.size() > 4 && jets.size() > 5) ? deltaR(electrons[4].eta, electrons[4].phi, jets[5].eta, jets[5].phi) : -100 ",
    "dR_Ele5Jet7_wh  :=  ? (electrons.size() > 4 && jets.size() > 6) ? deltaR(electrons[4].eta, electrons[4].phi, jets[6].eta, jets[6].phi) : -100 ",                      
    "dR_Pho1Jet3_wh :=  ? jets.size() > 2 ? deltaR(jets[2].eta, jets[2].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Jet3_wh :=  ? jets.size() > 2 ? deltaR(jets[2].eta, jets[2].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Jet4_wh :=  ? jets.size() > 3 ? deltaR(jets[3].eta, jets[3].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Jet4_wh :=  ? jets.size() > 3 ? deltaR(jets[3].eta, jets[3].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Jet5_wh :=  ? jets.size() > 4 ? deltaR(jets[4].eta, jets[4].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Jet5_wh :=  ? jets.size() > 4 ? deltaR(jets[4].eta, jets[4].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Jet6_wh :=  ? jets.size() > 5 ? deltaR(jets[5].eta, jets[5].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Jet6_wh :=  ? jets.size() > 5 ? deltaR(jets[5].eta, jets[5].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
    "dR_Pho1Jet7_wh :=  ? jets.size() > 6 ? deltaR(jets[6].eta, jets[6].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
    "dR_Pho2Jet7_wh :=  ? jets.size() > 6 ? deltaR(jets[6].eta, jets[6].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100"
]


wh_anom_dumper_vars = stxs_vars + whAnomVars + anom_diphoton_variables+anom_leptons_variables + anom_jets_variables + met_variables + anom_dR_variables_WHLeptonic
zh_anom_dumper_vars = stxs_vars + zhAnomVars + anom_diphoton_variables+anom_leptons_variables + anom_jets_variables + anom_dR_variables_WHLeptonic