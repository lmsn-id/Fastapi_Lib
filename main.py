from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routes.auth import router as auth_router
from config.middleware import check_api_key
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(check_api_key)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
