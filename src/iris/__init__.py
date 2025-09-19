from fastapi import APIRouter

from .ml import router as ml_router
from .data import router as data_router

router = APIRouter(
    prefix="/iris",
    tags=["Iris"]
)

router.include_router(ml_router)
router.include_router(data_router)