#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def compare_strands(str1, str2):
  """
  find the number of differences between two strings
  """
  if len(str1) != len(str2):
    return
  count = 0
  for i,c in enumerate (str1):
    if not c == str2[i]:
      count += 1
  return count

if __name__ == "__main__":
  humm_d = compare_strands(sys.argv[1], sys.argv[2])
  print humm_d

