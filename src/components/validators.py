from typing import Dict, List
from pydantic import BaseModel


class Config(BaseModel):
    token: str
    username: str
    channels: List[str]


class Features(BaseModel):
    delay: int
    memory: bool
    persona: str
    logging: bool
    model: str
