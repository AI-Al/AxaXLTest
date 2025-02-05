# AxaXL Technical Challenge
Demo API using FastAPI
This is to demonstrate the following:

A simple Python back end offering a RESTful API endpoint which in turn communicates with a database to persist data received in the RESTful API call.
This also demonstrates automated tests, and input sanitisation.

This example uses the following tech stack:
- Python
- Docker
- Postgres
- Tortoise ORM
- Pydantic
- FastAPI
- Pydantic Logfire
- Pytest

Development was done on an Apple Intel Macbook Air.

## Initial Setup
To run the project you will need the following:

- Docker Desktop (https://www.docker.com/products/docker-desktop/)
- A Pydantic Logfire token which is placed in the .env within the AXAXLTEST folder. This is to set a docker environment variable 

## Terminal Commands
To run this project, run the following commands:
```
docker-compose up -d --build    
```
You can then run the unit tests:
```
docker-compose exec web python -m pytest -s
```
You can see API calls being logged at the following location:
https://logfire.pydantic.dev/ai-al/first-fastapi-logfire-project?last=5m

Try using the endpoint http://localhost:8004/ping and if configured correctly, you should see it in the location above.


## Examples for testing manually 

### Create
```
curl -X POST "http://localhost:8004/summaries/" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```
### Read
```
curl -X GET "http://localhost:8004/summaries/1/" \
     -H "Content-Type: application/json"
```
### Read All
```
curl -X GET "http://localhost:8004/summaries/" \
     -H "Content-Type: application/json"
```
### Update
```
curl -X PUT "http://localhost:8004/summaries/1/" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com", "summary": "An Updated summary for 2025"}'
```
### Delete
```
curl -X DELETE "http://localhost:8004/summaries/1/" \
     -H "Content-Type: application/json"
```


When you are done, you can run:
```
docker-compose down
```
