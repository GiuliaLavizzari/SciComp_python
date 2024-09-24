# SciComp_python
Exam - Scientific Computing in python


## Lecture 1 - python interface to Oracle DB
The exercise contains a class ([DbInterface](https://github.com/GiuliaLavizzari/SciComp_python/blob/09459dc00b621f894b7a7fcb1f8f6fb99c8d673b/Lecture1/DbInterface.py)), which allows to interact with an oracle DB built for the CMS electromagnetic calorimeter (ECAL) upgrade for the High-Luminosity phase of the LHC.
It also contains a set of [utilities](https://github.com/GiuliaLavizzari/SciComp_python/tree/09459dc00b621f894b7a7fcb1f8f6fb99c8d673b/Lecture1/scripts) for quick operations on the db, such as printing or deleting tables.

The original code is hosted on CERN gitlab ([pyoracle](https://gitlab.cern.ch/ecal-daq-upgrade/pyoracle)).

**A DEMO can be found [here](https://drive.google.com/file/d/1M7lp7QczL5PBuhEJal0w_ra4H_J0Agxl/view?usp=sharing)**

## Lecture 2

### Game Of Life
The first exercise here contained is the game of life. It can be run in normal mode (random generation of starting point), or specifying `--spaceShip`. The latter will provide an animation of a spaceship, crossing the grid from the top left to the bottom right.

### Secret Santa
The second exercise here in lecture 2 is a very very simple script that shuffles a set of names in order to assign to each person his/her secret santa, and then sends an email to everyone wit the correct info. Note that the script works for a gmail server and it's necessary to allow the "Less Secure App access" in the settings of the account.
It was developed for a group of friends that live far from each other and thus cannot pick names written on paper (as normally one would to). Worked!!
