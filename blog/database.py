from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create our Sqlite database Url for SqlAlchemy model
SQLALCHAMY_DATABASE_URL = 'sqlite:///blog.db'

# Create SqlAlechemy engine for Access our database like migration opreations
# Here cheack_same_thread is false because sqlite only allow sigle thread , assuming that each thread would handle an independent request.
# This is to prevent accidentally sharing the same connection for different things (for different requests).
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
#But once we create an instance of the SessionLocal class, this instance will be the actual database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base is a class which is help us to create our database models
Base = declarative_base()

# It's a dependency for our database i.e. database is should be the type of session and after using db ,database must be closed
def get_db():
    db = SessionLocal()
    try:
        yield db  # yield is like return for handling dependencies.
    finally:
        db.close()
