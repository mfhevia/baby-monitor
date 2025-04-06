from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://baby_monitor_user:baby_monitor_pass@localhost:5432/baby_monitor"

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
