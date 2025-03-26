from sqlmodel import create_engine, SQLModel
import models   # noqa: F401 -> Don't remove this or optimize import, must be here to create the database/tables

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///./{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_db_and_tables()