# delixus_open_ai_semantic_search

delixus openai for building a semantic search for docs by using docs html files

---

## Resources

This project has two key dependencies:

| Dependency Name | Documentation                | Description                                                                            |
|-----------------|------------------------------|----------------------------------------------------------------------------------------|
| openai          | https://platform.openai.com  | Ai model for semantic search                                                           |
| FastAPI         | https://fastapi.tiangolo.com | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
---

## Clone repo

```
git clone git@github.com:DLXSMarks/chatgpt-doc-poc.git
```

## Install python3.10

```
cd chatgpt-doc-poc

./py/01-install-pre-reqs.py # Install pre-requisites

pip install requests

./py/02-install-python.py # Install python3.10.4
```

## Install PostgresSQL

[Install PostgresSQL](docs/install-postgresql.md)

## Run Locally

To run locally in debug mode run:

```
cd chatgpt-doc-poc

03-create_virtualenv.py

source venv/bin/activate
```

## Update .env

OPENAI_API_KEY=<get the value from the developer and update it in .env file>
DB_USERNAME=<set username of postgres database>
DB_PASSWORD=<set password of postgres database>
DB_HOSTNAME=<set hostname of postgres database>
DB_PORT=<set port number of postgres database>
DB_NAME=<set postgras databse name>

## Run application

```
uvicorn app.api:app --reload
```

Open your browser to http://localhost:8000/docs to view the OpenAPI UI.

For an alternate view of the docs navigate to http://localhost:8000/redoc
