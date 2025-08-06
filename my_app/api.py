from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from .database import get_db
from .models import User
from .schemas import UserCreate, UserResponse

# Create FastAPI application
app = FastAPI(
    title="User Management API",
    description="API for managing users with fetch and insert operations",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Root endpoint to check if API is running"""
    return {"message": "User Management API is running!"}

@app.get("/users", response_model=List[UserResponse])
def fetch_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Fetch all users from the database
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return
    """
    try:
        users = db.query(User).offset(skip).limit(limit).all()
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching users: {str(e)}"
        )

@app.get("/users/{user_id}", response_model=UserResponse)
def fetch_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch a specific user by ID
    
    - **user_id**: The ID of the user to fetch
    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching user: {str(e)}"
        )

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Insert a new user into the database
    
    - **name**: User's name (required)
    - **email**: User's email (required, must be unique)
    """
    try:
        # Check if user with this email already exists
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user.email} already exists"
            )
        
        # Create new user
        db_user = User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running properly"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)