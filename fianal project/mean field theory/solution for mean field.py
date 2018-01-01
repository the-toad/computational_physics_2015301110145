# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:29:32 2017

@author: liumingyang
"""
import pylab as pl
import math
s=[]
s.append(0.5)
def root_solution(T):
    fuction = s[-1] -math.tanh(4*s[-1]/T)
    while 0.000001< fuction or fuction<-0.000001:
        fuction = s[-1] -math.tanh(4*s[-1]/T)
        diff_fuction = 1-4/(T*((math.cosh(4*s[-1]/T))**2))
        s.append(s[-1]-fuction/diff_fuction)
    else:
        return (s[-2])
T=[]
Mag=[]
T.append(0.2)
Mag.append(root_solution(T[-1]))
for i  in range(39):
    T.append(T[-1]+0.2)
    if Mag[-1] > 0:
        Mag.append(root_solution(T[-1]))        
    else:
        Mag.append(0)      
pl.xlabel('Temperature')
pl.ylabel('Magnetization')
pl.xlim(0.0,8.0)
pl.ylim(0.0,1.0)
plot1,= pl.plot(T,Mag,'k.')
plot2,=pl.plot(T,Mag,'k')
pl.title('Mean field theory')
