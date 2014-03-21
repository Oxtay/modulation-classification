# Modulation Classification
## A novel method based on my dissertation

Orignally written in MATLAB
Now, importing to Python

There are two parts to the single-carrier modulation algorithm. k-means clustering takes care of the main task, while k-center clustering improves the performance of k-means.

Together, these two compile the input signal which is an array of complex numbers and maps them onto an Inphase-Quadrature diagram. On this I-Q diagram, the cluster centers are determined and then the results are passed to another code which decides what is the modulation type of our input signal. 

The modulation types that are considered are any M-ary QAM and M-ary PSK modulations, which cover most of today's popular modulations.


## k-center greedy algorithm
This function is used to for initializing `k-means` clustering. By performing this before `k-means` clustering, the performance of `k-means` improves significantly as shown in my paper:
    
[I-Q diagram utilization in a novel modulation classification technique for cognitive radio applications](http://jwcn.eurasipjournals.com/content/2013/1/289)
    
This performance is better than both `k-means` and `k-means++` algorithms when initializing them randomly. The cost of performing this is also small compared to what it achieves as it scans the points in theta(N) time and this performance can also be improved.
    
This is a greedy approximation algorithm of metric `k-center optimization problem` and it achieves an approximation factor of 2 in k iterations.

The greedy algorithm works as follows:

- Choose the ﬁrst center arbitrarily
- At every step, choose the vertex that is furthest from the
current centers to become a center
- Continue until k centers are chosen