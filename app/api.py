# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from app.service.Scrapper import Scrapper
from app.service.QueryParser import answer_question
from app.service.Codegen import query_codegen, process
from collections import defaultdict
import os

import pandas as pd
import numpy as np
from dotenv import load_dotenv, find_dotenv
from fastapi import Body, FastAPI, UploadFile, File, HTTPException
from fastapi_sqlalchemy import db
from starlette.responses import RedirectResponse
import srsly
import uvicorn

from app.config import middleware
from app.db_models.embedding_data import EmbeddingData
from app.models import (
    ENT_PROP_MAP,
    ScrapRequest,
    RecordsResponse,
    RecordsEntitiesByTypeResponse,
    Query,
    QueryResponse,
    FileQuestion
)


app = FastAPI(
    title="delixus_open_ai_semantic_search",
    version="1.0",
    description="delixus openai for building a semantic search for docs by using docs html files",
    middleware=middleware,
)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@app.post("/scrap_web")
async def scrap_the_url(body: ScrapRequest = Body(..., example="{\"url\": \"google.com\"}")):
    """Scrap the url using html parsing"""

    http_url_pattern = r'^http[s]{0,1}://.+$'
    scrapper = Scrapper()
    scrapper.crawl(url=body.url, http_url_pattern=http_url_pattern)
    return {"Submitted the scrap request": True}
    # res = []
    # documents = []
    #
    # for val in body.values:
    #     documents.append({"id": val.recordId, "text": val.data.text})
    #
    # entities_res = extractor.extract_entities(documents)
    #
    # res = [
    #     {"recordId": er["id"], "data": {"entities": er["entities"]}}
    #     for er in entities_res
    # ]
    #
    # return {"values": res}


#
# @app.post(
#     "/entities_by_type", response_model=RecordsEntitiesByTypeResponse, tags=["NER"]
# )
# async def extract_entities_by_type(body: RecordsRequest = Body(..., example=example_request)):
#     """Extract Named Entities from a batch of Records separated by entity label.
#         This route can be used directly as a Cognitive Skill in Azure Search
#         For Documentation on integration with Azure Search, see here:
#         https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface"""
#
#     res = []
#     documents = []
#
#     for val in body.values:
#         documents.append({"id": val.recordId, "text": val.data.text})
#
#     entities_res = extractor.extract_entities(documents)
#     res = []
#
#     for er in entities_res:
#         groupby = defaultdict(list)
#         for ent in er["entities"]:
#             ent_prop = ENT_PROP_MAP[ent["label"]]
#             groupby[ent_prop].append(ent["name"])
#         record = {"recordId": er["id"], "data": groupby}
#         res.append(record)
#
#     return {"values": res}


@app.post("/query")
async def query_model(body: Query = Body(..., example={"query": "What is Database Cloud Correlation?"})):
    """Ask question to model and get response"""

    df = pd.read_csv('./app/data/processed/embeddings.csv', index_col=0)
    df['embeddings'] = df['embeddings'].apply(eval).apply(np.array)

    response = answer_question(df, question=body.query, debug=False)
    return QueryResponse(data=response).dict()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    This API upload JSON file and prepare data for querying
    """
    # Check if the file is a JSON file
    if file.filename.endswith(".json"):
        # Create the necessary directories if they don't exist
        os.makedirs("data/uploads", exist_ok=True)

        # Read the contents of the file
        contents = await file.read()

        # Save the file in the data/uploads folder
        with open(f"data/uploads/{file.filename}", "wb") as f:
            f.write(contents)

        # preprocessing of uploaded file
        process(f"data/uploads/{file.filename}")

        response = {
            'filename': file.filename,
            'message': 'File uploaded successfully'
        }
        return response

    return {"message": "Invalid file format. Please upload a JSON file."}


@app.post("/codegen")
async def generate_codebase(file_question: FileQuestion):
    """
    This API will generate code based on question asked by user
    """
    filename = file_question.filename
    filename = 'data/uploads/' + ''.join(filename.split('.')[:-1]) + '.csv'

    question = file_question.question

    response = query_codegen(filename, question)
    return response
