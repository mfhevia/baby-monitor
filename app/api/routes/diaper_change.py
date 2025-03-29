from fastapi import APIRouter, HTTPException, Depends
from api.schemas.diaper_change import DiaperChangeCreateSchema
from application.uses_cases.diaper_change import DiaperChangeUseCases
from infrastructure.database import get_db
from infrastructure.repositories import DiaperChangeRepositoryDB

router = APIRouter()

# db = get_db()
# repository = DiaperChangeRepositoryDB(db)
# use_cases = DiaperChangeUseCases(repository=repository)


def get_repository(db=Depends(get_db)):
    return DiaperChangeRepositoryDB(db)


def get_use_case(repository: DiaperChangeRepositoryDB = Depends(get_repository)):
    return DiaperChangeUseCases(repository)


@router.post("/diaper-changes")
async def create_diaper_change(payload: DiaperChangeCreateSchema, use_cases: DiaperChangeUseCases = Depends(get_use_case)):
    try:
        event_created = use_cases.create(type=payload.type, date=payload.date)
        return {
            "message": "in progress",
            "payload": event_created
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/diaper-changes")
async def get_diaper_change(use_cases: DiaperChangeUseCases = Depends(get_use_case)):
    try:
        diaper_changes = use_cases.find()
        return {
            "message": "in progress",
            "data": diaper_changes
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
