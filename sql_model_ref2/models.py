from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    secret_name: str = Field(max_length=100, nullable=False)
    age: Optional[int] = Field(default=None)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    team: Optional["Team"] = Relationship(back_populates="heroes")


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")

