# Dockerfile for Service1 (Python)
FROM python:3.9-bullseye

WORKDIR /app

# Install Flask and requests
RUN pip install Flask requests

COPY service1.py /app/service1.py

CMD ["python", "service1.py"]