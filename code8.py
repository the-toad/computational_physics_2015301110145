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
```
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:47:32 2017

@author: liumingyang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:45:35 2017

@author: liumingyang
"""
import math
import pylab as pl
import numpy as np
from scipy.optimize import leastsq
class Precession:
    def rotation(self,ini_x,ini_y,ini_vx,ini_vy,alpha0):
        x = [0 for i in range(0,20000)]
        y = [0 for i in range(0,20000)]
        vx = [0 for i in range(0,20000)]
        vy = [0 for i in range(0,20000)]
        radius = [0 for i in range(0,19999)] 
        x[0] = ini_x
        y[0] = ini_y
        vx[0] = ini_vx
        vy[0] = ini_vy
        det_t = 0.0001
        alpha=0.0004
        array_alpha=[]
        angle_alpha=[]
        for i in range(8):
            alpha =0.0004*i
            spe_x=[]
            spe_y=[]
            angle=[]
            spe_t=[]
            t=[]
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
            angle_alpha.append(k)
            array_alpha.append(alpha)
        def fun1(q,w):
            e,r=q
            return e*w+r
        def err1(q,w,a):
            return fun1(q,w) -a
        q0=[1,1]
        l2=np.array(array_alpha)
        m2=np.array(angle_alpha)
        para = leastsq(err1,q0,args=(l2,m2))
        e,r = para[0]
        pl.figure(figsize=(8,8))
        pl.xlabel('alpha')
        pl.ylabel('angle_alpha(degrees/yr)')
        pl.xlim(0,0.006)
        pl.scatter(array_alpha,angle_alpha,color='red',label='sample point',linewidth=3)
        o=np.linspace(0,0.006,1000)
        p=e*o+r
        pl.plot(o,p,color="orange",label="Fitting Line",linewidth=2)
        total_precession=e*100*alpha0*3600
        print(total_precession)
        print(array_alpha,angle_alpha)
Mercury=Precession()
Mercury.rotation(0.47,0,0,8.2,1.1*10**(-8))
```
