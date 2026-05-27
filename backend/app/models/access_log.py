from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class AccessLog(Base):
    __tablename__ = "access_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    dataset_id: Mapped[int | None] = mapped_column(ForeignKey("datasets.id"), index=True, nullable=True)
    wallet_address: Mapped[str | None] = mapped_column(
        String(42),
        ForeignKey("users.wallet_address"),
        index=True,
        nullable=True,
    )

    action: Mapped[str] = mapped_column(String(100), nullable=False)
    details: Mapped[str | None] = mapped_column(Text, nullable=True)
    transaction_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    dataset = relationship("Dataset", back_populates="access_logs")
    user = relationship("User", back_populates="access_logs")