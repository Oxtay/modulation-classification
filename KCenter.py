import random
def KCenter(Data,K):
    # k-center clustering method
    # Written by: Okhtay Azarmanesh
    # Original: Mar 19, 2014
    # To use for initializing k-means clustering. By performing this before k-means clustering, the performance of k-means improves significantly as shown in my paper:
    
    # http://jwcn.eurasipjournals.com/content/2013/1/289
    
    # This performance is better than both k-means and k-means++ algorithms when initializing them randomly. The cost of performing this is also small compared to what it achieves as it scans the points in theta(N) time and this performance can also be improved.
    
    # This is a greedy approximation algorithm of metric k-center optimization problem and it achieves an approximation factor of 2 in k iterations.

    # randomly select an object as the initial point
    # To Do List
    #   Conversion of functions is not complete
    #   Try each function separately and make sure it works
    Init = ceil(random.uniform(1)*Data.shape[0])
    h = zeros(K,Data.shape[1])
    h[1,:] = Data[Init,:]

    rawdist = (Data-repmat(h(1,:),[Data.shape[0],1])).^2
    Euclid_dist = rawdist.sum(axis=1)
    cluster = ones((1,Data.shape[0]), Float)

    Euclid_dist1=Euclid_dist
    Hind=Init
    for i in range(2,K):
        Euclid_dist1(Hind) = -1
        D    = max(Euclid_dist1)
        ind  = (Euclid_dist == D).nonzero()
        Hind = [Hind,ind[1]]
        h(i,:) = Data[ind[1],:]
        newRawDist = (Data-repmat(h(i,:),[Data.shape[0],1])).^2
        Euclid_distnew = newRawDist.sum(axis=1)
        cluster((Euclid_distnew - dist < 0).nonzero())=i
        Euclid_dist((Euclid_distnew - dist < 0).nonzero) = Euclid_distnew((Euclid_distnew - dist < 0).nonzero)
        dist1=Euclid_dist
        
    return h


