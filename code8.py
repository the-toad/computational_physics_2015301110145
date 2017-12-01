```
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:45:35 2017

@author: liumingyang
"""
import math
import pylab as pl
class Precession:
    def rotation(self,ini_x,ini_y,ini_vx,ini_vy,alpha):
        x = [0 for i in range(0,20000)]
        y = [0 for i in range(0,20000)]
        vx = [0 for i in range(0,20000)]
        vy = [0 for i in range(0,20000)]
        radius = [0 for i in range(0,19999)] 
        x[0] = ini_x
        y[0] = ini_y
        vx[0] = ini_vx
        vy[0] = ini_vy
        spe_x=[]
        spe_y=[]
        angle=[]
        spe_t=[]
        t=[]
        det_t = 0.0001
        for i in range(19999):
            radius[i] = (x[i]**2+y[i]**2)**(1/2)
            vx[i+1] = vx[i]-4*(math.pi)**2*x[i]*det_t*(1+alpha/(radius[i]**2))/(radius[i])**3
            vy[i+1] = vy[i]-4*(math.pi)**2*y[i]*det_t*(1+alpha/(radius[i]**1))/(radius[i])**3
            x[i+1] = x[i]+vx[i+1]*det_t
            y[i+1] = y[i]+vy[i+1]*det_t
            t.append(det_t*i)
        for i in range(1,19998):
            if radius[i-1]<radius[i]:
                if radius[i+1]<radius[i]:
                    spe_x.append(x[i])
                    spe_y.append(y[i])
                    angle.append(180*math.atan(y[i]/x[i])/math.pi)
                    spe_t.append(t[i])
        import numpy as np
        from scipy.optimize import leastsq
        def fun(p,l):
            k,b = p
            return k*l+b
        def err(p,l,m):
            return fun(p,l) - m
        p0 = [1,1]
        l1=np.array(spe_t)
        m1=np.array(angle)
        para = leastsq(err,p0,args=(l1,m1))
        k,b = para[0]
        pl.figure(figsize=(8,8))
        pl.xlabel('time(yr)')
        pl.ylabel('angle(degrees)')
        pl.scatter(spe_t,angle,color='red',label='sample point',linewidth=3)
        o=np.linspace(0,2,1000)
        p=k*o+b
        pl.plot(o,p,color="orange",label="Fitting Line",linewidth=2) 
Mercury=Precession()
Mercury.rotation(0.47,0,0,8.2,0.0008)
```
