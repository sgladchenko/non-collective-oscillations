# modules of maths

from numpy import linalg as la
import numpy as np
import scipy as sc

# main constants

eV_2_erg = 1.60218e-12

hbar = 1.054e-27 # erg * sec
h = 6.3e-27 # erg * sec

c = 3e10 # cm/sec
pi = np.pi

delta_m21 = 2.4e-3*(eV_2_erg)**2 # erg^2, delta_m12^2 * c^4
delta_m32 = 7.6e-5*(eV_2_erg)**2 # erg^2, delta_m23^2 * c^4

c12 = np.sqrt(1 - 0.0841)
c23 = np.sqrt(1 - 0.321)

s12 = np.sqrt(0.0841)
s23 = np.sqrt(0.321)

# may vary

delta_m = delta_m21
cos     = c12
sin     = s12

Ve = 1e-7 * eV_2_erg # erg
E = 10e6 * eV_2_erg # erg

sigma_x = 1e-11 # cm, initial WPs' spatial length
sigma_p = h/sigma_x # the lenght in momentum-representation

C = 2 * sigma_x**2