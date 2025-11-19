import datetime
import uuid

from sqlalchemy import String, Text, Float, Integer, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import mapped_column, Mapped

from app.infrastructure.database.connection import Base


class Concert(Base):
    __tablename__ = "concerts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    image_url: Mapped[str] = mapped_column(Text, nullable=False)
    location: Mapped[str] = mapped_column(Text, nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[float | None] = mapped_column(Float, nullable=True)
    participants: Mapped[int | None] = mapped_column(Integer, nullable=True)