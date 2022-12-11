import fastapi
from my_app.logger import logger

router = fastapi.APIRouter()


@router.get("/")
def home_page(request: fastapi.Request):
    return fastapi.responses.JSONResponse(content={'req': request})
