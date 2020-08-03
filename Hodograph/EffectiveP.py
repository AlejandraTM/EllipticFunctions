import numpy as np
import math as mt
from scipy import constants as cts
import matplotlib.pyplot as plt

#Read File

f=open("Halpha=1,207.rtf","r")
l=[]
v=[]
for x in f.readlines():
    m=x.split(" ")
    m=[y.rstrip() for y in m]
    m=[y.replace("\\"," ") for y in m]
    for z in m:
        try:
            l.append(float(z))
        except:
            pass
f.close()

for i in range(4,len(l),4):
    v.append(l[i-3])
    v.append(l[i-2])
    v.append(l[i-1])
#print (v)

f=open("alpha=1,207.rtf","r")
ll=[]
r=[]
for x in f.readlines():
    m=x.split(" ")
    m=[y.rstrip() for y in m]
    m=[y.replace("\\"," ") for y in m]
    for z in m:
        try:
            ll.append(float(z))
        except:
            pass
f.close()

for i in range(4,len(ll),4):
    r.append(ll[i-3])
    r.append(ll[i-2])
    r.append(ll[i-1])


E=[]
rn=[]
alpha=1.EffectEffec
m=1.e+26
if len(v)<=len(r):
    for i in range (2,len(v),3):
        #a=(r[i-1]*v[i]-r[i]*v[i-1])
        #b=(v[i-2]*r[i]-r[i-2]*v[i])
        #c=(r[i-2]*v[i-1]-v[i-2]*r[i-1])
        #L=np.linalg.norm(np.array([a,b,c]))
        L=np.linalg.norm(np.cross(np.array([r[i-2],r[i-1],r[i]]),np.array([m*v[i-2],m*v[i-1],m*v[i]]))) 
        norm_r=np.linalg.norm([r[i-2],r[i-1],r[i]])
        rn.append(norm_r)
#        K=(m*(L**2.))/(2.*((norm_r)**2.))
        K=(L**2.)/(2.*m*((norm_r)**2.))
        U=1./(alpha*(norm_r**alpha))
        E.append(K+U)
else:
    for i in range (2,len(r)/2,3):
        a=(r[i-1]*v[i]-r[i]*v[i-1])
        b=(v[i-2]*r[i]-r[i-2]*v[i])
        c=(r[i-2]*v[i-1]-v[i-2]*r[i-1])
        L=np.linalg.norm(np.array([a,b,c])) 
        norm_r=np.linalg.norm([r[i-2],r[i-1],r[i]])
        rn.append(norm_r)
        K=(m*(L**2.))/(2.*((norm_r)**2.))
        U=1./(alpha*(norm_r**alpha))
        E.append(K+U)
plt.plot(rn,E)
plt.xlabel('Posiciones')
plt.ylabel('Potencial Efectivo')
plt.title("Posicion vs Potencial Efectivo")
plt.show()
