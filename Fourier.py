####### Importar los paquetes necesarios

import numpy as np
from matplotlib import pyplot as plt

######## Almacene las imagenes

imgmood = plt.imread("cara_02_grisesMF.png")
imgsmile= plt.imread("cara_03_grisesMF.png")
#plt.figure()
#plt.imshow(np.abs(imgmood))
#plt.imshow(np.abs(imgsmile))


######## Transformada de Fourier 2d

Transformada1=np.fft.fft2(imgsmile)
Transformada2=np.fft.fft2(imgmood)

print (Transformada1)
print (np.shape(Transformada1))

from matplotlib.colors import LogNorm


######## Graficas de Fourier 2d

plt.figure()
plt.imshow(np.abs(Transformada1), norm=LogNorm(vmin=2))
plt.savefig("TransformadaSonrisa.png")
plt.close()

plt.figure()
plt.imshow(np.abs(Transformada2), norm=LogNorm(vmin=2))
plt.savefig("TransformadaSeria.png")
plt.close()
#def filtro2d (freq,sen,u):
    #pasabajas
 #   filt=[]
  #  for i in range (len(freq)):
   #     if freq[i]>u or freq[i]<-u:
    #        sen[i]=0
     #       filt.append(sen[i])
      #  else:
       #     sen[i]=sen[i]
        #    filt.append(sen[i])
    #return np.asarray(filt)


######## Filtro pasabajas para la sonrisa


def filtrobajas2d(tfd,pt):
    for i in range(np.shape(tfd)[0]):
        if int(i>np.shape(tfd)[0]*pt and i<np.shape(tfd)[0]*(1-pt)):
            for j in range(np.shape(tfd)[1]):
                if int(j>np.shape(tfd)[1]*pt and j<np.shape(tfd)[1]*(1-pt)):
                    tfd[i][j]=0
    return tfd

            
                
new1=filtrobajas2d(Transformada1,0.02)

######## Fourier de sonrisa con pasabajas

plt.figure()
plt.imshow(np.abs(new1), norm=LogNorm(vmin=2))
plt.savefig("Filtropasabajas.png")
plt.close()



######## Imagen de sonrisa con filtro pasabajas


imgfilt1=np.fft.ifft2(Transformada1)

plt.figure()
plt.imshow(np.abs(imgfilt1))
plt.savefig("Imagenpasabajas.png")
plt.close()


Transformada1=np.fft.fft2(imgmood)


######## Filtro pasaaltas


def filtroaltas2d(tfd,pt):
    for i in range(np.shape(tfd)[0]):
        if int(i>np.shape(tfd)[0]*pt and i<np.shape(tfd)[0]*(1-pt)):
            for j in range(np.shape(tfd)[1]):
                if int(j>np.shape(tfd)[1]*pt and j<np.shape(tfd)[1]*(1-pt)):
                    tfd[i][j]=tfd[i][j]-tfd[i][j]*0.3
                else:
                    tfd[i][j]=0
        for j in range(np.shape(tfd)[1]):
            if int(i>np.shape(tfd)[0]*pt and i<np.shape(tfd)[0]*(1-pt)):
                tfd[i][j]=tfd[i][j]-tfd[i][j]*0.3
            else:
                    tfd[i][j]=0
    return tfd

######## Fourier de cara seria con pasaaltas
              
                
filtroaltas2d(Transformada2,0.001)


plt.figure()
plt.imshow(np.abs(Transformada2), norm=LogNorm(vmin=2))
plt.savefig("FiltroPasaAltas.png")
plt.close()



imgfilt2=np.fft.ifft2(Transformada2)
######## Imagen de cara seria con filtro pasaaltas

plt.figure()
plt.imshow(np.abs(imgfilt2))
plt.savefig("ImagenPasaAltas.png")


######## Imagen compuesta a partir de la suma de las dos imagenes filtradas


imgfinal=imgfilt1+imgfilt2
plt.figure()
plt.imshow(np.abs(imgfinal))
plt.savefig("ImagenCompuesta.png")

