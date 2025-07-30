import os
from fastapi import UploadFile
from .constraints import (
    UPLOAD_DIR,
    check_file_size,
    check_file_type,
    check_file_exists
)


def upload_pdf_file(file: UploadFile):
    check_file_size(file)
    check_file_type(file)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    file.file.seek(0)
    return {"filename": file.filename}
