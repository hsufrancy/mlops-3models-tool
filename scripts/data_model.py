# accept the input params/data payload
# output the score, class, latency

from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl
from typing import List



class NLPDataInput(BaseModel):
    text: List[str]
    user_id: EmailStr

class ImageDataInput(BaseModel):
    url: List[HttpUrl]
    user_id: EmailStr

class NLPDataOutput(BaseModel):
    model_name: str
    text: List[str]
    labels: List[str]
    scores: List[float]
    prediction_time: int

class ImageDataOutput(BaseModel):
    model_name: str
    url: List[HttpUrl]
    labels: List[str]
    scores: List[float]
    prediction_time: int





