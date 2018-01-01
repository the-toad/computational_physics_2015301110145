# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:41:43 2017

@author: liumingyang
"""

import math
import random
import pylab as pl

def sweep(mic,T,H):
    E_flip = [[0]*10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            if i == 0:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i+10-1][j]+mic[i][j+10-1])+H*mic[i][j]
                if j == 9:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-10]+mic[i-1+10][j]+mic[i][j-1])+H*mic[i][j]
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1+10][j]+mic[i][j-1])+H*mic[i][j]
            elif  i == 9:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+10])+H*mic[i][j]
                if j == 9:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1-10]+mic[i-1][j]+mic[i][j-1])+H*mic[i][j]
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])+H*mic[i][j]
            elif j == 0 and  0 < i < 9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+10])+H*mic[i][j]
            elif j == 9 and 0 < i < 9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-10]+mic[i-1][j]+mic[i][j-1])+H*mic[i][j]
            elif 0 < i < 9 and 0 < j <9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])+H*mic[i][j]
            if E_flip[i][j] <=0:
                mic[i][j] = - mic[i][j]
            else:
                r = random.random()
                if r <= math.exp(-2*E_flip[i][j]/T):
                    mic[i][j] = -mic[i][j]
    return mic
def Mag(T,H):
    Sum = 0
    t=[]
    M=[]
    mic_new = [[-1]*10 for i in range(10)]
    for k in range(1001):
        t.append(k-1)
        Sum = 0
        for i in range(10):
            for j in range(10):
                Sum = Sum + mic_new[i][j]
        mic_new = sweep(mic_new,T,H)
        M.append(0.01*Sum)
    plot1 ,= pl.plot(t,M)
    pl.title('Magnezation vs time')
    pl.legend([plot1],['T='+str(T)+',H='+str(H)+' ini=-1'],loc = "best")
    pl.xlabel('time')
    pl.ylabel('Magnezation')
Mag(5,1)
