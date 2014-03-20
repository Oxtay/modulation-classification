# Modulation Classification
## A novel method based on my dissertation

Orignally written in MATLAB
Now, importing to Python

There are two parts to the single-carrier modulation algorithm. k-means clustering takes care of the main task, while k-center clustering improves the performance of k-means.

Together, these two compile the input signal which is an array of complex numbers and maps them onto an Inphase-Quadrature diagram. On this I-Q diagram, the cluster centers are determined and then the results are passed to another code which decides what is the modulation type of our input signal. 

The modulation types that are considered are any M-ary QAM and M-ary PSK modulations, which cover most of today's popular modulations.
