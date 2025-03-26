# database.py
from sqlmodel import SQLModel, create_engine, Session
import models

# For SQLite database
database_filename = 'test.db'
DATABASE_URL = f'sqlite:///./{database_filename}'

# IF MYSQL
# pip install pymysql OR pip install mysql-connector-python (ie: mysql+mysqlconnector://<username>:...
# DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>/<database_name>" If mysql
# import os
# DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"


# echo=True is for development, not production
engine = create_engine(DATABASE_URL, echo=True)

# The .db file won't be created until database.py file is executed'
if __name__ == '__main__':
    # create test.db (if it doesn't alread exist)'
    SQLModel.metadata.create_all(engine)

