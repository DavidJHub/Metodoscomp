#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
# 
resorte=np.transpose(np.genfromtxt("resorte.dat"))
#print(resorte)
tobs = resorte[0,:]
xobs = resorte[1,:]
plt.figure()
plt.scatter(tobs,xobs)
plt.savefig("resorte.png")
# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:


# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  
#def bayesiana (pm,pb):

def func(pa,pgamma,pomega,tobs):
    return pa*np.exp(-pgamma*tobs)*np.cos(pomega*tobs)

    

# 2b.) Definir una funcion que retorne la funcion de verosimilitud

def verosimilidad(xobs,xmod,error):
    ver=sum(((xobs-xmod)**2)/error)
    return np.exp((1/2)*(-ver))
# 2c.) Caminata



def MH(tobs,pasos,sigma):
    aini=7.5
    gammaini=0.6
    omegaini=18.2
    a=[]
    gamma=[]
    omega=[]
    L=[]
    
    a.append(aini)
    gamma.append(gammaini)
    omega.append(omegaini)
    
    xini=func(a[0],gamma[0],omega[0],tobs)
    
    
    L.append(verosimilidad(xobs, xini,1))
    
    #print (L)
    
    for i in range(pasos):
        aact= np.random.normal(a[i],sigma) 
        gammaact=np.random.normal(gamma[i],sigma)
        omegaact=np.random.normal(omega[i],sigma) 
        
        xini=func(a[i],gamma[i],omega[i],tobs)
        xact= func(aact, gammaact, omegaact,tobs)
        
        
        lini = verosimilidad(xobs, xini,1)
        lact = verosimilidad(xobs, xact,1)
        
        
        alfa = lact/lini
        
        if(alfa>=1.0):
            a.append(aact)
            gamma.append(gammaact)
            omega.append(omegaact)
            L.append(lact)
        else:
            beta=np.random.random()
            if(beta<=alfa):
                a.append(aact)
                gamma.append(gammaact)
                omega.append(omegaact)
                L.append(lact)
            else:
                a.append(a[i])
                gamma.append(gamma[i])
                omega.append(omega[i])
                L.append(lini)
    return a,gamma,omega,L
    plt.figure()

MH(tobs,100000,0.1)


amejor = np.max(MH(tobs,100000,0.1)[0])
gammamejor = np.max(MH(tobs,100000,0.1)[1])
omegamejor = np.max(MH(tobs,100000,0.1)[2])
Lmejor = np.max(MH(tobs,100000,0.1)[3])

print("los mejores parametros son: a=",amejor,"gamama=",gammamejor,"omega=",omegamejor)

    
#condiciones iniciales


#numero de pasos
iteraciones=100000


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf
xmejor = func(amejor, gammamejor, omegamejor, tobs)

plt.figure()
plt.scatter(tobs,xobs)
plt.plot(tobs, xmejor,color="red")
plt.savefig("Resortefinal.png")

# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).
print("Si se puede determinar el valor individual de cada uno usando k y m como parámetros")


