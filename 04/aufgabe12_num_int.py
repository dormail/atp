# python script for numerical integral 

import numpy as np
import scipy.integrate as integrate

# values of Omegae
om_mass = 0.315
om_de = 1-0.315

result = integrate.quad(lambda z: 1 / np.sqrt(om_mass * (1+z)**5 + om_de * (1+z)**2), 0, np.inf)

print(result[0])
