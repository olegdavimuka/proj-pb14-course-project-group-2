
FROM python:3.11-slim

# Working directory in the container to /app
WORKDIR /app

# Here we should Copy the current directory contents into the container at /app
COPY . /app

# Here we can install packages if needed
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Defining environment variable for Python to not write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

CMD ["python", "bot.py"]
