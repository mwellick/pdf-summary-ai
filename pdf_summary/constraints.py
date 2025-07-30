from fastapi import UploadFile
from fastapi import HTTPException
from starlette import status

FILE_SIZE = 50 * 1024 * 1024


def check_file_size(file: UploadFile):
    file_data = file.file.read()

    if len(file_data) > FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size more than 50 MB"
        )

    file.file.seek(0)


def check_file_type(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
