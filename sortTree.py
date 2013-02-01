#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from pprint import pprint

def AddNode(tree, top, newid, newdata):
   """
   Tree is a py dict [-1, -1,newdata]
   [leftchild, rightchild, newdata]
   #leftchild: lower value
   #rightchild: higher value
   """
   # top is the ID of the first node
   # newid and newdata are the ID and data for new node
   k = top
   ok = 1

   # recursive adding nodes
   while ok:
      # go is to decide if the new node goes to the left or right
      # 0 is the left default
      go = 0   
      if newdata > tree[k][2]:
         go = 1 # 1 is the right

      # check if the child exists, if not
      if tree[k][go] == -1:
         tree[k][go] = newid
         tree[newid] = [-1, -1, newdata]
         ok = 0
      # if a child is exist
      else:
         k = tree[k][go]

def FindLefty(tree, top):
   """
   Find the smallest value (the most left parts of the tree)
   return the ID of the node with the smallest value and the parent's id
   """
   k, mom = top, -1
   ok = 1
   while ok:
      if tree[k][0] == -1:
         ok = 0
         return k, mom
      else:
         mom = k
         k = tree[k][0]

def RemoveNode(tree, loc, mom, top):

   rchild = tree[loc][1]
   if rchild != -1:
      if mom != -1:
         tree[mom][0] = tree[loc][1]
      else:
         top = tree[loc][1]
   elif mom != -1:
      tree[mom][0] = -1
   trash = tree.pop(loc)
   return top

if __name__ == "__main__":
   """
   Simulate the sorting tree algorithm
   """
   print "#Sorting tree (descending)#"
   data = np.random.rand(13)
   print "data:%s"%(data)
   tree = {}
   tree[0] = [-1,-1, data[0]]
   for i in range(1,13):
      AddNode(tree,0, i,data[i])
   print "Your tree (dict):" 
   pprint(tree)
   left_node = FindLefty(tree,0)[0]
   print "the most left node: %d" %left_node
   print "the lowest value: %.2f" %tree[left_node][2]

   print "sorted tree"
   top = 0
   while len(tree) > 0:
      me, mom = FindLefty(tree, top)
      print me, "%.2f" %tree[me][2]
      top = RemoveNode (tree, me,mom,top)
   print (tree)
