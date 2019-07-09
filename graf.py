
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



funcion=np.genfromtxt("init.txt")
f=np.transpose(funcion)

plt.figure()
plt.plot(f[0],f[1],color="r")
plt.title("Condicion inicial")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("init.png")
print(np.size(funcion))
print (f)
plt.close()


funcion=np.genfromtxt("Ufuturo.txt")
f=np.transpose(funcion)

plt.figure()
plt.plot(f[0],f[1],color="c")
plt.title("1")
plt.xlabel("x")
plt.ylabel("A")
plt.show()
plt.savefig("1.png")
print(np.size(funcion))
print (f)
plt.close()
