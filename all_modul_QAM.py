# Comparison of clustering with and without the use of k-Center clustering
# Written by: Okhtay Azarmanesh
# Penn State University

from KCenter import KCenter
import numpy as np
import scipy
import matplotlib

n = 256    # Number of samples
SNR = 5    # The amount of noise after passing from an AWGN channel

# Using K-center for initializing
for con in range(1,2):
    constel = 2*con
    K = 2^constel
    x = randintvec(n,K)        # Create a signal source for PSK.
    h = modem.qammod('M',K,'PhaseOffset',0,'SymbolOrder','binary')
    y = modulate(h,x)          # Modulate the signal x.
    y_chann = awgn(y,SNR)      # Output of AWGN channel
    g = modem.qamdemod(h)      
    # Create a demodulator object from a modem.qammod object
    # and display its properties.
    z = demodulate(g,y_chann)  # Demodulate the signal y_chann. 
    
    # The k-mean command should be performed on y_chann
    Data = [real(y_chann), imag(y_chann)]
    
    [cluster,u]=KCenter(Data,K)
    [IDX1, C1] = kmeans2(Data, K, 'Start', u)
    
# Using k observations at random
for con in range(1,2):
    constel = 2*con
    K = 2^constel
    x = randintvec(n,K)        # Create a signal source for PSK.
    h = modem.qammod('M',K,'PhaseOffset',0,'SymbolOrder','binary')
    y = modulate(h,x)          # Modulate the signal x.

    y_chann = awgn(y,SNR)      # Output of AWGN channel
    g = modem.qamdemod(h)      
    # Create a demodulator object from a modem.qammod object
    # and display its properties.
    z = demodulate(g,y_chann)  # Demodulate the signal y_chann. 


    # The k-mean command should be performed on y_chann
    Data = [real(y_chann), imag(y_chann)]

    [IDX1, C1] = kmeans2(Data, K, 'Start', 'uniform')

    