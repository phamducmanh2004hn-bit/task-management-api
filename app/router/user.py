from fastapi import APIRouter, Depends, HTTPException

from app.crud import user
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.db.deps import get_db
from app.schemas.task import TaskResponse
router = APIRouter()

@router.get("/", response_model=list[UserResponse])
def get_users(db=Depends(get_db)):
    db_users = user.get_users(db)
    return db_users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db=Depends(get_db)):
    db_user = user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.get("/{user_id}/tasks", response_model=list[TaskResponse])
def get_user_tasks(user_id: int, db=Depends(get_db)):
    db_tasks = user.get_user_tasks(db=db, user_id=user_id)
    if db_tasks is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_tasks

@router.post("/", response_model=UserResponse)
def create_user(user_ct: UserCreate, db=Depends(get_db)):
    db_user = user.create_user(db=db, user=user_ct)

    return db_user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_ud: UserUpdate, db=Depends(get_db)):
    db_user = user.update_user(db=db, user_id=user_id, user=user_ud)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db=Depends(get_db)):
    db_user = user.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user