class Validate:
	def __init__(self, adn):
		self.ADN = adn
		tempArr = []
		# Desglosamos el string en position de un array
		for row in self.ADN:
			tempArr.append(list(row))
		self.TEMPARR = tempArr

	def characters(self):
		valid = ['A', 'T', 'C', 'G']
		for y, row in enumerate(self.TEMPARR):
			for x, base in enumerate(row):
				if base not in valid:
					return False
		return True

	def dimension(self):
		print('123')
		lenX = []
		maxY = len(self.TEMPARR)
		maxX = len(self.TEMPARR[0])
		for y, row in enumerate(self.TEMPARR):
			rowLen = len(row)
			if maxX != rowLen:
				return False

		# Si existe mas de una longitud las dimensiones no son correctas
		if lenX and len(lenX) > 1:
			return False
		# Si la cantidad de filas no concuerdan con la cantida de columnas
		if maxY != maxY:
			return False

		return True

	def check(self):

		if self.characters() and self.dimension():
			return True
		return False
