# Используйте официальный базовый образ Python
FROM python:3.8-slim

# Установите рабочий каталог в контейнере
WORKDIR /app

# Установите gcc и другие зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Скопируйте файл зависимостей и установите зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Скопируйте остальные файлы приложения в рабочий каталог
COPY . .

# Укажите команду для запуска приложения
CMD ["python", "app.py"]

# Откройте порт, который использует ваше приложение
EXPOSE 5000
