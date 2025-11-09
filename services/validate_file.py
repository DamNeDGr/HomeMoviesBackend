import os
from fastapi import HTTPException, status, Form

def validate_file(file, filename):
    if not file.content_type.startswith("video/"): # type: ignore
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Ошибка, попробуйте другой формат видео')

    ext = os.path.splitext(str(file.filename))[1]
    if not ext:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Файл без расширения, попробуйте выбрать другой файл')
    
    return True


def validate_filename(title: str = Form(...)):
    if len(title) > 90:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Название файла слишком длинное')
    return title