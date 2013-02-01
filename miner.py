#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def Hoover (txt):
   """
   cleaning up the text string
   input: *.txt 
   """
   work = txt.lower()
   work = work.replace ('\n', ' ')
   #ASCII, 32: 'space'; 97-122: 'a-z'
   valid = [32] + range (97,123)
   #check characters based on ASCII code
   for i in range (256):
      if i not in valid:
         # convert integer into a character
         work = work.replace(chr(i), "")
   return work

if __name__ == "__main__":
   with open(sys.argv[1]) as f:
      txt_f = f.read()
      clean_txt = Hoover(txt_f)
      sys.stdout.write(clean_txt)


         
