class Settings:
    DB_URL = "postgresql://postgres:postgres@localhost:5432/meeting_room"
    SECRET_KEY = "your-super-secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DEBUG = True

settings = Settings()