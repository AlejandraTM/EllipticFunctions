import numpy as np
import math as mt
import matplotlib.pyplot as plt
f=open("PNewtoniano.txt","r")
l=[]
v=[]
for x in f.readlines():
    m=x.split(" ")
    m=[y.rstrip() for y in m]
    for z in m:
      try:
	l.append(float(z))
      except:
	pass
f.close()
    
sum=0
for i in range(0,len(l),4):
	v.append(l[i])
	sum=sum+l[i]
sum=sum/len(v)
ds=[]
max=min=sum
for i in range(0,len(v)):
	if v[i]>sum:
		if min<sum:
			ds.append(min)	
		if v[i]>max:
			min=max=v[i]
			
	else:
		if max>sum:
			ds.append(max)
		if v[i]<min:
			max=min=v[i]
for i in range(1,len(ds),2):
	ejemax=ds[i]+ds[i-1]
	ejemin=mt.sqrt(ds[i]*ds[i-1])
	e=(ds[i-1]-ds[i])/ejemax
	print ("%.3f" % ejemax, "%.3f" % ejemin,"%.3f" % e)		
x=[]
for i in range(0,len(l),4):
	x.append(i)

plt.plot(x,v,'ro')
plt.hlines(sum,0,len(l))
plt.xlabel('Tiempo en dias')
plt.ylabel('Dstancia en kilometros')
plt.title("Distancia al centro de masa del sistema.")
plt.xlim(0, 1400)
plt.show()
