# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:05:04 2016

@author: mauro
"""

import linear_system

n = arange(-5,26)
values = array([1.,3.,5.,7.,9.,7.,5.,3.,1.])
h = zeros(len(n))
for i in range(1,10):
    h[i] = values[i-1]

x = 5 * cos(0.2*pi*n)
conv = convolucao2(x,h,-5)

subplot(3,1,1)
stem(n,x)
subplot(3,1,2)
stem(n,h)
subplot(3,1,3)
stem(conv[0],conv[1])
