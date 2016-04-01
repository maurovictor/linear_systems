# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:12:59 2016

@author: mauro
"""

import linear_system

n = arange(-15,16)
x = 2*degrau(n,1,2)-2*degrau(n,1,-12)
h = 0.9**(n)*(degrau(n,1,-2)-degrau(n,1,-13))

conv = convolucao(x,h)

subplot(3,1,1)
stem(n,x)
subplot(3,1,2)
stem(n,h)
subplot(3,1,3)
stem(conv[0],conv[1])

show()