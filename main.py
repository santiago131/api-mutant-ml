from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Include.Database import Database
from Include.Validate import Validate
from Include.Analyze import Analyze

app = FastAPI()


def ratio(a, b):
	a = float(a)
	b = float(b)
	if b == 0:
		return a
	return ratio(b, a % b)


class Mutant(BaseModel):
	adn: object


@app.post("/mutant")
def mutant(mutant: Mutant, response: Response):
	validate = Validate(mutant.adn)
	if validate.check():
		db = Database(mutant.adn)
		if db.exists():
			response.status_code = status.HTTP_206_PARTIAL_CONTENT
			json_compatible_item_data = jsonable_encoder({"reclutador": "El adn ya fue analizado"})
		else:
			analysis = Analyze(mutant.adn)
			result = analysis.isMutant()
			if result:
				response.status_code = status.HTTP_200_OK
				json_compatible_item_data = jsonable_encoder({"Magneto": "Bienvenido a la Hermandad de mutantes, pronto te contactaremos"})
			else:
				response.status_code = status.HTTP_403_FORBIDDEN
				json_compatible_item_data = jsonable_encoder({"reclutador": "Usted no es un mutante, no regrese"})
			db.insert(result)
	else:
		response.status_code = status.HTTP_403_FORBIDDEN
		json_compatible_item_data = jsonable_encoder({"reclutador": "Adn invalido"})

	return JSONResponse(content=json_compatible_item_data)


@app.get("/stats")
def stats():
	db = Database()
	humans = db.humansCount()
	mutants = db.mutantsCount()
	ratio = float(mutants) / float(humans) if mutants and humans else 0
	json_compatible_item_data = jsonable_encoder({"count_mutant_dna": mutants, "count_human_dna": humans,"ratio": ratio})
	return JSONResponse(content=json_compatible_item_data)

