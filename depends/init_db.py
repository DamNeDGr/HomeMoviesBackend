from database.db import SessionLocal


async def init_db():
    async with SessionLocal() as session:
        yield session
