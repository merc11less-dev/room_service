from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, rooms, bookings


app = FastAPI(
    title="Meeting Room Booking Service",
    description="Service for booking meeting rooms in coworking space",
    version="1.0.0",
    swagger_ui_parameters={
        "persistAuthorization": True,
    }
)

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(bookings.router)

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

