# Scientific Computing with Python
Exam - Giulia Lavizzari (ay 2023/2024)


## Lecture 1 - python interface to Oracle DB
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

### Other
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
