from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''from config import DB_HOST
from config import DB_PORT
from config import DB_USER
from config import DB_PASSWORD
from config import DB_NAME'''


DATABASE_URL = (
    #f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    "postgresql://postgres:password@localhost:5433/job-search"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


"""Function to depend on which when getting database in other function"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

