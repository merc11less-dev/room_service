from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Room Service",
    description="Meeting room service",
    version="1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok", "message": "Service is running"}


@app.get("/")
async def root():
    return {
        "service": "Room Service",
        "version": "1.0",
        "endpoints": ["/healthcheck", "/auth/login", "rooms", "/bookings"]
    }