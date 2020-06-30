# sigma_konvergenz.py start
import numpy as np
import matplotlib.pyplot as plt

# natural units, c = me = 1
c = 1
me = 1

# crossection
A = 1.25 * 10**(-25)


def beta(E, eps, t):
    return np.sqrt(1 - 2 * me**2 * c**4 / (E * eps * (1 - np.cos(t))))

def sigma(E, eps, t):
    b = beta(E, eps, t)
    return A * (1 - b) * (2 * b * (b**2 - 2) + (3 - b**4) * np.log((1 + b) / (1 - b)) )

E = 10
eps = 10
t = np.linspace(0.00001, 5, 10000)
s = t.copy()

for i in range(0, len(t)):
    s[i] = sigma(E, eps, t[i])

plt.plot(t,s)
plt.show()

# sigma_konvergenz.py end
