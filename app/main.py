from fastapi import FastAPI
from app.router import task,user
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Task Management API is running"}

app.include_router(task.router,prefix="/task",tags=["Task"])
app.include_router(user.router,prefix="/user",tags=["User"])
