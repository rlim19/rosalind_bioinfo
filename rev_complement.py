#!/usr/bin/env python
# -*-: coding utf=8 -*-
import sys

def rev_complement(seq):
  """
  get the reverse complement DNA seq
  """
  compl_dict = {'A':'T', 'T':'A', 'G':'C', 'C': 'G'}
  rev_seq = seq[::-1]
  compl_rev_seq = [compl_dict[base] for base in rev_seq]
  print ''.join(compl_rev_seq)

if __name__ == "__main__":
  rev_complement(sys.argv[1])
