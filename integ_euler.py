# problema 3 ecuacion de euler hewel.ochoa@utp.ac.pa
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def eul(k, t, b, x, dt):
    DYdt = (-k/b )* x * dt 
    return DYdt

tiem = np.arange(0,10)

posIn = 0.5
b = 1
x = 0.5
dt = 0.1
pos = odeint(eul, posIn, tiem, args=(b,x,dt,))
print(pos)

plt.plot(tiem, pos, label="T vs X")
plt.title("dt = 1")
plt.legend()

plt.show()
