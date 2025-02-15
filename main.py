import json
from typing import List

import asyncio
from fastapi import FastAPI, UploadFile, File, Request
from starlette import datastructures

app = FastAPI()


@app.get("/")
async def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
  # Simulate an async operation
  await asyncio.sleep(1)
  return {"item_id": item_id, "q": q}


@app.post("/uploadfile")
async def create_upload_file(request: Request):
  form_data = await request.form()
  file = form_data.get("file")
  if isinstance(file, datastructures.UploadFile):
    result = {"filename": file.filename, "content": await file.read()}
  else:
    result = {"error": "No file uploaded"}
  metadata = form_data.get("metadata")

  result["metadata"] = json.loads(
      await metadata.read()) if metadata else None  # Parse metadata JSON

  return result


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
  results = []
  for file in files:
    results.append({"filename": file.filename, "content": await file.read()})
  return results
