# Profiling Exercise
As a basis, I used the script of lecture 7 (with some modification) that computes jet pulls given a set of Vector Boson Fusion events at LHC. I used only few events, as I was mainly interested in running several tests in little time.

First, I tried profiling the script as it was:
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/91e98e491f16d839da77c1f37a74a5f546f34764/Lecture8/profiling_exercise/snakeviz_nosleep.jpg)

I then tried some methods to slow down the function in some places, as for example adding sleeps. The result was the following!
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/91e98e491f16d839da77c1f37a74a5f546f34764/Lecture8/profiling_exercise/snakeviz_sleep.jpg)

I also discovered one can profile an 'entire script' via `python -m cProfile -o example.prof mypythonscript.py --args`! This makes it even more easy to use, now testing my scripts for work!

# pytest

### A quick summary on `numpy.random` tests (and why I chose this module)
For this exercise, I choose to study the implementation of testing methodologies in large-scale libraries, focusing in particular on `numpy`. Specifically I investigated the `numpy.random` module, which I often use in my work. The choice of this module was also influenced by my (little, in truth) prior experience developing random number generators, which I acquired during basic computing and statistics courses. In these contexts, we were asked to implement simple methods such as the linear congruential generator, and to test and study their performance. This gave me a slightly deeper insight into some potential issues and limitations inherent to random generation.


The `numpy.random` includes first of all tests for verifying the basic statistical properties of generated distributions and tests for corner cases and parameter validation. Each implemented distribution has dedicated tests to confirm the expected behavior across a range of inputs, including corner or problematic values.

Furthermore, the module implements performance and scalability tests to ensure that the random number generators produce stable results even with large-scale data. This need for scalability was one of the issues we faced when using simpler methods, where issues such as pattern emergence in large outputs appeared easily (in those cases, I typically only plotted distribution to check for issues, rather than building formal tests).

Finally, they employ regression tests to check that results are consistent across updates.


Numpy.random employs, besides pytest, also a numpy module specific for testing support, namely `numpy.testing` ([link](https://numpy.org/devdocs/reference/routines.testing.html)), which implements a set of basic utilities used across all numpy to test methods.

 
