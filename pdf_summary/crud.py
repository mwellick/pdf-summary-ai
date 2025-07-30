import os
from fastapi import UploadFile
from .constraints import check_file_size, check_file_type

UPLOAD_DIR = "uploads"

  # 50 MB file

os.makedirs(UPLOAD_DIR, exist_ok=True)


def upload_pdf_file(file: UploadFile):
    check_file_size(file)
    check_file_type(file)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    file.file.seek(0)
    return {"filename": file.filename}
