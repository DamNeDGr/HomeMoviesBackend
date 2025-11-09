from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DB_URL = 'postgresql+asyncpg://postgres:6286@127.0.0.1:5432/damned_movies'

engine = create_async_engine(DB_URL)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass