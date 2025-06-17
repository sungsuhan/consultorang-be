from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:softworks!12@localhost:5432/consultorang"

    class Config:
        env_file = ".env"

settings = Settings()