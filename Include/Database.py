from pymongo import MongoClient


class Database:
	DB_NAME = 'api'
	DOMAIN = 'localhost'

	def __init__(self, adn=None):
		self.ADN = adn
		self.CLIENT = MongoClient(str(self.DOMAIN))
		self.DB = self.CLIENT.get_database(self.DB_NAME)

	def exists(self):
		result = self.DB.mutants.find_one({"adn": self.ADN})
		print(result)
		if (result):
			return result
		else:
			return False

	def insert(self, result):
		return self.DB.mutants.insert_one({
			"adn": self.ADN,
			"result": result
		})

	def mutantsCount(self):
		result = self.DB.mutants.count_documents({"result": True})
		return result

	def humansCount(self):
		result = self.DB.mutants.count_documents({"result": False})

		return result
