import pytest
import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine
from alembic.config import Config
from alembic import command
from urllib.parse import urlparse
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.infrastructure.database import get_database_url
import os
import subprocess


def pytest_configure():
    # Aseguramos que ENVIRONMENT sea 'test' si no está definido
    os.environ.setdefault("ENVIRONMENT", "test")


# Función para eliminar y recrear la base de datos
def reset_database():
    """Reinicia el contenedor de la base de datos y aplica las migraciones."""

    # Parar y eliminar contenedores y volúmenes
    subprocess.run(["docker", "compose", "down", "-v"], check=True)

    # Levantar solo el servicio de la base de datos
    subprocess.run(["docker", "compose", "up", "-d", "db"], check=True)

    # Esperar un poco para asegurarse de que PostgreSQL esté listo
    import time
    time.sleep(5)

    # Aplicar migraciones
    database_url = get_database_url()
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", database_url)
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Llama a la función para reiniciar la base de datos antes de ejecutar los tests
    reset_database()

    # Espera un poco para asegurarte de que la DB está lista
    import time
    time.sleep(5)

    # Configura la conexión a la base de datos y las migraciones
    engine = create_engine(get_database_url())
    yield engine

    # Limpieza después de los tests
    engine.dispose()


@pytest.fixture(scope="session")
def engine():
    db_url = get_database_url()
    engine = create_engine(db_url, echo=True, future=True)
    yield engine
    engine.dispose()


@pytest.fixture()
def session(engine):
    """Crea una sesión nueva para cada test dentro de una transacción."""
    connection = engine.connect()
    transaction = connection.begin()

    TestingSessionLocal = sessionmaker(
        bind=connection, class_=Session, expire_on_commit=False)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        transaction.rollback()
        connection.close()
