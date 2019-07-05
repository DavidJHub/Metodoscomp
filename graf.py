
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



funcion=np.genfromtxt("Resorte.txt")
f=np.transpose(funcion)

plt.figure()
plt.plot(f[0],f[1],color="r")
plt.title("Resorte")
plt.xlabel("tiempo")
plt.ylabel("x")
plt.show()
plt.savefig("Resorte.png")
print(np.size(funcion))
print (f)
plt.close()