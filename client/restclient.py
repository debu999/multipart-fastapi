import json
import logging

import aiohttp
import asyncio

from logger_config import get_logger

# Configure logging
logger = get_logger(name=__name__, log_level=logging.DEBUG)


async def fetch_data(session, url, params=None):
  try:
    async with session.get(url, params=params) if params else session.get(
        url) as response:
      response.raise_for_status()  # Raise an exception for bad status codes
      return await response.json()
  except aiohttp.ClientError as e:
    logger.error(f"Error fetching data from {url}: {e}")
    return None


async def main():
  async with aiohttp.ClientSession() as session:
    # Example with item_id = 1 and q = "test"
    data = await fetch_data(session, "http://localhost:8000/items/1",
                            params={"q": "test"})
    logger.info(data)

    # Example with item_id = 5 (no q parameter)
    data = await fetch_data(session, "http://localhost:8000/items/5")
    logger.info(data)

    # Example with multiple item_ids and q parameters, using a loop:
    test_data = [{"item_id": 2, "q": "query2"}, {"item_id": 10, "q": "query10"},
                 {"item_id": 7}  # No q parameter
                 ]

    tasks = [
      fetch_data(session, f"http://localhost:8000/items/{item.get('item_id')}",
                 params={"q": item.get("q")}) if item.get("q") else fetch_data(
          session, f"http://localhost:8000/items/{item.get('item_id')}") for
      item in test_data]

    results = await asyncio.gather(*tasks)
    for result in results:
      logger.info(result)

    # Test root endpoint
    data = await fetch_data(session, "http://localhost:8000/")
    logger.info(
        data)  # Use logger.info instead of logger.error for the root endpoint


async def call_upload_endpoint(session, endpoint, file_path):
  url = f"http://localhost:8000/{endpoint}"
  with open(file_path, "rb") as f:
    fd = f.read()
  form_data = aiohttp.FormData()
  form_data.add_field(name="file", value=fd, filename=file_path)
  metadata = {"description": "Test upload",
              "version": "1.2"}  # Example metadata
  form_data.add_field("metadata", json.dumps(metadata).encode(),
                      content_type="application/json")
  async with session.post(url, data=form_data) as response:
    api_res = await response.json()
    print(api_res)
    return api_res


async def upload():
  async with aiohttp.ClientSession() as session:
    data = await call_upload_endpoint(session, "uploadfile", "__init__.py")
    logger.info(data)
    return data


if __name__ == "__main__":
  r = asyncio.run(upload())
  logger.info(f"res {json.dumps(r)}")
