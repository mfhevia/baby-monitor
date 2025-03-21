from fastapi import FastAPI
from mangum import Mangum
from api.routes import diaper_change

app = FastAPI()
app.include_router(diaper_change.router)


@app.get("/alive")
async def root():
    return {"message": "I am alive baby"}

handler = Mangum(app)
