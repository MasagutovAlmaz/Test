from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from src.api.tron import router as tron_router
from src.db.database import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    try:
        yield
    finally:
        await close_db()

app = FastAPI(lifespan=lifespan)

def main():

    app.include_router(tron_router)

main()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3451, reload=True)