from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# All of our models will inherit from this Base class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users' # The actual table name in the database

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"