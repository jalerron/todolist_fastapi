from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from sqlalchemy import URL


class DatabaseConfig(BaseModel):
    # url: str = URL.create(
    #         drivername="driver",
    #         username="dbuser",
    #         password="password",  # plain (unescaped) text
    #         host="host",
    #         database="database",
    #         )
    url: str = 'postgresql+asyncpg://postgres:yourpassword@localhost:5432/mydatabase'
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50
    

class AuthConfig(BaseModel):
    SECRET_KEY: str = "Secret key"
    JWT_ALGORITHM: str = "HS256"
    ACCES_TOKEN_EXPIRE_MINUTES: int = 30

    #SMTP
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None

class RunConfig(BaseModel):
    server_host: str = '127.0.0.1'
    server_port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    
    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()
    auth: AuthConfig = AuthConfig()
    

settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)