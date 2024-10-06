# Numba exercise
The script comprises a function written in standard python, and its rewriting using numba. Given a dataset containg jets from simulated Vector Boson Scattering events at the LHC, the function pairs a reconstructed jet of particles to its constituents, and computes collective properties of the jet based on the positions and energies of the constituents. In each event there is a number around 50 jets (varying from event to event), for a total of 10k events. 

The 'standard python' function took ~ **96 s to run on 1k events**.

Its numba rewriting took 2.83 s on 1k events, and **3.88 s on all the 10k events**.

The script needs an installation of `uproot` for running. The root file with the simulated events can be downloaded and unzipped as follows:
```
wget https://giulialavizzari.web.cern.ch/VBStagger_fileset/tree_Zjj_10k.tar.gz
tar -xf tree_Zjj_10k.tar.gz
```
