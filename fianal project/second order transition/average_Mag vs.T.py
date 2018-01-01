# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:47:29 2017

@author: liumingyang
"""

import random
import matplotlib.pyplot as pl
import math
import numpy as np
#calculation
def update_mic(T):
    mic = [[1]*10 for i in range(10)]  #Initialize all microstates
    E_flip = [[0]*10 for i in range(10)]
    
    t = []
    Mag=[]
    Mag.append(1)
    t.append(0)
    total = 1
    for k in range(1000):
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
        total = total +Mag[-1]
    aver_Mag = (1/1001)*total
    return aver_Mag
array_T=[]
Tem = 1
average_Mag = []
for i in range(41):
    array_T.append(Tem)
    average_Mag.append(update_mic(Tem))
    Tem = Tem +0.1
x_1=np.arange(0,5,0.01)
y_1=[0]*500
plot1 ,= pl.plot(array_T,average_Mag,'k.')
plot2 ,= pl.plot(x_1,y_1,'k--')
pl.xlabel('Temperature')
pl.ylabel('Magnetization')
pl.xlim(0,5.0)
pl.ylim(-0.2,1)
pl.title('Ising model Monte Carlo')
pl.legend([plot1],['10*10 lattice'],loc = "best") 
pl.show()   