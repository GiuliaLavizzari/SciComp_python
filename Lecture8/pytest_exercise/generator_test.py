import pytest
from numpy.random.tests.test_random import TestBinomial
from numpy.random import binomial

# ------------------------------------------------
# ------------ this is the numpy test ------------
#class TestBinomial:
#    def test_n_zero(self):
#        # Tests the corner case of n == 0 for the binomial distribution.
#        # binomial(0, p) should be zero for any p in [0, 1].
#        # This test addresses issue #3480.
#        zeros = np.zeros(2, dtype='int')
#        for p in [0, .5, 1]:
#            assert_(random.binomial(0, p) == 0)
#            assert_array_equal(random.binomial(zeros, p), zeros)
#
#    def test_p_is_nan(self):
#        # Issue #4571.
#        assert_raises(ValueError, random.binomial, 1, np.nan)

def run_binomial_test():
    test_case = TestBinomial()
    
    # Call specific binomial tests
    test_case.test_n_zero()  # Test for n == 0
    test_case.test_p_is_nan()  # Test for p being NaN

#if __name__ == "__main__":
#    run_binomial_test()
#
#    print (binomial(14, 0.4, size = 100))












#!/usr/bin/python
'''
generazione di numeri pseudo-casuali distribuiti secondo una distribuzione arbitraria
con il metodo try-and-catch fra xMin ed xMax
a partire da un determinato seed e disegno della distribuzione,
separando la generazione dal programma principale
python3 random_08.py 0. 10 2. 20000 2.4
'''

import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor

from myrand import *

def main () :
    '''
    Funzione che implementa il programma principale
    '''


    xMin = 0.  #float (sys.argv[1])  # minimum of the histogram drawing range
    xMax = 10. #float (sys.argv[2])  # maximum of the histogram drawing range
    yMax = 1.2 #float (sys.argv[3])  # maximum of the histogram drawing range    
    seed = 14  #float (sys.argv[5])
    N    = int (10000)

    print (' -------- ')
    print (' minimum : ', xMin)
    print (' maximum : ', xMax)
    print (' seed    : ', seed)
    print (' N       : ', N)
    print (' -------- ')

    randlist = generate_TAC (func, xMin, xMax, yMax, N, seed)

    # plotting of the generated list of numbers in a histogram

    nBins = floor (len (randlist) / 400.)             # number of bins of the hitogram
    bin_edges = np.linspace (xMin, xMax, nBins + 1)  # edges o the histogram bins

    # disegno della funzione
    fig, ax = plt.subplots ()
    ax.set_title ('Histogram of random numbers', size=14)
    ax.set_xlabel ('random value')
    ax.set_ylabel ('events in bin')
    ax.hist (randlist,      # list of numbers
             bins = bin_edges,
             color = 'orange',
             # normed = True,
            )

    plt.show ()


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == "__main__":
    main ()
