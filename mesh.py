class WrongLenghtException(Exception): # for checking the right number of points
	def __init__(self, error_msg):
		Exception.__init__(self, "lengths mismatch: in %s given %d, in %s given %d" % error_msg)
		self.error_msg = error_msg

class Mesh:
	def __init__(self, x=[], y=[], xe=[], ye=[]):
		# check how many points there're

		self._ps = None # crutch

		if len(x) != len(y):
			raise WrongLenghtException(("x", len(x), "y", len(y)))
		if len(x) != len(xe) and len(xe) != 0:
			raise WrongLenghtException(("x", len(x), "xe", len(xe)))			
		if len(x) != len(ye) and len(ye) != 0:
			raise WrongLenghtException(("x", len(x), "ye", len(ye)))

		self._data = [] # list of points: (x, y, xe, ye)

		if len(xe) != 0 and len(ye) != 0:
			for each in range(0, len(x)):
				self._data.append((x[each], y[each], xe[each], ye[each]))
		elif len(xe) != 0 and len(ye) == 0:
			for each in range(0, len(x)):
				self._data.append((x[each], y[each], xe[each], 0))
		elif len(xe) == 0 and len(ye) != 0:
			for each in range(0, len(x)):
				self._data.append((x[each], y[each], 0, ye[each]))
		else:
			for each in range(0, len(x)):
				self._data.append((x[each], y[each], 0, 0))

	def x(self, coeff=1):
		return tuple([each[0]*coeff for each in self._data])

	def y(self, coeff=1):
		return tuple([each[1]*coeff for each in self._data])

	def xe(self, coeff=1):
		return tuple([each[2]*coeff for each in self._data])

	def ye(self, coeff=1):
		return tuple([each[3]*coeff for each in self._data])

	def add_on_mesh(self, x0, y0, x0err = 0, y0err = 0):
		self._data.append((x0, y0, x0err, y0err))

