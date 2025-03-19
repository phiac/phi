# Use a Python base image
FROM python:3.12-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=your_project.settings
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "your_project.wsgi:application", "--bind", "0.0.0.0:8000"]
