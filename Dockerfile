FROM python:3.12-slim AS base

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=your_project.settings
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["gunicorn", "your_project.wsgi:application", "--bind", "0.0.0.0:8000"]
