import awkward as ak
import numpy as np
import uproot as uproot
import time

import cProfile

# ------------------------ original function

def getJetConstituents(i, nConst, allConst):
    # time.sleep(0.002)
    return allConst[sum(nConst[:i]):sum(nConst[:i+1])]


def jet_pull():
    filename = './tree_Zjj_10k.root'
    file = uproot.open(filename)

    f_LHEParticles = file["LHEParticles;1"]
    f_GenJets = file["GenJets;1"]
    f_GenParticles = file["GenParticles;2"]

    LHEParticles = f_LHEParticles.arrays(f_LHEParticles.keys())
    GenJets = f_GenJets.arrays(f_GenJets.keys())
    GenParticles = f_GenParticles.arrays(f_GenParticles.keys())


    for ev in range(10):

        genjets_pt = GenJets.GenJet_pt[ev]
        nConstituents = GenJets.GenJet_nConstituents[ev]
        constituents = GenJets.GenJet_constituents[ev]
        genParts_pt = GenParticles.GenPart_pt[ev]
        genParts_eta = GenParticles.GenPart_eta[ev]
        genParts_phi = GenParticles.GenPart_phi[ev]
        genJets_eta = GenJets.GenJet_eta[ev]
        genJets_phi = GenJets.GenJet_phi[ev]
            
        NJETS = len(GenJets.GenJet_pt[ev])
        genjets_pull = []
        
        pulls_m = []
        pulls_eta = []
        pulls_phi = []
        
        
        for i in range(NJETS):
            pull_m = 0
            pull_eta = 0
            pull_phi = 0
            
            genPartsInJetIndices = getJetConstituents(i, nConstituents, constituents)
            
            cs_pt  = genParts_pt[genPartsInJetIndices]
            cs_eta = genParts_eta[genPartsInJetIndices]
            cs_phi = genParts_phi[genPartsInJetIndices]
            
            jet_pt  = GenJets.GenJet_pt[ev][i]
            jet_eta = GenJets.GenJet_eta[ev][i]
            jet_phi = GenJets.GenJet_phi[ev][i]
            
            for c_pt, c_eta, c_phi in zip(cs_pt, cs_eta, cs_phi):
                pti = c_pt
                ri2 = (c_eta-jet_eta)**2+(c_phi-jet_phi)**2
                m = pti*ri2
                pull_m += m
                pull_eta += (c_eta-jet_eta)*m
                pull_phi += (c_phi-jet_phi)*m

            
            pull_m /= jet_pt
            pull_eta /= jet_pt
            pull_phi /= jet_pt
            
            pulls_m.append(pull_m)
            pulls_eta.append(pull_eta)
            pulls_phi.append(pull_phi)
            
            
        # dummy action that takes time
        print (pulls_m, pulls_eta, pulls_phi)



#cProfile.run('jet_pull()', sort='cumtime')

with cProfile.Profile() as pr:
    jet_pull()  

pr.dump_stats('profiling_example.prof')


