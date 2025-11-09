from fastapi import HTTPException, status


incorrect_file = HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail='Некорректный файл, попробуйте другой файл'
            )

incorrect_data = HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Некоректные данные')


movies_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Фильмы не найдены')
movie_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Фильм не найден')


file_delete = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Ошибка удаления файла с сервера')