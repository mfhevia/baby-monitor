import os
from sqlmodel import SQLModel, create_engine, Session


def get_database_url() -> str:
    """Construye la URL de la base de datos según el entorno."""
    environment = os.getenv("ENVIRONMENT", "development")

    if environment == "test":
        DB_USER = os.getenv("DB_TEST_USER")
        DB_PASSWORD = os.getenv("DB_TEST_PASSWORD")
        DB_HOST = os.getenv("DB_TEST_HOST")
        DB_PORT = os.getenv("DB_TEST_PORT")
        DB_NAME = os.getenv("DB_TEST_NAME", "baby_monitor_test")
    else:
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME", "baby_monitor")

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return DATABASE_URL


DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
