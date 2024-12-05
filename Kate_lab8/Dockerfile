FROM python:3.10-slim

WORKDIR /app

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Копіювання файлу залежностей
COPY requirements.txt .

# Встановлення залежностей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання решти проєкту
COPY . .

# Спочатку виконуємо скрипт app.py для створення таблиць
CMD python python manage.py runserver 0.0.0.0:8000
