from __future__ import annotations
from typing import List
from pydantic import BaseModel


class Tag(BaseModel):
    id: str
    __typename: str


class AddModel(BaseModel):
    name: str
    id: str
    tags: List[Tag]
    __typename: str


class Data(BaseModel):
    addModel: AddModel


class ModelResponse(BaseModel):
    data: Data
