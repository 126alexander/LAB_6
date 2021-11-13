#!/usr/bin/env python3
# -*- coding: utf-8 -*-

word = input()
a = word.find('а')
o = word.rfind('о')
if a != -1 and o != -1:
    tmp = list(word)
    tmp[a], tmp[o] = tmp[o], tmp[a]
    word = ''.join(tmp)
print(word)
