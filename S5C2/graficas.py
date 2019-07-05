import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


funcion=np.genfromtxt("EULER.txt")

plt.figure()
plt.plot(funcion[0],funcion[1],color="r")
plt.title("Metodo Euler")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("EULER.pdf")
plt.close()


funcion2=np.genfromtxt("RK.txt")

plt.figure()
plt.plot(funcion2[0],funcion2[1],color="b")
plt.title("Runge-kutta 4th order")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("RK.pdf")
plt.close()

