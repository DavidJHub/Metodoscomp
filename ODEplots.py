
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



funcion=np.genfromtxt("OrbitaEuler.txt")
f=np.transpose(funcion)

P= 1/332946*np.sqrt(f[3]*f[3]+f[4]*f[4])
K=1/2*1/332946*(f[3]*f[3]+f[4]*f[4])
U=-1/332946*39.478*1/(np.sqrt(f[1]*f[1]+f[2]*f[2]))
E=K+U

plt.figure()
plt.plot(f[1],f[2],color="r")
plt.title("Trayectoria de la orbita")
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.show()
plt.savefig("XY_Euler_dt.png")
plt.close()

plt.figure()
plt.plot(f[3],f[4],color="r")
plt.title("Velocidades en el plano")
plt.xlabel("Vx (AU)/Anio")
plt.ylabel("Vy (AU)/Anio")
plt.show()
plt.savefig("VxVy_Euler_dt.png")
plt.close()


plt.figure()
plt.plot(f[0],P,color="r")
plt.title("Momento de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("P")
plt.show()
plt.savefig("Mome_Euler_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],K,color="r")
plt.title("Energia cinetica de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("K")
plt.show()
plt.savefig("EK_Euler_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],U,color="r")
plt.title("Energia potencial de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("U")
plt.show()
plt.savefig("EP_Euler_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],E,color="r")
plt.title("Energia total de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("E")
plt.show()
plt.savefig("ET_Euler_dt.png")
plt.close()

##################################################################################################################################################################################################################################################################################
funcion=np.genfromtxt("OrbitaLF.txt")
f=np.transpose(funcion)


P= 1/332946*np.sqrt(f[3]*f[3]+f[4]*f[4])
K=1/2*1/332946*(f[3]*f[3]+f[4]*f[4])
U=-1/332946*39.478*1/(np.sqrt(f[1]*f[1]+f[2]*f[2]))
E=K+U

plt.figure()
plt.plot(f[1],f[2],color="r")
plt.title("Trayectoria de la orbita")
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.show()
plt.savefig("XY_LF_dt.png")
plt.close()

plt.figure()
plt.plot(f[3],f[4],color="r")
plt.title("Velocidades en el plano")
plt.xlabel("x (AU)/Anio")
plt.ylabel("y (AU)/Anio")
plt.show()
plt.savefig("VxVy_LF_dt.png")
plt.close()


plt.figure()
plt.plot(f[0],P,color="r")
plt.title("Momento de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("P")
plt.show()
plt.savefig("Mome_LF_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],K,color="r")
plt.title("Energia cinetica de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("K")
plt.show()
plt.savefig("EK_LF_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],U,color="r")
plt.title("Energia potencial de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("U")
plt.show()
plt.savefig("EP_LF_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],E,color="r")
plt.title("Energia total de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("E")
plt.show()
plt.savefig("ET_LF_dt.png")
plt.close()


###############################################################################################################################################################################################################################################################################################3


funcion=np.genfromtxt("OrbitaRK.txt")
f=np.transpose(funcion)

P= 1/332946*np.sqrt(f[3]*f[3]+f[4]*f[4])
K=1/2*1/332946*(f[3]*f[3]+f[4]*f[4])
U=-1/332946*39.478*1/(np.sqrt(f[1]*f[1]+f[2]*f[2]))
E=K+U

plt.figure()
plt.plot(f[1],f[2],color="r")
plt.title("Trayectoria de la orbita")
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.show()
plt.savefig("XY_RK_dt.png")
plt.close()

plt.figure()
plt.plot(f[3],f[4],color="r")
plt.title("Velocidades en el plano")
plt.xlabel("x (AU)/Anio")
plt.ylabel("y (AU)/Anio")
plt.show()
plt.savefig("VxVy_RK_dt.png")
plt.close()


plt.figure()
plt.plot(f[0],P,color="r")
plt.title("Momento de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("P")
plt.show()
plt.savefig("Mom_RK_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],K,color="r")
plt.title("Energia cinetica de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("K")
plt.show()
plt.savefig("EK_RK_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],U,color="r")
plt.title("Energia potencial de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("U")
plt.show()
plt.savefig("EP_RK_dt.png")
plt.close()

plt.figure()
plt.plot(f[0],E,color="r")
plt.title("Energia total de la tierra")
plt.xlabel("t(anios)")
plt.ylabel("E")
plt.show()
plt.savefig("ET_RK_dt.png")
plt.close()