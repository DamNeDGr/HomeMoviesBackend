from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError
from models.movies import MoviesBase
from schemas.movies_schema import MovieUpload
from exceptions import exceptions


async def get_all_movies(db: AsyncSession):
    movies = await db.execute(select(MoviesBase))
    movies = movies.scalars().all()
    if not movies:
        raise exceptions.movies_not_found
    return movies


async def get_movie_by_id(id: int, db: AsyncSession):
    movie = await db.execute(select(MoviesBase).where(MoviesBase.id == id))
    movie = movie.scalar_one_or_none()
    if not movie:
        raise exceptions.movie_not_found
    return movie


async def create_movie(movie_name: str, movie_url: str, movie_path: str | None, db: AsyncSession):
    movie = MoviesBase(
        name=movie_name,
        url=movie_url,
        file_path=movie_path
    )
    try:
        db.add(movie)
        await db.commit()
        await db.refresh(movie)
        movie.url = f'{movie_url}{movie.id}'
        await db.commit()
        await db.refresh(movie)
    except IntegrityError:
        raise exceptions.incorrect_data
    
    
    return movie

async def delete_movie(id: int, db: AsyncSession):
    movie = await get_movie_by_id(id=id, db=db)
    await db.delete(movie)
    await db.commit()
    return {
        "message": f'Фильм с id: {movie.id} удален'
    }