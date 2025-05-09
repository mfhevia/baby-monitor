import os
from sqlmodel import SQLModel, create_engine, Session

_engine = None  # cache interna opcional


def get_engine():
    global _engine
    if _engine is None:
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME")

        DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        # Verifica que la URL es correcta
        print(f"Connecting to database at {DATABASE_URL}")
        _engine = create_engine(DATABASE_URL, echo=True)
        SQLModel.metadata.create_all(_engine)
    return _engine


def get_db():
    engine = get_engine()
    with Session(engine) as session:
        yield session
