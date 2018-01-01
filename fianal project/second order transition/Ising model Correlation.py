# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:17:32 2017

@author: liumingyang
"""

import math
import random
import pylab as pl
def sweep(mic,T):
    E_flip = [[0]*20 for i in range(20)]
    for i in range(20):
        for j in range(20):
            if i == 0:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i+20-1][j]+mic[i][j+20-1])
                elif j == 19:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-20]+mic[i-1+20][j]+mic[i][j-1])
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1+20][j]+mic[i][j-1])
            if  i == 19:
                if j == 0:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-20][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+20])
                elif j == 19:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-20][j]+mic[i][j+1-20]+mic[i-1][j]+mic[i][j-1])
                else:
                    E_flip[i][j] = mic[i][j]*(mic[i+1-20][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])
            if j == 0 and  0 < i < 19:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1+20])
            if j == 9 and 0 < i < 19:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1-20]+mic[i-1][j]+mic[i][j-1])
            if 0 < i < 19 and 0 < j < 19:
                E_flip[i][j] = mic[i][j]*(mic[i+1][j]+mic[i][j+1]+mic[i-1][j]+mic[i][j-1])
            if E_flip[i][j] <=0:
                mic[i][j] = - mic[i][j]
            else:
                r = random.random()
                if r <= math.exp(-2*E_flip[i][j]/T):
                    mic[i][j] = -mic[i][j]
    return mic
def correlation(T,dis):
    mic_new = [[1]*20 for i in range(20)]
    total_f = 0
    for k in range(10000):
        total_f_i = 0
        for i in range(20):
            for j in range(20):
                if i + dis >19:
                    if j + dis >19:
                        f_i = mic_new[i][j]*(mic_new[i+dis-20][j] + mic_new[i-dis][j]+mic_new[i][j+dis-20]+mic_new[i][j-dis])
                    elif j - dis < 0:
                        f_i = mic_new[i][j]*(mic_new[i+dis-20][j] + mic_new[i-dis][j]+mic_new[i][j+dis]+mic_new[i][j-dis+20])                    
                    else:
                        f_i = mic_new[i][j]*(mic_new[i+dis-20][j] + mic_new[i-dis][j]+mic_new[i][j+dis]+mic_new[i][j-dis])
                elif i - dis< 0:
                    if j + dis >19:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis+20][j]+mic_new[i][j+dis-20]+mic_new[i][j-dis])
                    elif j - dis < 0:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis+20][j]+mic_new[i][j+dis]+mic_new[i][j-dis+20])                    
                    else:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis+20][j]+mic_new[i][j+dis]+mic_new[i][j-dis])
                else:
                    if j + dis >19:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis][j]+mic_new[i][j+dis-20]+mic_new[i][j-dis])
                    elif j - dis < 0:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis][j]+mic_new[i][j+dis]+mic_new[i][j-dis+20])                    
                    else:
                        f_i = mic_new[i][j]*(mic_new[i+dis][j] + mic_new[i-dis][j]+mic_new[i][j+dis]+mic_new[i][j-dis])
                total_f_i = total_f_i +0.25*f_i
        total_f = total_f + (1/400)*total_f_i
        mic_new = sweep(mic_new,T)
    corre = 0.0001 * total_f
    return corre
array_f1 = []
array_f2 = []
array_f3 = []
array_f4 = []
array_f5 = []
distance = []
array_f6 = []
for i in range(10):
    distance.append(i+1)
    array_f1.append(correlation(0.5,distance[-1]))
    array_f2.append(correlation(1.5,distance[-1]))
    array_f3.append(correlation(2,distance[-1]))
    array_f4.append(correlation(2.25,distance[-1]))
    array_f5.append(correlation(3,distance[-1]))
    array_f6.append(correlation(5,distance[-1]))
plot01,=pl.plot(distance,array_f1,'k.')
plot1 ,= pl.plot(distance,array_f1,'k')
plot02,=pl.plot(distance,array_f2,'b.')
plot2 ,= pl.plot(distance,array_f2,'b')
plot02,=pl.plot(distance,array_f2,'g.')
plot2 ,= pl.plot(distance,array_f2,'g')
plot03,=pl.plot(distance,array_f3,'m.')
plot3 ,= pl.plot(distance,array_f3,'m')
plot04,=pl.plot(distance,array_f4,'c.')
plot4 ,= pl.plot(distance,array_f4,'c')
plot05,=pl.plot(distance,array_f5,'r.')
plot5 ,= pl.plot(distance,array_f5,'r')
plot06,=pl.plot(distance,array_f6,'y.')
plot6 ,= pl.plot(distance,array_f6,'y')
pl.legend([plot1,plot2,plot3,plot4,plot5,plot6],['T=0.5','T=1.5','T=2','T=2.25','T=3','T=5'],loc="best")
pl.ylim(-0.1,1)
pl.xlim(0,10)
pl.xlabel('i = distance')
pl.ylabel('f(i)=<s_is_0>')