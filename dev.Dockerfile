# Use the official FastAPI image from Docker Hub
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
FROM python:3.10

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY ./app .

# Expose FastAPI port
EXPOSE 80

# Command to run the application using fastapi
CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
