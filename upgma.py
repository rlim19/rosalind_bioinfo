#!/usr/bin/env python
# -*- coding:utf-8 -*-

################################################################################################
# Each pair of data(vector) are compared and scored                                            #
# Those with the best scores (min abs.substraction)                                            #
# indicating better similarity are clustered to form a new tree or to join an existing tree    #
################################################################################################

# code from Jason Kinser

import copy
import numpy
from numpy import random,zeros

def UPGMA ( indata ):
   """
   generate UPGMA tree (greedy tree) given the input of list of vector data
   """
   # data is a list of vectors
   data = copy.deepcopy ( indata )
   N = len (data)
   N2 = 2*N - 1
   BIG = 999999
   # scmat: matrix containing the pairwise scores
   scmat = zeros( (N2,N2), float ) + BIG

   for i in range( N ):
      for j in range( i ):
         # pairwise scores based on simple abs substraction
         scmat[i,j] = (abs( data[i]-data[j] )).sum()

   # construct tree as dictionary and collect the used node in a list
   # {3: (2, 0, 2.0), 4: (3, 1, 4.0)}
   # key: node 
   # value: 2,0,2.0 (left-child, right-child, pairwise score)
   tree, used = {}, []
   for i in range(N-1):
      # the location of the scmat with min abs.substraction value in this case
      v,h = divmod( scmat.argmin(), N2 )
      tree[N+i] = (v,h, scmat.min())
      used.append(v)
      used.append(h)
      avg = (data[v] + data[h])/2.
      data.append(avg)
      for j in range(N+i):
         if j not in used:
            scmat[N+i, j] = (abs(avg-data[j])).sum()
      # eliminate all the rows and columns that are associated with v,h
      scmat[v] = zeros(N2) + BIG # eliminate row
      scmat[h] = zeros(N2) + BIG
      scmat[:,v] = zeros(N2) + BIG # eliminate column
      scmat[:,h] = zeros(N2) + BIG
   return tree

if __name__ == "__main__":
   data = [numpy.array([1,1,2]),numpy.array([2,2,3]), numpy.array([1,1,0])]
   net_tree = UPGMA(data)
   print net_tree
