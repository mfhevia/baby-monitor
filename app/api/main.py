from fastapi import FastAPI
from mangum import Mangum
from app.api.routes import diaper_change
from app.infrastructure.database import init_tables

app = FastAPI()
app.include_router(diaper_change.router)


@app.get("/alive")
async def root():
    return {"message": "I am alive baby"}

handler = Mangum(app)
