from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class DatasetAccess(Base):
    __tablename__ = "dataset_access"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    dataset_id: Mapped[int] = mapped_column(ForeignKey("datasets.id"), index=True, nullable=False)
    recipient_wallet_address: Mapped[str] = mapped_column(
        String(42),
        ForeignKey("users.wallet_address"),
        index=True,
        nullable=False,
    )

    encrypted_aes_key_for_recipient: Mapped[str | None] = mapped_column(Text, nullable=True)

    access_status: Mapped[str] = mapped_column(String(30), default="active", nullable=False)

    granted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    dataset = relationship("Dataset", back_populates="access_records")
    recipient_user = relationship("User", back_populates="access_records")

    __table_args__ = (
        UniqueConstraint("dataset_id", "recipient_wallet_address", name="uq_dataset_recipient_access"),
    )