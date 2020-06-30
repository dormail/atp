# range_of_particle.py start
import numpy as np
import matplotlib.pyplot as plt

# the range considering the loss of energy
def range_energy(a,b,E0):
    return 1 / b * np.log(a + b * E0)

# speed in terms of MeV
def v(E, m):
    if m/E > 1:
        print(m/E)
    return np.sqrt(1 - m**2 / E**2)

def gamma(v):
    return 1 / np.sqrt(1 - v**2)

# the range considering the particles lifetime
def range_lifetime(t, m, E0):
    # adjusting t for time dilation
    vel = v(E0,m)
    tp = t / np.sqrt(1 - vel**2)
    return t * gamma(vel) * vel

# mass of leptons
m_electron = 9.12 * 10**(-31) # in kilogram
m_electron = 1 # natural units
m_muon = 211 * m_electron
m_tauon = 17 * m_muon

E0 = np.linspace(1, 50, 100)

# defining constants for leptons
# for the muon
a_mu = 2.302
b_mu = 3.616 * 10**(-6)
lifetime_mu = 2.197 * 10**(-6)
# tau
a_tau = 2.525
b_tau = 2.299 * 10**(-7)
lifetime_tau = 290.3 * 10**(-15)

range_ener_muon = E0.copy()
range_life_muon = E0.copy()
range_ener_tauon = E0.copy()
range_life_tauon = E0.copy()

# computation for muon
for i in range(0, len(E0)):
    range_ener_muon[i] = range_energy(a_mu, b_mu, E0[i])
    range_life_muon[i] = range_lifetime(lifetime_mu, m_muon, E0[i])
    range_ener_tauon[i] = range_energy(a_tau, b_tau, E0[i])
    range_life_tauon[i] = range_lifetime(lifetime_tau, m_tauon, E0[i])

# plotting
# plt.plot(E0, range_ener_muon)
plt.plot(E0, range_life_muon)

# plt.plot(E0, range_ener_tauon)
plt.plot(E0, range_life_tauon)

plt.legend(['range_ener_muon', 'range_life_muon', 'range_ener_tauon', 'range_life_tauon'])

plt.show()

# range_of_particle.py end
