#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.daimi.au.dk/~mailund/suffix_tree.html
from suffix_tree import GeneralisedSuffixTree
import gc
import sys

#This link is for substringDIC!
#https://hkn.eecs.berkeley.edu/~dyoo/python/suffix_trees/


#input the list of the strings
#import pdb; pdb.set_trace()
list_string = []
with open(sys.argv[1], 'r') as f:
   for line in f:
      line = line.rstrip()
      list_string.append(line)

#build the tree 
list_string = open(sys.argv[1]).read()
stree = GeneralisedSuffixTree(list_string.split())

for shared in stree.sharedSubstrings(2):
    for seq,start,stop in shared:
        print stree.sequences[seq][start:stop],
        print stree.sequences[seq][:start]+'|'+stree.sequences[seq][start:stop]+\
              '|'+stree.sequences[seq][stop:]
