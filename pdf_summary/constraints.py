import os
import fitz
from fastapi import UploadFile
from fastapi import HTTPException
from starlette import status

FILE_SIZE = 50 * 1024 * 1024

UPLOAD_DIR = "uploads"  # 50 MB file

os.makedirs(UPLOAD_DIR, exist_ok=True)


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


def check_file_exists(file: str):
    if not os.path.exists(file):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )


def parse_pdf_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        doc = fitz.open(file_path)
        parsed_text = ""
        image_count = 0

        for page in doc:
            text = page.get_text()
            parsed_text += text

            images = page.get_images(full=True)
            image_count += len(images)

        number_of_pages = len(doc)
        doc.close()

        return {
            "text_preview": parsed_text[:100],
            "full_text": parsed_text,
            "number_of_images": image_count,
            "pages": number_of_pages
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occured during parsing file. Error:{e}"
        )
