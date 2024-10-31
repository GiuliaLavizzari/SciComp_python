# Scientific Computing with Python
Exam - Giulia Lavizzari (ay 2023/2024)


## Lecture 1 
### Python interface to Oracle DB
The exercise contains a class ([DbInterface](https://github.com/GiuliaLavizzari/SciComp_python/blob/09459dc00b621f894b7a7fcb1f8f6fb99c8d673b/Lecture1/DbInterface.py)), which allows to interact with an oracle DB built for the CMS electromagnetic calorimeter (ECAL) upgrade for the High-Luminosity phase of the LHC.
It also contains a set of [utilities](https://github.com/GiuliaLavizzari/SciComp_python/tree/09459dc00b621f894b7a7fcb1f8f6fb99c8d673b/Lecture1/scripts) for quick operations on the db, such as printing or deleting tables.

**A DEMO can be found [here](https://drive.google.com/file/d/1M7lp7QczL5PBuhEJal0w_ra4H_J0Agxl/view?usp=sharing)**

## Lecture 2

### Game Of Life
The first exercise here contained is the game of life. It can be run in normal mode (random generation of starting point), or specifying `--spaceShip`. The latter will provide an animation of a spaceship, crossing the grid from the top left to the bottom right.

### Secret Santa
The second exercise here in lecture 2 is a very very simple script that shuffles a set of names in order to assign to each person his/her secret santa, and then sends an email to everyone wit the correct info. Note that the script works for a gmail server and it's necessary to allow the "Less Secure App access" in the settings of the account.
It was developed for a group of friends that live far from each other and thus cannot pick names written on paper (as normally one would to). Worked!!

## Lecture 3

### Plot payload of CMS ECAL during 2024 data-taking
This exercise features a script ([plotPayloadData.py](https://github.com/GiuliaLavizzari/SciComp_python/blob/75c017603d64ff77d7f57596fa51d0246953568c/Lecture3/plotPayloadData.py)) that plots the payload in kB collected by each CMS ECAL partition, namely the endcaps (EE), barrel+ (EB+) and barrel- (EB-) during 2024 data-taking. Data are stored in a txt file, in the same folder, and output figures are collected in a [dedicated folder](https://github.com/GiuliaLavizzari/SciComp_python/tree/75c017603d64ff77d7f57596fa51d0246953568c/Lecture3/images) (and displayed in the dedicated README).

The exercise also contains a second version of the script ([plotPayloadData_improved.py](https://github.com/GiuliaLavizzari/SciComp_python/blob/75c017603d64ff77d7f57596fa51d0246953568c/Lecture3/plotPayloadData_improved.py)), which introduces some modifications (i.e. subplots, different font...).

### Game of life visualization
The Game of Life exercise in Lecture 1 also contains an example of use of matplotlib, more specifically it allows for creating a gif showing the result of the exercise.

## Lecture 4

### Smoothing exercise
After generating and smearing the data as illustrated in the exercise, Scipy `convolute` is used to smooth them, considering a gaussian kernel.

### Interpolation exercise
A function is created (A sine dumped by a decaying exponential, summed to a polynomial term) and used to generate a sample.
Interpolation of such sample is then performed, either using scipy CubicSpline (`--cubicSpline`) or via interp1d (the kind of interpolation can be specified via the `--intsetting` argument).
Residuals are computed as Ytrue (i.e. the actual function) -  Yinterpolated (i.e. the interpolated function).


## Lecture 6

### PR to scientificcomputing_bicocca_2023
I added a [PR to remove an attachment](https://github.com/dgerosa/scientificcomputing_bicocca_2023/pull/12) that was missing (it was preventing the notebook from showing).

### Project under version control (git)
The project I'm working on that was not under version control is this exam, which is now here on github! 
(In my usual work life I use mainly gitlab, as I mainly work on CERN projects hosted there.)

### Additional: github pages fix
I created a github page about two years ago, for a "digital" poster session in which I took part. We were asked not to print our poster, and instead of showing a standard poster in pdf I created a single-page website hosted on github pages (extremely simple). As I didn't really know how to use git, I created it under `https://giulialavizzari.github.io/`. While I was reading the lectures I decided it was time to fix this and moved it to a more proper url (namely `https://giulialavizzari.github.io/VAE-ACAT2023/`). Now my poster displays [there](https://giulialavizzari.github.io/VAE-ACAT2023/), and there is room for improving my "personal page" with for example CV info.


## Lecture 7

### Numba exercise
The script comprises a function written in standard python, and its rewriting using numba. Given a dataset containg jets from simulated Vector Boson Scattering events at the LHC, the function pairs a reconstructed jet of particles to its constituents, and computes collective properties of the jet based on the positions and energies of the constituents. In each event there is a number around 50 jets (varying from event to event), for a total of 10k events. 

The 'standard python' function took ~ **96 s to run on 1k events**.

Its numba rewriting took 2.83 s on 1k events, and **3.88 s on all the 10k events**.

The script needs an installation of `uproot` for running. The root file with the simulated events can be downloaded and unzipped as follows:
```
wget https://giulialavizzari.web.cern.ch/VBStagger_fileset/tree_Zjj_10k.tar.gz
tar -xf tree_Zjj_10k.tar.gz
```
### Plotting decorator
Designed a plotting decorator for quick plotting in python using CMS style. Luminosity and status can be changed, defaults are run2 (137/fb) and prelyminary. Can also change `rc.palette` on the fly. Figures are saved both in pdf and png. An example of the result can be found in the dedicated folder.


## Lecture 8

## profiling exercise
To test `cProfile` I took the script I had translated to numba in Lecture 7, slightly modifying the function (without numba!). I tried adding some dummy method for slowing down the scrip, e.g. a print, and checked the different outcome of the profiling. Everything was then displayed through snakeviz. Some screenshots are available in the dedicated README of Lecture 8.

## pytest
I choose to investigate the implementation of tests in a large-scale library, specifically focusing on `numpy` and `numpy.random`. A summary can be found in the dedicated readme of Lecture 8.
