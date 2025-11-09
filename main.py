from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from router.movies import router as movie_router
import os


STATIC_DIR = os.path.join(os.getcwd(), 'media')
os.makedirs(STATIC_DIR, exist_ok=True)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Or specify specific methods like ["GET", "POST"]
    allow_headers=["*"],  # Or specify specific headers
)


app.include_router(movie_router)


app.mount('/media', StaticFiles(directory=STATIC_DIR), name='media')
