import numpy as np
import matplotlib.pyplot as plt
import matplotlib



funcion1=np.genfromtxt("init.txt")
f1=np.transpose(funcion1)

plt.figure()
plt.plot(f1[0],f1[1],color="r")
plt.title("Condicion inicial")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("init.png")
print(np.size(funcion1))
print (f1)
plt.close()


funcion2=np.genfromtxt("Ufuturo.txt")
f2=np.transpose(funcion2)

plt.figure()
plt.plot(f2[0],f2[1],color="c")
plt.title("Primer paso")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("Primerpaso.png")
print(np.size(funcion2))
print (f2)
plt.close()


funcion3=np.genfromtxt("U.txt")
f3=np.transpose(funcion3)

plt.figure()
plt.plot(f3[0],f3[1],color="c")
plt.plot(f3[0],f3[2],color="b")
plt.plot(f3[0],f3[3],color="g")
plt.plot(f3[0],f3[4],color="r")
plt.title("Evolucion fija")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("Evolucionfija.png")
print(np.size(funcion3))
print (f3)
plt.close()


funcion4=np.genfromtxt("U2.txt")
f4=np.transpose(funcion4)

plt.figure()
plt.plot(f4[0],f4[1],color="c")
plt.plot(f4[0],f4[2],color="b")
plt.plot(f4[0],f4[3],color="g")
plt.plot(f4[0],f4[4],color="r")
plt.title("Evolucion Extremo Libre")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("EvolucionEL.png")
print(np.size(funcion4))
print (f4)
plt.close()
