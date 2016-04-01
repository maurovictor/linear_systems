# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:39:20 2016

@author: mauro
"""

def degrau(time_base,ampl=1,desloc=0):
    y = (time_base >= -desloc)*ampl
    return(y)

#Observação: o tamanho do vetor resultante da convolução é menor que o tamnho da soma dos vetores convoluídos em uma unidade
#Função para convoluir 2 sianis e retornar o sinal juntamente com a base de tempo
def convolucao(sinal1, sinal2):
    conv = convolve(sinal1, sinal2)
    n1 = arange(-(len(conv)//2),(len(conv)//2)+1)
    return [n1, conv]
    

def convolucao2(sinal1, sinal2, start=0):
    conv = convolve(sinal1, sinal2)
    start_mod = -1*start if start < 0 else start
    n1 = arange(start,len(conv)-start_mod) #cria a base temporal de acordo com o começo
    return [n1, conv]