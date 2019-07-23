# Tiene una serie de tiempo, donde los datos de tiempo estan almacenados en un arreglo t y los datos de amplitud en un arreglo amp.
#1) Usando los paquetes de scipy de la transformada de Fourier, haga un FILTRO de la senial que elimine las frecuencias mayores a 1000Hz en las senial original.
#2) Haga una grafica de la senial original y la senial filtarada y guardela SIN MOSTRARLA en filtro.pdf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)



plt.figure()
plt.plot(t,amp,c="r")
plt.savefig("Original.png")
plt.close()


A=np.asarray([t,amp])
print (A)

Trf=np.fft.fft(amp)
print (Trf)

plt.figure()
plt.plot(t,Trf,c="r")
plt.savefig("Transformada.png")
plt.close()


# SU FILTRO

Frecuencias=np.fft.fftfreq(n,dt)

for i in range(n):
    if Frecuencias[i]>1000:
        Trf[i]=0
        
print (Frecuencias)


plt.figure()
plt.plot(t,Trf,c="r")
plt.savefig("TransformadaFitrada.png")
plt.close()


# SU GRAFICA
iTrf=np.fft.ifft(Trf)
plt.figure()
plt.plot(t,iTrf,c="r")
plt.savefig("SenialFitrada.png")
plt.close()


# Puede usar los siguientes paquetes:
#from scipy.fftpack import fft, fftfreq, ifft

