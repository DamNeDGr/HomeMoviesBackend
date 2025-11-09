import os
import shutil
from uuid import uuid4
from exceptions import exceptions


UPLOAD_DIR = os.path.join(os.getcwd(), 'media', 'uploads', 'movies')
os.makedirs(UPLOAD_DIR, exist_ok=True);

def save_movies(file, filename):
    ext = os.path.splitext(str(file.filename))[1]
    new_file = f'{str(uuid4())}_{filename.replace(' ', '_')}{ext}'
    file_location = os.path.join(UPLOAD_DIR, new_file)
    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "file_name": new_file,
        "file_path": file_location
    }
    
    


def delete_movies(movie_path):
    try:
        if os.path.exists(movie_path):
            os.remove(movie_path)
            return True
        else: 
            raise exceptions.movie_not_found
    except Exception:
        raise exceptions.file_delete