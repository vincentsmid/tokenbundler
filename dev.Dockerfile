# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . /usr/src/app

# Install poetry
RUN apt-get update
RUN pip install poetry

# Install dependencies using poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only main

# Command to run the Uvicorn server
CMD ["sh", "-c", "bash /usr/src/app/bin/dev/migrate.sh && poetry run uvicorn main_app.main:app --host 0 --port 8000 --reload"]

# Expose the port the app runs on
EXPOSE 8000
