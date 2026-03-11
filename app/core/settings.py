from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AsyncKeel"
    ENV: str = "development"
    DEBUG: bool = True

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"


settings = Settings()
