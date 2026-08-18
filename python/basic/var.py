from fastapi import FastAPI, status ,HTTPException
from random import randrange
from pydantic import BaseModel
app=FastAPI()

class Post(BaseModel):
    name:str
    title:str
    published:bool=True
    


my_posts=[{"title":"the oddessy","actor":"mat damon","id":1},{"title":"the prestige","actor":"nolan","id":2}]

@app.get("/")
def get_data():
    return {"hey there"}

@app.post("/create_post")
def createUserPost():
    return {"This is the new start"}
    
    
        
@app.post("/post")
async def createPost(new_post:Post): 
    if not new_post:
        return HTTPException(status.HTTP_404_NOT_FOUND,{"message":"No post some error"})
    my_posts.append(new_post)
    return {"message": f"title{my_posts}" }


