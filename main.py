from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from models.requests import IngestResponseModel
from services.github import ingestGithubRepo

tags_metadata=[
  {
    "name": "ingest",
    "description": "Ingest github repo's codebase to vector store to further ask questions related to codebase",
  }
]

app = FastAPI(description="GithubRag", version="1.0.0", openapi_tags=tags_metadata, docs_url="/docs", openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ingest", response_model=IngestResponseModel, tags=["ingest"])
async def ingest(url: str = Form(...)):
    if url == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='No file selected')

    status = await ingestGithubRepo(url)

    return JSONResponse(status)