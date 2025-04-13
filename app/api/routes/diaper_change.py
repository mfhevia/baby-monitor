from fastapi import APIRouter, HTTPException, Depends, status
from api.schemas.diaper_change import DiaperChangeCreateSchema, DiaperChangeListResponseSchema, DiaperChangeResponseDataSchema, DiaperChangeSingleResponseSchema
from application.uses_cases.diaper_change import DiaperChangeUseCases
from infrastructure.database import get_db
from infrastructure.repositories import DiaperChangeRepositoryDB
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


def get_repository(db=Depends(get_db)):
    return DiaperChangeRepositoryDB(db)


def get_use_case(repository: DiaperChangeRepositoryDB = Depends(get_repository)):
    return DiaperChangeUseCases(repository)


@router.post("/diaper-changes", status_code=status.HTTP_201_CREATED, tags=["diaper_changes"])
async def create_diaper_change(
    payload: DiaperChangeCreateSchema,
    use_cases: DiaperChangeUseCases = Depends(get_use_case)
) -> DiaperChangeSingleResponseSchema:
    try:
        diaper_change = use_cases.create(type=payload.type, date=payload.date)
        response_data = DiaperChangeResponseDataSchema(
            **diaper_change.to_dict())

        return DiaperChangeSingleResponseSchema(data=response_data)
    except Exception as e:
        logger.exception("Unexpected error in create diaper_change")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


@router.get("/diaper-changes", status_code=status.HTTP_200_OK, tags=["diaper_changes"])
async def get_diaper_change(
    use_cases: DiaperChangeUseCases = Depends(get_use_case)
) -> DiaperChangeListResponseSchema:
    try:
        diaper_changes = use_cases.find()
        response_data = [DiaperChangeResponseDataSchema(
            **diaper_change.to_dict()) for diaper_change in diaper_changes]

        return DiaperChangeListResponseSchema(data=response_data)
    except Exception as e:
        logger.exception("Unexpected error in list diaper_changes")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
