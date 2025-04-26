import uvicorn
from fastapi import FastAPI
from app.api import auth, events

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(events.router, prefix="/calendar", tags=["Calendar Events"])
uvicorn.run(app, host="0.0.0.0", port=8000)
