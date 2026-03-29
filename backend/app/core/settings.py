from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
    )

    app_env: str = 'development'
    app_version: str = '0.1.0'
    log_level: str = 'INFO'
    allowed_origins: list[str] = ['http://localhost:3000', 'http://localhost:5173']

    @property
    def is_development(self) -> bool:
        return self.app_env == 'development'


@lru_cache
def get_settings() -> Settings:
    return Settings()
