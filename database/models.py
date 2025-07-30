import datetime
from .database import Base
from sqlalchemy import Text, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class DocumentSummary(Base):
    __tablename__ = "document_summaries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    filename: Mapped[str] = mapped_column(String(128), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False,
                                                          server_default=func.now())
