#########################################################################################


import numpy as np
import matplotlib.pylab as plt



#########################################################################################

HIERRO=np.transpose(np.genfromtxt("HIERRO.txt"))
COBRE=np.transpose(np.genfromtxt("COBRE.txt"))
NIQUEL=np.transpose(np.genfromtxt("NIQUEL.txt"))
CAMPO=np.transpose(np.genfromtxt("CAMPO.txt"))
errorx=1 + HIERRO
errory=0.05 + HIERRO



plt.figure()
#plt.rcParams['font.family'] = 'Tahoma'
plt.title(u"Curvas de magnetostricción", fontsize=12)
#plt.plot(HIERRO[0],HIERRO[1],'-s',color="r",label="Hierro")
plt.plot(COBRE[0],COBRE[1],'-s',color="g",label="Cobre")
plt.plot(NIQUEL[0][8:len(NIQUEL[0]):1],NIQUEL[1][8:len(NIQUEL[0]):1],'-s',color="b",label="Niquel")
plt.errorbar(HIERRO[0],HIERRO[1], fmt="-s", color="r",xerr=0.25,yerr=1 ,ecolor='black')


plt.legend()
plt.savefig("magnet.png")


print (HIERRO)