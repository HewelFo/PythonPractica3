# problema 5 hewel.ochoa@utp.ac.pa
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import seaborn as sns

plt.close('all')

#Definicion de Tiempo
a = 1.1
b = 0.4
c = 0.4
d = 0.1

#Ecuaciones Simultaneas
def dP_dt(P, t):
    return [P[0]*(a - b*P[1]), -P[1]*(c - d*P[0])]

tiempoIn = np.linspace(0, 60, 500)

P0 = [10, 5]

interaccion = odeint(dP_dt, P0, tiempoIn)

monos = interaccion[:,0]
jaguares = interaccion[:,1]


plt.figure()
sns.kdeplot(monos, jaguares)

