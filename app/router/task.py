from fastapi import APIRouter,Depends,HTTPException
from app.db.deps import get_db
from app.crud import task
from app.schemas.task import TaskCreate,TaskUpdate,TaskResponse
router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db=Depends(get_db)):
    db_tasks = task.get_tasks(db)
    return db_tasks
@router.get("/{task_id}",response_model= TaskResponse)
def get_task(task_id: int, db = Depends(get_db)):
    db_task = task.get_task(db,task_id=task_id)
    if db_task is None :
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/",response_model= TaskResponse)
def create_task(task_ct: TaskCreate, db=Depends(get_db)):
    db_task = task.create_task(db=db,task=task_ct)
    if db_task is None:
            raise HTTPException(status_code=404, detail="User not found")
    return db_task 

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_ud : TaskUpdate,db = Depends(get_db)):
    db_task = task.update_task(db=db,task_id=task_id,task=task_ud)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(task_id : int, db = Depends(get_db)):
    db_task = task.delete_task(task_id=task_id, db=db)
    if db_task is None :
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
    




    


        


