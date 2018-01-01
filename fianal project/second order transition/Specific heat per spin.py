# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:22:24 2017

@author: liumingyang
"""
import math
import random
import pylab as pl

def sweep(mic,T):
    E_flip = [[0]*10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            if i == 0:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i+10-1][j]+mic[i][j+10-1])
                if j == 9:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-10]+mic[i-1+10][j]+mic[i][j-1])
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1+10][j]+mic[i][j-1])
            elif  i == 9:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+10])
                if j == 9:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1-10]+mic[i-1][j]+mic[i][j-1])
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-10][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])
            elif j == 0 and  0 < i < 9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+10])
            elif j == 9 and 0 < i < 9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-10]+mic[i-1][j]+mic[i][j-1])
            elif 0 < i < 9 and 0 < j <9:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])
            if E_flip[i][j] <=0:
                mic[i][j] = - mic[i][j]
            else:
                r = random.random()
                if r <= math.exp(-2*E_flip[i][j]/T):
                    mic[i][j] = -mic[i][j]
    return mic
def Specific_heat(T):
    mic_old = [[1]*10 for i in range(10)]
    mic_new = mic_old
    Energy = 0
    Energy1 = 0
    for k in range(1000):
        E_total = [[0]*10 for i in range(10)]
        Sum = 0
        for i in range(10):
            for j in range(10):
                if i == 0:
                    if j == 0:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1]+mic_new[i+10-1][j]+mic_new[i][j+10-1])
                    if j == 9:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1-10]+mic_new[i-1+10][j]+mic_new[i][j-1])
                    else:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1]+mic_new[i-1+10][j]+mic_new[i][j-1])
                elif  i == 9:
                    if j == 0:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1-10][j]+mic_new[i][j+1]+mic_new[i-1][j]+mic_new[i][j-1+10])
                    if j == 9:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1-10][j]+mic_new[i][j+1-10]+mic_new[i-1][j]+mic_new[i][j-1])
                    else:
                        E_total[i][j] = -mic_new[i][j]*(mic_new[i+1-10][j]+mic_new[i][j+1]+mic_new[i-1][j]+mic_new[i][j-1])
                elif j == 0 and  0 < i < 9:
                    E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1]+mic_new[i-1][j]+mic_new[i][j-1+10])
                elif j == 9 and 0 < i < 9:
                    E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1-10]+mic_new[i-1][j]+mic_new[i][j-1])
                elif 0 < i < 9 and 0 < j <9:
                    E_total[i][j] = -mic_new[i][j]*(mic_new[i+1][j]+mic_new[i][j+1]+mic_new[i-1][j]+mic_new[i][j-1])
                Sum = Sum + E_total[i][j]
        Energy = Energy + 0.5*Sum
        Energy1 = Energy1 + (0.5*Sum)**2
        mic_new = sweep(mic_new,T)
    ave_E = 0.001 * Energy
    ave_E1 = 0.001 * Energy1
    spe_heat =0.01* (ave_E1-ave_E**2)/(T**2)
    return spe_heat
Tem = 0
array_T=[]
array_aveH = []
for i in range(50):
    Tem = Tem +0.1
    array_T.append(Tem)
    array_aveH.append(Specific_heat(Tem))
plot1,= pl.plot(array_T,array_aveH,'.')
pl.xlim(0,5)
pl.ylim(0.0,1.5)
pl.xlabel('Temperature')
pl.ylabel('Specific heat per spin')
pl.title('Ising model ')
pl.legend([plot1],['10*10 lattice'],loc = "best")
pl.show()
