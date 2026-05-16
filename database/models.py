from datetime import datetime

from sqlalchemy import String, Text, Integer, BigInteger, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None] = mapped_column(String(255))

    full_name: Mapped[str] = mapped_column(String(255), default="Worker")
    about: Mapped[str | None] = mapped_column(Text)

    rank: Mapped[str] = mapped_column(String(100), default="Новичок")

    usdt_wallet: Mapped[str | None] = mapped_column(String(255))
    bank_card: Mapped[str | None] = mapped_column(String(255))

    balance: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    total_leads: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    chat_id: Mapped[int] = mapped_column(BigInteger)
    price_per_lead: Mapped[float] = mapped_column(Numeric(10, 2))
    description: Mapped[str | None] = mapped_column(Text)
    bonuses: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50), default="active")

