#!/usr/bin/env python


# Comparison of clustering with and without the use of k-Center clustering
# Written by: Okhtay Azarmanesh
# Penn State University

from KCenter import KCenter
from pylab import plot,show
import numpy as np
from scipy.cluster.vq import kmeans,vq
import matplotlib
import csv

n   = 256  # Number of samples
SNR = 5    # The amount of noise after passing from an AWGN channel
K   = 16   # Testing 16-QAM as an example

# load data
data = numpy.loadtxt(open("signal_16QAM.csv","rb"),delimiter=",")

# Using K-center for initializing
##################
#
#    Modulator
#
##################
 
# The k-mean command should be performed on y_chann
data = [real(y_chann), imag(y_chann)]   
u = KCenter(data,K)
centroids, idx = kmeans2(data, K, iter = 10, 'Start', u)

# some plotting using numpy's logical indexing
# plot(data[idx==0,0],data[idx==0,1],'ob', data[idx==1,0],data[idx==1,1],'or')
# plot(centroids[:,0],centroids[:,1],'sg',markersize=8)

# Using k observations at random
##################
#
#    Modulator
#
##################

data = [real(y_chann), imag(y_chann)]
u = KCenter(data,K)
centroids, idx = kmeans2(data, K, iter = 10, 'Start', 'uniform')

# some plotting using numpy's logical indexing
# plot(data[idx==0,0],data[idx==0,1],'ob', data[idx==1,0],data[idx==1,1],'or')
# plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
