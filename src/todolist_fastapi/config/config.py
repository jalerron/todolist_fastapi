from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy import URL


class DatabaseConfig(BaseModel):
    url: str = URL.create(
            drivername="driver",
            username="dbuser",
            password="password",  # plain (unescaped) text
            host="host",
            database="database",
            )


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
    

settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)