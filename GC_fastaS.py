#!/usr/bin/env python
# -*-: coding utf-8 -*-
from __future__ import division
import sys
import operator

def read_fasta(fp):
  """
  read fasta file
  """
  name, seq = None, []
  for line in fp:
    line = line.rstrip()
    if line.startswith(">"):
      if name: yield(name, ''.join(seq))
      name, seq = line, []
    else:
      seq.append(line)
  if name: yield(name, ''.join(seq))

#store gc content for each fasta file
dict_gc = {}
with open(sys.argv[1]) as f:
  for name, seq in read_fasta(f):
    perc_gc = 100 * (seq.count("G") + seq.count("C"))/ len(seq)  
    dict_gc[name.strip('>')] = perc_gc

#sort the dict_gc based on the percentage of gc and show only the top three
sorted_dict_gc = dict(sorted(dict_gc.iteritems(), 
    key = operator.itemgetter(1), reverse= True)[:3])
for key in sorted_dict_gc:
  print ("%s\n%s"%(key, sorted_dict_gc[key]))
