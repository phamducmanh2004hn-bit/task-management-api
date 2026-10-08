from app.models.task import Task
from app.models.user import User

def create_task(db, task):
    db_user = db.query(User).filter(User.id == task.user_id).first()

    if db_user is None:
        return None

    new_task = Task(
        title=task.title,
        description=task.description,
        status="todo",
        user_id=task.user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_task(db, task_id):
    result = db.query(Task).filter(Task.id == task_id).first()
    return result

def get_tasks(db):
    return db.query(Task).all()

def update_task(db, task_id, task):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if db_task is None:
        return None

    if task.title is not None:
        db_task.title = task.title

    if task.description is not None:
        db_task.description = task.description

    if task.status is not None:
        db_task.status = task.status

    db.commit()
    db.refresh(db_task)

    return db_task

def delete_task(db, task_id):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if db_task is None:
        return None

    db.delete(db_task)
    db.commit()

    return db_task
    



    
    
    