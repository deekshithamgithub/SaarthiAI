from pydantic import BaseModel

class RequestModel(BaseModel):
    text: str
    user_id: str