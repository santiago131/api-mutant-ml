### Stack
*	Python
*	BD MongoDB
*	AWS EC2 ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609
*	Servidor web Uvicorn

### Requerimientos
- Python
-	MongoDB
-	PIP
-	Librerias
	-	uvicorn
	-	fastapi
	-	pydantic
	-	numpy
	-	pymongo

# Instrucciones
`sudo apt update`

`sudo apt install pip`

`sudo apt install zip`

`sudo apt install python3`

`pip install numpy   `

`pip install fastapi   `

`pip install uvicorn`

`pip install pymongo`

`sudo apt install uvicorn`

`wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`
`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list`

`sudo apt-get update`

`sudo apt-get install -y mongodb-org`

`systemctl start mongod`

`sudo systemctl start mongod`

`sudo systemctl enable mongod`

`cd api/`

`uvicorn main:app --reload --host 0.0.0.0`

# API
** URL **: 54.204.172.244:8000

** ENDPOINT: **

** POST /mutant/ **
```
Host: 54.204.172.244:8000
Content-Type: application/json
Content-Length: 45

{
“dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
```


** GET /stats **
```
Host: 54.204.172.244:8000
```
Response

```
