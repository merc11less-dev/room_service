# Meeting Room Booking Service

Сервис для бронирования переговорных комнат в коворкинге.

## Технологии

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- JWT аутентификация
- Docker

## Запуск через Docker

### 1. Клонировать репозиторий

```bash
git clone https://github.com/merc11less-dev/room_service.git
cd room_service
```

### 2. Запустить контейнеры
```bash
docker-compose up --build
```

### 3. Документация API
```bash
http://localhost:8000/docs
```

### 4. Примеры работы API
Регистрация:
```bash
curl -X POST http://localhost:8000/auth/register -H "Content-Type: application/json" -d '{"username": "alex", "email": "alex@mail.com", "password": "123", "role": "employee"}'
```

Логин:
```bash
curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=alex&password=123"
```

Получить комнаты (с токеном):
```bash
curl -X GET http://localhost:8000/rooms/ -H "Authorization: Bearer <токен>"
```

Создать бронь:
```bash
curl -X POST http://localhost:8000/bookings/ -H "Authorization: Bearer <токен>" -H "Content-Type: application/json" -d '{"room_id": 1, "slot_id": 1, "booking_date": "2026-06-20"}'
```

Мои брони:
```bash
curl -X GET http://localhost:8000/bookings/my -H "Authorization: Bearer <токен>"
```

Отменить бронь:
```bash
curl -X DELETE http://localhost:8000/bookings/1 -H "Authorization: Bearer <токен>"
```

#### 5. Запуск без Docker
```bash
poetry install
CREATE DATABASE meeting_booking;
python init_db.py
INSERT INTO slots (start_time, end_time) VALUES ('09:00', '11:00'), ('11:00', '13:00'), ('13:00', '15:00'), ('15:00', '17:00'), ('17:00', '19:00');
uvicorn app.main:app --reload
```


