from fastapi import APIRouter, HTTPException
from api.schemas.diaper_change import DiaperChangeSchema
from application.uses_cases.diaper_change import DiaperChangeUseCases
from infrastructure.diaper_change.repository import DiaperChangeRepositoryDB

router = APIRouter()

# Create repository
diaper_change_repository = DiaperChangeRepositoryDB()

# Create use case
use_cases = DiaperChangeUseCases(
    repository=diaper_change_repository)


@router.post("/diaper-changes")
async def create_diaper_change(payload: DiaperChangeSchema):
    try:
        use_cases.create(type=payload.type, date=payload.date)
        return {
            "message": "in progress",
            "payload": payload
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/diaper-changes")
async def get_diaper_change():
    try:
        diaper_changes = use_cases.find()
        return {
            "message": "in progress",
            "data": diaper_changes
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
