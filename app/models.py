# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import unicodedata
from typing import Dict, List, Optional
from pydantic import BaseModel, validator

ENT_PROP_MAP = {
    "CARDINAL": "cardinals",
    "DATE": "dates",
    "EVENT": "events",
    "FAC": "facilities",
    "GPE": "gpes",
    "LANGUAGE": "languages",
    "LAW": "laws",
    "LOC": "locations",
    "MONEY": "money",
    "NORP": "norps",
    "ORDINAL": "ordinals",
    "ORG": "organizations",
    "PERCENT": "percentages",
    "PERSON": "people",
    "PRODUCT": "products",
    "QUANTITY": "quanities",
    "TIME": "times",
    "WORK_OF_ART": "worksOfArt",
}


class RecordDataRequest(BaseModel):
    text: str
    language: str = "en"


class ScrapRequest(BaseModel):
    url: str


class RecordDataResponse(BaseModel):
    entities: List


class Message(BaseModel):
    message: str


class RecordResponse(BaseModel):
    recordId: str
    data: RecordDataResponse
    errors: Optional[List[Message]]
    warnings: Optional[List[Message]]


class RecordsResponse(BaseModel):
    values: List[RecordResponse]


class RecordEntitiesByTypeResponse(BaseModel):
    recordId: str
    data: Dict[str, List[str]]


class RecordsEntitiesByTypeResponse(BaseModel):
    values: List[RecordEntitiesByTypeResponse]


class Query(BaseModel):
    query: str


class QueryResponse(BaseModel):
    data: str


class EmbeddingsDistance(BaseModel):
    text: str

    @validator('text', pre=True)
    def remove_unicode(cls, value):
        return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8', 'ignore')


class FileQuestion(BaseModel):
    filename: str
    question: str
