from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME : str = "Task Management API"
    SQLALCHEMY_DATABASE_URI : str = "sqlite:///./app.db"
settings = Settings()
