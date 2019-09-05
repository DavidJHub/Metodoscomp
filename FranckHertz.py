#########################################################################################


import numpy as np
import matplotlib.pylab as plt



#########################################################################################

serie1=np.transpose(np.genfromtxt("Punto1Datos1_180_2_0.txt",delimiter="	",skip_header=3))
serie2=np.transpose(np.genfromtxt("Punto1Datos2_180_2_0.txt",delimiter="	",skip_header=3))
serie3=np.transpose(np.genfromtxt("Punto1Datos3_180_2_0.txt",delimiter="	",skip_header=3))
serie4=np.transpose(np.genfromtxt("Punto1Datos4_180_2_0.txt",delimiter="	",skip_header=3))
serie5=np.transpose(np.genfromtxt("Punto1Datos5_180_2_0.txt",delimiter="	",skip_header=3))

#errorx=1 + HIERRO
#errory=0.05 + HIERRO


print(serie1)
plt.figure()
#plt.rcParams['font.family'] = 'Tahoma'
#plt.title(u"V vs I picos", fontsize=12)
#plt.plot(HIERRO[0],HIERRO[1],'-s',color="r",label="Hierro")
plt.plot(serie1[0],serie1[1],'-',color="g",label="Serie 1")
plt.plot(serie2[0],serie2[1],'-',color="b",label="Serie 2")
plt.plot(serie3[0],serie3[1],'-',color="r",label="Serie 3")
plt.plot(serie4[0],serie4[1],'-',color="black",label="Serie 4")
plt.plot(serie5[0],serie5[1],'-',color="cyan",label="Serie 5")
plt.xlabel("Voltaje U1 (V)")
plt.ylabel("Corriente IA (nA)")
plt.legend()
plt.grid()
#plt.errorbar(HIERRO[0],HIERRO[1], fmt="-s", color="r",xerr=0.25,yerr=1 ,ecolor='black')


#plt.legend()
plt.savefig("Tempconstante.png")

