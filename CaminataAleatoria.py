import numpy as np
import matplotlib.pyplot as plt
import random 


def caminata(umbral,punto):
        opciones=[0,1]
        
        X=0
        pasos=0
        recorrido=[]
        for i in range(umbral):
            el=random.choice(opciones)
            if X==punto:
                    break
            if el==0:
                X=X+1
                recorrido.append(X)
                pasos=pasos+1
                
            if el==1:
                X=X-1
                pasos=pasos+1
                recorrido.append(X)

        return pasos


def iterar(iteraciones):
    ret=[]
    for j in range (iteraciones):
        ret.append(np.asarray(caminata(200,1)))
    return np.asarray(ret)


print (iterar(1000))

plt.figure()
plt.hist(iterar(200),bins=100,color="red")
plt.savefig("Caminata.png")


def ejercicio():
    primera=iterar(50)
    segunda=iterar(100)
    tercera=iterar(500)
    cuarta=iterar(1000)
    f= open("tablaCaminata.txt","w+")
    f.write("Iteraciones" + " " + "Promedio"+"\r\n")
    f.write(str(50) + " " + str(np.mean(primera))+"\r\n")
    f.write(str(100) + " " + str(np.mean(segunda))+"\r\n")
    f.write(str(500) + " " + str(np.mean(tercera))+"\r\n")
    f.write(str(1000) + " " + str(np.mean(cuarta))+"\r\n")
print (ejercicio())





        