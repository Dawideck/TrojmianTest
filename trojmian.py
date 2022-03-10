import math

class Trojmian:

	def licz_miejsca_zerowe(self, a, b, c):

		if a == 0: # wspolczynnik kierunkowy rowny 0 => funkcja liniowa
			return -c/(2*b)

		delta = (b*b) - (4 * a * c)
		print(delta)

		if delta < 0:
			return False
		elif delta == 0:
			return -b/2 * a
		elif delta > 0:
			return [round((-b -math.sqrt(delta))/(2 * a), 2), round((-b +math.sqrt(delta))/(2 * a), 2)]

