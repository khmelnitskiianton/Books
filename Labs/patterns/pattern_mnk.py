# -*- coding: utf-8 -*-
"""pattern_mnk.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mRZFsrhzCPJn0ed7aCUUDjHEobBfty9s
"""

from math import *

x = []
y = []

file = open('data_1.txt', 'r')
while (line := file.readline()):
  s = line.split()
  if (len(s) != 0):
    x.append(float(s[0].replace(',','.')))
    y.append(float(s[1].replace(',','.'))/1000)

amount = len(x)

x.sort()
y.sort()

summ_xy = 0
summ_x = 0
summ_y = 0
summ_x2 = 0
summ_y2 = 0

for i in range(amount):
  summ_xy += x[i]*y[i]
  summ_x += x[i]
  summ_y += y[i]
  summ_x2 += x[i]**2
  summ_y2 += y[i]**2

k = (summ_xy/amount - summ_x/amount*summ_y/amount)/(summ_x2/amount - (summ_x/amount)**2)

sigma_k = 1/(sqrt(amount))*sqrt(((summ_y2/amount - (summ_y/amount)**2)/(summ_x2/amount - (summ_x/amount)**2))-k**2)

b = summ_y/amount - k*(summ_x/amount)

sigma_b = sigma_k * sqrt(summ_x2/amount)

print("k = ",k)
print("\sigma_k = ", sigma_k)
print("b = ", b)
print("\sigma_b = ", sigma_b)