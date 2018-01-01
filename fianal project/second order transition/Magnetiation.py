# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:42:34 2017

@author: liumingyang
"""

import random
import matplotlib.pyplot as pl
import math
#calculation
def update_mic(T):
    mic = [[1]*10 for i in range(10)]  #Initialize all microstates
    E_flip = [[0]*10 for i in range(10)]
    
    t = []
    Mag=[]
    Mag.append(1)
    t.append(0)
    for k in range(1001):
        Sum = 0
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
                Sum = Sum +mic[i][j]
        Mag.append(0.01*Sum)
        t.append(t[-1]+1)
    plot1 ,= pl.plot(t,Mag,'c')
    pl.title('Ising model Magnetization vs. time')
    pl.xlim(0,1000)
    pl.ylim(-1.2,1.2)
    pl.xlabel('time')
    pl.ylabel('Magnetization')
    pl.legend([plot1],['T=4.0'],loc ="best")
update_mic(4.0)