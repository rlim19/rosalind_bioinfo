#!/usr/bin/env python
# -*- coding:utf-8 -*-


#tree = [listofkidletters, listofkidIds, letter, endFlag]

def AddWord(tree, word):
   treeloc = 0
   wi = 0 # word's location
   NW = len(word)
   ok = 1
   while ok:
      # if the letter is already in the tree
      if word[wi] in tree[treeloc][0]:
         # if it is the last letter of the word
         if wi == NW -1:
            ndx = tree[treeloc][0].index(word[wi])
            treeloc = tree[treeloc][1][ndx]
            tree[treeloc][3] = True
            ok = 0
         else:
            # move down the tree
            ndx = tree[treeloc][0].index(word[wi])
            treeloc = tree[treeloc][1][ndx]
            wi += 1
      else:
         # the rest of the word is not in the tree
         TL = len(tree)
         last = TL
         tree[treeloc][0].append(word[wi])
         tree[treeloc][1].append(TL)
         for i in range(wi, NW-1):
            newnode = [ [word[i+1]], [last+1], word[i], False]
            tree.append(newnode)
            last += 1
         # last letter
         TL = len(tree)
         newnode = [ [], [], word[-1], True ]
         tree.append(newnode)
         ok = 0



