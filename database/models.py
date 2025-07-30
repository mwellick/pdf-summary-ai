from .database import Base
from sqlalchemy import Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class DocumentSummary(Base):
    __tablename__ = "document_summaries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    filename: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[Text] = mapped_column(nullable=False)
    created_at: Mapped[DateTime] = mapped_column(nullable=False, timezone=True, server_default=func.now())
