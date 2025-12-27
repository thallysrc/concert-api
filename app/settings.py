from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = Field(default="local")
    DATABASE_URL: str = "postgresql+psycopg2://gandalf:ring@postgres:5432/postgres"


    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
