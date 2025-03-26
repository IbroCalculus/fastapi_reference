from typing import Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel, field_validator

router = APIRouter(prefix='/api/v1', tags=["blogpost"])


class BlogPost(BaseModel):
    title: str
    author: str
    description: Optional[str] = ""

    @field_validator('title')
    def validate_title(cls, value):
        if not value or len(value.strip()) == 0:
            raise ValueError('Title cannot be empty')
        return value

    @field_validator('author')
    def validate_author(cls, value):
        if not value or len(value.strip()) == 0:
            raise ValueError('Author cannot be empty')
        return value

    @field_validator('description')
    def validate_description(cls, value):
        if value and len(value) > 5:
            raise ValueError('Description cannot exceed 5 characters')
        return value


@router.post('/create_blog')
async def create_blog(blogpost: BlogPost,
                      blog_metadata: Optional[int] = Query(
                          None,
                          title="Blog metadata",
                          description="Metadata associated with the blog",
                          alias='The alias to Blog Metadata',
                          deprecated=True)
                      ):
    return {"message": blogpost, 'blog_metadata': blog_metadata}
