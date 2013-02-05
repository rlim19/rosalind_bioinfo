#!/usr/bin/env python
# -*- coding:utf-8 -*-
#problems: http://rosalind.info/problems/subs/
#implementation of Rabin-Karp algorithm , http://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

import sys

def substr_in_all(arr, part):
   for dna in arr:
      if part not in dna:
         return False
   return True

def common_substr(arr, l):
   first = arr[0]
   for i in range(len(first)-l+1):
      part = first[i:i+l]
      if substr_in_all(arr, part):
         return part
   return ""

def longest_common_substr(arr):
   """
   solved with divide and conquer method by Petar Ivanov
   """
   l = 0; r = len(arr[0])
   while l+1<r:
		mid = (l+r) / 2
		if common_substr(arr, mid)!="":
			l=mid
		else:
			r=mid
   return common_substr(arr, l)

if __name__ == "__main__":
   f_ = open(sys.argv[1]).read().strip().split()
   l_str = longest_common_substr(f_)
   print l_str
