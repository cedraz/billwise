import db.postgresql.models                # carrega todos os módulos de modelo
from db.postgresql.base import Base        # seu DeclarativeBase
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# -----------------------------------------------------------------------------
# 1) Ajusta o PYTHONPATH para que possamos importar seu pacote "db"
# -----------------------------------------------------------------------------
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

# -----------------------------------------------------------------------------
# 2) Importe aqui o seu Base e todos os seus modelos para que o Alembic os detecte
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 3) Defina o metadata alvo para o autogenerate
# -----------------------------------------------------------------------------
target_metadata = Base.metadata

# -----------------------------------------------------------------------------
# 4) Carrega a configuração do alembic.ini
# -----------------------------------------------------------------------------
config = context.config

# Se quiser sobrescrever a URL pelo env var DATABASE_URL:
db_url = os.getenv("DATABASE_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

# Configura o logging conforme o arquivo alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# -----------------------------------------------------------------------------
# 5) Funções que rodam as migrations offline e online
# -----------------------------------------------------------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (gera SQL sem conexão real)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode (usa um Engine real)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# -----------------------------------------------------------------------------
# 6) Escolhe o modo de execução
# -----------------------------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
