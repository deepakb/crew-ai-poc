from pydantic import BaseModel

class IngestResponseModel(BaseModel):
    repositoryId: str
    status: bool