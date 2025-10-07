from fastapi import FastAPI
from api.v1.routes import router

app = FastAPI(title="Trip Service")
app.include_router(router, prefix="/api/v1/trips", tags=['trips'])