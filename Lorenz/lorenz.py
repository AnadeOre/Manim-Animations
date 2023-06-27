import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

state0 = [1.0, 1.0, 1.0]
state1 = [1.5, 1.6, 1.7]
state2 = [-1, 2, 0]
t = np.arange(0.0, 40.0, 0.01)

states = odeint(f, state0, t)
states2 = odeint(f, state1, t)
states3 = odeint(f, state2, t)


fig = plt.figure(facecolor='white')
ax = fig.add_subplot(projection='3d')

ax.plot(states3[:, 0], states3[:, 1], states3[:, 2], 'b')
ax.plot(states[:, 0], states[:, 1], states[:, 2], 'r')
ax.plot(states2[:, 0], states2[:, 1], states2[:, 2], 'y')
plt.draw()
ax.axis('off')
plt.show()