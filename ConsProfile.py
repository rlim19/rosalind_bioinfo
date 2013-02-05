#!/usr/bin/env python
# -*- coding:utf-8 -*-

##########################################
# find the consensus and build a profile #
##########################################

#code learnt from jdp, many thanks!

from collections import Counter
import sys

#get the dataset
with open(sys.argv[1], 'r') as f:
  dna_strings = [line.strip() for line in f]

#find the consensus
counts = map(Counter, zip(*dna_strings))
consensus = [base.most_common(1)[0][0]for base in counts]
print ''.join(consensus)

#build the profile
bases = ('A','T','G','C')
#build a dict profile
profile = dict((base, [c.get(base,0) for c in counts])for base in bases)
for base in bases:
  print "%s: %s" % (base, ' '.join(map(str,profile[base])))
