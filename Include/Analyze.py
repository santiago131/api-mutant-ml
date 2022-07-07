import numpy as np


class Analyze:
	def __init__(self, adn):
		self.ADN = adn

	# Analiza si se repite 4 veces algunas de las bases
	def read(self, adn):
		valid = ['A', 'T', 'C', 'G']
		for base in valid:
			for row in adn:
				# Contamos la cantidad de veces que se repite una base*4 EJ: TTTT
				count = row.count(base*4)
				if count >= 1:
					return True

		return False

	# Convierte las columnas en filas
	def transpose(self):
		newArr = []
		for x, column in enumerate(self.ADN[0]):
			base = False
			for row in self.ADN:
				if base:
					base = base + row[x]
				else:
					base = row[x]

			newArr.append(base)
		return newArr

	def getCross(self):
		arr = []
		arrReverse = []
		diagList = []

		# Convertimos el string a posiciones de un array
		for row in self.ADN:
			arr.append(list(row))
			# Invertimos el string para recorrer las diagonales en sentido contrario
			arrReverse.append(list(row[::-1]))

		# Obtenemos todas las diagonales positivas
		for x, column in enumerate(arr[0]):
			diagonal = np.diag(arr, x)
			if len(diagonal) >= 4:
				diagList.append(''.join(diagonal))

		# Obtenemos todas las diagonales negativas
		for y, row in enumerate(arr):
			if y > 0:
				diagonal = np.diag(arr, -y)
				if len(diagonal) >= 4:
					diagList.append(''.join(diagonal))

		# Obtenemos todas las diagonales positivas
		for x, column in enumerate(arrReverse[0]):
			diagonal = np.diag(arrReverse, x)
			if len(diagonal) >= 4:
				diagList.append(''.join(diagonal))

		# Obtenemos todas las diagonales negativas
		for y, row in enumerate(arrReverse):
			if y > 0:
				if len(diagonal) >= 4:
					diagList.append(''.join(diagonal))
		return diagList

	def isMutant(self):
		cross = self.getCross()
		transposed = self.transpose()
		if self.read(self.ADN) or self.read(transposed) or self.read(cross):
			return True

		return False
