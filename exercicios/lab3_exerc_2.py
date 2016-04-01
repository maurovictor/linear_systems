# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:10:24 2016

@author: mauro
"""

import linear_system

time_base = arange(-5,6)
deg = degrau(time_base)

exp = (5.**(-1*time_base))

sinal1 = exp*deg

conv = convolucao(sinal1,deg)


subplot(3,1,1)
stem(time_base, exp*deg)

subplot(3,1,2)
stem(time_base, deg)

subplot(3,1,3)
stem(conv[0], conv[1])

show()