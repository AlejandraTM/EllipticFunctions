import numpy as np
import math as mt
from scipy import constants as cts
import matplotlib.pyplot as plt

#Read File

f=open("alpha=0,9.rtf","r")
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

#i=0
#while i<=len(L)-1:
#    if L[i]== 1000:
#        l.append(L[i+1]*1000)
#        l.append(L[i+2]*1000)
#        l.append(L[i+3]*1000)
#        i=i+4
#    else:
#        l.append(L[i])
#        i=i+1

#Function Definition

def ang_vec(x,y): # This determines the vector between angles
    dot=np.dot(x,y)
    ny=np.linalg.norm(y)
    nx=np.linalg.norm(x)
    q=(dot)/(ny*nx)
    return np.arccos(q)

#Distances everage

sum=0
for i in range(0,len(l),4):
    v.append(l[i])
    sum=sum+l[i]
sum=sum/len(v)
#Maximun and minimun distance

ds=[]
max=min=sum
for i in range(0,len(v)):
	if v[i]>sum:
		if min<sum:
			ds.append(min)	
		if v[i]>max:
			min=max=v[i]
			a=i
	else:
		if max>sum:
			ds.append(max)
			P.append(l[(a*4)+1])
			P.append(l[(a*4)+2])
			P.append(l[(a*4)+3])
		if v[i]<min:
			max=min=v[i]
			
#Determinacion de los elementos orbitales
			
ang=0
ejemax=0
ejemin=0
e=0
c=0
a=0
for i in range(1,len(ds),2):
    c=(ds[i-1]-ds[i])*.5
    a=ds[i]+ds[i-1]
    ejemax=ejemax+a
    ejemin=ejemin+mt.sqrt(((ds[i]+ds[i-1])**2.)-c**2.)
    e=e+np.abs(c/a)
    ang=ang+1
	
ejemax= ejemax/ang
ejemin=ejemin/ang
e=e/ang

#Calculo del angulo entre vada orbita
#A=[]
c=0
angulo=0
#angulo2=0
#print (ds)
#print (P)
if (len(P)/3)%2 == 0:
	for i in range(0,len(P)-3,3):
                y=np.array([P[i],P[i+1],P[i+2]])
                z=np.array([P[i+3],P[i+4],P[i+5]])
                #print (y,z)
                theta=ang_vec(y,z)
                #print (theta)
                angulo=angulo+theta
                c=c+1
else:
	for i in range(0,len(P)-4,3):
		y=np.array([P[i],P[i+1],P[i+2]])	
		z=np.array([P[i+3],P[i+4],P[i+5]])
		#print (y,z)
		theta=ang_vec(y,z)
		#print (theta)
		angulo=angulo+theta
		c=c+1
		
angulo=angulo/c

#print("Movimiento de los angulos con respecto a uno fijo")
#if (len(ds)/2)>=8:
#    for i in range (1,int(len(P)/3),1):
#        a=3*((4*i)-1)
#        if i==1:
#            y=np.array([P[a],P[a+1],P[a+2]])
#        else:
#            if a<=len(P)-2:
#                x=np.array([P[a],P[a+1],P[a+2]])
#                theta=ang_vec(x,y)
#                A.append(theta)
#                angulo2=angulo2+theta
#                c=c+1
#            else:
#                i=len(P)
#    print(angulo2/c)          
#else:
#    print ("No son los datos suficientes")
               
#Calculo delperiodo
    
mu=cts.gravitational_constant*(2*1.e+26)
periodo= ((2*np.pi)/(mu)**(1./2.))*(ejemax*1000)**(3./2.)

#Results
print ("%.3f" % ejemax, "%.3f" % ejemin,"%.3f" % e,"%.3f" % angulo,"%.3f"% periodo)

x=[]
#x2=[]
for i in range(0,len(l),4):
    x.append(i)
#for i in range (0,len(A),1):
#    x2.append(angulo)
    
#Grafica de las distancias
	
plt.plot(v,'.')
plt.hlines(sum,0,len(l))
plt.xlim(0,1000)
plt.xlabel('Cantidad de datos analizados')
plt.ylabel('Distancia (km)')
plt.title("Distancia al centro de masa del sistema \n para el potencial con exponente $1,207$.")
plt.show()

#Plot of change angles
#fig, ax = plt.subplots() 
#ax.plot(A,'.',label='Measure of angle between a fix angle and a variational angle.')
#ax.plot(x2,label ='Angle average between vector of maximun distance.')
#box = ax.get_position()
#ax.set_position([box.x0, box.y0 + box.height * 0.1,
 #                box.width, box.height * 0.9])
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
 #         fancybox=True, shadow=True, ncol=1);


#plt.title('Angle variation to one fixed')
#plt.ylabel('Angle in radians')
#plt.xlim(0,130)
#plt.show()
