# Multipart Form Data API with FastAPI

This repository provides a basic framework for building a RESTful API that handles multipart form data using FastAPI. 

**Features:**

* **File Uploads:** Handles file uploads using FastAPI's `File` parameter.
* **Metadata Support:** Allows for optional metadata to be included with file uploads.
* **Basic File Processing:** Includes a simple example of file processing (saving to disk).
* **Error Handling:** Includes basic error handling for file uploads and processing.

**Getting Started:**

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
# API Endpoints:

/upload (POST):
  Accepts a file and optional metadata in the request body.
  Processes the uploaded file (e.g., saves it to disk).
  Returns a JSON response with success/error messages and optional metadata.

Example Usage:

Use a tool like Postman or cURL or httpie to send a POST request to the /upload endpoint with a file and optional metadata.

Contributing:

Contributions are welcome! Please feel free to submit pull requests for bug fixes, improvements, and new features.

License:

This project is licensed under the Apache 2 License. See the LICENSE file for more details.   

