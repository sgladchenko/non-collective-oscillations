from constants import *

# determine the mixing matrix

H_traceless = [
	[-(delta_m*cos)/(4*E), -(delta_m*sin)/(4*E)],
	[-(delta_m*sin)/(4*E), +(delta_m*cos)/(4*E)]
]

some, V = la.eig(np.array(H_traceless))
U = la.inv(V)

# dispertions

def Dx(x):
	res = [[1, 1], [1, 1]]

	for a in (0, 1):
		for b in (0, 1):
			if a < b:
				res[a][b] = (2*sigma_x**2 - 2.0j*delta_m*c**2*hbar/E**3 * x/c)
			elif a > b:
				res[a][b] = (2*sigma_x**2 + 2.0j*delta_m*c**2*hbar/E**3 * x/c)
			else:
				res[a][b] = 2*sigma_x**2

	return np.array(res)

def Dyz(x):
	res = [[1, 1], [1, 1]]

	for a in (0, 1):
		for b in (0, 1):
			if a < b:
				res[a][b] = (2*sigma_x**2 - 2.0j*delta_m*c**2*hbar/E**3 * x/c)
			elif a > b:
				res[a][b] = (2*sigma_x**2 + 2.0j*delta_m*c**2*hbar/E**3 * x/c)
			else:
				res[a][b] = 2*sigma_x**2

	return np.array(res)

def phase(x):
	res = [[1, 1], [1, 1]]

	for a in (0, 1):
		for b in (0, 1):
			if a < b:
				res[a][b] = np.exp(-1.0j*delta_m/(2*hbar*E*c) * x)
			elif a > b:
				res[a][b] = np.exp(+1.0j*delta_m/(2*hbar*E*c) * x)
			else:
				res[a][b] = 1.0

	return np.array(res)

def decoherence(x):
	res = [[1, 0], [0, 1]]

	for a in (0, 1):
		for b in (0, 1):
			if a != b:
				res[a][b] = np.exp( - (0.5*delta_m/E**2)**2 * x**2 / Dx(x)[a][b])
			else:
				res[a][b] = 1.0

	return np.array(res)

# main functions of density matrix

def rho_propagation(x):
	res = [[1, 1], [1, 1]]

	for a in (0, 1):
		for b in (0, 1):
			element = C**1.5

			element *= U[0][a].conjugate() * U[0][b]
			element *= phase(x)[a][b]
			element *= decoherence(x)[a][b]
			element *= Dx(x)[a][b]**(-0.5) * Dyz(x)[a][b]**(-1.0)

			res[a][b] = element

	return np.array(res)

def rho_flavours(x):
	return np.dot(np.dot(U, rho_propagation(x)), V)
	