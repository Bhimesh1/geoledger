from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    blockchain_dataset_id: Mapped[int | None] = mapped_column(Integer, unique=True, index=True, nullable=True)
    owner_wallet_address: Mapped[str] = mapped_column(
        String(42),
        ForeignKey("users.wallet_address"),
        index=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    ipfs_cid: Mapped[str | None] = mapped_column(String(255), nullable=True)
    file_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)

    encrypted_aes_key_for_owner: Mapped[str | None] = mapped_column(Text, nullable=True)

    original_filename: Mapped[str | None] = mapped_column(String(255), nullable=True)
    file_format: Mapped[str | None] = mapped_column(String(50), nullable=True)
    file_size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    owner_user = relationship("User", back_populates="datasets")
    access_records = relationship("DatasetAccess", back_populates="dataset", cascade="all, delete-orphan")
    access_logs = relationship("AccessLog", back_populates="dataset", cascade="all, delete-orphan")