﻿# PDF Summary AI



## Description 

#### PDF Summary AI is a simple web application that allows users to upload large PDF documents (up to 50MB, 100 pages) and receive AI-generated summaries of those documents using the OpenAI API. The app also keeps a history of the last 5 processed documents.


## Core Features

- **PDF Upload**: Users can upload a PDF file via the API.
- **PDF Parsing**: Supports PDFs containing images and tables.
- **Summary Generation**: Uses OpenAI's API to generate a textual summary of the uploaded PDF.
- **History Display**: Shows the last 5 processed documents along with their summaries.

## Getting Started

### How to Run:

### a) Locally:

```
git clone https://github.com/mwellick/pdf-summary-ai.git
cd pdf-summary-ai

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt

#
Create a .env file in the root directory with the variables from .env.sample and update it
with your own specific values

#Run FastAPI server
uvicorn main:app --reload

```

### API Documentation
* Swagger: Visit http://127.0.0.1:8000 


### b) Run with Docker:
```
docker-compose up --build
```

## API Documentation

#### Upload a PDF

* POST /pdf/upload

* Parameters: file — PDF file (form-data)

* Response: Upload confirmation

### Parse a PDF
* GET /pdf/parse

* Parameters: parse uploaded PDF file

* Response: Parsed PDF content

### Get AI-generated summary
* GET /pdf/summary?filename={filename}

* Parameters: filename — name of the PDF document

* Response: Text summary saved in the database

### Get last 5 summaries
* GET /pdf/summaries

* Response: List of the last 5 documents and their summaries
