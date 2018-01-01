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
    mic_new = [[-1]*10 for i in range(10)]
    for k in range(1000):
        mic_new = sweep(mic_new,T,H)
        for i in range(10):
            for j in range(10):
                Sum = Sum + mic_new[i][j]
    Magnetization = 0.01 * 0.001 * Sum
    return Magnetization
H1=[]
M1=[]
H2=[]
M2=[]
for i in range(101):
    H1.append(-10 + 0.2 * i)
    M1.append( Mag(0.5,H1[-1]))
for j in range(101):
    H2.append(10-0.2 * j)
    M2.append((Mag(0.5,H2[-1])))
plot1 ,= pl.plot(H1,M1)
plot2 ,= pl.plot(H2,M2)
pl.xlabel('H')
pl.ylabel('Magnetization')
pl.xlim(-10,10)
pl.ylim(-1.1,1.1)
pl.legend([plot1,plot2],['from negetive','from positive'],loc ="best" )
pl.title('Ising model Monte Carlo,T = 0.5')
pl.show()
    