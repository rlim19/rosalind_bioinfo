#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################
# do the permutation of gene order #
####################################

import itertools 
import sys

input_ = range(1, int(sys.argv[1])+1)
permlist_ = list(itertools.permutations(input_))

#output
sys.stdout.write(str(len(permlist_))+ '\n')
for i in permlist_:
  sys.stdout.write(' '.join(map(str,i)) + '\n')
