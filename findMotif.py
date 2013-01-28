#!/usr/bin/env python
# -*- coding:utf-8 -*-
#problems: http://rosalind.info/problems/subs/

import sys
import re

substring = sys.argv[1]
string = sys.argv[2]
# overlapping (look ahead match)
r_gex = r"(?=" + re.escape(substring) + ")"

motif_pyInd = [motif.start() for motif in re.finditer(r_gex,sys.argv[2])]
motif_ind = [motif + 1 for motif in motif_pyInd]
print ' '.join(str(x) for x in motif_ind)
