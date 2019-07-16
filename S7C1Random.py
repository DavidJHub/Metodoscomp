#Ejercicio 0
#Lean el capitulo 5 del Landau (ver el programa del curso).

import numpy as np
import matplotlib.pylab as plt

#Ejercicio 1
# Usando los generadores de numeros aleatorios de numpy (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html):
# a) Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf
# a) Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf
nums=np.random.random(1000)*20-10
plt.figure()
plt.hist(nums,color="g")
plt.savefig("uniforme.png")
plt.close()
# Ejercicio 2
# Escriba un programa en Python que: 
# Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf. 
# Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf. 

x1=[]
y1=[]

r1=30.5
for i in range(1000):
    xr=np.random.rand()*r1
    yr=np.random.rand()*r1
    x1.append(xr)
    y1.append(yr)
x1r=np.asarray(x1)
y1r=np.asarray(y1)

plt.figure()
plt.scatter(x1r,y1r,color="b")
plt.savefig("cuadrado.png")
plt.close()

x2=[]
y2=[]

r2=23
puntos=0
while puntos<1000:
    xr=np.random.rand()*(r2*2)-r2
    yr=np.random.rand()*(r2*2)-r2
    if(xr*xr+yr*yr<23*23):
        x2.append(xr)
        y2.append(yr)
        puntos=puntos+1
x1r=np.asarray(x2)
y1r=np.asarray(y2)


plt.figure()
plt.scatter(x1r,y1r,color="b")
plt.savefig("circulo.png")
plt.close()


# Ejercicio 3 
# Lean sobre caminatas aleatorias.


# Ejercicio 4
# Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
# La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25
# Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro  

# Grafique la distribucion final de puntos y guarde dicha grafica sin mostrarla en un archivo llamado DistCaminata.pdf
# Grafique la caminata de UNO de sus puntos y guarde dicha grafica sin mostrarla en un archivo llamado puntoCaminata.pdf

# Repita el proceso para sigma = 0.00025 y sigma= 2.5. Grafique la caminata de UNO de sus puntos para los distintos sigmas y guardela sin mostrarla en sigmaCaminata.pdf

# Repita el proceso para condiciones abiertas: si un punto se "sale" del cuadrado deja de ser considerado en la simulacion.



inicio=np.transpose(np.asarray([x1,y1]))
#print (inicio)
#print (len(inicio))
def caminatafinal(inicio,pasos):
    xpuntosnew=[]
    ypuntosnew=[]
    for i in range(len(inicio)):
        xi=inicio[i][0]
        yi=inicio[i][1]
        xnew=0
        ynew=0
        for j in range(pasos):
            xrd=np.random.normal(scale=0.25)
            xnew=xnew+xrd
            if(xnew+xi>30.5):
                xnew=(xnew+xi)%30.5
            if(xnew+xi<0):
                xnew=30.5+(xnew+xi)
            yrd=np.random.normal(scale=0.25)
            ynew=xnew+yrd
            if(ynew+yi>30.5):
                ynew=(ynew+yi)%30.5
            if(ynew+yi<0):
                ynew=30.5+(ynew+yi)
        if(xnew+xi>30.5 or xnew+xi<0):
            xpuntosnew.append(xnew)
        if(xnew+xi<30.5 and xnew+xi>0):
            xpuntosnew.append(xnew+xi)
        if(ynew+yi>30.5 or xnew+xi<0):
            ypuntosnew.append(ynew)
        if(ynew+yi<30.5 and ynew+yi>0):
            ypuntosnew.append(ynew+yi)
    camx=np.asarray(xpuntosnew)
    camy=np.asarray(ypuntosnew)
    plt.figure()
    plt.scatter(camx,camy,color="b")
    plt.savefig("caminata.png")
    plt.close()
    
caminatafinal(inicio,100)

def caminatauno(inicio,pasos):
    xpuntosnew=[]
    ypuntosnew=[]
    
    xi=inicio[0][0]
    yi=inicio[0][1]
    xnew=0
    ynew=0
    for j in range(pasos):
        xrd=np.random.normal(scale=0.25)
        xnew=xnew+xrd
        if(xnew+xi>30.5):
            xnew=(xnew+xi)%30.5
            xpuntosnew.append(xnew)
        if(xnew+xi<0):
            xnew=30.5+(xnew+xi)
            xpuntosnew.append(xnew)
        if(xnew+xi<30.5 and xnew+xi>0):
            xpuntosnew.append(xnew+xi)
            
            
            
        yrd=np.random.normal(scale=0.25)
        ynew=xnew+yrd
        
        if(ynew+yi>30.5):
            ynew=(ynew+yi)%30.5
            ypuntosnew.append(ynew)
        if(ynew+yi<0):
            ynew=30.5+(ynew+yi)
            ypuntosnew.append(ynew)
        if(ynew+yi<30.5 and ynew+yi>0):
            ypuntosnew.append(ynew+yi)
            
    
    
 
    X=np.asarray(xpuntosnew)
    Y=np.asarray(ypuntosnew)
    plt.figure()
    plt.plot(X,Y,color="r")
    plt.savefig("caminatauno.png")
    plt.close()
    
caminatauno(inicio,100)


# Si le queda tiempo puede:



##################################################################################################################################################################
############################################################ Ejercicio  ##########################################################################
##################################################################################################################################################################

#difusion: una gota de crema en un Cafe.
#
#Condiciones iniciales:
#Cafe: 10000 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 230
#Crema: 100 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 2
#
#Nota: si su codigo se esta demorando mucho en correr, puede usar 1000 particulas de cafe en vez de 10000.
#
# 1) Haga una grafica de las condiciones iniciales donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheIni.pdf
#
#2) Todas las particulas deben hacer una caminata aleatoria de 1000 pasos. Los pasos en las coordenadas x y deben seguir una distribucion gausiana de sigma 2.5. Si va a usar coordenadas polares elija un sigma apropiado.
#
#3) Condiciones de frontera: implemente unas condiciones tales que si la particulas "sale" del circulo, usted vuelva a dar el paso. Si no puede implementar solo las condiciones antes descritas, debe al menos escribir comentarios explicando que hace cada linea de codigo de las condiciones propuestas (comentado abajo)
#
# 4) Haga una grafica de las posiciones finales de las particulas despues de la caminata donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheFin.pdf
#



x=[]
y=[]

r=np.sqrt(230)
for i in range(1000):
    xr=np.random.rand()*r
    yr=np.random.rand()*r
    x.append(xr)
    y.append(yr)
np.asarray(x)
np.asarray(y)
plt.figure()
plt.scatter(x,y,color="b")
plt.savefig("scatter.png")


#Una posible implementacion de condiciones de frontera. Trate de hacer la suya propia sin usar esta. 
#Si usa esta (obtiene menos puntos) debe comentar cada una de las lineas explicando en palabras que hace el codigo. Debe tambien naturalmente usar los nombres de variables que uso en el resto de su codigo propio.
#indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>230)
#indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>230)
#while(len(indexcafe[0])>1):
#	xcafenuevo[indexcafe]=xcafe[indexcafe] + np.random.normal(0,sigma)
#	ycafenuevo[indexcafe]=ycafe[indexcafe] + np.random.normal(0,sigma)
#	indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>=230)
#while(len(indexcrema[0])>1):
#	xcremanuevo[indexcrema]=xcrema[indexcrema] + np.random.normal(0,sigma)
#	ycremanuevo[indexcrema]=ycrema[indexcrema] + np.random.normal(0,sigma)
#	indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>=230) 



	
