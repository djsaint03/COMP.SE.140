# Dockerfile for Service1 (Python)
FROM python:3.9-bullseye

WORKDIR /app

# Install Flask and requests
RUN pip install Flask requests
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY service1app.py /app/service1.py

CMD ["python", "service1.py"]