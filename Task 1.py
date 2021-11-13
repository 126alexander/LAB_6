#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
  a = input('Введите речь ')
  n = 0

  for i in range(1, len(a) - 1):
   if a[i] == a[i+1]:
        n += 1

  print(f' n = {n}')