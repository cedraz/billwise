from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        extra="ignore"
    )

    SQLALCHEMY_DATABASE_URI: str


settings = Settings()
