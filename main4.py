from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# USING ENUMS TYPE
class BlogType(str, Enum):
    short = 'Short'
    story = 'Story'
    howto = 'Howto'

@app.get('/')
async def index():
    return 'Welcome'

# http://127.0.0.1:8000/blog/Story
@app.get("/blog/{blog_type}")
async def read_blog(blog_type: BlogType):
    return {"blog_type": f'You chose blog type: {blog_type.value}'}
