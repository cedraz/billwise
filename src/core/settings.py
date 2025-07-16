import sys
from pydantic import ValidationError, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = PROJECT_ROOT / ".env"

print(f"Project root directory: {PROJECT_ROOT}")
print(f"Using environment file: {ENV_FILE_PATH}")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )

    PROJECT_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int
    MONGODB_ROOT_USERNAME: str
    MONGODB_ROOT_PASSWORD: str
    MONGODB_DATABASE: str
    MONGODB_HOST: str
    MONGODB_PORT: int

    SQLALCHEMY_DATABASE_URI: str | None = None
    MONGODB_URI: str | None = None

    @model_validator(mode='after')
    def assemble_computed_uris(self) -> 'Settings':
        """
        Executa após a validação de todos os outros campos
        para montar as URIs de conexão.
        """
        # Monta a URI do PostgreSQL
        self.SQLALCHEMY_DATABASE_URI = (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

        # Monta a URI do MongoDB
        self.MONGODB_URI = f"mongodb://{self.MONGODB_ROOT_USERNAME}:{self.MONGODB_ROOT_PASSWORD}@{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DATABASE}?authSource=admin"
        return self


try:
    settings = Settings()
    print("✅ Ambiente e configurações carregados com sucesso!")
except ValidationError as e:
    print("🔥🔥🔥 Erro de validação nas variáveis de ambiente! 🔥🔥🔥")
    print(f"Tentando carregar .env de: {ENV_FILE_PATH}")
    print(e)
    sys.exit(1)
