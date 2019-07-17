# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)
XI=np.linspace(-4,4,200)
YI=mifun(XI)
plt.figure()
plt.plot(XI,YI,color="red",label="f(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("funcion.png")
plt.close
# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion. 

x=[]
init=np.random.random()*8-4
x.append(init)
print (x)
def MH(pasos,sigma):
    
    for i in range(pasos):
        xact= np.random.normal(x[i],sigma) 
        alfa = mifun(xact)/mifun(x[i])
        if(alfa>=1.0):
            x.append(xact)
        else:
            beta=np.random.random()
            if(beta<=alfa):
                x.append(xact)
            else:
                x.append(x[i])
    normalizada=mifun(XI)/np.sum(mifun(XI)*(XI[1]-XI[0]))
    #print (normalizada)
    plt.figure()
    plt.plot(XI,normalizada,color="red",label="f(x)")
    plt.legend()
    plt.hist(x,500, density=True)
    plt.xlim(-4,4)
    plt.ylim(0,3)
    plt.savefig("MH "+str(pasos)+" "+str(sigma)+".png")
    plt.close()
    
    


MH(100000,0.1)
MH(100000,0.01)
MH(1000,0.1)
MH(100000,5)
MH(100000,0.2)



# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
