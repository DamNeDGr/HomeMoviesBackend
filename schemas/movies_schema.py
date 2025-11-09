from pydantic import BaseModel, Field
from datetime import datetime



class All_movies(BaseModel):
    
    id: int
    name: str
    url: str
    
class MovieBase(All_movies):
    
    file_path: str
    upload_date: datetime
    

class MovieUpload(BaseModel):

    name: str
    file_path: str
    url: str