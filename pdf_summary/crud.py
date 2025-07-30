import os
from fastapi import UploadFile
from database.models import DocumentSummary
from dependencies import db_dependency
from .constraints import (
    UPLOAD_DIR,
    check_file_size,
    check_file_type,
)
from .utils import generate_summary


def upload_pdf_file(file: UploadFile):
    check_file_size(file)
    check_file_type(file)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    file.file.seek(0)
    return {"filename": file.filename}


def save_summary_to_db(filename: str, db: db_dependency):
    summary = generate_summary(filename)
    doc_summary = DocumentSummary(filename=filename, summary=summary)
    db.add(doc_summary)
    db.commit()
    db.refresh(doc_summary)

    return {"filename": filename, "summary": summary}


def get_last_five_docs(db: db_dependency):
    history = db.query(DocumentSummary).order_by(
        DocumentSummary.created_at.desc()
    ).limit(5).all()

    return history
