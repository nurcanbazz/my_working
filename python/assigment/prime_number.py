# -*- coding: utf-8 -*-
"""Prime_Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHBF_DTlhVIR2GeukGb31gZHozH4hvxr

#1 ile 100 arasındaki asal sayıları yazdıran python kodu.
"""

prime_number = []
for i in range(1,101):
    for prime in range(2,i):
        if i % prime == 0:
          break
        elif (prime == i-1) and (i % prime !=0) :
            prime_number.append(i)
print(prime_number)