from fastapi import FastAPI
from pdf_summary.routers import pdf_router

app = FastAPI(title="PDF Summary AI",docs_url="/")

app.include_router(pdf_router)
