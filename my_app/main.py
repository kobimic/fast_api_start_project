import uvicorn
from logger import logger
from core import app
from fastapi.middleware.cors import CORSMiddleware
from routers import simple

origins = ["*"]
methods = ["*"]
headers = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=methods, allow_headers=headers)


def configure_routes():
    logger.info("Configuring routes")
    app.include_router(simple.router)


def configure():
    configure_routes()


def main():
    logger.info("Main start")
    configure()
    uvicorn.run(app)


if __name__ == '__main__':
    main()
