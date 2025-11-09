from fastapi import APIRouter,  Depends, File, UploadFile, Request
from fastapi.responses import StreamingResponse
from depends.init_db import init_db
from sqlalchemy.ext.asyncio import AsyncSession
from services import movies_crud
from services.file_service_movie import save_movies, delete_movies
from schemas.movies_schema import All_movies
from services.validate_file import validate_file, validate_filename
from exceptions import exceptions
from config.config import Secret
import os



BASE_URL = Secret.BASE_URL
UPLOAD_URL = Secret.UPLOAD_URL


router = APIRouter(
    prefix='/movies',
    tags=['Фильмы']
)



@router.get('/all', response_model=list[All_movies])
async def all_movies(db: AsyncSession = Depends(init_db)):
    return await movies_crud.get_all_movies(db=db)


# @router.get('/{id}', response_model=All_movies)
# async def get_movie_by_id(id: int, db: AsyncSession = Depends(init_db)):
#     return await movies_crud.get_movie_by_id(id=id, db=db)

@router.get('/stream/{movie_id}')
async def stream_movie(movie_id: int, request: Request, db: AsyncSession = Depends(init_db)):
    movie = await movies_crud.get_movie_by_id(id=movie_id, db=db)
    movie_path = movie.file_path
    movie_size = os.path.getsize(movie_path)
    def iterfile():
        with open(movie_path, mode='rb') as file_like:
            yield from file_like
    
    headers = {
        "Content-type": "video/mp4",
        "Accept-Ranges": "bytes",
        "Content-Length": str(movie_size),
    }
    
    return StreamingResponse(iterfile(), headers=headers)

@router.post('/upload', response_model=All_movies)
async def upload_movie(file: UploadFile = File(...), filename: str = Depends(validate_filename), db: AsyncSession = Depends(init_db)):
    if not validate_file(file=file, filename=filename):
        raise exceptions.incorrect_file
    new_file = save_movies(file=file, filename=filename)
    return await movies_crud.create_movie(movie_name=filename, movie_url=f'{UPLOAD_URL}',movie_path=new_file.get('file_path'),db=db)


@router.delete('/{id}')
async def delete_movie(id: int, db: AsyncSession = Depends(init_db)):
    movies = await movies_crud.get_movie_by_id(id=id, db=db)
    delete_movies(movie_path=movies.file_path)
    return await movies_crud.delete_movie(id=id, db=db)

