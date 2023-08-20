from __future__ import annotations
from pydantic import BaseModel, field_validator
from Models.group_of_model import GroupOfModel


class AddModelGroup(BaseModel):
    id: str
    name: str
    nameShortRu: str
    __typename: str

    @classmethod
    @field_validator("id")
    def check_group_of_model_id(cls, id):
        assert id == GroupOfModel.ID, f"id ответа {id} не соответствует ID GroupOfModel {GroupOfModel.ID}"
        return id

    @classmethod
    @field_validator("name")
    def check_group_of_model_name(cls, name):
        assert name == GroupOfModel.NAME, f"name ответа {name} не соответствует NAME GroupOfModel {GroupOfModel.NAME}"
        return name


class Data(BaseModel):
    addModelGroup: AddModelGroup


class GroupOfModelResponse(BaseModel):
    data: Data
