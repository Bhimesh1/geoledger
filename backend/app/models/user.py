from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    wallet_address: Mapped[str] = mapped_column(String(42), unique=True, index=True, nullable=False)
    rsa_public_key: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    datasets = relationship("Dataset", back_populates="owner_user")
    access_records = relationship("DatasetAccess", back_populates="recipient_user")
    access_logs = relationship("AccessLog", back_populates="user")