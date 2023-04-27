from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["hello world"])


@router.get("/hello")
def user_hello():
    return {
        "Hello": "World",
    }
