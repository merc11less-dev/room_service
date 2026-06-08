class Settings:
    DB_URL = "postgresql://postgres:postgres@localhost:5432/room_service"

    # JWT
    SECRET_KEY = "your-super-secret-key-change-in-production"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    DEBUG = True

settings = Settings()