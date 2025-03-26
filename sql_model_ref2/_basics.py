from sqlmodel import Field, SQLModel, create_engine


# THE MODEL
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# THE DATABASE CONNECTION
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# EXECUTE DATABASE AND ASSOCIATED TABLE CREATION
SQLModel.metadata.create_all(engine)
