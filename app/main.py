from fastapi import FastAPI
from .db import init_db
from .routers.listings import router as listings_router

app = FastAPI(
    title="Rental Insights API",
    version="0.1.0",
    description="A housing market and rental insights API with CRUD for listings and analytics endpoints."
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(listings_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Rental Insights API is running"}