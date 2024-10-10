# Profiling Exercise
As a basis, I used the script of lecture 7 (with some modification) that computes jet pulls given a set of Vector Boson Fusion events at LHC. I used only few events, as I was mainly interested in running several tests in little time.

First, I tried profiling the script as it was:
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/91e98e491f16d839da77c1f37a74a5f546f34764/Lecture8/profiling_exercise/snakeviz_nosleep.jpg)

I then tried some methods to slow down the function in some places, as for example adding sleeps. The result was the following!
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/91e98e491f16d839da77c1f37a74a5f546f34764/Lecture8/profiling_exercise/snakeviz_sleep.jpg)

I also discovered one can profile an 'entire script' via `python -m cProfile -o example.prof mypythonscript.py --args`! This makes it even more easy to use, now testing my scripts for work!
