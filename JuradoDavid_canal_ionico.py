import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

canal=np.genfromtxt("Canal_ionico.txt")
print (canal)

def circulo(x,y):
    return np.sqrt(x*x+y*y)
def mcmc(datos,sigma):
    r=[]
    x=datos[:,0]
    y=datos[:,1]
    randx=random.rand(len(datos))*20-5
    randy=random.rand(len(datos))*26-8
    

    for i in range(len(datos)):
        xactual= np.random.normal(randx[0,i],sigma) 
        yactual=np.random.normal(randy[1,i],sigma)
       
        rini=circulo(x[i],y[i])
        ract=circulo(xactual,yactual)
        
        alfa = ract/rini
        
        if(alfa>=1.0):
            r.append(ract)
        else:
            beta=np.random.random()
            if(beta<=alfa):
                r.append(ract)
            else:
                
                r.append(r[i])
        return r
fig, ax = plt.subplots()
plt.axis('equal')
circle1 = plt.Circle(x,y), np.max(np.min(mcmc(canal,0.5))), color='r',fill=False)
ax.add_artist(circle1)
plt.savefig("canal.png")
plt.close()


