from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AsyncKeel"
    ENV: str = "development"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
