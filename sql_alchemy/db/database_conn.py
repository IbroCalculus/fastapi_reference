from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
# Define database credentials for mySQL connection
db_username = "root"
db_password = "Admin123"
db_host = "localhost"
db_port = 3306
db_name = "blogapplication"     # Where: blogapplication is the name of the database created in mysql, ie using workbench

URL_DATABASE = f'mysql+pymsql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
# URL_DATABASE = 'mysql+pymsql://root:Admin123@localhost:3306/blogapplication'

engine = create_engine(URL_DATABASE, connect_args={"check_same_threads": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
'''

# ========= IF DB IS SQLite ============
URL_DATABASE = 'sqlite:///./blogapplication.db'  # Once api run, will create db in same directory

engine = create_engine(URL_DATABASE)  # For SQLite database, REMOVE: connect_args={"check_same_threads": False} in mysql above
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# =============== ADDITIONAL CODES =============
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
