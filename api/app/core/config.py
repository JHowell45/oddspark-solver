from functools import lru_cache

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # model_config = SettingsConfigDict()
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql",
            host=self.DB_HOST,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            path=self.DB_NAME,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
