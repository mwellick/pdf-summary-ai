from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status
from .crud import upload_pdf_file, save_summary_to_db, get_last_five_docs
from .constraints import parse_pdf_file
from dependencies import db_dependency

pdf_router = APIRouter(tags=["pdf"], prefix="/pdf")


@pdf_router.post("/upload", status_code=status.HTTP_201_CREATED)
def upload_pdf(file: UploadFile = File(...)):
    return upload_pdf_file(file)


@pdf_router.get("/parse", status_code=status.HTTP_200_OK)
def parse_pdf(filename: str):
    return parse_pdf_file(filename)


@pdf_router.get("/summary", status_code=status.HTTP_200_OK)
def get_ai_summary(filename: str, db: db_dependency):
    return save_summary_to_db(filename, db)


@pdf_router.get("/summaries", status_code=status.HTTP_200_OK)
def get_last_five_summaries(db: db_dependency):
    return get_last_five_docs(db)
