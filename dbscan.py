def DBSCAN(D, eps, MinPts):
   C = 0
   for each unvisited point P in dataset D
      mark P as visited
      NeighborPts = regionQuery(P, eps)
      if sizeof(NeighborPts) < MinPts
         mark P as NOISE
      else
         C = next cluster
         expandCluster(P, NeighborPts, C, eps, MinPts)
          
def expandCluster(P, NeighborPts, C, eps, MinPts):
   add P to cluster C
   for each point poi in NeighborPts 
      if poi is not visited
         mark p as visited
         NeighborPts = regionQuery(poi, eps)
         if sizeof(NeighborPts) >= MinPts
            NeighborPts = NeighborPts joined with NeighborPts
      if poi is not yet member of any cluster
         add poi to cluster C
          
def regionQuery(P, eps):
   return all points within P's eps-neighborhood (including P)