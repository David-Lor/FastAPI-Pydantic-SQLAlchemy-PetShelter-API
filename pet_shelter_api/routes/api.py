from fastapi import APIRouter

from ..models.generic_responses import OK_200

__all__ = ("router",)

router = APIRouter()


@router.get("/status", description="Get API status")
def get_status():
    return OK_200
