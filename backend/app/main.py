from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routers import router
from infrastructure.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

def get_app() -> FastAPI:
    application = FastAPI(
        title="Concerts API",
        description="API for managing concerts and events",
        version="1.0.0",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router)

    return application

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:get_app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )