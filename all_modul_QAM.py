#!/usr/bin/env python


# Comparison of clustering with and without the use of k-Center clustering
# Written by: Okhtay Azarmanesh
# Penn State University

from KCenter import KCenter
import numpy as np
import scipy
import matplotlib
import csv

n   = 256  # Number of samples
SNR = 5    # The amount of noise after passing from an AWGN channel
K   = 16   # Testing 16-QAM as an example
# Using K-center for initializing
##################
#
#    Modulator
#
##################
 
# The k-mean command should be performed on y_chann
Data        = [real(y_chann), imag(y_chann)]   
[cluster,u] = KCenter(Data,K)
[IDX1, C1]  = kmeans2(Data, K, 'Start', u)
  
# Using k observations at random
##################
#
#    Modulator
#
##################

Data        = [real(y_chann), imag(y_chann)]
[cluster,u] = KCenter(Data,K)
[IDX1, C1]  = kmeans2(Data, K, 'Start', 'uniform')

    