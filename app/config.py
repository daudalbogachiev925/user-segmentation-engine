from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/segments"
    K_CLUSTERS: int = 5
    class Config:
        env_file = ".env"

settings = Settings()
