import numpy as np
import math as mt
from scipy import constants as cts
import matplotlib.pyplot as plt

#Read File

f=open("alpha=1.rtf","r")
l=[]
L=[]
v=[]
P=[]
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
    v.append(l[i-2])
print (v)
