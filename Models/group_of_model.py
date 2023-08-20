from __future__ import annotations
import uuid
from datetime import datetime
from typing import List
from pydantic import BaseModel


class GroupOfModelSchema(BaseModel):
    NAME: str
    ID: str
    START_DATE: str
    END_DATE: str
    MODEL: MODEL


class MODEL(BaseModel):
    PLAN: PLAN
    FACT: FACT
    UC: UC
    UH: UH
    UR: UR


class PLAN(BaseModel):
    id: str
    Tag: List[str]


class FACT(BaseModel):
    id: str
    Tag: List[str]


class UC(BaseModel):
    id: str
    Tag: List[str]


class UH(BaseModel):
    id: str
    Tag: List[str]


class UR(BaseModel):
    id: str
    Tag: List[str]


# class DictObj:
#     def __init__(self, in_dict: dict):
#         assert isinstance(in_dict, dict)
#         for key, val in in_dict.items():
#             if isinstance(val, (list, tuple)):
#                 setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
#             else:
#                 setattr(self, key, DictObj(val) if isinstance(val, dict) else val)

def GroupOfModel():
    return GroupOfModelSchema.model_validate({
        "NAME": f"Test {datetime.now():%Y-%m-%d %H:%M}",
        "ID": f"{uuid.uuid4()}",
        "START_DATE": "",
        "END_DATE": "",
        "MODEL": {
            "PLAN": {
                "id": f"{uuid.uuid4()}",
                "Tag": [
                    "19b802aa-a203-467f-8ea5-ec28e3136941",
                    "502243ce-2166-410c-8a9a-67bf335d86ad",
                    "01339100-abe1-49b1-a945-c8335f287651",
                    "2e9db115-3923-4abb-9a8d-bf9213e39cf4",
                    "1d86f59b-b6e1-4f65-b265-53a8d94d8421"
                ]
            },
            "FACT": {
                "id": f"{uuid.uuid4()}",
                "Tag": [
                    "327cb883-03cd-45ef-9c28-4f2f6da25a93"
                ]
            },
            "UC": {
                "id": f"{uuid.uuid4()}",
                "Tag": [
                    "95b46569-543d-4a17-8a63-a10d0e03a08e"
                ]
            },
            "UH": {
                "id": f"{uuid.uuid4()}",
                "Tag": [
                    "7cdddc4f-aca2-4660-a714-21e2e4f1bd0a"
                ]
            },
            "UR": {
                "id": f"{uuid.uuid4()}",
                "Tag": [
                    "002a0099-f4c8-4b89-80f9-4e214f3e3c17"
                ]
            }
        }
    })


GroupOfModelStatic = GroupOfModel()
